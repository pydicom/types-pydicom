import numpy
from _typeshed import Incomplete
from pydicom import config as config
from pydicom.dataset import Dataset as Dataset
from pydicom.encaps import generate_frames as generate_frames
from pydicom.misc import warn_and_log as warn_and_log
from pydicom.pixels.utils import get_j2k_parameters as get_j2k_parameters, get_nr_frames as get_nr_frames, pixel_dtype as pixel_dtype
from pydicom.uid import JPEG2000 as JPEG2000, JPEG2000Lossless as JPEG2000Lossless, JPEGBaseline8Bit as JPEGBaseline8Bit, JPEGExtended12Bit as JPEGExtended12Bit, UID as UID

HAVE_NP: bool
HAVE_PIL: bool
HAVE_JPEG: Incomplete
HAVE_JPEG2K: Incomplete
logger: Incomplete
PillowJPEG2000TransferSyntaxes: Incomplete
PillowJPEGTransferSyntaxes: Incomplete
PillowSupportedTransferSyntaxes: Incomplete
HANDLER_NAME: str
DEPENDENCIES: Incomplete

def is_available() -> bool: ...
def supports_transfer_syntax(transfer_syntax: UID) -> bool: ...
def needs_to_convert_to_RGB(ds: Dataset) -> bool: ...
def should_change_PhotometricInterpretation_to_RGB(ds: Dataset) -> bool: ...
def get_pixeldata(ds: Dataset) -> numpy.ndarray: ...
