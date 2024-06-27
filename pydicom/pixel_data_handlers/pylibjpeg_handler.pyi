import numpy as np
from _typeshed import Incomplete
from collections.abc import Iterable
from pydicom import config as config
from pydicom.dataset import Dataset as Dataset
from pydicom.pixels.utils import get_expected_length as get_expected_length, get_j2k_parameters as get_j2k_parameters, get_nr_frames as get_nr_frames, pixel_dtype as pixel_dtype, reshape_pixel_array as reshape_pixel_array
from pydicom.uid import JPEG2000 as JPEG2000, JPEG2000Lossless as JPEG2000Lossless, JPEGBaseline8Bit as JPEGBaseline8Bit, JPEGExtended12Bit as JPEGExtended12Bit, JPEGLSLossless as JPEGLSLossless, JPEGLSNearLossless as JPEGLSNearLossless, JPEGLossless as JPEGLossless, JPEGLosslessSV1 as JPEGLosslessSV1, RLELossless as RLELossless, UID as UID

HAVE_NP: bool
HAVE_PYLIBJPEG: bool
HAVE_OPENJPEG: bool
HAVE_LIBJPEG: bool
HAVE_RLE: bool
LOGGER: Incomplete
HANDLER_NAME: str
SUPPORTED_TRANSFER_SYNTAXES: Incomplete
DEPENDENCIES: Incomplete

def is_available() -> bool: ...
def supports_transfer_syntax(tsyntax: UID) -> bool: ...
def needs_to_convert_to_RGB(ds: Dataset) -> bool: ...
def should_change_PhotometricInterpretation_to_RGB(ds: Dataset) -> bool: ...
def as_array(ds: Dataset) -> np.ndarray: ...
def generate_frames(ds: Dataset, reshape: bool = True) -> Iterable['np.ndarray']: ...
def get_pixeldata(ds: Dataset) -> np.ndarray: ...
