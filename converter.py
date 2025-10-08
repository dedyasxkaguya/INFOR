isContinue = True

while(isContinue):

    try : 
        idr = int(input("Masukkan jumlah uang : \n"))
        print(f'Kamu ingin konversi {idr} ke usd')
        print("Sedang konversi ke USD")
        hasil = idr / 16602
        print(f'{idr} jika dikonversi ke usd adalah {hasil}')
        
        q = input("Apakah ingin lanjut? Y/N : ")
        
        if(q=='N' or q == 'n'):
            isContinue = False        
            
    except :
        print("Masukkan jumlah Uang dengan benar")
    