print("tas,kagit,makas oyunumuza hosgeldiniz.  2 tur kazanan taraf oyunun galibidir.Basarilar. ")






import random
def tas_kagit_makas_huseyindogru():
    secenekler=["tas","kagit","makas"]
    bilgisayar_skor=0
    oyuncu_skor=0
    while bilgisayar_skor<2 and oyuncu_skor<2:
        oyuncu_secim=input("tas mi kagit mi makas mi?")
        bilgisayar_secim=random.choice(secenekler)
        print("bilgisayar: " ,bilgisayar_secim)
        print("oyuncu: ",oyuncu_secim)
        
        if bilgisayar_secim==oyuncu_secim:
            print("durum berabere")
        elif(oyuncu_secim=="tas" and bilgisayar_secim=="makas") or (oyuncu_secim=="kagit" and bilgisayar_secim=="tas") or\
            (oyuncu_secim=="makas" and bilgisayar_secim=="kagit"):
                print("oyuncu puani aldi.")
                oyuncu_skor +=1
        else:
            print("bilgisayar puan aldi")
            bilgisayar_skor +=1
            
        print("oyuncu: ",oyuncu_skor,"-","bilgisayar: ",bilgisayar_skor)
        
    if oyuncu_skor==2:
        print("tebrikler oyunu siz kazandiniz")
    else:
        print("üzgünüm bilgisayar kazandi")
        
        
    tekrar=input("oyunu tekrar oynamak ister misiniz? ")
    bilgisayar_tekrar_liste=["evet","hayir"]
    bilgisayar_karar=random.choice(bilgisayar_tekrar_liste)
    print(bilgisayar_karar)
    

    
    if tekrar == "evet" and bilgisayar_karar == "evet":
        tas_kagit_makas_huseyindogru()
    else:
        print("tekrardan görüşmek üzere :)")
        
tas_kagit_makas_huseyindogru()        
        
        
        
        
        
        