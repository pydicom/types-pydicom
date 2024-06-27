import numpy as np
from _typeshed import Incomplete
from collections.abc import Iterable, Iterator
from pydicom import config as config
from pydicom.dataset import Dataset as Dataset
from pydicom.encaps import generate_frames as generate_frames, get_frame as get_frame
from pydicom.misc import warn_and_log as warn_and_log
from pydicom.pixels.common import Buffer as Buffer, CoderBase as CoderBase, RunnerBase as RunnerBase, RunnerOptions as RunnerOptions
from pydicom.pixels.processing import convert_color_space as convert_color_space
from pydicom.pixels.utils import get_j2k_parameters as get_j2k_parameters
from pydicom.uid import DeflatedExplicitVRLittleEndian as DeflatedExplicitVRLittleEndian, ExplicitVRBigEndian as ExplicitVRBigEndian, ExplicitVRLittleEndian as ExplicitVRLittleEndian, HTJ2K as HTJ2K, HTJ2KLossless as HTJ2KLossless, HTJ2KLosslessRPCL as HTJ2KLosslessRPCL, ImplicitVRLittleEndian as ImplicitVRLittleEndian, JPEG2000 as JPEG2000, JPEG2000Lossless as JPEG2000Lossless, JPEG2000TransferSyntaxes as JPEG2000TransferSyntaxes, JPEGBaseline8Bit as JPEGBaseline8Bit, JPEGExtended12Bit as JPEGExtended12Bit, JPEGLSLossless as JPEGLSLossless, JPEGLSNearLossless as JPEGLSNearLossless, JPEGLSTransferSyntaxes as JPEGLSTransferSyntaxes, JPEGLossless as JPEGLossless, JPEGLosslessSV1 as JPEGLosslessSV1, JPEGTransferSyntaxes as JPEGTransferSyntaxes, RLELossless as RLELossless, UID as UID
from typing import Any, BinaryIO

HAVE_NP: bool
LOGGER: Incomplete
DecodeFunction: Incomplete
ProcessingFunction: Incomplete

class DecodeOptions(RunnerOptions, total=False):
    pixel_vr: str
    allow_excess_frames: bool
    correct_unused_bits: bool
    view_only: bool
    be_swap_ow: bool
    rle_segment_order: str
    byteorder: str
    apply_jls_sign_correction: bool
    apply_j2k_sign_correction: bool
    as_rgb: bool
    force_rgb: bool
    force_ybr: bool

PROCESSORS: list[ProcessingFunction]

class DecodeRunner(RunnerBase):
    def __init__(self, tsyntax: UID) -> None: ...
    def decode(self, index: int) -> bytes | bytearray: ...
    def get_data(self, src: Buffer | BinaryIO, offset: int, length: int) -> bytes: ...
    def iter_decode(self) -> Iterator[bytes | bytearray]: ...
    @property
    def pixel_dtype(self) -> np.dtype: ...
    def pixel_properties(self, as_frame: bool = False) -> dict[str, str | int]: ...
    def process(self, arr: np.ndarray) -> tuple['np.ndarray', dict[str, str | int]]: ...
    def reshape(self, arr: np.ndarray, as_frame: bool = False) -> np.ndarray: ...
    def set_decoders(self, decoders: dict[str, DecodeFunction]) -> None: ...
    def set_source(self, src: Buffer | Dataset | BinaryIO) -> None: ...
    @property
    def src(self) -> Buffer | BinaryIO: ...
    def validate(self) -> None: ...

class Decoder(CoderBase):
    def __init__(self, uid: UID) -> None: ...
    def as_array(self, src: Dataset | Buffer | BinaryIO, *, index: int | None = None, validate: bool = True, raw: bool = False, decoding_plugin: str = '', **kwargs: DecodeOptions) -> tuple['np.ndarray', dict[str, str | int]]: ...
    def as_buffer(self, src: Dataset | Buffer | BinaryIO, *, index: int | None = None, validate: bool = True, decoding_plugin: str = '', **kwargs: Any) -> tuple[Buffer, dict[str, str | int]]: ...
    def iter_array(self, src: Dataset | Buffer | BinaryIO, *, indices: Iterable[int] | None = None, raw: bool = False, validate: bool = True, decoding_plugin: str = '', **kwargs: Any) -> Iterator[tuple['np.ndarray', dict[str, str | int]]]: ...
    def iter_buffer(self, src: Dataset | Buffer | BinaryIO, *, indices: Iterable[int] | None = None, validate: bool = True, decoding_plugin: str = '', **kwargs: Any) -> Iterator[tuple[Buffer, dict[str, str | int]]]: ...

ImplicitVRLittleEndianDecoder: Incomplete
ExplicitVRLittleEndianDecoder: Incomplete
ExplicitVRBigEndianDecoder: Incomplete
DeflatedExplicitVRLittleEndianDecoder: Incomplete
JPEGBaseline8BitDecoder: Incomplete
JPEGExtended12BitDecoder: Incomplete
JPEGLosslessDecoder: Incomplete
JPEGLosslessSV1Decoder: Incomplete
JPEGLSLosslessDecoder: Incomplete
JPEGLSNearLosslessDecoder: Incomplete
JPEG2000LosslessDecoder: Incomplete
JPEG2000Decoder: Incomplete
HTJ2KLosslessDecoder: Incomplete
HTJ2KLosslessRPCLDecoder: Incomplete
HTJ2KDecoder: Incomplete
RLELosslessDecoder: Incomplete

def get_decoder(uid: str) -> Decoder: ...
