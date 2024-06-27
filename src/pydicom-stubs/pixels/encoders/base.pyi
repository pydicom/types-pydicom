import numpy as np
from _typeshed import Incomplete
from collections.abc import Iterable, Iterator
from pydicom import config as config
from pydicom.dataset import Dataset as Dataset
from pydicom.pixels.common import Buffer as Buffer, CoderBase as CoderBase, RunnerBase as RunnerBase, RunnerOptions as RunnerOptions
from pydicom.uid import JPEG2000 as JPEG2000, JPEG2000Lossless as JPEG2000Lossless, JPEGBaseline8Bit as JPEGBaseline8Bit, JPEGExtended12Bit as JPEGExtended12Bit, JPEGLSLossless as JPEGLSLossless, JPEGLSNearLossless as JPEGLSNearLossless, JPEGLSTransferSyntaxes as JPEGLSTransferSyntaxes, JPEGLossless as JPEGLossless, JPEGLosslessSV1 as JPEGLosslessSV1, RLELossless as RLELossless, UID as UID
from typing import Any

LOGGER: Incomplete
EncodeFunction: Incomplete

class EncodeOptions(RunnerOptions, total=False):
    byteorder: str
    jls_error: int
    j2k_cr: list[float]
    j2k_psnr: list[float]

class EncodeRunner(RunnerBase):
    def __init__(self, tsyntax: UID) -> None: ...
    def encode(self, index: int | None) -> bytes: ...
    def get_frame(self, index: int | None) -> bytes: ...
    def set_encoders(self, encoders: dict[str, EncodeFunction]) -> None: ...
    def set_source(self, src: np.ndarray | Dataset | Buffer) -> None: ...
    @property
    def src(self) -> Buffer | np.ndarray: ...
    def validate(self) -> None: ...

class Encoder(CoderBase):
    def __init__(self, uid: UID) -> None: ...
    def encode(self, src: bytes | np.ndarray | Dataset, *, index: int | None = None, validate: bool = True, encoding_plugin: str = '', **kwargs: Any) -> bytes: ...
    def iter_encode(self, src: bytes | np.ndarray | Dataset, *, validate: bool = True, encoding_plugin: str = '', **kwargs: Any) -> Iterator[bytes]: ...
ProfileType = tuple[str, int, Iterable[int], Iterable[int], Iterable[int]]
ENCODING_PROFILES: dict[UID, list[ProfileType]]
RLELosslessEncoder: Incomplete
JPEGLSLosslessEncoder: Incomplete
JPEGLSNearLosslessEncoder: Incomplete
JPEG2000LosslessEncoder: Incomplete
JPEG2000Encoder: Incomplete

def get_encoder(uid: str) -> Encoder: ...
