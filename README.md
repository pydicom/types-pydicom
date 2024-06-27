# types-pydicom
Extended type hints for pydicom

Basic generation

```bash
pip install mypy
git clone https://github.com/pydicom/types-pydicom
cd types-pydicom
stubgen path/to/pydicom -o .
```

Some types will have `Incomplete`, these need to be fixed in pydicom

Then run script to fill out the attribute types.

* Need GH action to monitor pydicom merge and run auto-update action as required
* Failure on `Incomplete` types?
* Remove pixel plugin stubs
