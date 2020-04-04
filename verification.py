import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
from mylib import *

def main():
    getPicture()
    images = ['D:/Coding/python/FR/images/newDetection.jpg']
    newAligned = facenet2.align_face(images)
    newEmbeddings = facenet2.embedding(newAligned)
    length,aadharNos,aligned,embeddings = getAllImages()
    length += 1
    aligned = np.append(aligned,newAligned)
    embeddings = np.append(embeddings,newEmbeddings)
    aligned = aligned.reshape((length,160,160,3))
    embeddings = embeddings.reshape((length,512))
    comparisions = facenet2.compare(aligned,embeddings)
    # print(aadharNos)
    # print(comparisions)
    match = ''
    flag = True
    for i in range(len(comparisions)-1):
        if comparisions[i]==1:
            match = aadharNos[i]
            print('Matched to '+aadharNos[i])
            flag = False
            break
    if flag:
        print('No such Face Exist')
    else:
        getAllInfo(match)


if __name__ == '__main__':
    main()