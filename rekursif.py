import sys
import timeit
sys.setrecursionlimit(10000)
# hello word dengan perulangan
def helloword_perulangan(n):
    for i in range(n):
        print(f" {i+1} Hello word!")

# hello word dengan rekursif
def helloword_rekursif(n):
    if n == 0:
        print(f"{n} Hello word!")
    else:
        print("Hello word!")
        helloword_rekursif(n-1)

# test case
start = timeit.default_timer()
helloword_perulangan(2000)
end = timeit.default_timer()
print(f"Waktu yang diperlukan: {(end-start)/1000}ms.")
start2 = timeit.default_timer()
helloword_rekursif(2000)
end2 = timeit.default_timer()
print(f"Waktu yang diperlukan: {(end2-start2)/1000}ms.")