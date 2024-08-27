from _typeshed import Incomplete
from collections.abc import Callable
from pydicom.dataset import Dataset as Dataset
from pydicom.misc import warn_and_log as warn_and_log
from pydicom.valuerep import FLOAT_VR as FLOAT_VR, INT_VR as INT_VR, VR as VR
from typing import Any, TypeAlias

JSON_VALUE_KEYS: Incomplete

def convert_to_python_number(value: Any, vr: str) -> Any: ...
OtherValueType = None | str | int | float
PNValueType = None | str | dict[str, str]
SQValueType = dict[str, Any] | None
ValueType: TypeAlias
InlineBinaryType: TypeAlias
BulkDataURIType: TypeAlias
JSONValueType = list[ValueType] | InlineBinaryType | BulkDataURIType
BulkDataType = None | str | int | float | bytes
BulkDataHandlerType = Callable[[str, str, str], BulkDataType] | None

class JsonDataElementConverter:
    dataset_class: Incomplete
    tag: Incomplete
    vr: Incomplete
    value: Incomplete
    value_key: Incomplete
    bulk_data_element_handler: Incomplete
    def __init__(self, dataset_class: type['Dataset'], tag: str, vr: str, value: JSONValueType, value_key: str | None, bulk_data_uri_handler: BulkDataHandlerType | Callable[[str], BulkDataType] | None = None) -> None: ...
    def get_element_values(self) -> Any: ...
    def get_regular_element_value(self, value: ValueType) -> Any: ...
    def get_sequence_item(self, value: SQValueType) -> Dataset: ...
    def get_pn_element_value(self, value: str | dict[str, str]) -> str: ...
