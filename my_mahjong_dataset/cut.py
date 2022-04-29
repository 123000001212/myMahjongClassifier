import cv2

#for filename in ['ori1.jpg','ori2.jpg','ori3.jpg']:
for filename in ['ori3.jpg']:
    filename='./ori/'+filename
    p=cv2.imread(filename)
    width,height,_=p.shape
    w,h=width//9,height//12
    for i in range(9):
        for j in range(12):
            box=(i*w,j*h,(i+1)*w,(j+1)*h)
            cut_img=p[i*w+10:(i+1)*w-10,j*h+10:(j+1)*h-10,:]
            cv2.imwrite('./datas/test/'+filename[9]+'_'+str(i)+'_'+str(j)+'.png',cut_img)  
