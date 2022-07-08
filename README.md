# Simple CCTV camera for a location without WIFI

The purpose of this project was to enable recording an animal's environment in the zoo for a week between 6AM and 6PM. The location has now wifi nor mobile network.

This is a simple camera script for recording footage with a Raspberry Pi. The script splits recording to hour-long .h264 video clips. Currently, the  program records from 6AM to 6PM, and sleeps for the remaining 12 hour window. The quality of the videos is kept low, around 200MB/hour, and the footage is saved into a USB stick.
