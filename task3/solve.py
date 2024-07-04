lst = [int(input(f"Введите {i+1} число: ")) for i in range(9)]
s = 0
p = 1
for el in lst: 
    s += el ** 2
    p *= el 

x = (s + p) / 9
print(round(x, 1))