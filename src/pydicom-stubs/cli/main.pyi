import argparse
from _typeshed import Incomplete
from pydicom import dcmread as dcmread
from pydicom.data.data_manager import get_charset_files as get_charset_files, get_testdata_file as get_testdata_file
from pydicom.dataset import Dataset as Dataset
from typing import Any

subparsers: argparse._SubParsersAction | None
re_kywd_or_item: str
re_file_spec_object: Incomplete
filespec_help: str

def eval_element(ds: Dataset, element: str) -> Any: ...
def filespec_parts(filespec: str) -> tuple[str, str, str]: ...
def filespec_parser(filespec: str) -> list[tuple[Dataset, Any]]: ...
def help_command(args: argparse.Namespace) -> None: ...

SubCommandType: Incomplete

def get_subcommand_entry_points() -> SubCommandType: ...
def main(args: list[str] | None = None) -> None: ...
