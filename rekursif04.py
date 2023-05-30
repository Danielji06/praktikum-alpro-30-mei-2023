def jumlah_digit(n):
    # konversi dulu ke string supaya bisa di looping
    nstr = str(n)
    total = 0
    for i in nstr:
        #konversi lagi ke int supaya bisa di jumlah kan
        total = total + int(i)
    return total

def jumlah_digit_rekursif(n):
    if n < 10:
        return n
    else:
        return n % 10 + jumlah_digit_rekursif(n//10)

hasil = jumlah_digit(8912)
print(hasil)

hasil = jumlah_digit_rekursif(8912)
print(hasil)