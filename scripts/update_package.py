
import os
from pathlib import Path
import shutil
import subprocess
import sys

from pydicom import __version__


BASE_DIRECTORY = Path(__file__).parent.parent
SRC_DIRECTORY = BASE_DIRECTORY / "custom"
DST_DIRECTORY = BASE_DIRECTORY / "src" / "pydicom-stubs"
PYDICOM_DIRECTORY = BASE_DIRECTORY.parent / "pydicom" / "src" / "pydicom"


REMOVALS = [
    DST_DIRECTORY / "pixels" / "decoders" / "gdcm.pyi",
    DST_DIRECTORY / "pixels" / "decoders" / "pillow.pyi",
    DST_DIRECTORY / "pixels" / "decoders" / "pyjpegls.pyi",
    DST_DIRECTORY / "pixels" / "decoders" / "pylibjpeg.pyi",
    DST_DIRECTORY / "pixels" / "decoders" / "rle.pyi",
    DST_DIRECTORY / "pixels" / "encoders" / "gdcm.pyi",
    DST_DIRECTORY / "pixels" / "encoders" / "native.pyi",
    DST_DIRECTORY / "pixels" / "encoders" / "pyjpegls.pyi",
    DST_DIRECTORY / "pixels" / "encoders" / "pylibjpeg.pyi",
    DST_DIRECTORY / "pixel_data_handlers" / "gdcm_handler.pyi",
    DST_DIRECTORY / "pixel_data_handlers" / "jpeg_ls_handler.pyi",
    DST_DIRECTORY / "pixel_data_handlers" / "numpy_handler.pyi",
    DST_DIRECTORY / "pixel_data_handlers" / "pillow_handler.pyi",
    DST_DIRECTORY / "pixel_data_handlers" / "pylibjpeg_handler.pyi",
    DST_DIRECTORY / "pixel_data_handlers" / "rle_handler.pyi",
]


def update_stubs() -> None:
    # Clear out the stub files
    if DST_DIRECTORY.exists():
        shutil.rmtree(DST_DIRECTORY)

    if (BASE_DIRECTORY / "pydicom").exists():
        shutil.rmtree(BASE_DIRECTORY / "pydicom")

    print("Generating basic stub files with stubgen")
    p = subprocess.run(
        [f"stubgen {os.fspath(PYDICOM_DIRECTORY)} -o ."],
        shell=True,
    )

    if p.returncode != 0:
        print("  Failed to generate the basic stub files")
        sys.exit(1)

    print(f"Moving basic stub files to {DST_DIRECTORY}")
    shutil.move(BASE_DIRECTORY / "pydicom", DST_DIRECTORY)

    print("Generating custom stub files")
    if not SRC_DIRECTORY.exists():
        SRC_DIRECTORY.mkdir(parents=True, exist_ok=True)

    subprocess.run(["python scripts/generate_stubs.py"], shell=True)

    print("Replacing basic stub files with custom ones")
    for path in SRC_DIRECTORY.glob("*.pyi"):
        shutil.copyfile(path, DST_DIRECTORY / path.name)

    print("Removing unnecessary stubs")
    for path in REMOVALS:
        path.unlink(missing_ok=True)


def update_version() -> None:
    # Get the current package version
    typd_version = ""
    contents = []
    with open(BASE_DIRECTORY / "pyproject.toml", "r") as f:
        for line in f.readlines():
            contents.append(line.rstrip())
            if line.startswith("version = "):
                typd_version = line.rstrip()

    # types-pydicom version: X.Y.Z.N[.dev0]
    typd_version = typd_version.strip("version = ")
    typd_version = typd_version.strip("\"")
    print(f"Found current package version '{typd_version}'")
    typd_version = typd_version.split(".")
    if not typd_version or len(typd_version) < 3:
        raise RuntimeError(
            f"Unable to determine the current package version from '{typd_version}'"
        )

    # pydicom version: X.Y.Z[.dev0]
    pyd_version = __version__.strip().split(".")
    if len(pyd_version) not in (3, 4):
        raise RuntimeError(f"Unexpected pydicom version string '{pyd_version}'")

    # Determine new package version
    if pyd_version[-1] == "dev0":
        # If pydicom is dev0 then use X.Y.Z.0.dev0:
        version = f"{'.'.join(pyd_version[:-1])}.0.dev0"
    elif pyd_version == typd_version[:3]:
        # If X.Y.Z match -> increment N
        version = f"{'.'.join(pyd_version)}.{int(typd_version[3]) + 1}"
    else:
        # If X.Y.Z don't match, use X.Y.Z.0
        version = f"{'.'.join(pyd_version)}.0"

    if version.split(".") == typd_version:
        print(f"No package version change required")
        return

    print(f"Changing package version to '{version}'")
    for idx, line in enumerate(contents):
        if line.startswith("version = "):
            contents[idx] = f"version = \"{version}\""
            break

    with open(BASE_DIRECTORY / "pyproject.toml", "w") as f:
        f.write("\n".join(contents))


if __name__ == "__main__":
    update_stubs()
    update_version()
