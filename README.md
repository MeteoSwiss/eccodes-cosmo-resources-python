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

## Credits

The eccodes_definitions.edzw on https://opendata.dwd.de are provided under the CC BY 4.0 license (https://creativecommons.org/licenses/by/4.0/) and the attribution rules apply if you use it (e.g. https://wiki.creativecommons.org/wiki/License_Versions#Attribution_reasonable_to_means.2C_medium.2C_and_context ); the owner is the DWD.
