# https://github.com/tobiipro/prosdk-addons-python

import time
import tobii_research as tr
from tobii_research_addons import ScreenBasedCalibrationValidation, Point2

found_eyetrackers = tr.find_all_eyetrackers()
my_eyetracker = found_eyetrackers[0]

eyetracker_address = my_eyetracker.address
eyetracker = tr.EyeTracker(eyetracker_address)
sample_count = 30
timeout_ms = 1000
points_to_collect = [
    Point2(0.1, 0.1),
    Point2(0.1, 0.9),
    Point2(0.5, 0.5),
    Point2(0.9, 0.1),
    Point2(0.9, 0.9)]

with ScreenBasedCalibrationValidation(eyetracker, sample_count, timeout_ms) as calib:
    for point in points_to_collect:
        # Visualize point on screen
        # ...
        calib.start_collecting_data(point)
        while calib.is_collecting_data:
            time.sleep(0.5)
    calibration_result = calib.compute()

