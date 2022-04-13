from unittest import result
import cv2
from cv2 import VideoCapture
import dropbox
import time
import random
start_time= time.time()
def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        image_name="img"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        start_time=time.time
        result=False
    return image_name
    print('snapshot taken')
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def uploadFile(image_name):
    access_token="sl.BFaWuyvjkofHM5J-aFqXAZgGvbFCiqE1UhgVDMla2ml0CHxIOrm7XhhTPIDEI3TGX_b9HTM07nwhcvhoC1GsoqrOcF7dDnDHdPnSxh9Vp6-W88sQiyjArYHpUOGa3OlJURxQcoY"
    file=image_name
    file_from="C:/Users/jashi/Desktop/c102/c102.py"
    file_to="C:/Users/jashi/Desktop/c102/"+(image_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overWrite)
        print('file uploaded')
def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            uploadFile(name)
main()
