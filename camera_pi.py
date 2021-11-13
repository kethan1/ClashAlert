import io
import time
import picamera
from base_camera import BaseCamera

import cv2
import numpy as np


class Camera(BaseCamera):
    @staticmethod
    def frames():
        with picamera.PiCamera(resolution=(900, 640)) as camera:
            camera.vflip = True
            # let camera warm up
            time.sleep(2)

            stream = io.BytesIO()
            for _ in camera.capture_continuous(stream, "jpeg", use_video_port=True):
                # return current frame
                stream.seek(0)

                # Construct a numpy array from the stream
                data = np.fromstring(stream.getvalue(), dtype=np.uint8)
                # "Decode" the image from the array, preserving colour
                frame = cv2.imdecode(data, 1)
                stream.seek(0)
                stream_read = stream.read()

                # Convert BGR to HSV
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                
                # boundary RED color range values; Hue (160 - 180)
                lower2 = np.array([160, 100, 175])
                upper2 = np.array([179, 255, 255])
                
                mask = cv2.inRange(hsv, lower2, upper2)

                # Bitwise-AND mask and original image
                res = cv2.bitwise_and(frame, frame, mask=mask)

                if cv2.countNonZero(cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)) > 300:
                    print("Red LED Detected")
                    Camera.red_led_detected = True
                else:
                    Camera.red_led_detected = False

                cv2.imshow("res", res)
                time.sleep(0.001)

                yield stream_read

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()
                time.sleep(0.05)
