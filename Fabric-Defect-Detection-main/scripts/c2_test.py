import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf
import numpy as np
from picamera2 import Picamera2
import threading

class CameraWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Camera")
        
        self.picam2 = Picamera2()
        self.picam2.configure(self.picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
        self.picam2.start()
        
        self.image = Gtk.Image()
        self.add(self.image)

        self.thread = threading.Thread(target=self.update_image)
        self.thread.daemon = True
        self.thread.start()

    def update_image(self):
        while True:
            frame = self.picam2.capture_array()  # Capture a frame from the camera

            # Convert the frame from BGRA to BGR
            frame_bgr = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

            # Convert frame to GdkPixbuf
            pixbuf = GdkPixbuf.Pixbuf.new_from_data(frame_bgr.tobytes(), GdkPixbuf.Colorspace.RGB, False, 8, frame_bgr.shape[1], frame_bgr.shape[0], frame_bgr.shape[2] * frame_bgr.shape[1])

            # Set the GdkPixbuf as the image source
            self.image.set_from_pixbuf(pixbuf)
            

win = CameraWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

