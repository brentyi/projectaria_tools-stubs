from typing import Any, Dict, Iterator, List, Optional, Tuple

from typing import overload
import _core_pybinds.calibration
import _core_pybinds.sensor_data
import _core_pybinds.stream_id

class DeliverQueuedOptions(SubstreamSelector):
    def __init__(self, arg0: int, arg1: int, arg2: Dict[_core_pybinds.stream_id.StreamId,int]) -> None: ...
    def get_subsample_rate(self, stream_id: _core_pybinds.stream_id.StreamId) -> int: ...
    def get_truncate_first_device_time_ns(self) -> int: ...
    def get_truncate_last_device_time_ns(self) -> int: ...
    def set_subsample_rate(self, stream_id: _core_pybinds.stream_id.StreamId, rate: int) -> None: ...
    def set_truncate_first_device_time_ns(self, time_ns: int) -> None: ...
    def set_truncate_last_device_time_ns(self, time_ns: int) -> None: ...

class SensorDataIterator:
    def __init__(self) -> None: ...

class SensorDataSequence:
    def __init__(self, arg0, arg1: DeliverQueuedOptions) -> None: ...

class SubstreamSelector:
    def __init__(self, arg0: Set[_core_pybinds.stream_id.StreamId]) -> None: ...
    @overload
    def activate_stream(self, arg0: _core_pybinds.stream_id.StreamId) -> bool: ...
    @overload
    def activate_stream(self, arg0: _core_pybinds.stream_id.StreamId) -> bool: ...
    def activate_stream_all(self) -> None: ...
    @overload
    def deactivate_stream(self, arg0: _core_pybinds.stream_id.StreamId) -> bool: ...
    @overload
    def deactivate_stream(self, arg0: _core_pybinds.stream_id.StreamId) -> bool: ...
    def deactivate_stream_all(self) -> None: ...
    def get_active_stream_ids(self) -> List[_core_pybinds.stream_id.StreamId]: ...
    @overload
    def get_stream_ids(self) -> List[_core_pybinds.stream_id.StreamId]: ...
    @overload
    def get_stream_ids(self, arg0: _core_pybinds.stream_id.RecordableTypeId) -> List[_core_pybinds.stream_id.StreamId]: ...
    def get_type_ids(self) -> List[_core_pybinds.stream_id.RecordableTypeId]: ...
    def is_active(self, stream_id: _core_pybinds.stream_id.StreamId) -> bool: ...
    def toggle_stream(self, arg0: _core_pybinds.stream_id.StreamId) -> bool: ...

