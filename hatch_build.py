"""Custom build hook to dereference symlinks in the defintions."""

import shutil
from typing import Any

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    def initialize(
        self,
        version: str,
        build_data: dict[str, Any],
    ) -> None:
        shutil.copytree(
            "eccodes-cosmo-resources",
            "tmp",
            symlinks=False,
            dirs_exist_ok=True,
        )

    def finalize(
        self,
        version: str,
        build_data: dict[str, Any],
        artifact_path: str,
    ) -> None:
        shutil.rmtree("tmp", ignore_errors=True)
