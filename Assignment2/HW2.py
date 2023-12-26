# 2.1
import numpy as np 
import matplotlib. pyplot as plt 
from scipy import stats 
from functools import reduce 
## Since µ = E[Y] = 1/λ and y_bar = 10, we can know that λ_hat = 0.1
## L(λ) ＝ λ＾{2} * e^{-ny}
fig, ((ax1, ax2, ax3, ax4)) = plt.subplots (4, 1, figsize= (8, 14), sharex= True)
n_value = np.arange (0.01, 1.00, 0.01) 

list1= [] 
list2 = [] 
for i in n_value:
    b = pow(i, 1) * np.exp(-i*10*1) - pow(1/10, 1) * np.exp(-1/10*10*1) 
    list1.append(i) 
    list2.append(b)
ax1.set_title('n = {}'.format(1)) 
ax1.plot(list1, list2)

list1= [] 
list2 = [] 
for i in n_value:
    b = pow(i, 5) * np.exp(-i*10*5) - pow(1/10, 5) * np.exp(-1/10*10*5) 
    list1.append(i) 
    list2. append(b)
ax2.set_title('n = {}'.format(5)) 
ax2.plot(list1, list2, color = 'green') 

list1= [] 
list2 = [] 
for i in n_value:
    b = pow(i, 10) * np.exp(-i*10*10) - pow(1/10, 10) * np.exp(-1/10*10*10)
    list1.append(i) 
    list2. append(b)
ax3.set_title('n = {}'.format(10)) 
ax3.plot(list1, list2, color = 'orange') 

list1= [] 
list2 = [] 
for i in n_value:
    b = pow(i, 30) * np.exp(-i*10*30) - pow(1/10, 30) * np.exp(-1/10*10*30)
    list1.append(i) 
    list2. append(b)
ax4.set_title('n = {}'.format(30)) 
ax4.plot(list1, list2, color = 'pink')


# 2.2 
import numpy as np 
n_value = [1, 5, 10, 30] 
for n in n_value:
    confidence_interval = np.array([1/10 - (1/10*1.96)/np.sqrt(n), 1/10 + (1/10*1.96)/np.sqrt (n) ])
    print(confidence_interval) 