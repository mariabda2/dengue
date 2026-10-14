"""Configuracion central del proyecto. Generado por 00_entorno.ipynb."""
from pathlib import Path

PROJECT_ROOT = Path(r"D:\Documentos\GitHub\dengue")
DATA_RAW     = PROJECT_ROOT / "data" / "raw"
DATA_INTERIM = PROJECT_ROOT / "data" / "interim"
DATA_PROC    = PROJECT_ROOT / "data" / "processed"
OUT_FIGURES  = PROJECT_ROOT / "outputs" / "figures"
OUT_TABLES   = PROJECT_ROOT / "outputs" / "tables"
OUT_MODELS   = PROJECT_ROOT / "outputs" / "models"
CHECKPOINTS  = PROJECT_ROOT / "outputs" / "checkpoints"
DATA_FILE    = DATA_RAW / "datos_dengue_bucaramanga_depurado.csv"

RANDOM_STATE = 42
TEST_SIZE    = 0.20
CV_FOLDS     = 5
TARGET_COL   = "TARGET_HOSPITALIZACION_ORIGINAL"

SIGNOS_ALARMA = [
    "DOLOR_ABDO","VOMITO","DIARREA","SOMNOLENCI",
    "HIPOTENSIO","HEPATOMEG","HEM_MUCOSA",
    "HIPOTERMIA","AUM_HEMATO","CAIDA_PLAQ","ACUM_LIQUI"
]
SINTOMAS_GENERALES = [
    "FIEBRE","CEFALEA","DOLRRETROO","MALGIAS","ARTRALGIA","ERUPCIONR"
]

COLORS = {
    "primary":   "#2C7BB6",
    "secondary": "#D7191C",
    "accent":    "#FDAE61",
    "neutral":   "#7F7F7F",
    "con_signos":"#E74C3C",
    "sin_signos":"#3498DB",
    "grave":     "#8E44AD",
}