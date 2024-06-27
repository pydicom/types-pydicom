from pydicom import config as config
from pydicom.misc import warn_and_log as warn_and_log
from typing import Any

def __getattr__(name: str) -> Any: ...
