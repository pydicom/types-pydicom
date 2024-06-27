from _typeshed import Incomplete
from pydicom import uid as uid
from pydicom.pixels.decoders.base import DecodeRunner as DecodeRunner
from pylibjpeg.utils import Decoder as Decoder

DECODER_DEPENDENCIES: Incomplete

def is_available(uid: str) -> bool: ...
