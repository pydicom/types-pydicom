from pydicom import config as config, datadict as datadict, values as values
from pydicom.dataelem import RawDataElement as RawDataElement
from pydicom.valuerep import VR as VR
from typing import Any

def fix_separator_callback(raw_elem: RawDataElement, **kwargs: Any) -> RawDataElement: ...
def fix_separator(invalid_separator: bytes, for_VRs: tuple[str, ...] = ('DS', 'IS'), process_unknown_VRs: bool = True) -> None: ...
def fix_mismatch_callback(raw_elem: RawDataElement, **kwargs: Any) -> RawDataElement: ...
def fix_mismatch(with_VRs: tuple[str, ...] = ...) -> None: ...