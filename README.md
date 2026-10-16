# Predicción de Hospitalización por Dengue en Bucaramanga
Análisis Avanzado de Datos en Salud Pública

---

## Descripción del Proyecto

Este repositorio contiene el pipeline completo de análisis de datos para la predicción de hospitalización por dengue en el municipio de **Bucaramanga, Colombia**, a partir de datos epidemiológicos del Sistema Nacional de Vigilancia en Salud Pública (SIVIGILA).

El objetivo central es desarrollar modelos de clasificación supervisada capaces de identificar, al momento de la consulta, qué pacientes con dengue requieren hospitalización. El análisis se estratifica por clasificación clínica:

- **Dengue con signos de alarma (DCSA)** — 12,713 casos · 64.8% hospitalización
- **Dengue sin signos de alarma (DSSA)** — 15,734 casos · 3.9% hospitalización

---

## Estructura del Repositorio

```
dengue_maestria/
│
├── data/
│   ├── raw/
│   │   └── datos_dengue_bucaramanga_depurado.csv   # Datos originales SIVIGILA 2015–2025
│   ├── interim/                                     # Subcohortes por estrato clínico
│   │   ├── datos_con_signos.pkl                     # DCSA
│   │   └── datos_sin_signos.pkl                     # DSSA
│   └── processed/                                   # Particiones train/test
│       ├── particion_DCSA.pkl
│       └── particion_DSSA.pkl
│
├── notebooks/
│   ├── 00_setup/
│   │   └── 00_entorno_y_dependencias.ipynb          # Instalación y verificación del entorno
│   │
│   ├── 01_eda/
│   │   └── 01_exploracion_general.ipynb             # EDA completo · calidad · temporalidad
│   │
│   ├── 02_analisis_clinico/
│   │   ├── 02a_analisis_univariado_bivariado.ipynb  # OR crudos · forest plots · heatmaps
│   │   └── 02b_regresion_logistica_clinica.ipynb    # OR ajustados · VIF · modelos anidados
│   │
│   ├── 03_modelado/
│   │   ├── con_signos/
│   │   │   ├── 03a_modelado_con_signos.ipynb        # DCSA · baseline + portafolio + evaluación
│   │   │   └── 03b_validacion_temporal_con_signos.ipynb  # DCSA · validación 2015-2021 → 2022-2025
│   │   └── sin_signos/
│   │       ├── 03c_modelado_sin_signos.ipynb        # DSSA · baseline + portafolio + evaluación
│   │       └── 03d_validacion_temporal_sin_signos.ipynb  # DSSA · validación temporal
│   │
│   ├── 04_clustering/
│   │   └── 04_analisis_no_supervisado.ipynb         # KMeans + clustering jerárquico + PCA
│   │
│   └── 05_reportes/
│       └── 05_resultados_consolidados.ipynb         # Síntesis final · tabla comparativa
│
├── outputs/
│   ├── figures/        # Figuras exportadas 300 dpi
│   ├── tables/         # Tablas CSV
│   ├── models/         # Modelos serializados .pkl
│   └── checkpoints/    # Estados intermedios para no repetir cálculos costosos
│
├── src/
│   └── config.py       # Rutas · semillas · variables · paleta de colores
│
├── docs/
│   ├── diccionario_variables.md    # 82 variables SIVIGILA documentadas
│   └── decisiones_analiticas.md   # Registro de decisiones metodológicas
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Flujo Analítico

```
[Datos SIVIGILA 2015–2025 · 28,626 casos · 82 variables]
      ↓
[00_setup]          → Entorno reproducible · dependencias fijadas
      ↓
[01_EDA]            → Calidad del dato · correcciones auditadas · sesgo temporal
      ↓
[02_Análisis Clínico] → OR crudos y ajustados · VIF · modelos explicativos
      ↓
[03_Modelado DCSA]  → Baseline → portafolio 9 modelos → validación temporal
      ↓
[04_Clustering]     → Segmentación no supervisada de perfiles de riesgo
      ↓
[05_Reportes]       → Síntesis · comparativa DCSA vs DSSA · recomendaciones
```

---

## Instalación

```bash
git clone https://github.com/usuario/dengue_maestria.git
cd dengue_maestria
pip install -r requirements.txt
```

Antes de ejecutar cualquier notebook, copia el CSV a `data/raw/`:
```
data/raw/datos_dengue_bucaramanga_depurado.csv
```
Luego ejecuta `00_entorno_y_dependencias.ipynb` completo.

---

## Datos

| Atributo | Detalle |
|----------|---------|
| Fuente | SIVIGILA — Instituto Nacional de Salud, Colombia |
| Municipio | Bucaramanga, Santander |
| Período | 2015–2025 |
| Registros | 28,626 casos notificados |
| Variables | 82 columnas (demográficas, clínicas, epidemiológicas) |
| Variable objetivo | `TARGET_HOSPITALIZACION_ORIGINAL` (1=hospitalizado, 0=ambulatorio) |

> **Nota de privacidad:** Los datos han sido anonimizados conforme a los lineamientos del INS. No se incluyen identificadores personales.

---

## Contexto Clínico

La OMS clasifica el dengue en tres categorías:
1. **Sin signos de alarma (DSSA)** — manejo ambulatorio en la mayoría de casos
2. **Con signos de alarma (DCSA)** — requiere observación hospitalaria cercana
3. **Dengue grave** — requiere hospitalización inmediata

La predicción de hospitalización en los estratos DSSA y DCSA es crítica para la gestión de recursos hospitalarios durante picos epidémicos. Bucaramanga registró un incremento sostenido en la tasa de hospitalización DCSA del 19.7% (2015) al 89.1% (2025), asociado a cambios en los protocolos de clasificación del INS.

---

## Métricas y Estrategia por Estrato

| Estrato | Desbalance | Métrica primaria | Justificación |
|---------|-----------|-----------------|---------------|
| DCSA | 65% / 35% | F1-score | Desbalance moderado — F1 equilibra precisión y sensibilidad |
| DSSA | 96% / 4% | AUC-PR | Desbalance severo — AUC-ROC es engañosamente alto; AUC-PR penaliza falsos negativos en clase minoritaria |

---






