"""
Configuración central — Predicción de Hospitalización por Dengue, Bucaramanga.

Este módulo es importado por todos los notebooks del pipeline para garantizar
coherencia en rutas, semillas aleatorias, variables y parámetros visuales.

Uso en notebooks:
    import sys
    sys.path.insert(0, "../../src")  # ajustar nivel según profundidad del notebook
    import config
    from config import DATA_RAW, RANDOM_STATE, SIGNOS_ALARMA
"""

from pathlib import Path

# ── Rutas del proyecto ────────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_RAW     = PROJECT_ROOT / "data" / "raw"
DATA_INTERIM = PROJECT_ROOT / "data" / "interim"
DATA_PROC    = PROJECT_ROOT / "data" / "processed"
OUT_FIGURES  = PROJECT_ROOT / "outputs" / "figures"
OUT_TABLES   = PROJECT_ROOT / "outputs" / "tables"
OUT_MODELS   = PROJECT_ROOT / "outputs" / "models"
CHECKPOINTS  = PROJECT_ROOT / "outputs" / "checkpoints"

# Crear directorios si no existen
for _path in [DATA_RAW, DATA_INTERIM, DATA_PROC,
              OUT_FIGURES, OUT_TABLES, OUT_MODELS, CHECKPOINTS]:
    _path.mkdir(parents=True, exist_ok=True)

# ── Reproducibilidad ──────────────────────────────────────────────────────────
RANDOM_STATE = 42
TEST_SIZE    = 0.20   # 80/20 estratificado
CV_FOLDS     = 5      # K-fold estratificado

# ── Variable objetivo ─────────────────────────────────────────────────────────
TARGET_COL = "TARGET_HOSPITALIZACION_ORIGINAL"
# 1 = hospitalizado, 0 = no hospitalizado

# ── Etiquetas de clasificación SIVIGILA ───────────────────────────────────────
CLASFINAL_CON_SIGNOS = "DENGUE CON SIGNOS DE ALARMA"
CLASFINAL_SIN_SIGNOS = "DENGUE SIN SIGNOS DE ALARMA"
CLASFINAL_GRAVE      = "DENGUE GRAVE"
CLASFINAL_MORTALIDAD = "MORTALIDAD POR DENGUE"

# ── Variables clínicas ────────────────────────────────────────────────────────
# Signos de alarma OMS: predictores primarios de dengue grave/hospitalización
SIGNOS_ALARMA = [
    "DOLOR_ABDO",   # Dolor abdominal intenso
    "VOMITO",       # Vómito persistente
    "DIARREA",      # Diarrea
    "SOMNOLENCI",   # Somnolencia / irritabilidad
    "HIPOTENSIO",   # Hipotensión postural
    "HEPATOMEG",    # Hepatomegalia
    "HEM_MUCOSA",   # Hemorragia de mucosas
    "HIPOTERMIA",   # Hipotermia
    "AUM_HEMATO",   # Aumento del hematocrito
    "CAIDA_PLAQ",   # Caída rápida de plaquetas
    "ACUM_LIQUI",   # Acumulación de líquidos
]

# Síntomas generales del dengue (fase febril)
SINTOMAS_GENERALES = [
    "FIEBRE",       # Fiebre (>95% de prevalencia — alta colinealidad)
    "CEFALEA",      # Cefalea intensa
    "DOLRRETROO",   # Dolor retroocular
    "MALGIAS",      # Mialgias
    "ARTRALGIA",    # Artralgias
    "ERUPCIONR",    # Erupción cutánea
]

# Variables demográficas y socioeconómicas
VARIABLES_DEMOGRAFICAS = [
    "SEXO_",        # 1=Masculino, 2=Femenino
    "DEF_CLAS_EDAD",# Grupo etario definido
    "TIP_SS_",      # Tipo de seguridad social (1=Contributivo, 2=Subsidiado, ...)
    "ESTRATO_",     # Estrato socioeconómico (1-6)
    "GP_GESTAN",    # Gestante (1=sí, 2=no)
    "GRUPO_ETARIO", # Grupo etario SIVIGILA
]

VARIABLES_TEMPORALES = ["AÑO", "SEMANA"]

# ── Período con posible sesgo estructural ─────────────────────────────────────
# Entre 2017-2020 hubo una concentración anómala de clasificaciones DCSA
# y ausencia de DSSA/Grave. Controlar en modelos o evaluar en análisis de
# sensibilidad incluyendo / excluyendo este período.
PERIODO_SOSPECHOSO = (2017, 2020)

# ── Paleta de colores del proyecto ───────────────────────────────────────────
COLORS = {
    "primary":             "#2C7BB6",   # Azul: clase negativa (no hospitalizado)
    "secondary":           "#D7191C",   # Rojo: clase positiva (hospitalizado)
    "accent":              "#FDAE61",   # Naranja: destacados / demográficas
    "neutral":             "#7F7F7F",   # Gris: referencias
    "background":          "#F8F9FA",   # Fondo suave
    "con_signos":          "#E74C3C",   # Dengue con signos de alarma
    "sin_signos":          "#3498DB",   # Dengue sin signos de alarma
    "grave":               "#8E44AD",   # Dengue grave
    "mortalidad":          "#2C3E50",   # Mortalidad
}

PALETTE_HOSPIT = [COLORS["primary"], COLORS["secondary"]]

# ── Estilos para figuras Q1 ───────────────────────────────────────────────────
RCPARAMS_Q1 = {
    "figure.dpi":          150,
    "savefig.dpi":         300,
    "figure.facecolor":    "white",
    "axes.facecolor":      "white",
    "axes.spines.top":     False,
    "axes.spines.right":   False,
    "axes.titlesize":      14,
    "axes.titleweight":    "bold",
    "axes.labelsize":      12,
    "xtick.labelsize":     10,
    "ytick.labelsize":     10,
    "legend.fontsize":     10,
    "legend.frameon":      False,
    "font.family":         "DejaVu Sans",
    "axes.grid":           True,
    "grid.alpha":          0.3,
}
