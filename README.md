# Predicción de Hospitalización por Dengue en Bucaramanga

---

##  Descripción del Proyecto

Este repositorio contiene el pipeline completo de análisis de datos para la predicción de hospitalización por dengue en el municipio de **Bucaramanga, Colombia**, a partir de datos epidemiológicos del Sistema Nacional de Vigilancia en Salud Pública (SIVIGILA).

El objetivo central es desarrollar modelos de clasificación supervisada capaces de identificar, al momento de la notificación, qué pacientes con dengue requieren hospitalización. El análisis se estratifica por clasificación clínica:

- **Dengue con signos de alarma (DCSA)**
- **Dengue sin signos de alarma (DSSA)**

---

##  Estructura del Repositorio

```
dengue_maestria/
│
├── data/
│   ├── raw/                        # Datos originales sin modificar
│   │   └── datos_dengue_bucaramanga_depurado.csv
│   ├── interim/                    # Datos intermedios (post-limpieza, pre-features)
│   │   ├── datos_con_signos.pkl
│   │   └── datos_sin_signos.pkl
│   └── processed/                  # Datos listos para modelado
│       ├── X_train_con_signos.pkl
│       ├── X_test_con_signos.pkl
│       ├── X_train_sin_signos.pkl
│       └── X_test_sin_signos.pkl
│
├── notebooks/
│   ├── 00_setup/
│   │   └── 00_entorno_y_dependencias.ipynb      # Instalación y verificación del entorno
│   │
│   ├── 01_eda/
│   │   └── 01_exploracion_general.ipynb         # EDA completo sobre todas las categorías
│   │
│   ├── 02_analisis_clinico/
│   │   ├── 02a_analisis_univariado_bivariado.ipynb  # Análisis estadístico de síntomas
│   │   └── 02b_regresion_logistica_clinica.ipynb    # Odds Ratios y modelos explicativos
│   │
│   ├── 03_modelado/
│   │   ├── con_signos/
│   │   │   └── 03_modelado_con_signos.ipynb   # DCSA · baseline + portafolio + evaluación final
│   │   └── sin_signos/
│   │       └── 03_modelado_sin_signos.ipynb   # DSSA · baseline + portafolio + evaluación final
│   │
│   ├── 04_clustering/
│   │   └── 04_analisis_no_supervisado.ipynb     # KMeans + Clustering jerárquico
│   │
│   └── 05_reportes/
│       └── 05_resultados_consolidados.ipynb     # Síntesis final de hallazgos
│
├── outputs/
│   ├── figures/                    # Gráficas exportadas en alta resolución (300 dpi)
│   ├── tables/                     # Tablas exportadas en CSV y Excel
│   ├── models/                     # Modelos entrenados serializados (.pkl, .json)
│   └── checkpoints/                # Estados intermedios para reproducibilidad
│
├── src/
│   ├── config.py                   # Rutas, semillas, hiperparámetros globales
│   ├── preprocessing.py            # Funciones de limpieza y transformación
│   ├── features.py                 # Ingeniería de variables
│   ├── modeling.py                 # Entrenamiento y evaluación de modelos
│   └── visualization.py            # Funciones de visualización Q1
│
├── docs/
│   ├── diccionario_variables.md    # Descripción de todas las variables SIVIGILA
│   └── decisiones_analiticas.md    # Registro de decisiones metodológicas
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

##  Flujo Analítico

```
[Datos SIVIGILA] 
      ↓
[00_setup] → Entorno reproducible
      ↓
[01_EDA] → Exploración, calidad, temporalidad
      ↓
[02_Análisis Clínico] → Estadística descriptiva, OR, modelos explicativos
      ↓
[03_Modelado] → Clasificación supervisada por estrato clínico
      ↓
[04_Clustering] → Segmentación no supervisada de perfiles de riesgo
      ↓
[05_Reportes] → Síntesis, visualizaciones finales, tabla comparativa
```

---

##  Instalación

```bash
git clone https://github.com/usuario/dengue_maestria.git
cd dengue_maestria
pip install -r requirements.txt
```

---

##  Datos

- **Fuente:** SIVIGILA — Instituto Nacional de Salud, Colombia
- **Municipio:** Bucaramanga, Santander
- **Período:** 2015–2023
- **Registros:** ~36,000 casos notificados
- **Variables:** 82 columnas (demográficas, clínicas, epidemiológicas)
- **Variable objetivo:** `TARGET_HOSPITALIZACION_ORIGINAL` (1 = hospitalizado, 0 = ambulatorio)

> **Nota de privacidad:** Los datos han sido anonimizados conforme a los lineamientos del INS. No se incluyen identificadores personales.

---

##  Contexto Clínico

La OMS clasifica el dengue en tres categorías:
1. **Sin signos de alarma** — manejo ambulatorio en la mayoría de casos
2. **Con signos de alarma** — requiere observación hospitalaria cercana
3. **Dengue grave** — requiere hospitalización inmediata

La predicción de hospitalización en los estratos 1 y 2 es crítica para la gestión de recursos hospitalarios durante picos epidémicos.

---

##  Métricas Principales

| Estrato | Métrica primaria | Justificación |
|---|---|---|
| DCSA | F1-score (clase positiva) | Balance entre sensibilidad y precisión en clase mayoritaria hospitalizada |
| DSSA | Balanced Accuracy + AUC-PR | Desbalance severo (~8% hospitalizados); relevancia clínica de falsos negativos |


