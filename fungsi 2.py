#variable global
nama = "python"
versi = "1.0.0"

def help():
    #variable lokal
    nama = "c++"
    versi = "1.2.1"
    #akses variable lokal
    print("Nama : %s" % nama)
    print("Versi : %s" % versi)

#akses variable global
print("Nama : %s" % nama)
print("Versi : %s" % versi)

#memanggil fungsi help
help()