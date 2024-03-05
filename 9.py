# 2024-03-05,8点32 优化最后可视化图像.
# ==========最终的模板匹配算法.=======计算两个时间序列的差距.
# ========采样为400




import numpy as np

import re

#=======如果有原始数据可以这么读取:
if 0:
  muban=np.loadtxt(r'1\1v19\1.txt')
  a=np.loadtxt(r'1\1v19\0.txt')
  b=np.loadtxt(r'100\100v05\0.txt')

#==========我直接把数据也写在这里了.
# muban是1\1v19\1.txt 这个里面波的2个高峰之间的部分.
muban=[ 3480., 3467.,
       3665., 4091., 4091., 3073., 1673., 1209., 1197., 1308., 1460.,
       1587., 1702., 1781., 1837., 1888., 1911., 1937., 1970., 1989.,
       2008., 2018., 2029., 2045., 2058., 2060., 2063., 2059., 2051.,
       2062., 2063., 2059., 2055., 2036., 2013., 2007., 2012., 2119.,
       2363., 2428., 2373., 2200., 1927., 1781., 1828., 1930., 1990.,
       2021., 2034., 2038., 2038., 2042., 2032., 2034., 2027., 2013.,
       2008., 2015., 2090., 2264., 2404., 2349., 2196., 1990., 1775.,
       1785., 1900., 1977., 2024., 2048., 2072., 2070., 2062., 2066.,
       2064., 2056., 2048., 2052., 2048., 2046., 2051., 2047., 2041.,
       2037., 2041., 2040., 2032., 2023., 2016., 2022., 2038., 2035.,
       2032., 2006., 1898., 1626., 1044.,  390.,  806., 2090., 3178.,
       3626., 3866., 4091., 4091., 2939., 1790., 1342., 1270., 1343.,
       1482., 1588., 1688., 1777., 1830., 1869., 1908., 1946., 1964.,
       1988., 1999., 2014., ]
