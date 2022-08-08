# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import sys
import os
import datetime as dt
import time
import picamera
import csv

sys.excepthook = sys.__excepthook__

def printlog(content):

    timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = [[timestamp, content]]

    with open('output.txt', 'a', newline='') as logfile:
        logwriter = csv.writer(logfile, delimiter=',')
        for row in data:
            logwriter.writerow(row)

    # print to shell too
    print(timestamp,content)
    

if __name__ == "__main__":

  printlog('Starting up CCTV')
  camera = picamera.PiCamera()
  camera.resolution = (640, 480)
  camera.framerate = 15

  filePath = '/media/pi/KINGSTON/camera-records/'
  start = dt.datetime.now()

  while not os.path.isdir(filePath):
    printlog('Usb not found yet, sleeping')
    time.sleep(10)
    if (dt.datetime.now()-start).total_seconds() > 180:
      printlog('USB still not found after 3 minutes, exiting')
      exit(0)

  try:

    while True:

      if (dt.datetime.now().hour > 6 and dt.datetime.now().hour < 18):
        # start when after 6 AM

        printlog('Time is {}, starting to record.'.format(dt.datetime.now()))
        camera.start_recording(filePath + dt.datetime.now().strftime(
        '%m-%d_%H-%M') + '.h264')
        camera.wait_recording(60*60)

        # Keep recording in hour interwals until evening
        #while (dt.datetime.now().hour > 6 and dt.datetime.now().hour < 18):
        while (True):
          printlog('Splitting recording, time now {}.'.format(dt.datetime.now()))
          camera.split_recording(filePath + dt.datetime.now().strftime(
          '%m-%d_%H-%M') + '.h264')
          camera.wait_recording(60*60)
      
      else:
        # sleep when after 6PM and before 6AM
        printlog('Time is {}, going to sleep for an hour.'.format(dt.datetime.now()))
        time.sleep(60*60)
    
  except KeyboardInterrupt:
    printlog('Exiting: KeyboardInterrupt')

  finally:
    try:
      printlog('Stopping camera')
      camera.stop_recording()
      camera.close()
    except:
      printlog('Camera already stopped')