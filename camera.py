import cv2

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        self.video1 = cv2.VideoCapture(1)
        self.video2 = cv2.VideoCapture(2)
        #self.video3 = cv2.VideoCapture(3)
        
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):        
        self.video.release()
        self.video1.release()
        self.video2.release()
        #self.video3.release()
    
    def get_frame(self):        
        success, image = self.video.read()
        success1, image1 = self.video1.read()
        success2, image2 = self.video2.read()
        #success3, image3 = self.video3.read()
        final = cv2.hconcat([image, image1])
        #final1 = cv2.hconcat([image2, image3])    
        #final2 = cv2.vconcat([final, image2])
        resize = cv2.resize(final,None, fx=0.8, fy=0.8)
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', resize)
        return jpeg.tobytes()