a=[2053., 2043., 2052., 2061., 2057., 2049., 2064., 2063., 2049.,
       2056., 2046., 2050., 2051., 2055., 2055., 2058., 2059., 2060.,
       2040., 2042., 2051., 2043., 2047., 2051., 2061., 2041., 2058.,
       2049., 2061., 2049., 2042., 2052., 2036., 2051., 2071., 2057.,
       2043., 2036., 2051., 2048., 2072., 2053., 2054., 2061., 2048.,
       2043., 2052., 2047., 2051., 2045., 2043., 2046., 2069., 2037.,
       2060., 2054., 2068., 2044., 2033., 2044., 2044., 2057., 2040.,
       2027., 2031., 2034., 2041., 2035., 2020., 2014., 1984., 1961.,
       1981., 2142., 2318., 2347., 2293., 2135., 1961., 1887., 1904.,
       1959., 2003., 2027., 2033., 2051., 2073., 2059., 2045., 2048.,
       2043., 2041., 2042., 2042., 2038., 2030., 2025., 2020., 2016.,
       2021., 2014., 2027., 2021., 2022., 2039., 2045., 2061., 2015.,
       1893., 1565.,  840.,  161.,  819., 2422., 3405., 3568., 4112.,
       4112., 4115., 2877., 1557., 1127., 1169., 1321., 1500., 1639.,
       1744., 1820., 1864., 1901., 1905., 1946., 1970., 1982., 1997.,
       1998., 2041., 2048., 2031., 2047., 2056., 2050., 2048., 2048.,
       2066., 2052., 2043., 2016., 2006., 2008., 2120., 2336., 2400.,
       2331., 2163., 1912., 1818., 1890., 1980., 2020., 2044., 2062.,
       2067., 2053., 2052., 2042., 2035., 2030., 1999., 1987., 1981.,
       2037., 2239., 2429., 2437., 2310., 2128., 1866., 1753., 1825.,
       1906., 1972., 2014., 2051., 2050., 2070., 2040., 2043., 2061.,
       2047., 2031., 2046., 2055., 2044., 2032., 2032., 2028., 2032.,
       2018., 2024., 2021., 2012., 2031., 2057., 2054., 2067., 2068.,
       2025., 1839., 1384.,  616.,  402., 1477., 2879., 3417., 3446.,
       4131., 4127., 3674., 2054., 1346., 1214., 1307., 1456., 1603.,
       1717., 1804., 1858., 1886., 1909., 1920., 1935., 1983., 1983.,
       2004., 2003., 2021., 2025., 2042., 2058., 2055., 2061., 2046.,
       2051., 2047., 2038., 2020., 1985., 1973., 2043., 2257., 2407.,
       2346., 2240., 2050., 1886., 1859., 1928., 1994., 2021., 2041.,
       2056., 2052., 2042., 2030., 2041., 2004., 1984., 1951., 1948.,
       2070., 2292., 2392., 2348., 2205., 1933., 1823., 1868., 1939.,
       2000., 2021., 2046., 2069., 2080., 2056., 2048., 2059., 2046.,
       2045., 2032., 2050., 2051., 2029., 2032., 2040., 2040., 2025.,
       2033., 2030., 2040., 2039., 2067., 2081., 2079., 2024., 1879.,
       1502.,  840.,  670., 1639., 2860., 3475., 3935., 4119., 3550.,
       1951., 1346., 1303., 1427., 1594., 1713., 1812., 1877., 1908.,
       1931., 1952., 1968., 1979., 2002., 1999., 2015., 2038., 2027.,
       2033., 2057., 2056., 2058., 2055., 2056., 2062., 2044., 2057.,
       2062., 2059., 2056., 2052., 2049., 2055., 2045., 2062., 2061.,
       2050., 2055., 2066., 2044., 2042., 2060., 2058., 2061., 2050.,
       2061., 2069., 2051., 2071., 2056., 2049., 2049., 2046., 2039.,
       2051., 2054., 2048., 2055., 2056., 2041., 2040., 2046., 2057.,
       2057., 2054., 2058., 2056., 2061., 2055., 2051., 2042., 2039.,
       2035., 2046., 2057., 2056., 2060., 2046., 2049., 2049., 2048.,
       2055., 2040., 2050., 2052.]
