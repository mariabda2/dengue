# Registro de Decisiones Analíticas

**Proyecto:** Predicción de Hospitalización por Dengue — Bucaramanga  
**Formato:** Cada decisión incluye la justificación clínica/estadística y el notebook donde se implementa.

---

## DA-01 · Corrección de inconsistencias en PAC_HOS_
**Notebook:** `01_eda/01_exploracion_general.ipynb`  
**Decisión:** Reclasificar como hospitalizados (PAC_HOS_=1) los registros que:
- Tienen PAC_HOS_=2 (no hospitalizado), Y
- Tienen fecha de hospitalización registrada, Y
- Tienen conducta "Hospitalización piso" o "UCI"  

**Justificación:** La fecha de hospitalización y la conducta clínica son evidencia objetiva
que prevalece sobre el campo PAC_HOS_. El formulario SIVIGILA puede tener errores de tipeo
en un campo dicotómico (1/2 es fácil de confundir).  
**Impacto:** 2 registros afectados de ~36,000.

---

## DA-02 · Exclusión de CLASFINAL como variable predictora
**Notebook:** `01_eda/01_exploracion_general.ipynb`  
**Decisión:** No incluir CLASFINAL entre los predictores de los modelos de clasificación principal.  
**Justificación:** CLASFINAL presenta una asociación casi perfecta con la hospitalización
(DCSA: ~65%, DSSA: ~8%, Grave: ~95%). Su inclusión convertiría el problema en una tarea
trivial e impediría identificar el aporte independiente de síntomas y factores demográficos.
Clínicamente, CLASFINAL se define por los mismos signos de alarma que ya son predictores.  
**Alternativa:** Usar CLASFINAL como variable de estratificación para construir modelos
separados (DCSA vs DSSA).

---

## DA-03 · Estratificación por CLASFINAL para el modelado
**Notebooks:** `03_modelado/con_signos/` y `03_modelado/sin_signos/`  
**Decisión:** Construir modelos separados para DCSA y DSSA, en lugar de un modelo único.  
**Justificación:**
- La prevalencia de hospitalización difiere radicalmente: ~65% en DCSA vs ~8% en DSSA.
- Los predictores relevantes son distintos: en DCSA dominan los signos de alarma;
  en DSSA la señal clínica es más débil y los factores no clínicos pueden ser más informativos.
- Un modelo único necesitaría CLASFINAL como predictor (ver DA-02).

---

## DA-04 · Uso de SMOTE para el desbalance de clases
**Notebooks:** `03_modelado/`  
**Decisión:** Aplicar SMOTE solo sobre X_train (nunca sobre el conjunto de prueba).  
**Justificación:** SMOTE genera ejemplos sintéticos interpolando entre vecinos reales
en el espacio de características. Aplicarlo al test set produciría fuga de datos (data leakage).
Se prefiere SMOTE sobre pesos de clase (class_weight) porque en boosters la combinación
SMOTE + pesos proporciona más estabilidad en las métricas de validación.  
**Parámetros:** k_neighbors=5 (default conservador).

---

## DA-05 · Métrica primaria según estrato clínico
**Notebooks:** `03_modelado/`  
**Decisión:**  
- DCSA → F1-score (clase positiva = hospitalizado)  
- DSSA → Balanced Accuracy + AUC-PR (Average Precision)  

**Justificación:**  
- En DCSA el desbalance es moderado (65/35): F1 equilibra precisión y sensibilidad.
- En DSSA el desbalance es severo (~92/8): AUC-ROC es engañosamente alto (un modelo
  que predice "nunca hospitalizar" tiene AUC~0.5 pero accuracy~92%). AUC-PR penaliza
  adecuadamente los falsos negativos en la clase minoritaria.

---

## DA-06 · Control del sesgo temporal 2017–2020
**Notebooks:** `01_eda/`, `03_modelado/`  
**Decisión:** Incluir `AÑO` como predictor en los modelos de ML. Realizar análisis de
sensibilidad excluyendo el período 2017–2020.  
**Justificación:** Entre 2017–2020, >95% de registros se clasificaron como DCSA con
ausencia casi total de DSSA/Grave. Simultáneamente, la tasa de hospitalización en DCSA
fue anómalamente baja (<45% vs >83% desde 2021). Esto sugiere un cambio en el protocolo
de clasificación o en la completitud del reporte. Ignorar este sesgo puede producir
modelos que aprendan el año como proxy de la clasificación, no de la gravedad clínica.

---

## DA-07 · Permutation Importance sobre Feature Importance intrínseca
**Notebooks:** `03_modelado/`  
**Decisión:** Usar permutation_importance de scikit-learn para la interpretación de modelos.  
**Justificación:**
- La feature importance intrínseca de Random Forest y boosters sobreestima variables
  de alta cardinalidad y variables correlacionadas.
- Permutation importance mide el impacto real en la métrica de interés (F1) al permutar
  aleatoriamente cada variable, siendo agnóstica del modelo y comparable entre algoritmos.
- n_repeats=20 garantiza estimaciones estables.

---

## DA-08 · Uso de statsmodels (no scikit-learn) para modelos explicativos
**Notebook:** `02_analisis_clinico/02b_regresion_logistica_clinica.ipynb`  
**Decisión:** Usar statsmodels para los modelos de regresión logística del análisis clínico.  
**Justificación:** statsmodels provee OR directamente como exp(coef), IC95% por
verosimilitud de perfil, p-valores de Wald, AIC/BIC y pseudo-R² de McFadden.
scikit-learn no proporciona estos estadísticos de forma nativa y está orientado
a predicción, no a inferencia estadística.

---

## DA-09 · Distancia utilizada en clustering jerárquico
**Notebook:** `04_clustering/04_analisis_no_supervisado.ipynb`  
**Decisión:** Usar linkage='ward' con distancia euclidiana sobre variables escaladas.  
**Justificación:** Aunque las variables clínicas son binarias, después de StandardScaler
la distancia euclidiana es una aproximación práctica. La distancia de Jaccard sería más
apropiada teóricamente, pero scipy.cluster.hierarchy con Jaccard no soporta Ward.
Se documenta como limitación metodológica.

---

## DA-10 · Partición temporal vs aleatoria
**Notebooks:** `03_modelado/`  
**Decisión:** Usar partición ALEATORIA estratificada (no temporal).  
**Justificación:** Una partición temporal (entrenar 2015–2021, testear 2022–2023) sería
más realista para evaluar capacidad de generalización a brotes futuros. Sin embargo,
el sesgo 2017–2020 complica la partición temporal: el conjunto de entrenamiento
contendría datos de distinta naturaleza. Se opta por la partición aleatoria estratificada
y se documenta como trabajo futuro la validación temporal cruzada (year-out CV).
