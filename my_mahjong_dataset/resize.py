import cv2
for i in range(9):
        for j in range(12):
            #filename='./datas/train/'+'1'+'_'+str(i)+'_'+str(j)+'.png'
            filename='./datas/train/'+'2'+'_'+str(i)+'_'+str(j)+'.png'
            filename='./datas/test/'+'3'+'_'+str(i)+'_'+str(j)+'.png'
            p=cv2.imread(filename)
            p=cv2.resize(p, (67, 100))
            cv2.imwrite(filename,p)
