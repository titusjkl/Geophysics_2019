import numpy as np


#Tsunami Traveltime 1

g = 9.81
d = 2_207
s = 151_000

v = np.sqrt(g * d)
t = s / np.sqrt(g * d)

t = t / 60
print(f"{t.round(3)} Min")


#Traveltime Of Seismic Waves 2

Vp = 5379

#Vp / Vs = np.sqrt(3)
Vs = Vp / np.sqrt(3)

x = Vp - Vs

print(f"{x.round(2)} m/s")

a = 302 #Ankunftszeit P Welle -- Ankunftszeit S Welle

#d =  ((Vp - Vs) * (a))

vp = 5379
vs = Vs = Vp / np.sqrt(3)

tp = ((302*vs) / (vp - vs))
print(f"{tp.round(2)} Sek")

#Ankunftszeit P Welle - tp = Ursprungszeit

Dst = tp * vp
print(f"{(Dst/10**3).round(2)} km Distanz Epizentrum - Station")


#Seismic Wavelenght And Resolution 3

f = 40

c1 = 4000
c2 = 6500

l1 = c1 / f 
l2 = c2 / f
print(f"{l1}, {l2}")


v = 0.32
a = np.sqrt(((2 * v) - 2 )/ ((2 * v) - 1))

print(a)


#Hooke's Law 3
E = 21.96 * 10 **3
p = 2500
h = 11.15
g = 9.81


Top = h-h
Middle = h/2
Bottom = h/1
#o = E * e 

Ss = p * g * h

Sr_Top = (p * g * 0) / 10**6
Sr_Middle = (p * g * h * 0.5) / 10**6
Sr_Bottom = (p * g * h) / 10**6
print(f"{round(Sr_Top, 4)}, {round(Sr_Middle, 4)}, {round(Sr_Bottom, 4)}")


Ss = 0.2735
#Ss = E * dl/l
dl = Ss / E * h
print(round(dl* 10**3, 4))