b=[2060., 2049., 2049., 2052., 2053., 2058., 2062., 2053., 2043.,
       2061., 2052., 2048., 2039., 2058., 2060., 2056., 2054., 2055.,
       2060., 2052., 2047., 2051., 2049., 2059., 2062., 2056., 2049.,
       2050., 2058., 2059., 2047., 2049., 2054., 2059., 2059., 2055.,
       2051., 2056., 2049., 2056., 2059., 2051., 2059., 2052., 2051.,
       2046., 2039., 2041., 2037., 2040., 2012., 2014., 2010., 2015.,
       2033., 2050., 2083., 2050., 1947., 1657.,  926.,    7.,   15.,
       2403., 4092., 4092., 4092., 2918., 2026., 1777., 1740., 1755.,
       1818., 1887., 1929., 1952., 1953., 1939., 1913., 1843., 1605.,
       1141., 1035., 1978., 3175., 3889., 3231., 2295., 1875., 1764.,
       1748., 1791., 1837., 1892., 1935., 1958., 2003., 1999., 1968.,
       1869., 1539.,  712.,    6.,  325., 3056., 4092., 4092., 4091.,
       2538., 1882., 1733., 1729., 1787., 1833., 1891., 1935., 1968.,
       1969., 1931., 1799., 1482.,  809.,  111.,  909., 3082., 4092.,
       4092., 3771., 2385., 1841., 1707., 1704., 1752., 1815., 1885.,
       1927., 1949., 1933., 1917., 1830., 1609., 1166., 1115., 2104.,
       3144., 3876., 3061., 2155., 1842., 1765., 1777., 1815., 1864.,
       1899., 1950., 2000., 2022., 2004., 1940., 1730., 1179.,   48.,
          7., 1859., 4091., 4092., 4091., 2985., 2068., 1788., 1759.,
       1794., 1844., 1909., 1959., 1996., 1988., 1978., 1916., 1848.,
       1632., 1264., 1144., 1935., 3088., 3750., 3137., 2313., 1917.,
       1797., 1801., 1804., 1839., 1886., 1926., 1965., 1987., 1991.,
       1964., 1819., 1357.,  299.,    6., 1193., 4049., 4092., 4092.,
       3482., 2198., 1797., 1731., 1753., 1795., 1862., 1917., 1974.,
       1991., 1983., 1918., 1774., 1351.,  423.,    6., 1021., 3829.,
       4092., 4092., 3609., 2314., 1851., 1720., 1759., 1814., 1868.,
       1925., 1948., 1958., 1956., 1929., 1840., 1625., 1254., 1216.,
       2061., 3048., 3597., 3055., 2283., 1919., 1807., 1802., 1832.,
       1859., 1902., 1953., 1984., 2007., 2009., 1948., 1779., 1313.,
        329.,    7., 1731., 4091., 4092., 4092., 3006., 2035., 1769.,
       1730., 1767., 1822., 1878., 1947., 1971., 1981., 1964., 1921.,
       1826., 1583., 1230., 1260., 2120., 3128., 3612., 3003., 2246.,
       1893., 1787., 1782., 1812., 1843., 1893., 1934., 1985., 2003.,
       1990., 1946., 1835., 1543.,  925.,  343., 1007., 2780., 4091.,
       4092., 4081., 2587., 1900., 1664., 1642., 1692., 1742., 1825.,
       1894., 1959., 1981., 1987., 1938., 1793., 1414.,  492.,    6.,
        555., 3251., 4092., 4092., 4091., 2589., 1879., 1698., 1695.,
       1744., 1819., 1886., 1941., 1977., 1982., 1974., 1941., 1854.,
       1624., 1240., 1133., 1931., 3029., 3761., 3224., 2333., 1904.,
       1781., 1784., 1815., 1855., 1888., 1934., 1972., 2005., 2001.,
       1936., 1774., 1325.,  463.,  199., 1818., 4089., 4092., 4091.,
       2911., 2094., 1805., 1733., 1764., 1821., 1882., 1917., 1931.,
       1955., 1953., 1965., 1974., 1985., 1994., 2009., 2013., 2019.,
       2034., 2051., 2047., 2050., 2064., 2052., 2061., 2057., 2069.,
       2067., 2061., 2066., 2064.]
print(1)


def jisuanguaidian(a):
  aaaa=np.array(a)

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
  return out

mubanout=jisuanguaidian(muban)
aout=jisuanguaidian(a)
bout=jisuanguaidian(b)
print(1)



#======2024-03-01,11点33 两个波采样的比较方法: 局部贪心法:
#      *                                    *
#   *                                   
# *       *                           *           *
#           *                                         *
#             *                                          *
#               *                                          *
# 如何比较上述连个波. 左边波7个点, 右边波六个点. 右边当模板, 左边当被匹配的波. 模板上面的点可以部分匹配上或者全匹配上, 被匹配的波必须所有点都匹配上.
# 1. 找到两个波的最高点. 左边是第三个点记作p1, 右边是第二个点记作q1. 他俩对应就行
# 2. 因为被匹配的波必须所有点都匹配上,找p2点就是左边波的p1的下一个点,也就是第四个点. 使用贪婪方法:他对应的是跟的q1的后面四个点里面跟他距离最小的. (一直用这个方法找完即可).



#===========下面核心匹配算法: 输入连个波的采样数组, 输出diff


