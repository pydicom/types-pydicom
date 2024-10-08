import PIL
import numpy as np
from pydicom.data import get_palette_files as get_palette_files
from pydicom.dataset import Dataset as Dataset
from pydicom.misc import warn_and_log as warn_and_log
from pydicom.uid import UID as UID
from pydicom.valuerep import VR as VR

HAVE_NP: bool
HAVE_PIL: bool

def apply_color_lut(arr: np.ndarray, ds: Dataset | None = None, palette: str | UID | None = None) -> np.ndarray: ...
def apply_icc_profile(arr: np.ndarray, ds: Dataset | None = None, transform: PIL.ImageCms.ImageCmsTransform | None = None, intent: int | None = None, color_space: str | None = None) -> np.ndarray: ...
def apply_modality_lut(arr: np.ndarray, ds: Dataset) -> np.ndarray: ...
def apply_presentation_lut(arr: np.ndarray, ds: Dataset) -> np.ndarray: ...
apply_rescale = apply_modality_lut

def apply_voi_lut(arr: np.ndarray, ds: Dataset, index: int = 0, prefer_lut: bool = True) -> np.ndarray: ...
def apply_voi(arr: np.ndarray, ds: Dataset, index: int = 0) -> np.ndarray: ...
def apply_windowing(arr: np.ndarray, ds: Dataset, index: int = 0) -> np.ndarray: ...
def convert_color_space(arr: np.ndarray, current: str, desired: str, per_frame: bool = False) -> np.ndarray: ...
def create_icc_transform(ds: Dataset | None = None, icc_profile: bytes = b'', intent: int | None = None, color_space: str | None = None) -> PIL.ImageCms.ImageCmsTransform: ...
