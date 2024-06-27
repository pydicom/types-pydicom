from _typeshed import Incomplete
from collections.abc import Iterable
from pydicom.dataset import Dataset as Dataset
from pydicom.multival import ConstrainedList as ConstrainedList
from typing import TypeVar

Self = TypeVar('Self', bound='Sequence')

class Sequence(ConstrainedList[Dataset]):
    is_undefined_length: Incomplete
    def __init__(self, iterable: Iterable[Dataset] | None = None) -> None: ...
    def extend(self, val: Iterable[Dataset]) -> None: ...
    def __iadd__(self, other: Iterable[Dataset]) -> Self: ...
    def __setitem__(self, index: slice | int, val: Iterable[Dataset] | Dataset) -> None: ...
