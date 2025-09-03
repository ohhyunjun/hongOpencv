import cv2
import numpy as np

mouse_position = (0,0)
screen_width = 800
screen_height = 600
image = np.zeros((screen_width, screen_height, 3), np.uint8)
mouse_on = False

# 로고 및 마스크 준비
logo = cv2.imread("/home/hyunjun/hongOpencv/data/samsung_logo.png", cv2.IMREAD_UNCHANGED)
logo = cv2.resize(logo, (50, 50), logo)

# 로고 이미지의 알파 채널(투명도)을 마스크로 사용
mask = logo[:, :, 3]
logo = logo[:, :, 0:3]

def input_logo(img):
    global logo, mask
    
    # 로고를 삽입할 위치
    x, y = 10, 10
    h, w = logo.shape[:2]
    
    # ROI(관심 영역) 설정
    roi = img[y:y+h, x:x+w]

    # 로고 이미지를 전경으로, 로고 외 부분을 배경으로 사용
    fg_mask = mask
    bg_mask = cv2.bitwise_not(mask)

    # 전경 마스크와 배경 마스크를 BGR 3채널로 변환
    fg_mask = cv2.cvtColor(fg_mask, cv2.COLOR_GRAY2BGR)
    bg_mask = cv2.cvtColor(bg_mask, cv2.COLOR_GRAY2BGR)

    # 마스크를 사용하여 전경(로고)과 배경(ROI) 분리
    foreground_logo = cv2.bitwise_and(logo, fg_mask)
    background_roi = cv2.bitwise_and(roi, bg_mask)

    # 전경과 배경을 합성
    dst = cv2.add(foreground_logo, background_roi)
    
    # 최종 결과 이미지를 원본 이미지에 삽입
    img[y:y+h, x:x+w] = dst
    return img

def onMouse(event, x, y, flags, param):
    global mouse_position, image, mouse_on
    clone_img = image.copy()
    if event == cv2.EVENT_MOUSEMOVE:
        if mouse_on:
            cv2.circle(clone_img, (x,y), 10, (0,255,0), -1)
            cv2.line(clone_img, mouse_position, (x,y), (255,255,255), 2)
        else:
            cv2.rectangle(clone_img, (x-10, y-10), (x+10, y+10), (255,0,0), -1)
    elif event == cv2.EVENT_LBUTTONDOWN:
        if not mouse_on:
            mouse_position = (x, y)
        mouse_on = True
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.line(image, mouse_position, (x,y), (255,255,255), 2)
        mouse_on = False
    cv2.imshow("main", clone_img)

def main():
    switch_case = {
        ord('r'): 10,
        ord('g'): -10,
        ord('b'): 30,
        65361: -1,
        65363: 1,
        65364: -5,
        65362: 5,
    }

    cv2.namedWindow("main")
    cv2.setMouseCallback("main", onMouse)
    global image

    while True:
        key = cv2.waitKeyEx(30)
        if key == 27: break
        try:
            cv2.add(image, switch_case[key], image)
            image = input_logo(image)
            cv2.imshow("main", image)
        except KeyError:
            result = -1
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()