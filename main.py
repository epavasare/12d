import math
a=int(input("Ievadi kvadrāta malas garumu lielāku par 5cm :"))
laukums=math.pow(a,2)
b=a+5
laukums2=math.pow(b,2)
c=(laukums2-laukums)/laukums*100
print(round(c),"%")