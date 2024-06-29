
from pathlib import Path
from typing import Any

from pydicom._dicom_dict import DicomDictionary

BASE_DIRECTORY = Path(__file__).parent.parent
DS_DST = BASE_DIRECTORY / "custom" / "dataset.pyi"
DS_SRC = BASE_DIRECTORY / "src" / "pydicom-stubs" / "dataset.pyi"


ElementDictType = dict[int, tuple[str, str, str, str]]


def generate_dataset_hints(d: ElementDictType, indent: str = "    ") -> list[str]:
    """Generate element type hints for the Dataset class."""
    exclusions = {
        "FileMetaInformationGroupLength",
        "FileMetaInformationVersion",
        "MediaStorageSOPClassUID",
        "MediaStorageSOPInstanceUID",
        "TransferSyntaxUID",
        "ImplementationClassUID",
        "ImplementationVersionName",
        "SourceApplicationEntityTitle",
        "SendingApplicationEntityTitle",
        "ReceivingApplicationEntityTitle",
        "SourcePresentationAddress",
        "ReceivingPresentationAddress",
        "PrivateInformationCreatorUID",
        "PrivateInformation",
        "SamplesPerPixel",
        "PlanarConfiguration",
        "PhotometricInterpretation",
        "Rows",
        "Columns",
        "BitsAllocated",
        "BitsStored",
        "HighBit",
        "PixelRepresentation",
    }
    custom_hints = [
        "# Keyword: type hint  # VR, VM, Type",
        "# Part 10, 7.1: File Meta Information Elements"
        "FileMetaInformationGroupLength: int  # UL, 1, 1",
        "FileMetaInformationVersion: bytes  # OB, 1, 1",
        "MediaStorageSOPClassUID: str | UID  # UI, 1, 1",
        "MediaStorageSOPInstanceUID: str | UID  # UI, 1, 1",
        "TransferSyntaxUID: str | UID  # UI, 1, 1",
        "ImplementationClassUID: str | UID  # UI, 1, 1",
        "ImplementationVersionName: str | None  # SH, 1, 3",
        "SourceApplicationEntityTitle: str | None  # AE, 1, 3",
        "SendingApplicationEntityTitle: str | None  # AE, 1, 3",
        "ReceivingApplicationEntityTitle: str | None  # AE, 1, 3",
        "SourcePresentationAddress: str | None  # UR, 1, 3",
        "ReceivingPresentationAddress: str | None  # UR, 1, 3",
        "PrivateInformationCreatorUID: str | UID | None  # UI, 1, 3",
        "PrivateInformation: bytes  # OB, 1, 1C",
        "",
        "# Part 3, C.7.6.3.3: Image Pixel Description Macro",
        "SamplesPerPixel: int  # US, 1, 1",
        "PlanarConfiguration: int  # US, 1, 1C",
        "PhotometricInterpretation: str  # CS, 1, 1",
        "Rows: int  # US, 1, 1",
        "Columns: int  # US, 1, 1",
        "BitsAllocated: int  # US, 1, 1",
        "BitsStored: int  # US, 1, 1",
        "HighBit: int  # US, 1, 1",
        "PixelRepresentation: int  # US, 1, 1",
        "",
        "# Part 6, Table 6-1: All other public elements",
    ]

    hints = [f"{indent}{hint}\n" for hint in custom_hints]
    for tag, (vr, vm, name, retired, keyword) in d.items():
        if (
            not keyword
            or keyword in exclusions
            or retired == "Retired"
            or vr == "NONE"
        ):
            continue

        if len(vr) > 2:
            # Ambiguous VRs
            vr = vr.replace(" or ", "_")
            hints.append(f"{indent}{keyword}: {vr}_Type\n")
            continue

        if vr == "SQ":
            hints.append(f"{indent}{keyword}: SQType\n")
            continue

        if vm == "1":
            hints.append(f"{indent}{keyword}: {vr}_1_Type\n")
        elif vm == "1-n":
            hints.append(f"{indent}{keyword}: {vr}_1N_Type\n")
        else:
            hints.append(f"{indent}{keyword}: {vr}_N_Type\n")

    return hints


def write_dataset_stub(d: ElementDictType) -> None:
    """Update the custom/dataset.pyi file."""

    modified = []
    modified.append("from pydicom._type_definitions import *\n")

    with open(DS_SRC, 'r') as f:
        for idx, line in enumerate(f.readlines()):
            modified.append(line)
            if line.startswith("class Dataset:"):
                modified.append("    # Auto-generated class attributes below\n")
                modified.append("\n")
                modified.extend(generate_dataset_hints(d))
                modified.append("\n")
                modified.append("    # Auto-generated class attributes above\n")
                modified.append("\n")

    with open(DS_DST, "w") as f:
        f.write("".join(modified))


if __name__ == "__main__":
    write_dataset_stub(DicomDictionary)
