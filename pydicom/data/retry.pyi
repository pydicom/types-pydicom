import logging
from collections.abc import Callable as Callable
from typing import Any

def retry(exc: type[Exception] | tuple[type[Exception], ...], exc_msg: str | None = None, tries: int = 4, delay: int = 3, backoff: int = 2, logger: logging.Logger | None = None) -> Callable[[Callable], Any]: ...
