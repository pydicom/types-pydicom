from _typeshed import Incomplete
from pydicom.pixels.encoders.base import EncodeRunner as EncodeRunner
from pydicom.uid import RLELossless as RLELossless

GDCM_VERSION: Incomplete
HAVE_GDCM: bool
ENCODER_DEPENDENCIES: Incomplete

def is_available(uid: str) -> bool: ...
def encode_pixel_data(src: bytes, runner: EncodeRunner) -> bytes: ...