class VrsDataProvider:
    def __init__(self, arg0, arg1, arg2, arg3, arg4: Optional[_core_pybinds.calibration.DeviceCalibration]) -> None: ...
    def check_stream_is_active(self, stream_id: _core_pybinds.stream_id.StreamId) -> bool: ...
    def check_stream_is_type(self, stream_id: _core_pybinds.stream_id.StreamId, type: _core_pybinds.sensor_data.SensorDataType) -> bool: ...
    def convert_from_device_time_to_timecode_ns(self, device_time_ns: int) -> int: ...
    def convert_from_timecode_to_device_time_ns(self, timecode_time_ns: int) -> int: ...
    @overload
    def deliver_queued_sensor_data(self) -> Iterator: ...
    @overload
    def deliver_queued_sensor_data(self, arg0: DeliverQueuedOptions) -> Iterator: ...
    def get_all_streams(self) -> List[_core_pybinds.stream_id.StreamId]: ...
    def get_audio_configuration(self, stream_id: _core_pybinds.stream_id.StreamId) -> _core_pybinds.sensor_data.AudioConfig: ...
    def get_audio_data_by_index(self, stream_id: _core_pybinds.stream_id.StreamId, index: int) -> Tuple[_core_pybinds.sensor_data.AudioData,_core_pybinds.sensor_data.AudioDataRecord]: ...
    def get_audio_data_by_time_ns(self, stream_id: _core_pybinds.stream_id.StreamId, time_ns: int, time_domain: _core_pybinds.sensor_data.TimeDomain, time_query_options: _core_pybinds.sensor_data.TimeQueryOptions = ...) -> Tuple[_core_pybinds.sensor_data.AudioData,_core_pybinds.sensor_data.AudioDataRecord]: ...
    def get_barometer_configuration(self, stream_id: _core_pybinds.stream_id.StreamId) -> _core_pybinds.sensor_data.BarometerConfigRecord: ...
    def get_barometer_data_by_index(self, stream_id: _core_pybinds.stream_id.StreamId, index: int) -> _core_pybinds.sensor_data.BarometerData: ...
    def get_barometer_data_by_time_ns(self, stream_id: _core_pybinds.stream_id.StreamId, time_ns: int, time_domain: _core_pybinds.sensor_data.TimeDomain, time_query_options: _core_pybinds.sensor_data.TimeQueryOptions = ...) -> _core_pybinds.sensor_data.BarometerData: ...
    def get_bluetooth_configuration(self, stream_id: _core_pybinds.stream_id.StreamId) -> _core_pybinds.sensor_data.BluetoothBeaconConfigRecord: ...
    def get_bluetooth_data_by_index(self, stream_id: _core_pybinds.stream_id.StreamId, index: int) -> _core_pybinds.sensor_data.BluetoothBeaconData: ...
    def get_bluetooth_data_by_time_ns(self, stream_id: _core_pybinds.stream_id.StreamId, time_ns: int, time_domain: _core_pybinds.sensor_data.TimeDomain, time_query_options: _core_pybinds.sensor_data.TimeQueryOptions = ...) -> _core_pybinds.sensor_data.BluetoothBeaconData: ...
    def get_configuration(self, stream_id: _core_pybinds.stream_id.StreamId) -> _core_pybinds.sensor_data.SensorConfiguration: ...
    def get_default_deliver_queued_options(self) -> DeliverQueuedOptions: ...
    def get_device_calibration(self) -> Optional[_core_pybinds.calibration.DeviceCalibration]: ...
    def get_first_time_ns(self, stream_id: _core_pybinds.stream_id.StreamId, time_domain: _core_pybinds.sensor_data.TimeDomain) -> int: ...
    def get_first_time_ns_all_streams(self, time_domain: _core_pybinds.sensor_data.TimeDomain) -> int: ...
    def get_gps_configuration(self, stream_id: _core_pybinds.stream_id.StreamId) -> _core_pybinds.sensor_data.GpsConfigRecord: ...
    def get_gps_data_by_index(self, stream_id: _core_pybinds.stream_id.StreamId, index: int) -> _core_pybinds.sensor_data.GpsData: ...
    def get_gps_data_by_time_ns(self, stream_id: _core_pybinds.stream_id.StreamId, time_ns: int, time_domain: _core_pybinds.sensor_data.TimeDomain, time_query_options: _core_pybinds.sensor_data.TimeQueryOptions = ...) -> _core_pybinds.sensor_data.GpsData: ...
    def get_image_configuration(self, stream_id: _core_pybinds.stream_id.StreamId) -> _core_pybinds.sensor_data.ImageConfigRecord: ...
    def get_image_data_by_index(self, stream_id: _core_pybinds.stream_id.StreamId, index: int) -> Tuple[_core_pybinds.sensor_data.ImageData,_core_pybinds.sensor_data.ImageDataRecord]: ...
    def get_image_data_by_time_ns(self, stream_id: _core_pybinds.stream_id.StreamId, time_ns: int, time_domain: _core_pybinds.sensor_data.TimeDomain, time_query_options: _core_pybinds.sensor_data.TimeQueryOptions = ...) -> Tuple[_core_pybinds.sensor_data.ImageData,_core_pybinds.sensor_data.ImageDataRecord]: ...
    def get_imu_configuration(self, stream_id: _core_pybinds.stream_id.StreamId) -> _core_pybinds.sensor_data.MotionConfigRecord: ...
    def get_imu_data_by_index(self, stream_id: _core_pybinds.stream_id.StreamId, index: int) -> _core_pybinds.sensor_data.MotionData: ...
    def get_imu_data_by_time_ns(self, stream_id: _core_pybinds.stream_id.StreamId, time_ns: int, time_domain: _core_pybinds.sensor_data.TimeDomain, time_query_options: _core_pybinds.sensor_data.TimeQueryOptions = ...) -> _core_pybinds.sensor_data.MotionData: ...
    def get_index_by_time_ns(self, stream_id: _core_pybinds.stream_id.StreamId, time_ns: int, time_domain: _core_pybinds.sensor_data.TimeDomain, time_query_options: _core_pybinds.sensor_data.TimeQueryOptions = ...) -> int: ...
    def get_label_from_stream_id(self, stream_id: _core_pybinds.stream_id.StreamId) -> Optional[str]: ...
    def get_last_time_ns(self, stream_id: _core_pybinds.stream_id.StreamId, time_domain: _core_pybinds.sensor_data.TimeDomain) -> int: ...
    def get_last_time_ns_all_streams(self, time_domain: _core_pybinds.sensor_data.TimeDomain) -> int: ...
    def get_magnetometer_configuration(self, stream_id: _core_pybinds.stream_id.StreamId) -> _core_pybinds.sensor_data.MotionConfigRecord: ...
    def get_magnetometer_data_by_index(self, stream_id: _core_pybinds.stream_id.StreamId, index: int) -> _core_pybinds.sensor_data.MotionData: ...
    def get_magnetometer_data_by_time_ns(self, stream_id: _core_pybinds.stream_id.StreamId, time_ns: int, time_domain: _core_pybinds.sensor_data.TimeDomain, time_query_options: _core_pybinds.sensor_data.TimeQueryOptions = ...) -> _core_pybinds.sensor_data.MotionData: ...
    def get_nominalRateHz(self, stream_id: _core_pybinds.stream_id.StreamId) -> float: ...
    def get_num_data(self, stream_id: _core_pybinds.stream_id.StreamId) -> int: ...
    def get_sensor_calibration(self, stream_id: _core_pybinds.stream_id.StreamId) -> Optional[_core_pybinds.calibration.SensorCalibration]: ...
    def get_sensor_data_by_index(self, stream_id: _core_pybinds.stream_id.StreamId, index: int) -> _core_pybinds.sensor_data.SensorData: ...
    def get_sensor_data_by_time_ns(self, stream_id: _core_pybinds.stream_id.StreamId, time_ns: int, time_domain: _core_pybinds.sensor_data.TimeDomain, time_query_options: _core_pybinds.sensor_data.TimeQueryOptions = ...) -> _core_pybinds.sensor_data.SensorData: ...
    def get_sensor_data_type(self, stream_id: _core_pybinds.stream_id.StreamId) -> _core_pybinds.sensor_data.SensorDataType: ...
    def get_stream_id_from_label(self, label: str) -> Optional[_core_pybinds.stream_id.StreamId]: ...
    def get_timestamps_ns(self, stream_id: _core_pybinds.stream_id.StreamId, time_domain: _core_pybinds.sensor_data.TimeDomain) -> List[int]: ...
    def get_wps_configuration(self, stream_id: _core_pybinds.stream_id.StreamId) -> _core_pybinds.sensor_data.WifiBeaconConfigRecord: ...
    def get_wps_data_by_index(self, stream_id: _core_pybinds.stream_id.StreamId, index: int) -> _core_pybinds.sensor_data.WifiBeaconData: ...
    def get_wps_data_by_time_ns(self, stream_id: _core_pybinds.stream_id.StreamId, time_ns: int, time_domain: _core_pybinds.sensor_data.TimeDomain, time_query_options: _core_pybinds.sensor_data.TimeQueryOptions = ...) -> _core_pybinds.sensor_data.WifiBeaconData: ...
    def supports_time_domain(self, stream_id: _core_pybinds.stream_id.StreamId, time_domain: _core_pybinds.sensor_data.TimeDomain) -> bool: ...

def create_vrs_data_provider(*args, **kwargs) -> Any: ...
