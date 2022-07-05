# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import datetime as dt
import picamera

if __name__ == "__main__":

  print('Starting up CCTV')
  camera = picamera.PiCamera()
  camera.resolution = (640, 480)
  camera.framerate = 24

  filePath = '/home/pi/cctv/recordings/'

  camera.start_recording(filePath + dt.datetime.now().strftime(
    '%m-%d_%H:%M:%S') + '.h264')
  camera.wait_recording(30) # 30 seconds

  start = dt.datetime.now()
  while (dt.datetime.now() - start).seconds < 30:
    camera.split_recording(filePath + '{}' + '.h264'.format(
    dt.datetime.now().strftime('%m-%d_%H:%M:%S')))
    camera.wait_recording(5)
  camera.stop_recording()
  

  #start = dt.datetime.now()
  #while (dt.datetime.now() - start).seconds < 30:
  #    camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  #    camera.wait_recording(0.2)
  # camera.stop_recording()


    #while(datetime.now().hour < 18 or datetime.now().hour >6):

    # if camera.is_recording:
    #     # turn of recording 
    #     camera.stop_recording()

    # print('Time is {}, going to sleep for an hour.'.format(datetime.now().hour))
    # sleep(60*60)
