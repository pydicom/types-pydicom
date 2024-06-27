from _typeshed import Incomplete
from collections.abc import MutableSequence, Sequence
from pydicom import config as config
from pydicom.dataelem import DataElement as DataElement
from pydicom.misc import warn_and_log as warn_and_log
from pydicom.valuerep import CUSTOMIZABLE_CHARSET_VR as CUSTOMIZABLE_CHARSET_VR, PersonName as PersonName, TEXT_VR_DELIMS as TEXT_VR_DELIMS, VR as VR

default_encoding: str
python_encoding: Incomplete
STAND_ALONE_ENCODINGS: Incomplete
ESC: bytes
CODES_TO_ENCODINGS: Incomplete
ENCODINGS_TO_CODES: Incomplete
handled_encodings: Incomplete
need_tail_escape_sequence_encodings: Incomplete
custom_encoders: Incomplete

def decode_bytes(value: bytes, encodings: Sequence[str], delimiters: set[int]) -> str: ...
decode_string = decode_bytes

def encode_string(value: str, encodings: Sequence[str]) -> bytes: ...
def convert_encodings(encodings: None | str | MutableSequence[str]) -> list[str]: ...
def decode_element(elem: DataElement, dicom_character_set: str | list[str] | None) -> None: ...
