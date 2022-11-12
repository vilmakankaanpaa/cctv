# Simple CCTV camera for a location without WIFI

The purpose of this project was to enable recording an animal's environment in the zoo for a week between 6AM and 6PM. The location has no wifi nor mobile network which prevented use of the off-the-shelf cameras that all rely on wifi network.

This is a simple camera script for recording footage with a Raspberry Pi. The script splits recording to hour-long .h264 video clips. Currently, the  program records from 7AM to 6PM, and sleeps for the remaining 13 hour window. The quality of the videos is kept low, around 200MB/hour, and the footage is saved into a USB stick.

## Hardware

If used without internet connection, Real Time Clock (RTC) is required for the raspberry pi to keep time accurate. Instructions for using RTC https://pimylifeup.com/raspberry-pi-rtc/.

Notice that USB stick needs ample space if the files are not transferred often.

## Starting at boot

There are multiple ways of setting up programs to run at boot. For this I used file /etc/rc.local:

```bash
sudo nano /etc/rc.local
```

content of the file:

```bash
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi

bash -c 'sh /home/pi/cctv/launcher.sh >> /home/pi/cctv/output.txt 2>&1' &

exit 0
```
