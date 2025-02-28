from pathlib import Path


def get_definitions_path() -> Path:
    here = Path(__file__)
    return here / "eccodes-cosmo-resources/definitions"
