import datetime
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterator, Sequence
from decimal import Decimal
from enum import Enum
from pydicom import config as config
from pydicom.misc import warn_and_log as warn_and_log
from typing import Any

default_encoding: str
TEXT_VR_DELIMS: Incomplete
PN_DELIMS: Incomplete
MAX_VALUE_LEN: Incomplete
VR_REGEXES: Incomplete
STR_VR_REGEXES: Incomplete
BYTE_VR_REGEXES: Incomplete

def validate_type(vr: str, value: Any, types: type | tuple[type, type]) -> tuple[bool, str]: ...
def validate_vr_length(vr: str, value: Any) -> tuple[bool, str]: ...
def validate_type_and_length(vr: str, value: Any) -> tuple[bool, str]: ...
def validate_regex(vr: str, value: Any) -> tuple[bool, str]: ...
def validate_type_and_regex(vr: str, value: Any) -> tuple[bool, str]: ...
def validate_date_time(vr: str, value: Any, date_time_type: type) -> tuple[bool, str]: ...
def validate_length_and_type_and_regex(vr: str, value: Any) -> tuple[bool, str]: ...
def validate_pn_component_length(vr: str, value: Any) -> tuple[bool, str]: ...
def validate_pn(vr: str, value: Any) -> tuple[bool, str]: ...
def validate_pn_component(value: str | bytes) -> None: ...

VALUE_LENGTH: Incomplete

def validate_number(vr: str, value: Any, min_value: int, max_value: int) -> tuple[bool, str]: ...

VALIDATORS: Incomplete

def validate_value(vr: str, value: Any, validation_mode: int, validator: Callable[[str, Any], tuple[bool, str]] | None = None) -> None: ...

class VR(str, Enum):
    AE = 'AE'
    AS = 'AS'
    AT = 'AT'
    CS = 'CS'
    DA = 'DA'
    DS = 'DS'
    DT = 'DT'
    FD = 'FD'
    FL = 'FL'
    IS = 'IS'
    LO = 'LO'
    LT = 'LT'
    OB = 'OB'
    OD = 'OD'
    OF = 'OF'
    OL = 'OL'
    OW = 'OW'
    OV = 'OV'
    PN = 'PN'
    SH = 'SH'
    SL = 'SL'
    SQ = 'SQ'
    SS = 'SS'
    ST = 'ST'
    SV = 'SV'
    TM = 'TM'
    UC = 'UC'
    UI = 'UI'
    UL = 'UL'
    UN = 'UN'
    UR = 'UR'
    US = 'US'
    UT = 'UT'
    UV = 'UV'
    US_SS_OW = 'US or SS or OW'
    US_SS = 'US or SS'
    US_OW = 'US or OW'
    OB_OW = 'OB or OW'

STANDARD_VR: Incomplete
AMBIGUOUS_VR: Incomplete
DEFAULT_CHARSET_VR: Incomplete
CUSTOMIZABLE_CHARSET_VR: Incomplete
BYTES_VR: Incomplete
FLOAT_VR: Incomplete
INT_VR: Incomplete
LIST_VR: Incomplete
STR_VR = DEFAULT_CHARSET_VR | CUSTOMIZABLE_CHARSET_VR
ALLOW_BACKSLASH: Incomplete
LONG_VALUE_VR: Incomplete
EXPLICIT_VR_LENGTH_16: Incomplete
EXPLICIT_VR_LENGTH_32: Incomplete
BUFFERABLE_VRS: Incomplete

class _DateTimeBase:
    original_string: str
    def __reduce_ex__(self, protocol: int) -> tuple[Any, ...]: ...

class DA(_DateTimeBase, datetime.date):
    def __new__(cls, *args: Any, **kwargs: Any) -> DA | None: ...
    original_string: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class DT(_DateTimeBase, datetime.datetime):
    def __new__(cls, *args: Any, **kwargs: Any) -> DT | None: ...
    original_string: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class TM(_DateTimeBase, datetime.time):
    def __new__(cls, *args: Any, **kwargs: Any) -> TM | None: ...
    original_string: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

