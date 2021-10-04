import numpy as np
import datetime

#Global Seismotectonics 3
#A strike slip
#E thrust
#C normal

#Seismotectonics 3
#a
x = 160
y = 120
A = x * y
print(A)
D = 2

A = A * 10**6
print(A)
#Vs = sqrt.µ/p
p = 2800
Vs = 3.3*10**3
print(Vs)

µ = p * (Vs)**2
print(µ)


Mo = µ * D * A
print(Mo)

#Local Earthquake 1
import datetime
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import math



tp1 = datetime.datetime(2020,1,1,21,14,54,650000)
tp2 = datetime.datetime(2020,1,1,21,14,57,340000)
tp3 = datetime.datetime(2020,1,1,21,15,00,490000)
tp4 = datetime.datetime(2020,1,1,21,15,1,800000)
tp5 = datetime.datetime(2020,1,1,21,15,1,900000)
tp6 = datetime.datetime(2020,1,1,21,15,2,250000)
tp7 = datetime.datetime(2020,1,1,21,15,3,100000)
tp8 = datetime.datetime(2020,1,1,21,15,3,500000)
tp9 = datetime.datetime(2020,1,1,21,15,6,80000)
tp10 = datetime.datetime(2020,1,1,21,15,7,70000)
tp11 = datetime.datetime(2020,1,1,21,15,8,320000)
tp12 = datetime.datetime(2020,1,1,21,15,11,120000)
tp13 = datetime.datetime(2020,1,1,21,15,11,500000)
tp14 = datetime.datetime(2020,1,1,21,15,17,800000)



ts1 = datetime.datetime(2020,1,1,21,15,7,180000)
ts2 = datetime.datetime(2020,1,1,21,15,11,920000)
ts3 = datetime.datetime(2020,1,1,21,15,17,670000)
ts4 = datetime.datetime(2020,1,1,21,15,20,220000)
ts5 = datetime.datetime(2020,1,1,21,15,20,290000)
ts6 = datetime.datetime(2020,1,1,21,15,21,20000)
ts7 = datetime.datetime(2020,1,1,21,15,22,700000)
ts8 = datetime.datetime(2020,1,1,21,15,23,980000)
ts9 = datetime.datetime(2020,1,1,21,15,28,180000)
ts10 = datetime.datetime(2020,1,1,21,15,30,40000)
ts11 = datetime.datetime(2020,1,1,21,15,33,30000)
ts12 = datetime.datetime(2020,1,1,21,15,38,330000)
ts13 = datetime.datetime(2020,1,1,21,15,38,670000)
ts14 = datetime.datetime(2020,1,1,21,15,50,630000)

 


tp = []
for i in range(1,15):
    tp.append(vars()["tp" + str(i)])

 

    
ts = []
for i in range(1,15):
    ts.append(vars()["ts" + str(i)])
    
diff = []
for i in range(0,14):
    diff.append((ts[i] - tp[i]).total_seconds())
    #diff[i] = diff[i].total_seconds()
    
tp = []
for i in range(1,15):
    tp.append(vars()["tp" + str(i)])
    tp[i-1] = (tp[i-1] - tp1).total_seconds()
    
slope, intercept, r, p, std_err = stats.linregress(tp, diff)

 

def myfunc(x):
    return slope * x + intercept

 

mymodel = list(map(myfunc, tp))
    
    
plt.style.use('seaborn')
plt.scatter(tp, diff)
plt.plot(tp, mymodel)
plt.gcf().autofmt_xdate()
plt.title('Wadati-diagram')
plt.xlabel('Seconds after first arrival')
plt.ylabel('Arrival time difference')
plt.tight_layout()



ratio = 1 + slope
print(ratio)

plt.show()

#Focal Time
#21:14:41