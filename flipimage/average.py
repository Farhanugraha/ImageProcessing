
n = int(input("banyaknya data : "))
print()

data = []
sum = 0

for i in range (0,n):
    temp = int(input("Masukkan banyaknya data ke-%d = \n" % (i+1)))
    data.append(temp)
    sum += data[i]
    average = sum/n
    
    print("\n Rata-rata = % 0.2f"%average)
     