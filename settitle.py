import wx
import time

def main():
    
    app = wx.App()
    frame = wx.Frame(None, -1, u'window')
    frame.Show()
    for num in range(10):
        frame.SetTitle(str(num))
        time.sleep(1)
    # app.MainLoop()
    

if __name__ == '__main__':
    main()

# def execute(eyetracker):
#     gaze_data(eyetracker)

# import time
# import tobii_research as tr
# global_gaze_data = []
# found_eyetrackers = tr.find_all_eyetrackers()
# eyetracker = found_eyetrackers[0]


# def gaze_data_callback(gaze_data):
#     global global_gaze_data
#     global_gaze_data.append(gaze_data)

# def gaze_data(eyetracker):
#     global global_gaze_data

# print("Subscribing to gaze data for eye tracker with serial number {0}.".format(eyetracker.serial_number))
# eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)

# # Wait while some gaze data is collected.
# time.sleep(2)

# eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
# print("Unsubscribed from gaze data.")

# print("global_gaze_data:")
# print(global_gaze_data)
# # <EndExample>