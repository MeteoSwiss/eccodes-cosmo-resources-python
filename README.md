# eccodes-cosmo-resources-python

[![PyPI - Version](https://img.shields.io/pypi/v/eccodes-cosmo-resources-python.svg)](https://pypi.org/project/eccodes-cosmo-resources-python)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/eccodes-cosmo-resources-python.svg)](https://pypi.org/project/eccodes-cosmo-resources-python)

-----

## Installation

```console
pip install eccodes-cosmo-resources-python
```

## Usage

```python
import eccodes
import eccodes_cosmo_resources

vendor = eccodes.codes_definition_path()
cosmo = eccodes_cosmo_resources.get_definitions_path()
eccodes.set_definition_path(f"{cosmo}:{vendor}")
```
