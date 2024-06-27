from _typeshed import Incomplete
from pydicom import uid as uid
from pydicom.pixels.decoders.base import DecodeRunner as DecodeRunner

HAVE_NP: bool
DECODER_DEPENDENCIES: Incomplete

def is_available(uid: str) -> bool: ...
