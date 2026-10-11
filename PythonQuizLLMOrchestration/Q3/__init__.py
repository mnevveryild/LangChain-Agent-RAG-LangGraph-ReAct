# 3) Tüm dairelerin çevresini içeren başka yeni bir liste oluşturunuz. (İpucu: 2 * pi * r)  Pi 3.14 alınabilir.

r_list = [3,2,5,8,4,6,9,12]
pi = 3.14
perimeter_list=[]

for num in r_list:
    perimeter = pi*2*num
    perimeter_list.append(perimeter)
    num+=1

print(perimeter_list)