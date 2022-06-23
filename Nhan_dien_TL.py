from keras.models import  load_model
import cv2 
import numpy as np 
from keras.utils import img_to_array

video = cv2.VideoCapture('./video/1.mp4')
label = ['Thanh long','Khong phai thanh long']
model = load_model("project.h5")

while True:
    #Doc IP tu Cam 
    [ret, frame] = video.read() #ret la ket qua doc anh , frame la anh doc ve 
    #Neu doc thanh cong thi hien thi
    if ret == True:
        # Resize
        image = frame.copy()
        image = image[:,:] # Tao ra anh 480x480
        image = cv2.resize(image, dsize=(100, 100))
        image = img_to_array(image)
        image = image.reshape(1,100,100,3)  
        image = image.astype('float32') 
        image = image/255 
        # Predict
        predict = model.predict(image)
        if (np.max(predict)>=0.90):
            print(np.argmax(predict[0]))
            font = cv2.FONT_HERSHEY_SIMPLEX
            org = (50, 50)
            fontScale = 1.5
            color = (0, 255, 0)
            thickness = 2
            if np.argmax(model.predict(image))!=0:
                a=1
            else: 
                a=0
            cv2.putText(frame, label[a], org, font,fontScale, color, thickness, cv2.LINE_AA)
        cv2.imshow("Nhan dien thanh long",frame)
    #Bam q de thoat
    if cv2.waitKey(1) == ord("q"):
        break
#video.release()
cv2.destroyAllWindows()