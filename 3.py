import numpy as np

import re

aaaa=np.loadtxt(r'1\1v19\1.txt')
aaaa=np.loadtxt(r'5\5v05\0.txt')
aaaa=np.loadtxt(r'100\100v05\0.txt')
# aaaa=np.loadtxt(a)
# aaaa=np.loadtxt(r'10\10v05\0.txt')
# print(1)


xielv=aaaa[1:]-aaaa[:-1]
xielv=np.concatenate([np.zeros(1),xielv]).astype(int)

# print(xielv)
#进行 截断, 这里使用400和100作为分界.  还有-400 和-100
# gaopin=400

# xielv[xielv>=gaopin]=gaopin
# xielv[xielv<=-gaopin]=-gaopin


# xielv[np.logical_and(xielv >=100,xielv<gaopin)]=100
# xielv[np.logical_and(xielv <=-100,xielv>-gaopin)]=-100
# xielv[np.logical_and(xielv <100,xielv>-100)]=0

pinghuan=10
#=找到所有拐点!!!!!!!!!记录到out  ======这里拐点指的是那些尖点.
out=[]
for dex in range(1,len(xielv)-1):
 if aaaa[dex]>2200:
  if xielv[dex]>=15  :
    if xielv[dex+1]<=-15 :
      out.append(dex)
    if abs(xielv[dex+1])<pinghuan and xielv[dex+2]<=-15:
      out.append(dex)
    if abs(xielv[dex+1])<pinghuan and abs(xielv[dex+2])<pinghuan and xielv[dex+3]<=-15:
      out.append(dex)
    if abs(xielv[dex+1])<pinghuan and abs(xielv[dex+2])<pinghuan and abs(xielv[dex+3])<pinghuan and xielv[dex+4]<=-15:
      out.append(dex)
print(1)



#========下面找到周期


maxi_duration=len(out)//2
mini_duration=3


save=float('inf')
savedex=0
for iiii in range(mini_duration,maxi_duration+1):
  #=======现充最长开始算.
  tmp_duration=iiii-1
  #从第二个节点开始算.
  diyipian=aaaa[out[1]:out[1+tmp_duration]]
  dierpian=aaaa[out[1+tmp_duration]:out[1+tmp_duration*2]]

  print(111)
  if 1:
    import matplotlib.pyplot as plt
    plt.clf()
    plt.plot(diyipian)
    plt.plot(dierpian)
    plt.savefig(f'周期检测图像周期为{iiii}.png')


  long=max(len(diyipian),len(dierpian))
  diyipian=list(diyipian)
  dierpian=list(dierpian)

  diyipian=diyipian+[0]*(long-len(diyipian))
  dierpian=dierpian+[0]*(long-len(dierpian))

  diff= np.sum(np.abs(np.array(diyipian)-np.array(dierpian)))
  print(diff)
  if diff<save:
    save=diff
    savedex=iiii
print('最好的单周期图像是从第二个高点,持续几个高点',savedex)