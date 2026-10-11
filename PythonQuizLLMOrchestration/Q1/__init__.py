# 1) Aşağıdaki sözlükte, değerler içinde c harfinin geçip geçmediğini gösteren bir if koşulu yazınız

my_dictionary = {"k1":10,"k2k":"a","k32":30,"k4":"c"}


list1 = list(my_dictionary.values())
print(list1)

if "c" in list1:
    print("c is here")
else:
    print("c is not here")

