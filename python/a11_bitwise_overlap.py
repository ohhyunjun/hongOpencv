import numpy as np
import cv2

def main():
    image = cv2.imread("/home/hyunjun/hongOpencv/data/background.jpg", cv2.IMREAD_COLOR)
    logo = cv2.imread("/home/hyunjun/hongOpencv/data/samsung_logo.png", cv2.IMREAD_UNCHANGED)
    # if image is None or logo in None: raise Exception("영상파일 읽기 오류")
    # 로고 크기를 50x50으로 변경합니다.
    logo = cv2.resize(logo, (50, 50))

    # 로고에서 컬러(BGR) 채널과 알파(투명도) 채널을 분리합니다.
    # logo[:,:,0:3]은 BGR 컬러 채널을, logo[:,:,3]은 알파 채널을 나타냅니다.
    b, g, r, alpha = cv2.split(logo)
    
    # 알파 채널을 마스크로 사용합니다.
    fg_mask = alpha
    bg_mask = cv2.bitwise_not(alpha)

    # 배경 이미지에 로고를 삽입할 영역(ROI)을 설정합니다.
    (h, w) = logo.shape[:2]  # 로고의 높이와 너비
    x, y = 10, 10           # 로고를 삽입할 시작점
    roi = image[y:y+h, x:x+w]

    # 비트와이즈 AND 연산을 사용해 로고 영역과 배경 영역을 분리합니다.
    # 1. 로고가 들어갈 배경 부분만 남깁니다.
    background_roi = cv2.bitwise_and(roi, roi, mask=bg_mask)
    
    # 2. 로고의 컬러 부분만 남깁니다.
    foreground_logo = cv2.bitwise_and(logo[:,:,0:3], logo[:,:,0:3], mask=fg_mask)

    # 두 이미지를 더해 합성합니다.
    dst = cv2.add(background_roi, foreground_logo)

    # 합성된 이미지를 원본 배경 이미지의 ROI에 덮어씌웁니다.
    image[y:y+h, x:x+w] = dst

    cv2.imshow("Result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()