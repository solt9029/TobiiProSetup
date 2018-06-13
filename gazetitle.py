import time
import tobii_research as tr
import wx

found_eyetrackers = tr.find_all_eyetrackers()
eyetracker = found_eyetrackers[0]

app = wx.App()
frame = wx.Frame(None, -1, u'window')
frame.Show()

time.sleep(2)

def gaze_data_callback(gaze_data):
    global frame
    frame.SetTitle(str(gaze_data['left_gaze_point_on_display_area']))

eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)

time.sleep(10)

eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)