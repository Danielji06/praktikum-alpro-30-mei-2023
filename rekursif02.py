import timeit
def fibo(n):
    f1,f2=1,1
   # print(f1,", ",f2,", ",end='')
    for i in range(2,n):
        fib = f1+f2
        f1 = f2
        f2 = fib
        #print(fib,", ",end='')
    return fib

def fibo_rekursif(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo_rekursif(n-1) + fibo_rekursif(n-2)
    
def fibo_rekursif_upgrade(n, list_fibo):
    if n == 1 or n == 2:
        return 1
    else:
        if list_fibo[n-1] !=0: # kalau sudah pernah dihitung
            return list_fibo[n-1]
        else:
            # kalau belum
            list_fibo[n-1] = fibo_rekursif_upgrade(n-1, list_fibo) + fibo_rekursif_upgrade(n-2, list_fibo)
        return fibo_rekursif_upgrade(n-1, list_fibo) + fibo_rekursif_upgrade(n-2, list_fibo)
    
start = timeit.default_timer()
hasil = fibo(41)
end = timeit.default_timer()
waktu_perulangan = end - start
print(f"Fibo perulangan dengan waktu {waktu_perulangan} detik.")


start = timeit.default_timer()
hasil = fibo_rekursif(41)
end = timeit.default_timer()
waktu_perulangan = end - start
print(f"Fibo rekursif dengan waktu {waktu_perulangan} detik.")

n = 41
list_fibo = [0] * n
start = timeit.default_timer()
hasil = fibo_rekursif_upgrade(n, list_fibo)
end = timeit.default_timer()
waktu_perulangan = end - start
print(f"Fibo rekursif upgrade dengan waktu {waktu_perulangan} detik.")
