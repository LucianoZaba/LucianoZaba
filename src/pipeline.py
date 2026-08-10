import logging
from pathlib import Path

# --- Logger: para saber donde falla ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
    handlers=[
        logging.FileHandler("data/processed/log.txt"),
        logging.StreamHandler()
    ]
)
log = logging.getLogger("pipeline")

# --- Errores con nombre para saber el origen ---
class ReadError(Exception): pass
class CleanError(Exception): pass
class ExportError(Exception): pass

class Pipeline:
    """Orquestador central: todo pasa por aca."""
    def run(self, filepath: str):
        from . import processors  # import aca para evitar circulares
        
        try:
            log.info(f"[1/3] READER -> {filepath}")
            df = processors.read(filepath)

            log.info(f"[2/3] CLEANER -> {len(df)} filas")
            df = processors.clean(df)

            log.info(f"[3/3] EXPORTER")
            out = processors.export(df)
            
            log.info(f"OK -> {out}")
            return out

        except Exception as e:
            log.error(f"FALLO en {type(e).__name__}: {e}")
            raise
