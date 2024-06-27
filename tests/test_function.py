

from pydicom import Dataset

ds = Dataset()
ds.NumberOfFrames = ["foo"]
reveal_type(ds.SamplesPerPixel)
ds.SamplesPerPixel = "abcd"
reveal_type(ds.PixelData)


"""
If the package is working correctly this should result in the following
when running `mypy tests/` (exit code 1):

tests/test_function.py:6: error: Incompatible types in assignment (expression has type "list[str]", variable has type "str | int | IS | ISfloat | None")  [assignment]
tests/test_function.py:7: note: Revealed type is "builtins.int"
tests/test_function.py:8: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
Found 2 errors in 1 file (checked 1 source file)


Otherwise it will result in (exit code 0):

tests/test_function.py:7: note: Revealed type is "Any"
Success: no issues found in 1 source file
"""
