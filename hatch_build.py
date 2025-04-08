"""Custom build hook to dereference symlinks in the defintions."""

import shutil
import tarfile
from pathlib import Path
from typing import Any

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


def common_root(names: list[str]):
    common = None
    for name in names:
        if common is None:
            common, *_ = Path(name).parts
            continue
        current, *_ = Path(name).parts
        if current != common:
            raise ValueError("non matching root")
    return common


class CustomBuildHook(BuildHookInterface):
    def initialize(
        self,
        version: str,
        build_data: dict[str, Any],
    ) -> None:
        [path] = Path(".").glob("eccodes_definitions*.tar.bz2")
        with tarfile.open(path, "r:bz2") as tar:
            root = common_root(tar.getnames())
            if not root.startswith("definitions"):
                raise RuntimeError
            tar.extractall(filter="data")
        shutil.copytree(
            root,
            "tmp",
            symlinks=False,
            dirs_exist_ok=True,
        )
        shutil.rmtree(root)

    def finalize(
        self,
        version: str,
        build_data: dict[str, Any],
        artifact_path: str,
    ) -> None:
        shutil.rmtree("tmp", ignore_errors=True)
