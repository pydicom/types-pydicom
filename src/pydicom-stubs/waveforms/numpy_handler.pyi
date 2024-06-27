import numpy as np
from _typeshed import Incomplete
from collections.abc import Generator
from pydicom.dataset import Dataset as Dataset

HAVE_NP: bool
HANDLER_NAME: str
DEPENDENCIES: Incomplete
WAVEFORM_DTYPES: Incomplete

def is_available() -> bool: ...
def generate_multiplex(ds: Dataset, as_raw: bool = True) -> Generator['np.ndarray', None, None]: ...
def multiplex_array(ds: Dataset, index: int, as_raw: bool = True) -> np.ndarray: ...
