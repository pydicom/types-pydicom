from _typeshed import Incomplete
from pydicom import uid as uid
from pydicom.pixels.decoders.base import DecodeRunner as DecodeRunner

GDCM_VERSION: Incomplete
HAVE_GDCM: bool
DECODER_DEPENDENCIES: Incomplete

def is_available(uid: str) -> bool: ...
