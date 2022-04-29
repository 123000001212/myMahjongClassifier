dic={}
dic['0']='1m'
dic['1']='2m'
dic['2']='3m'
dic['3']='4m'
dic['4']='5m'
dic['5']='6m'
dic['6']='7m'
dic['7']='8m'
dic['8']='9m'
dic['9']='1p'
dic['10']='2p'
dic['11']='3p'
dic['12']='4p'
dic['13']='5p'
dic['14']='6p'
dic['15']='7p'
dic['16']='8p'
dic['17']='9p'
dic['18']='1s'
dic['19']='2s'
dic['20']='3s'
dic['21']='4s'
dic['22']='5s'
dic['23']='6s'
dic['24']='7s'
dic['25']='8s'
dic['26']='9s'

dic2={}
for key in dic:
    dic2[dic[key]]=key

f=open('train_label.csv','w')
for i in range(9):
    for j in range(12):
        for k in range(2):
            name=str(k+1)+'_'+str(i)+'_'+str(j)+'.png'
            if j<4:
                label='m'
            elif j<8:
                label='p'
            else:
                label='s'
            label=dic2[str(i+1)+label]
            f.write(name+','+label+'\n')
f.close()
