l1 = float(input())
l2 = float(input())
l3 = float(input())
a = l1*l2 - l3 / 2.5 if l1 > l2 else 2.0
b = 15 - (abs(l1))**0.5 if l1 == l3 else l1 + 2*l2
print(f"a = {a}\nb = {b}")