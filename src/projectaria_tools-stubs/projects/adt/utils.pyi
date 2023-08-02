import numpy as _np
from _typeshed import Incomplete
from projectaria_tools.core.calibration import CameraCalibration as _CameraCalibration
from typing import Dict, List, Optional
from zipfile import ZipFile

MIN_SYM_ANGLE_STEP: float
VERTICES_AXIS: Incomplete

def project_3d_bbox_to_image(aabb: List[float], transform_cam_obj: _np.ndarray, cam_calibration: _CameraCalibration) -> List[int]: ...
def get_timed_homo_poses(archive: ZipFile, seq_name: str): ...
def get_rotation_matrices(symmetry: Dict) -> List[_np.ndarray]: ...
def apply_pose(pose: Dict, vertices: _np.ndarray, sym_rot: Optional[_np.ndarray] = ...) -> _np.ndarray: ...
def compute_mssd(predicted_pose: Dict, annotated_pose: Dict, symmetries: List[Dict], vertices: _np.ndarray): ...
def voc_ap(rec, prec): ...
def get_timed_poses(archive, seq_name: str): ...
def get_vertices(archive): ...
def get_3d_bounding_box(archive): ...
def get_symmetries(archive): ...
def get_diameters(archive): ...
