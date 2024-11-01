
#Program 1 (Praktikum 3)

print("Laba Invetasi")

x = int(input("UAng Modal Awal:"))

a = 0*x
b = 0*x
c = 0.01*x
d = 0.01*x
e = 0.05*x
f = 0.05*x
g = 0.05*x
h = 0.02*x

y=[a,b,c,d,e,f,g,h]

for i in range(len(y)):
    print("Keuntungan Bulan ke", i+1,"sebesar:",y[i])


z=(a+b+c+d+e+f+g+h)
print("Total Keuntungan Selama 8 Bulan: ",z)
