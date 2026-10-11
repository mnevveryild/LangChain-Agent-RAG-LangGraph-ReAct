# 2) Aşağıdaki listedeki sayılardan sadece çift sayı olanları başka bir listeye kaydeden bir kod yazınız.

my_numbers = [1,2,3,4,5,6,19,20,32,21,20,1111,23,24]
even_numbers = []
for num in my_numbers:
    if num%2==0:
        even_numbers.append(num)
        num+=1
    else:
        num +=1

print(even_numbers)
