# types-pydicom
Extended type hints for [pydicom's](https://github.com/pydicom/pydicom) [Dataset](https://pydicom.github.io/pydicom/stable/reference/generated/pydicom.dataset.Dataset.html#pydicom.dataset.Dataset) element keywords.

## Installation
```bash
$ pip install types-pydicom
```

## Usage
```python
# test_typing.py

from pydicom import Dataset

ds = Dataset()
ds.SamplesPerPixel = "abc"
reveal_type(ds.PixelData)
```

```bash
$ pip install pydicom types-pydicom mypy
$ mypy test_typing.py
test_typing.py:5: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
test_typing.py:6: note: Revealed type is "Union[None, builtins.bytes]"
Found 1 errors in 1 file (checked 1 source file)
```

## Development
```bash
git clone https://github.com/pydicom
git clone https://github.com/pydicom/types-pydicom
cd types-pydicom
mkdir env
python3.10 -m venv env/env310
source env/env310/bin/activate
pip install -e .[dev]
```

### Updating
```bash
python scripts/update_package.py
```
