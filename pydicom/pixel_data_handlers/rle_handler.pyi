import numpy as np
from _typeshed import Incomplete
from pydicom.dataset import Dataset as Dataset
from pydicom.encaps import generate_frames as generate_frames
from pydicom.misc import warn_and_log as warn_and_log
from pydicom.pixels.utils import get_nr_frames as get_nr_frames, pixel_dtype as pixel_dtype

HAVE_RLE: bool
HANDLER_NAME: str
DEPENDENCIES: Incomplete
SUPPORTED_TRANSFER_SYNTAXES: Incomplete

def is_available() -> bool: ...
def supports_transfer_syntax(transfer_syntax: str) -> bool: ...
def needs_to_convert_to_RGB(ds: Dataset) -> bool: ...
def should_change_PhotometricInterpretation_to_RGB(ds: Dataset) -> bool: ...
def get_pixeldata(ds: Dataset, rle_segment_order: str = '>') -> np.ndarray: ...
