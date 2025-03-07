import sysconfig
from pathlib import Path


def get_definitions_path() -> Path:
    root = Path(sysconfig.get_path("data"))
    return root / "share/eccodes-cosmo-resources/definitions"
