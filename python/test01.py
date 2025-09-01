import cv2

def main():
    # 이미지 경로를 현재 사용자(hyunjun)의 홈 디렉터리로 수정
    image_path = '/home/hyunjun/hongOpencv/data/lenna.bmp'
    
    # 이미지 불러오기
    img = cv2.imread(image_path)
    
    # 이미지가 제대로 로드되었는지 확인
    if img is None:
        print(f"오류: {image_path}에서 이미지를 불러올 수 없습니다. 경로를 확인하세요.")
        return
        
    # 이미지 화면에 표시
    cv2.imshow("lenna img", img)
    
    # 키 입력 대기 후 창 닫기
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()