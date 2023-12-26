# 2.1 Question1

# 2.1.1
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon
np.random.seed(0)
scale = 2.0
n = 100
data1 = np.random.exponential(scale, n)
plt.hist(data1, bins=20, density=True)
x = np.linspace(0, 15, 100)
plt.plot(x, expon.pdf(x, scale=scale), label='Expoential PDF') 
plt.legend()
plt.show()

# 2.1.2
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon
mean1 = np.mean(data1)
var1 = np.var(data1)
t1 = (mean1 - 2)/(np.sqrt(var1/n))
print('mean is {}, variance is {}, T-statistics is {}'.format(mean1, var1,t1))

# 2.1.3
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
t_values = []
for i in range(1000):
    data1 = np.random.exponential(scale, n)     
    mean1 = np.mean(data1)
    var1 = np.var(data1)
    t1 = (mean1 - 2)/(np.sqrt(var1/n))
    t_values.append(t1)

plt.hist(t_values, bins=100, density=True)
x = np.linspace(-5, 5, 100)
plt.plot(x, norm.pdf(x),  label='Standard Normal PDF') 
plt.legend()
plt.show() 

# 2.1.4
import numpy as np
from scipy.stats import norm 
from scipy.stats import uniform 
import matplotlib.pyplot as plt
t_values = []
for i in range(1000):
    data1 = np.random.exponential(scale, n)     
    mean1 = np.mean(data1)
    var1 = np.var(data1)
    t1 = (mean1 - 2)/(np.sqrt(var1/n))
    t_values.append(t1)

s_values = []
plt.xlim((0,1))
plt.ylim((0,2))
for i in range(1000):
    s_values.append(1-norm.cdf(t_values[i]))
plt.hist(s_values, bins=100, density=True)
x = np.linspace(0,1,5)
plt.plot(x, uniform.pdf(x,0,1),  label='uniform PDF')

# 2.2 Question2

# 2.2.1
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon
size=100
low = 0
high = 1
data_x = np.random.uniform(low,high,size)
mean = 0
standard_deviation = 1
data_epsilon = np.random.normal(mean,standard_deviation,size) 
data_y = np.sin(2 * np.pi * data_x) + data_epsilon
plt.scatter(data_x,data_y)

# 2.2.2
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon
size=100
low = 0
high = 1
data_x = np.random.uniform(low,high,size)
mean = 0
standard_deviation = 1
data_epsilon = np.random.normal(mean,standard_deviation,size) 
data_y = np.sin(2 * np.pi * data_x) + data_epsilon
x = np.linspace(start = 0,stop = 1.0, num = 20)
ret1 = np.zeros(20) 
ret2 = np.zeros(20) 
ret3 = np.zeros(20) 
for i in range(20):
    z = x[i]
    ret1[i] = np.sum((np.absolute(data_x - z) <= 0.05) * 1.0 * data_y) / (2.0 * 100 * 0.05)     
    ret2[i] = np.sum((np.absolute(data_x - z) <= 0.15) * 1.0 * data_y) / (2.0 * 100 * 0.15)     
    ret3[i] = np.sum((np.absolute(data_x - z) <= 0.25) * 1.0 * data_y) / (2.0 * 100 * 0.25)

plt.plot(x, ret1, label = 'h = {}'.format(0.05)) 
plt.plot(x, ret2, label = 'h = {}'.format(0.15)) 
plt.plot(x, ret3, label = 'h = {}'.format(0.25)) 
plt.legend()
plt.show()

# 2.2.3
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon
size=100
low = 0
high = 1
data_x = np.random.uniform(low,high,size)
mean = 0
standard_deviation = 1
data_epsilon = np.random.normal(mean,standard_deviation,size) 
data_y = np.sin(2 * np.pi * data_x) + data_epsilon
x = np.linspace(start = 0,stop = 1.0, num = 20)
ret4 = np.zeros(20) 
ret5 = np.zeros(20) 
ret6 = np.zeros(20) 
for i in range(20):
    z = x[i]
    ret4[i] = np.sum(data_y/ (100 * 0.05) * (1/ np.sqrt(2 * np.pi)) * np.exp(((z - data_x) / 0.05)))    
    ret5[i] = np.sum(data_y/ (100 * 0.15) * (1/ np.sqrt(2 * np.pi)) * np.exp(((z - data_x) / 0.15)))   
    ret6[i] = np.sum(data_y/ (100 * 0.25) * (1/ np.sqrt(2 * np.pi)) * np.exp(((z - data_x) / 0.25)))
plt.plot(x, ret4, label = 'h = {}'.format(0.05)) 
plt.plot(x, ret5, label = 'h = {}'.format(0.15)) 
plt.plot(x, ret6, label = 'h = {}'.format(0.25)) 
plt.legend()
plt.show()
