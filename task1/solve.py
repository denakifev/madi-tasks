from math import pow, log
def func(x : float) -> float: 
    return pow(pow(x, 4 /3) + pow(x, (4-x) / 5), 0.5) + log(abs(x - 20.5))

a, b = map(float, input().split())
while (a == b): 
    a, b = map(float, input("Invalid interval!\n").split())
if a > b: 
    a, b = b, a
n = int(input())
while (n < 3): 
    n = int(input("Invalid parameter!\n"))
d = (b - a) / (n - 1)
with open("output.txt", "w") as f:
    while a < b:
        try: 
            res = func(a)
            f.write("{:.5f}         {:.5f}\n".format(a, res))
        except Exception:
            f.write("{:.5f}         out of D(f)\n".format(a))
        finally:
            a += d






