from _typeshed import Incomplete
from collections.abc import Generator
from pydicom.dataelem import RawDataElement as RawDataElement
from typing import Any, Protocol

have_numpy: bool

class ElementCallback(Protocol):
    def __call__(self, raw_elem: RawDataElement, **kwargs: Any) -> RawDataElement: ...

use_DS_decimal: bool
data_element_callback: ElementCallback | None
data_element_callback_kwargs: dict[str, Any]

def reset_data_element_callback() -> None: ...
def DS_numpy(use_numpy: bool = True) -> None: ...
def DS_decimal(use_Decimal_boolean: bool = True) -> None: ...

use_DS_numpy: bool
use_IS_numpy: bool
allow_DS_float: bool
enforce_valid_values: bool
IGNORE: int
WARN: int
RAISE: int

class Settings:
    def __init__(self) -> None: ...
    @property
    def buffered_read_size(self) -> int: ...
    @buffered_read_size.setter
    def buffered_read_size(self, size: int) -> None: ...
    @property
    def reading_validation_mode(self) -> int: ...
    @reading_validation_mode.setter
    def reading_validation_mode(self, value: int) -> None: ...
    @property
    def writing_validation_mode(self) -> int: ...
    @writing_validation_mode.setter
    def writing_validation_mode(self, value: int) -> None: ...
    @property
    def infer_sq_for_un_vr(self) -> bool: ...
    @infer_sq_for_un_vr.setter
    def infer_sq_for_un_vr(self, value: bool) -> None: ...

settings: Incomplete

def disable_value_validation() -> Generator: ...
def strict_reading() -> Generator: ...

convert_wrong_length_to_UN: bool
datetime_conversion: bool
use_none_as_empty_text_VR_value: bool
replace_un_with_known_vr: bool
show_file_meta: bool
logger: Incomplete
pixel_data_handlers: Incomplete
APPLY_J2K_CORRECTIONS: bool
assume_implicit_vr_switch: bool
INVALID_KEYWORD_BEHAVIOR: str
INVALID_KEY_BEHAVIOR: str
debugging: bool

def debug(debug_on: bool = True, default_handler: bool = True) -> None: ...
def future_behavior(enable_future: bool = True) -> None: ...
