import cv2
import time

def main():
    cap = cv2.VideoCapture('./video/6.mp4')
    time.sleep(1)
    if cap is None or not cap.isOpened():
        print('Khong the mo file video')
        return
    cv2.namedWindow('Image', cv2.WINDOW_AUTOSIZE)
    n = 1
    dem = 1000
    while True:
        [success, img] = cap.read()
        ch = cv2.waitKey(5)
        if success:
            imgROI = cv2.resize(imgROI,(100,100))
            cv2.imshow('Image', imgROI)
        else:
            break
        if n%4 == 0:
            filename = './thanhlong/%03d.jpg'%(dem)
            cv2.imwrite(filename,imgROI)
            dem = dem + 1
        n = n + 1
    return

if __name__ == "__main__":
    main()
