import os
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterator
from pydicom.datadict import dictionary_VR as dictionary_VR
from pydicom.misc import size_in_bytes as size_in_bytes
from pydicom.tag import ItemTag as ItemTag, TupleTag as TupleTag
from pydicom.uid import UID as UID
from pydicom.valuerep import EXPLICIT_VR_LENGTH_32 as EXPLICIT_VR_LENGTH_32
from types import TracebackType
from typing import BinaryIO

extra_length_VRs_b: Incomplete
ExplicitVRLittleEndian: bytes
ImplicitVRLittleEndian: bytes
DeflatedExplicitVRLittleEndian: bytes
ExplicitVRBigEndian: bytes

class dicomfile:
    fobj: Incomplete
    preamble: Incomplete
    def __init__(self, filename: str | bytes | os.PathLike) -> None: ...
    def __enter__(self) -> dicomfile: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> bool | None: ...
    def __iter__(self) -> Iterator[_ElementType]: ...

def data_element_generator(fp: BinaryIO, is_implicit_VR: bool, is_little_endian: bool, stop_when: Callable[[int, int], bool] | None = None, defer_size: str | int | float | None = None) -> Iterator[_ElementType]: ...
