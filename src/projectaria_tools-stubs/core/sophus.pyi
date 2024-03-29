from typing import List

import numpy

class SE3d:
    def __init__(self) -> None: ...
    def inverse(self) -> SE3d: ...
    def matrix(self) -> numpy.ndarray[numpy.float64[4, 4]]: ...
    def quaternion(self) -> List[float]: ...
    def rotation_matrix(self) -> numpy.ndarray[numpy.float64[3, 3]]: ...
    def translation(self) -> numpy.ndarray[numpy.float64[3, 1]]: ...
