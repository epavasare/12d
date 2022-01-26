#import math
#a=int(input("Ievadi kvadrāta malas garumu lielāku par 5cm :"))
#laukums=math.pow(a,2)
#b=a+5
#laukums2=math.pow(b,2)
#c=(laukums2-laukums)/laukums*100
#print(round(c),"%")
import math
a=int(input("Ievadi riņķa rādiusu:"))
b=int(input("Ievadi vienādsāna taisnleņķa trijstūra hipotenūzas garumu : "))
rinkaS=math.pi*math.pow(a,2)
trijsturaS=b*(b/2)/2
lielaks=rinkaS-trijsturaS
print("Riņķa laukums ir par",round(lielaks, 1),"cm^3 lielāks nekā trijstūra laukums.")
