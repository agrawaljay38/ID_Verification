import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from easyfacenet.simple import facenet2
import cv2
from mysql.connector import connect
import pickle
import numpy as np

def checkFaceExist(newAligned,newEmbeddings):
    length, aadharNos, aligned, embeddings = getAllImages()
    length += 1
    aligned = np.append(aligned, newAligned)
    embeddings = np.append(embeddings, newEmbeddings)
    aligned = aligned.reshape((length, 160, 160, 3))
    embeddings = embeddings.reshape((length, 512))
    comparisions = facenet2.compare(aligned, embeddings)
    flag = False
    for i in range(len(comparisions)-1):
        if comparisions[i]==1:
            flag = False
            return True
    return flag

def getAllImages():
    mydb = connect(host="localhost", user="root", passwd="root1", database="db1")
    mycursor = mydb.cursor()
    sql = "select * from ae"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    aadharNos = []
    aligneds = []
    embeddings = []
    for row in result:
        aadharNo = row[0]
        aligned = pickle.loads(row[1])
        aligned.flatten()
        aligned = aligned.reshape((160,160,3))
        embedding = pickle.loads(row[2])
        embedding = embedding.flatten()
        aadharNos.append(aadharNo)
        aligneds.append(aligned)
        embeddings.append(embedding)

    return len(result),aadharNos,np.array(aligneds),np.array(embeddings)

def getPicture():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    count = 0
    while True:
        ret, test_img = cap.read()
        count += 1

        cv2.imshow("Press 'q' to capture", test_img)
        k = cv2.waitKey(1)
        if (k == ord('q')):
            break

    cv2.imwrite('D:/Coding/python/FR/images/newDetection.jpg', test_img)
    cap.release()
    cv2.destroyAllWindows()

def getAllInfo(match):
    mydb = connect(host="localhost", user="root", passwd="root1", database="db1")
    mycursor = mydb.cursor()
    sql = "select * from aadhar where number='"+match+"'"
    mycursor.execute(sql)
    result = mycursor.fetchone()
    print('Name: ',result[0],result[1])
    print('Date of Birth:',result[2])
    print('Aadhar Number:',result[3])
    print('Address:')
    print('Son/Daughter of',result[4])
    print(result[5])
    print(result[6])
    print(result[7])
    print(result[8])
    print('Mobile Number:',result[9])

def checkAadharRecord(aadhar):
    mydb = connect(host="localhost", user="root", passwd="root1", database="db1")
    mycursor = mydb.cursor()
    sql = "select * from aadhar where number='"+aadhar+"'"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if len(result)!=0:
        return True
    else:
        return False

def insertface(aadhar,align,emb):
    align = pickle.dumps(align)
    emb = pickle.dumps(emb)
    mydb = connect(host="localhost", user="root", passwd="root1", database="db1")
    mycursor = mydb.cursor()
    sql = 'insert into ae values(%s,%s,%s)'
    val = (aadhar,align,emb)
    try:
        mycursor.execute(sql,val)
        print('Face Record Inserted Successfully')
    except Exception as e:
        print("Aadhar Record Doesn't Exist")
    mydb.commit()

def checkFaceRecord(aadhar):
    mydb = connect(host="localhost", user="root", passwd="root1", database="db1")
    mycursor = mydb.cursor()
    sql = "select * from ae where number='" + aadhar + "'"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if len(result) == 0:
        return True
    else:
        return False