#=====首先我们的对应波高点数量一致.
print('aout',[a[i] for i in aout])
muban999=muban[mubanout[0]:mubanout[-1]+1]
beipipei999=a[aout[0]:aout[len(mubanout)-1]+1]
beipipei9991=a[aout[1]:aout[1+len(mubanout)-1]+1]
beipipei9992=a[aout[2]:aout[2+len(mubanout)-1]+1]
beipipei9993=a[aout[3]:aout[3+len(mubanout)-1]+1]
beipipei9994=a[aout[4]:aout[4+len(mubanout)-1]+1]
beipipeiall=[]
kkk=0
while 1:

  end=kkk+len(mubanout)-1
  if kkk and end ==len(aout):
    break
  beipipeiall.append(a[aout[kkk]:aout[end]+1])
  kkk+=1
print(1)


cnt=0
def jisuan_diff(b,m):
  global cnt
  '''
  b,m是时序数列, 可以看做波的采集数字信号.
  b是被比配的波
  m是模板波.
  我们输出的结果是拿模板上每一个采集点去找b上对应的位置.
  模板上的采集点都对应结束之后,我们的计算就结束.这个逻辑能保证模板上所有的特征都进行了比较.我们用这个diff值来表示b和m的相似度.
   
  我们规定输入的b和m的 索引0位置互相对应上,这点需要在波b和波m输入
到这个函数之前预处理掉.否则起点在函数内部用逻辑遍历太过复杂不适合函数处理.
所以我们后续点都匹配上即可.
  '''
  maxy=max(max(b),max(m))
  maxx=max(len(b),len(m))
  changdu=0 # 横坐标的偏移 产生的diff
  gaodu=0  # 纵坐标的偏移 产生的diff
  kaishi=1
  saving=0
  jilu=0 # 记录上一个匹配成功的位置.
  saving_forpic=[0]
  for i in range(1,len(m)): # 模板第0个,跟被查数组0个假设已经对齐, 从索引1开始对齐.


      chagndu=7  # ========搜索范围超参数. 对于点多的也设置大一点.

      tmpjuli=float('inf')
      
      for j in range(kaishi,kaishi+chagndu+1):
       if j<len(b):
        gaodu=abs(m[i]-b[j])
        if i!=1:
          changdu=(abs(abs(j-kaishi)-1))
        diff=(gaodu/maxy)**2+(changdu/maxx)**2
        if diff<tmpjuli:
          tmpjuli=diff
          jilu=j

      # 加上横坐标偏移惩罚: 移动一个格作为0惩罚.
      # tmpjuli+=abs(jilu-kaishi-1)
      kaishi=jilu
      saving_forpic.append(jilu)
      # print(i,jilu,tmpjuli,kaishi)
      saving+=tmpjuli
  debugpic=1
  chaju=(saving+abs(b[0]-m[0]))/len(m)
  if debugpic:
    import matplotlib.pyplot as plt
    import matplotlib.pyplot as plt
    plt.clf()
    plt.rcParams["font.sans-serif"]=["SimHei"]
    plt.rcParams["axes.unicode_minus"]=False

    # plt.plot(m,c='r',label='模板')
    plt.scatter(range(len(m)),m,c='r',label='模板',s=1)
    # plt.plot(b,c='g',label='信号')
    plt.scatter(range(len(b)),b,c='g',label='信号',s=1)
    plt.text(50,4000,f"差距是:{chaju}",horizontalalignment='center',verticalalignment='top',)
    # change x internal size
    # plt.gcf().subplots_adjust(left=margin, right=1. - margin)
    # print(plt.gcf().get_size_inches()[0])
    # print(plt.gcf().get_size_inches()[1])
    #========图片横坐标放大2被.
    plt.gcf().set_size_inches(plt.gcf().get_size_inches()[0]*1.2, plt.gcf().get_size_inches()[1])


#==========加上各个点的折线:
    for dex,itm in enumerate(saving_forpic):
      plt.plot([dex,itm],[m[dex],b[itm]],linewidth=0.2,c='b')
      # break

    plt.legend()
    plt.savefig(f'debuggg{cnt}.png')

  print(f'第{cnt}个')
  cnt+=1

  return chaju




for i in beipipeiall:
      print(jisuan_diff(muban999,i))







