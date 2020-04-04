import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
from mylib import *
import sys
import os

def main():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    flag = True
    count = 0
    test_img = 0
    # aadhar = input('Enter your aadhar number:')
    aadhar = sys.argv[1]
    aadharRecordPresent = checkAadharRecord(aadhar)
    aadharRecordAbsent = not aadharRecordPresent
    faceRecordPresent = not checkFaceRecord(aadhar)
    faceRecordAbsent = not faceRecordPresent

    if aadharRecordPresent and faceRecordAbsent:
        while True:
            ret, test_img = cap.read()
            count += 1

            cv2.imshow("Press 'q' to Capture", test_img)
            k = cv2.waitKey(1)
            if (k == ord('q')):
                break

        # print(test_img)
        cv2.imwrite('D:/Coding/python/FR/images/'+aadhar+'.jpg',test_img)

        images = ['D:/Coding/python/FR/images/'+aadhar+'.jpg']
        aligned = facenet2.align_face(images)
        embeddings = facenet2.embedding(aligned)
        os.remove('D:/Coding/python/FR/images/'+aadhar+'.jpg')
        if checkFaceExist(aligned,embeddings):
            print('This face is already registered')
        else:
            insertface(aadhar,aligned,embeddings)
    elif aadharRecordPresent and faceRecordPresent:
        print('Already have a face record')
    elif aadharRecordAbsent:
        print("Aadhar Record Doesn't Exist")
    else:
        print('Something went wrong')

if __name__ == '__main__':
    main()