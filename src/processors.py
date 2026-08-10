import pandas as pd
from pathlib import Path
from .pipeline import ReadError, CleanError, ExportError, log

def read(path: str) -> pd.DataFrame:
    """Lee Excel. Falla -> ReadError"""
    try:
        log.info(f"Leyendo {path}")
        return pd.read_excel(path)
    except Exception as e:
        raise ReadError(f"No se pudo leer {path}: {e}")

def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Limpieza basica y profesional."""
    try:
        # 1. Normaliza nombres de columnas: " Precio " -> "precio"
        df.columns = [str(c).strip().lower() for c in df.columns]
        
        # 2. Elimina filas totalmente vacias
        df = df.dropna(how='all')
        
        # 3. Elimina duplicados
        df = df.drop_duplicates()
        
        return df
    except Exception as e:
        raise CleanError(f"Error limpiando datos: {e}")

def export(df: pd.DataFrame) -> Path:
    """Exporta resultado limpio."""
    try:
        out = Path("data/processed/reporte_limpio.xlsx")
        out.parent.mkdir(parents=True, exist_ok=True)
        df.to_excel(out, index=False)
        return out
    except Exception as e:
        raise ExportError(f"Error exportando: {e}")
