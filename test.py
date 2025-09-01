import cv2

def main():
    print("hello, OpenCV!")
    print("a의 차원 :")
    print(cv2.__version__)
    imgfile = '/mnt/c/Users/MakerSpace/Downloads/data/lenna.bmp'
    img = cv2.imread(imgfile)
    cv2.imshow("lenna", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
