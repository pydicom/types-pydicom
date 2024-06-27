import numpy as np
import pydicom.uid
from _typeshed import Incomplete
from pydicom.dataset import Dataset as Dataset
from pydicom.misc import warn_and_log as warn_and_log
from pydicom.pixels.utils import get_expected_length as get_expected_length, pixel_dtype as pixel_dtype, unpack_bits as unpack_bits

HAVE_NP: bool
HANDLER_NAME: str
DEPENDENCIES: Incomplete
SUPPORTED_TRANSFER_SYNTAXES: Incomplete

def is_available() -> bool: ...
def supports_transfer_syntax(transfer_syntax: pydicom.uid.UID) -> bool: ...
def needs_to_convert_to_RGB(ds: Dataset) -> bool: ...
def should_change_PhotometricInterpretation_to_RGB(ds: Dataset) -> bool: ...
def get_pixeldata(ds: Dataset, read_only: bool = False) -> np.ndarray: ...
