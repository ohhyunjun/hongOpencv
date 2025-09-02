import cv2
import numpy as np

def main():
    blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)
    
    # Define orange and cyan colors
    orange = (0, 165, 255)  
    cyan = (255, 255, 0)

    image = np.zeros((400, 600, 3), np.uint8)
    pt1, pt2 = (50, 50), (250, 150)
    pt3, pt4 = (400, 150), (500, 50)
    
    # The 'roi' tuple should be (x, y, width, height) which is not supported by cv2.rectangle
    # The function expects (x1, y1) and (x2, y2)
    # So, we'll redefine the 'roi' points for cv2.rectangle
    roi_pt1 = (50, 200)
    roi_pt2 = (50 + 200, 200 + 100) # (250, 300)
    
    # The rectangle tuple (400, 200, 100, 10) also needs to be converted to two points
    rect_pt1 = (400, 200)
    rect_pt2 = (400 + 100, 200 + 10) # (500, 210)

    cv2.line(image, pt1, pt2, red, 2, cv2.LINE_AA)
    cv2.line(image, pt3, pt4, green, 3, cv2.LINE_AA)

    cv2.rectangle(image, pt1, pt2, blue, 2, cv2.LINE_8)
    # Use the corrected roi points
    cv2.rectangle(image, roi_pt1, roi_pt2, red, 3, cv2.LINE_8)
    # Use the corrected rectangle points
    cv2.rectangle(image, rect_pt1, rect_pt2, green, cv2.FILLED)

    cv2.circle(image, (300, 300), 50, orange, -1)
    cv2.circle(image, (500, 300), 50, cyan, 3, cv2.LINE_AA)
    cv2.ellipse(image, (500, 300), (80, 40), 30, 0, 360, red, 3, cv2.LINE_AA)

    cv2.imshow("draw", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()