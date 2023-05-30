def palindrome(kalimat):
    kalimat_balik = kalimat[::-1]
    if kalimat == kalimat_balik:
        return True
    else:
        return False
    
def palindrome_rekusif(kalimat, depan, belakang):
    # base case jika tinggal 1 karakter
    if depan == belakang:
        return True
    # base case jika tinggal 2 karakter
    elif depan == belakang -1: 
        if kalimat[depan] == kalimat[belakang]:
            return True
        else:
            return False
    # recursive case
    else:
        if kalimat[depan] == kalimat[belakang]:
            return palindrome_rekusif(kalimat, depan + 1, belakang + 1)
        else:
            return False


print(palindrome("kasur rusak"))
print(palindrome("duta wacana"))

kalimat = 'kasur rusak'
print(palindrome_rekusif(kalimat, 0, len(kalimat)- 1))