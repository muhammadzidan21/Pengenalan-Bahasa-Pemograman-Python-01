print("----------RUMUS ENERGI POTENSIAL----------")
##Rumus Energi Potensial##
#Input massa benda dalam Kg
m = float(input("masukan massa benda :"))
#Input nilai percepatan gravitasi m/s^2
g = 9.8
#Input ketinggian benda dalam M
h = float(input("masukan ketinggian benda :"))

#rumus Ep=mxgxh
Ep = m*g*h
print(f" Maka Ep = {Ep}","joule")
 


print("########## RUMUS GERAK VERTIKAL KEBAWAH (Menentukan Vt) ##########")
# Input nilai kecepatan mula-mula (m/s)
Vo = float(input("masukan nilai kecepatan awal :"))
# Input nilai waktu (s)
t = float(input("masukan t:"))
# Input nilai gravitasi (m/s^2)
g = 9.8
# Menentukan ketinggian pada saat t
Vt = Vo+(g*t)
print(f"maka kecepatan dalam {t}s, Vt = {Vt}m/s")



print("---------- RUMUS TEKANAN ----------")
#Input massa dalam (Kg)
m=float(input("masukan massa benda:"))
#Input percepatan(m/s^2)
a=float(input("masukan percepatan:"))
#Input rumus gaya (F= m x a)
F= m*a
#input panjang dan luas (m)
p=float(input("masukan panjang :"))
l=float(input("masukan lebar:"))
#Input rumus tekanan (Paskal)
P= F/(p*l)
print(f"maka tekanan = {P} Paskal")
