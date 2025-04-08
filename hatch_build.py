"""Custom build hook to dereference symlinks in the defintions."""

import shutil
import tarfile
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Callable

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


def common_root(names: list[str], abort: Callable[[str], None]) -> str:
    common = None
    for name in names:
        if common is None:
            common, *_ = Path(name).parts
            continue
        current, *_ = Path(name).parts
        if current != common:
            raise ValueError("non matching root")
    return common


@contextmanager
def unpack_definitions(abort: Callable[[str], None]) -> str:
    if (root := Path("eccodes-cosmo-resources")).exists():
        yield str(root / "definitions")
        return

    [path] = Path(".").glob("eccodes_definitions*.tar.bz2")
    with tarfile.open(path, "r:bz2") as tar:
        root = common_root(tar.getnames(), abort)
        if not root.startswith("definitions"):
            abort("")
        tar.extractall(filter="data")
    try:
        yield root
    finally:
        shutil.rmtree(root)


class CustomBuildHook(BuildHookInterface):
    def initialize(
        self,
        version: str,
        build_data: dict[str, Any],
    ) -> None:
        with unpack_definitions(self.app.abort) as root:
            shutil.copytree(
                root,
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
