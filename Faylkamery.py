import rospy
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
error_x =int()
error_y=int()

class LineFollower(object):

    def __init__(self):
    
        self.bridge_object = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/rgb/image_raw",Image,self.camera_callback)

    def camera_callback(self,data):
        
        try:
            cv_image = self.bridge_object.imgmsg_to_cv2(data, desired_encoding="bgr8")
        except CvBridgeError as e:
            print(e)
            
       
        height, width, channels = cv_image.shape
        crop_img = cv_image[1:height][1:width]
        
        hsv = cv2.cvtColor(crop_img, cv2.COLOR_BGR2HSV)
        
        lower_yellow = np.array([0,0,200])
        upper_yellow = np.array([0,0,255])

        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        
        m = cv2.moments(mask, False)
        try:
            cx, cy = m['m10']/m['m00'], m['m01']/m['m00']
        except ZeroDivisionError:
            cy, cx = height/2, width/2
        
        res = cv2.bitwise_and(crop_img,crop_img, mask= mask)
        cv2.circle(res,(int(cx), int(cy)), 10,(0,0,255),-1)

        cv2.imshow("Original", cv_image)
        cv2.imshow("HSV", hsv)
        cv2.imshow("MASK", mask)
        cv2.imshow("RES", res)
        
        cv2.waitKey(1)
        global error_y
        global error_x
        
        error_x = cx - width / 2
        error_y = cy - height/2

       
    
    

    def clean_up(self):
        cv2.destroyAllWindows()
        
        

def main():
    rospy.init_node('line_following_node', anonymous=True)
    
    
    line_follower_object = LineFollower()
   
    rate = rospy.Rate(5)
    ctrl_c = False
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()
     

    
    
if __name__ == '__main__':
    main()