import subprocess, signal, time

class Camera:
    """A simple hack which uses a binary which captures a 
       frame from the isight camera. """

    def __init__(self):
        self.p = None

    def on(self):
        """turn on the camera led by asking isightcapture to 
           take a snapshot then putting it to sleep"""
        if not self.p:
            self.p = subprocess.Popen(["isightcapture", "-n 100", "/tmp/foo.png"])
            time.sleep(0.5)
            self.p.send_signal(signal.SIGSTOP)
    def off(self):
        """turn off the camera led by killing isightcapture"""
        if self.p:
            self.p.kill()
            self.p = None


if __name__ == '__main__':
    c = Camera()
    print "Turning camera on"
    c.on()
    time.sleep(100)
    print "Turning camera off"
    c.off()

