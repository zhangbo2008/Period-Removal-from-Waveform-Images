#傅里叶方法算周期!!!带噪音的图像都能算.


import numpy as np
import matplotlib.pyplot as plt
import numpy as np
 
fs = 100  # frequency: 100  Hz        #======这个是cos函数的周期也就是我们最后要求的东西., cos频率100, 也就是周期1/100. 下面采样频率 1000, 所以一个cos周期包含10个采样点. 所以我们最后计算应该得到10!!!!!!!!!!!!!!!
Fs = 1000 # sampling frequency: 1000 Hz  # 这个是采样率.
 
dt = 1/Fs # sampling period
N = 2048      # 总共有多少个点,.
 
T = N * dt # span
 
t = np.linspace(0, T, N, endpoint = False) # time
data = np.cos(2 * np.pi * fs * t) + np.random.normal(scale = 0.2, size = len(t))
 
# data = np.random.randint(6, 10, 300)  # 生成随机数
X = np.fft.fft(data) # Discrete Fourier Transform by fft
X = np.abs(X)

plt.subplot(2, 1, 1)
plt.plot(data[:100])  #==========只画出前100个点.


plt.subplot(2, 1, 2)
plt.plot(X)

 
mean_X = np.mean(X)
distance = (X-mean_X) ** 2
mean_distance = np.mean(distance)   # 均值和方差.
frequency = [i for i in range(len(distance)) if distance[i] > 0.8 * mean_distance]  # 把X标准差数组里面大于他自己方差0.8倍的数据索引找出来.
 
length = len(X)
if len(frequency) > 2:
    if frequency[0] == 0:
        period = length // frequency[1]  # length个点中，完成了frequency[1]个周期
        if period >= 0.5 * length:
            print("none")
        print(period)
    else:
        period = length // frequency[1]     # length是总时间, frequcency是频率第一个高点.
        if period >= 0.5 * length: #周期大于长度一半的是不合法的!!!!!!!
            print("none")
        print(period)
else:
    print("none")
plt.savefig('傅里叶算周期.png')
print(1)