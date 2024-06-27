from pydicom.data import get_testdata_file as get_testdata_file
from pydicom.filereader import dcmread as dcmread
from typing import Any

def __getattr__(name: str) -> Any: ...
