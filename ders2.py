
import random 
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("uzunluk girin"))
sifre =""
for i in range(uzunluk):
    sifre += random.choice(karakterler)

print(sifre)    
