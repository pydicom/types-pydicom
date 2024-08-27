from _typeshed import Incomplete
from collections.abc import Callable as Callable, MutableSequence
from pydicom import config as config
from pydicom.datadict import dictionary_VR as dictionary_VR, private_dictionary_VR as private_dictionary_VR
from pydicom.dataelem import RawDataElement as RawDataElement
from pydicom.dataset import Dataset as Dataset
from pydicom.errors import BytesLengthException as BytesLengthException
from pydicom.misc import warn_and_log as warn_and_log
from pydicom.tag import BaseTag as BaseTag
from pydicom.valuerep import VR as VR
from typing import Any, Protocol

class RawDataHook(Protocol):
    def __call__(self, raw: RawDataElement, data: dict[str, Any], *, encoding: str | MutableSequence[str] | None = ..., ds: Dataset | None = ..., **kwargs: Any) -> None: ...

class Hooks:
    raw_element_value: Incomplete
    raw_element_vr: Incomplete
    raw_element_kwargs: Incomplete
    def __init__(self) -> None: ...
    def register_callback(self, hook: str, func: Callable) -> None: ...
    def register_kwargs(self, hook: str, kwargs: dict[str, Any]) -> None: ...

def raw_element_vr(raw: RawDataElement, data: dict[str, Any], *, encoding: str | MutableSequence[str] | None = None, ds: Dataset | None = None, **kwargs: Any) -> None: ...
def raw_element_value(raw: RawDataElement, data: dict[str, Any], *, encoding: str | MutableSequence[str] | None = None, ds: Dataset | None = None, **kwargs: Any) -> None: ...
def raw_element_value_fix_separator(raw: RawDataElement, data: dict[str, Any], *, encoding: str | MutableSequence[str] | None = None, ds: Dataset | None, separator: str | bytes = b',', target_VRs: tuple[str, ...] | None = None, **kwargs: Any) -> None: ...
def raw_element_value_retry(raw: RawDataElement, data: dict[str, Any], *, encoding: str | MutableSequence[str] | None = None, ds: Dataset | None, target_VRs: dict[str, tuple[str, ...]] | None = None, **kwargs: Any) -> None: ...

hooks: Hooks
