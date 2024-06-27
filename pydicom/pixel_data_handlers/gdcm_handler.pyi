import gdcm
import numpy
from _typeshed import Incomplete
from gdcm import DataElement
from pydicom import config as config
from pydicom.dataset import Dataset as Dataset
from pydicom.encaps import generate_fragmented_frames as generate_fragmented_frames, generate_frames as generate_frames
from pydicom.pixels.utils import get_expected_length as get_expected_length, get_j2k_parameters as get_j2k_parameters, get_nr_frames as get_nr_frames, pixel_dtype as pixel_dtype
from pydicom.uid import JPEG2000 as JPEG2000, JPEG2000Lossless as JPEG2000Lossless, UID as UID

HAVE_NP: bool
HAVE_GDCM: bool
HAVE_GDCM_IN_MEMORY_SUPPORT: Incomplete
HANDLER_NAME: str
DEPENDENCIES: Incomplete
SUPPORTED_TRANSFER_SYNTAXES: Incomplete
should_convert_these_syntaxes_to_RGB: Incomplete

def is_available() -> bool: ...
def needs_to_convert_to_RGB(ds: Dataset) -> bool: ...
def should_change_PhotometricInterpretation_to_RGB(ds: Dataset) -> bool: ...
def supports_transfer_syntax(transfer_syntax: UID) -> bool: ...
def create_data_element(ds: Dataset) -> DataElement: ...
def create_image(ds: Dataset, data_element: DataElement) -> gdcm.Image: ...
def get_pixeldata(ds: Dataset) -> numpy.ndarray: ...
