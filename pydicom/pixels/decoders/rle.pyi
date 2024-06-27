from _typeshed import Incomplete
from pydicom.misc import warn_and_log as warn_and_log
from pydicom.pixels.decoders.base import DecodeRunner as DecodeRunner
from pydicom.uid import RLELossless as RLELossless

DECODER_DEPENDENCIES: Incomplete

def is_available(uid: str) -> bool: ...
