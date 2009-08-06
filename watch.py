#!/usr/bin/env python
import subprocess, camera, time

cam = camera.Camera()
while True:
    if subprocess.Popen("vpnclient stat | grep 'No connection exists'", 
                        shell=True, stdout=subprocess.PIPE).stdout.read():
        cam.off()
    else:
        cam.on()

    time.sleep(5)

