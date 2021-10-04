import numpy as np

# Flexure of the elastic Lithosphere

# a = ((4*D)/((p,-pw)*g)**1/4)


# E = 70*10**9
# ha = 
# hb = 
# v = 0.25

# D = (E*ha**3)/(12(1-v**2))

# D = (E*hb**3)/(12(1-v**2))

x0 = -5200
xb = -3400

a0 = x0/(np.pi/2)
ab = xb/(0.75*np.pi)

# print(round(abs(a0),3), round(abs(ab),3))

pm = 3300
pw = 997
g = 9.81

D0 = (a0**4*((pm-pw)*g))/4
Db = (ab**4*((pm-pw)*g))/4

# print(D0, Db)


#Rheology 2
#a
n = 10**23
G = 6*10**10

tm = n/G
tmyrs = tm / (60*60*24*365)

# print(tm, tmyrs)

#b
e = 5.6 / (60*60*24*365)
# print(e)

n = 10**23

scm = (n * e) / (100*10**5)
scm10 = scm / 10
print(scm)

# print(scm > 500_000_000) #; If True: Fail In Plastic Manner
# print(scm10 < 500_000_000) #; If True: Not Fail

#c
e = 5.6
s = 100*10**6

n = (s/e) * (1/G)
t = n * (100*10**5)
# print(n, t)

#d
l = t * e 
lcm = l / 100
# print(l, lcm)

#Bubbles In Pumice 3
#a
pl = 1.225
pp = 1421
p = abs(pl - pp)
g = 9.81
n = 4*10**5
R = (0.84/100)/2

V = (1/3) * (p*g*(R**2))/(n)
Vyrs = V * 60*60*24*360
print(p,V,Vyrs)

#b
t = 1000 / Vyrs
print(t)