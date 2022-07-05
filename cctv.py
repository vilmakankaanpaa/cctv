# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import sys
import datetime as dt
import time
import picamera

sys.excepthook = sys.__excepthook__

if __name__ == "__main__":

  print('Starting up CCTV')
  camera = picamera.PiCamera()
  camera.resolution = (640, 480)
  camera.framerate = 15

  filePath = '/home/pi/cctv/recordings/'

  try:

    while True:

      if (dt.datetime.now().hour > 6 and dt.datetime.now().hour < 18):
        # start when after 6 AM

        print('Time is {}, starting to record.'.format(dt.datetime.now()))
        camera.start_recording(filePath + dt.datetime.now().strftime(
        '%m-%d_%H-%M') + '.h264')
        camera.wait_recording(60*60)

        # Keep recording in hour interwals until evening
        while (dt.datetime.now().hour > 6 and dt.datetime.now().hour < 18):
          print('Splitting recording, time now {}.'.format(dt.datetime.now()))
          camera.split_recording(filePath + dt.datetime.now().strftime(
          '%m-%d_%H-%M') + '.h264')
          camera.wait_recording(60*60)
        
        camera.stop_recording()
      else:
        # sleep when after 6PM and before 6AM
        print('Time is {}, going to sleep for an hour.'.format(dt.datetime.now()))
        time.sleep(60*60)
    
  except KeyboardInterrupt:
    print('Exiting: KeyboardInterrupt')

  finally:
    try:
      print('Stopping camera')
      camera.stop_recording()
      camera.close()
    except:
      print('Camera already stopped')