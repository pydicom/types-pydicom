import numpy as np
from _typeshed import Incomplete
from pydicom.dataelem import DataElement as DataElement
from pydicom.dataset import Dataset as Dataset
from pydicom.misc import warn_and_log as warn_and_log
from pydicom.pixels.utils import unpack_bits as unpack_bits
from typing import Any

HAVE_NP: bool
HANDLER_NAME: str
DEPENDENCIES: Incomplete

def is_available() -> bool: ...
def get_expected_length(elem: dict[str, Any], unit: str = 'bytes') -> int: ...
def reshape_overlay_array(elem: dict[str, Any], arr: np.ndarray) -> np.ndarray: ...
def get_overlay_array(ds: Dataset, group: int) -> np.ndarray: ...