def is_valid_ds(s: str) -> bool: ...
def format_number_as_ds(val: float | Decimal) -> str: ...

class DSfloat(float):
    auto_format: bool
    def __new__(cls, val: None | str | int | float | Decimal, auto_format: bool = False, validation_mode: int | None = None) -> str | DSfloat | None: ...
    original_string: Incomplete
    def __init__(self, val: str | int | float | Decimal, auto_format: bool = False, validation_mode: int | None = None) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: Any) -> Any: ...

class DSdecimal(Decimal):
    auto_format: bool
    def __new__(cls, val: None | str | int | float | Decimal, auto_format: bool = False, validation_mode: int | None = None) -> str | DSdecimal | None: ...
    original_string: Incomplete
    def __init__(self, val: str | int | float | Decimal, auto_format: bool = False, validation_mode: int | None = None) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: Any) -> Any: ...

DSclass: Any
DSclass = DSdecimal
DSclass = DSfloat

def DS(val: None | str | int | float | Decimal, auto_format: bool = False, validation_mode: int | None = None) -> None | str | DSfloat | DSdecimal: ...

class ISfloat(float):
    def __new__(cls, val: str | float | Decimal, validation_mode: int | None = None) -> float | str: ...
    original_string: Incomplete
    def __init__(self, val: str | float | Decimal, validation_mode: int | None = None) -> None: ...

class IS(int):
    def __new__(cls, val: None | str | int | float | Decimal, validation_mode: int | None = None) -> str | IS | ISfloat | None: ...
    original_string: Incomplete
    def __init__(self, val: str | int | float | Decimal, validation_mode: int | None = None) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other: Any) -> Any: ...

class PersonName:
    def __new__(cls, *args: Any, **kwargs: Any) -> PersonName | None: ...
    original_string: Incomplete
    encodings: Incomplete
    validation_mode: Incomplete
    def __init__(self, val: bytes | str | PersonName, encodings: Sequence[str] | None = None, original_string: bytes | None = None, validation_mode: int | None = None) -> None: ...
    @property
    def components(self) -> tuple[str, ...]: ...
    @property
    def family_name(self) -> str: ...
    @property
    def given_name(self) -> str: ...
    @property
    def middle_name(self) -> str: ...
    @property
    def name_prefix(self) -> str: ...
    @property
    def name_suffix(self) -> str: ...
    @property
    def alphabetic(self) -> str: ...
    @property
    def ideographic(self) -> str: ...
    @property
    def phonetic(self) -> str: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __contains__(self, x: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def decode(self, encodings: Sequence[str] | None = None) -> PersonName: ...
    def encode(self, encodings: Sequence[str] | None = None) -> bytes: ...
    def family_comma_given(self) -> str: ...
    def formatted(self, format_str: str) -> str: ...
    def __bool__(self) -> bool: ...
    @classmethod
    def from_named_components(cls, family_name: str | bytes = '', given_name: str | bytes = '', middle_name: str | bytes = '', name_prefix: str | bytes = '', name_suffix: str | bytes = '', family_name_ideographic: str | bytes = '', given_name_ideographic: str | bytes = '', middle_name_ideographic: str | bytes = '', name_prefix_ideographic: str | bytes = '', name_suffix_ideographic: str | bytes = '', family_name_phonetic: str | bytes = '', given_name_phonetic: str | bytes = '', middle_name_phonetic: str | bytes = '', name_prefix_phonetic: str | bytes = '', name_suffix_phonetic: str | bytes = '', encodings: list[str] | None = None) -> PersonName: ...
    @classmethod
    def from_named_components_veterinary(cls, responsible_party_name: str | bytes = '', patient_name: str | bytes = '', responsible_party_name_ideographic: str | bytes = '', patient_name_ideographic: str | bytes = '', responsible_party_name_phonetic: str | bytes = '', patient_name_phonetic: str | bytes = '', encodings: list[str] | None = None) -> PersonName: ...
