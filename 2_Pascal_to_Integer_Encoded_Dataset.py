import os
import cv2
import shutil
import numpy as np

def saveimgsandmasks(segclasspath,JPEGimagespath,ExclusionList,finalCompletedir,finalmaskdir,finalimagedir):
    for imgname in os.listdir(JPEGimagespath):
        # For some images (around nine), the naming convention was different, so the next three lines were commented out.
        _,imgNumber=imgname.split('_')
        imgNumber,_=imgNumber.split('.')
        if  int(imgNumber) not in ExclusionList:
            img=cv2.imread(JPEGimagespath+'/'+imgname)
            cv2.imwrite(finalimagedir+'/'+imgname ,img)  

    print('Finished Copying Images')

    for maskname in os.listdir(segclasspath):
        # For some images (around nine), the naming convention was different, so the next three lines were commented out.
        _,maskNumber=maskname.split('_')
        maskNumber,_=maskNumber.split('.')

        if  int(maskNumber) not in ExclusionList:
        
            mask=cv2.imread(segclasspath+'/'+maskname)
            newmask=np.zeros((mask.shape[0],mask.shape[1]),dtype=np.uint8)

            for i,row in enumerate(mask):
                for j,bgr in enumerate(row):
                    rgb=bgr[::-1]    
                    string_rgb=','.join(map(str,rgb))
                    newmask[i][j]=colorvec[string_rgb]
            
            cv2.imwrite(finalmaskdir+'/'+maskname ,newmask)
    print('Finished Copying masks')
    print('Total',len(os.listdir(finalmaskdir)),' images dataset')



colorvec={
"128,128,0":1,#fat
"0,0,128":0,#reticulin
"0,0,0":2,#cell
"0,128,0":2,#cell
"128,0,0":3#bone
}

segclasspath='ANNOTATIONS/SegmentationClass'
JPEGimagespath='ANNOTATIONS/JPEGImages'
ExclusionList=[]

finalCompletedir='integer-encoded-dataset'
finalmaskdir='integer-encoded-dataset/integer-encoded-masks'
finalimagedir='integer-encoded-dataset/integer-encoded-images'

shutil.rmtree(finalCompletedir)
os.mkdir(finalCompletedir)
os.mkdir(finalmaskdir)
os.mkdir(finalimagedir)
saveimgsandmasks(segclasspath,JPEGimagespath,ExclusionList,finalCompletedir,finalmaskdir,finalimagedir)


