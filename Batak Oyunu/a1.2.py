
# -- Trakya Ünviersitesi, Bilgisayar Mühendisliği Bölümü, Programlama Dillerine Giriş Dersi --
# Bir iskmabil destesinin 4 oyuncuya rastgele dağıtılması ve Batak (Spades) oyunu için temel
# kuralların tanımlı olduğu bir program kodu verilmiştir. Oyunu oynamamış olan öğrenciler
# çeşitli internet sitelerinden veya videolardan kuralları öğrenebilirler.

# Program kodunun aşağıdaki yönlerden eksiklerinin öğrenciler tarafından giderilmesi beklenmektedir:
# + Bu kodda sadece 1 tur oynanmaktadır. Önceden belirlenen sayıda tur adedi ile oynanması sağlanmalıdır.
# + Her oyuncunun tur başında kaç el alacağını tahmin etmesi eklenmelidir. Bu 3 farklı şekilde yapılabilir:
#   1) Her oyuncu için rastgele belirlenebilir (mantıklı değil)
#   2) Oyuncunun kartlarına göre bilgisayar karar vermeye çalışabilir (yapması zor)
#   3) Kullanıcı her oyuncu için bu değeri girebilir (yapması kolay)
# + Puanlama sistemi eklenmeli ve her tur sonunda güncel puan tablosu gösterilmelidir:
#   - Oyuncu tahmin ettiği eli alırsa "tahmin x 10" puan kazanır (3 tahmin edip tam 3 el almışsa 30 puan)
#   - Fazladan aldığı her el için 1 puan eklenir (3 tahmin edip 5 aldıysa: 32)
#   - Tahmininden az el alırsa "tahmin x 10" puan kaybeder (3 tahmin edip 2 aldıysa: -30)

# Program kodunda aşağıdaki yönlerden geliştirmeler de yapılabilir (şart değil ama ek puan kazandırır):
# + Oyuncular bu kodda genel olarak elindeki o tipten en büyük kartı atmaktadır (sadece Maça kartını bir koz
#   olarak kullanacağı zaman en küçüğünü atmaktadır). Çoğu durumda bu mantıklı bir seçim değildir (Kod içinde
#   bununla ilgili bir NOT yazılmıştır). Oyuncuların daha mantıklı kart atmaları için kontroller eklenebilir.
# + Kodun içinde fonksiyonlar veya sınıflar kullanılmamıştır. Öğrenciler sonraki derslerde görecekleri bu
#   tür yapıları da kullanarak kodu daha güzel hale getirebilir.

import random

A = ['♠', '♣', '♥', '♦']
B = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
n=1
tüm_oyun_skorları= []

tursayısı=int(input("Lütfen Oynanacak Tur Sayısını Giriniz:"))
for i in range(tursayısı):

    n+=1
    deste = []
    for i in A:
        for j in B:
            deste.append(i+j)

    oyuncular = {}
    oyuncu_sira = ['oyuncu1', 'oyuncu2', 'oyuncu3', 'oyuncu4']  # oyuncu isimleri girilecek ise boş liste olmalı
    # print("OYUNCULARIN İSİMLERİNİ GİRİN:") # oyuncu isimleri girilecek ise bu satır açılmalı
    for i in range(4):
        # oyuncular.setdefault(input("Oyuncu " + str(i+1) + ": "), {}.fromkeys(A))
        oyuncular.setdefault(oyuncu_sira[i], {}.fromkeys(A)) # isimler girilecek ise bu kapatılmalı, üstteki açılmalı

    for oyuncu in oyuncular:
        # oyuncu_sira.append(oyuncu)  # oyuncu isimleri girilecek ise bu satır açılmalı
        for i in A:
            oyuncular[oyuncu][i] = []
        for i in range(13):
            kart = random.choice(deste)
            oyuncular[oyuncu][kart[0]].append(kart[1:])
            deste.remove(kart)

    print("\nDAĞITILAN KARTLAR:")
    for oyuncu in oyuncular:
        print(oyuncu + ":")
        for karttip in oyuncular[oyuncu]:
            oyuncular[oyuncu][karttip].sort(key=B.index)  # kartlar B listesindeki sıraya göre dizilir
            print(karttip, oyuncular[oyuncu][karttip])


    #İHALE SON HALİ BİTTİ ÇALIŞIYOR
    tahminler={}
    print("0 = Pas demektir")
    for i in range(4):
        oyuncu_tahmin=int(input(f"{oyuncu_sira[i]} Lütfen Tahmin Giriniz:"))
        if bool(tahminler):
            while oyuncu_tahmin in list(tahminler.values()) or oyuncu_tahmin<max(tahminler.values()) and oyuncu_tahmin!=0:
                print("Tahmininizde hata var")
                oyuncu_tahmin=int(input(f"{oyuncu_sira[i]} Lütfen Tahmin Giriniz:"))
        else:
            while oyuncu_tahmin in list(tahminler.values()) or oyuncu_tahmin<5 and oyuncu_tahmin!=0:
                print("Tahmininizde hata var")
                oyuncu_tahmin=int(input(f"{oyuncu_sira[i]} Lütfen Tahmin Giriniz:"))
        tahminler.update({oyuncu_sira[i]:oyuncu_tahmin})
    

    for anahtar,value00 in tahminler.items():
        if value00 == list(tahminler.values()).sort()[-1]:
            print(anahtar)

    print(tahminler)


    print("\nOYUN BAŞLADI...")  # Oyun sadece 1 tur (13 el) oynanacak
    oyun_skor = dict()
    macaAtildi = False
    sira = random.randrange(4)  # oyuna başlayacak oyuncu rastgele belirleniyor
    for el in range(13):  # 13 el oynanacak
        print(str(el+1) + ". el:")
        oynayan = 0
        oynanan_kartlar = []  # bu liste içine kimin hangi kartı attığı yazılacak
        while oynayan < 4:
            oyuncu = oyuncu_sira[sira]
            if oynayan == 0:  # ilk kart atacak oyuncu ise kart tipi belirlenecek (rastgele)
                while True:
                    if macaAtildi:  # Maça önceki bir elde koz olarak kullanıldı ise oyuncu Maça ile başlayabilir
                        kart_tipi = random.choice(A)
                    else:  # Maça önceki bir elde koz olarak kullanılmadı ise diğer üç kart tipinden atabilir
                        kart_tipi = random.choice(A[1:])
                    if len(oyuncular[oyuncu_sira[sira]][kart_tipi]):  # o tipte kartı yoksa döngü devam edecek
                        break
                oyuncu_kart = (oyuncu, kart_tipi, oyuncular[oyuncu][kart_tipi].pop())  # o tipteki en büyük kartı atıyor
                # NOT: Oyuncunun o tipteki en büyük kartı atması çoğu durumda mantıklı değil. Rastgele olarak seçilmesi veya
                # en küçüğü atmak da mantıklı olmaz. Oyuncunun mantıklı bir kart atmasını sağlamak için birçok ilave kontrol
                # eklenmesi gerekir (Daha önce 'A' çıktı ise 'K' ile başlamak mantıklı olabilir vb.). Bu programda o elin
                # ilk kartı atılırken de, sonraki kartlar için de mantıklı olmasına yönelik kontroller bulunmamaktadır.
            else:  # diğer oyuncular ilk oyuncunun belirlediği kart tipinde kart atacak
                if len(oyuncular[oyuncu][kart_tipi]):  # o kart tipinde kartı varsa en büyük olanı atacak
                    oyuncu_kart = (oyuncu, kart_tipi, oyuncular[oyuncu][kart_tipi].pop())
                elif len(oyuncular[oyuncu]['♠']):  # o kart tipinde kartı yoksa en küçük maça kartını atacak
                    oyuncu_kart = (oyuncu, '♠', oyuncular[oyuncu]['♠'].pop(0))
                    macaAtildi = True  # Maça koz olarak oynandığı için sonraki ellerde doğrudan Maça atılabilecek
                else:  # maça kartı da yoksa, diğer tiplerin birinden en küçük kartı atacak
                    kart_tipleri = A[1:].copy()  # maça hariç diğer 3 kart tipi kopyalandı
                    for tip in kart_tipleri:
                        if len(oyuncular[oyuncu][tip]):
                            oyuncu_kart = (oyuncu, tip, oyuncular[oyuncu][tip].pop(0))
                            break
            print(oyuncu_kart[0], oyuncu_kart[1] + oyuncu_kart[2])
            oynanan_kartlar.append(oyuncu_kart)
            oynayan += 1
            sira += 1
            if sira >= 4:
                sira -= 4
        # atılan 4 karta göre eli kazananı bulma:
        en_buyuk = oynanan_kartlar[0]   # ilk atılanı en büyük kart kabul et
        for kart in oynanan_kartlar[1:]:
            if kart[1] == en_buyuk[1] and B.index(kart[2]) > B.index(en_buyuk[2]):
                en_buyuk = kart  # en büyük ile aynı kart tipinde daha büyük atıldı ise en büyük kart kabul et
            elif en_buyuk[1] != '♠' and kart[1] == '♠':
                en_buyuk = kart  # en büyük maça değilken maça atıldı ise en büyük kart kabul et
        print("eli kazanan:", en_buyuk[0])
        sira = oyuncu_sira.index(en_buyuk[0])
        oyun_skor[en_buyuk[0]] = oyun_skor.setdefault(en_buyuk[0], 0) + 1
        

    
    print("SKOR:", oyun_skor)  # oyuncuların kaçar el adığını gösterir (gerçek kurallara göre bir puanlama sistemi yok)

    
    
    
    sıralı_skor = dict(sorted(oyun_skor.items()))
    skor_toplam = {'oyuncu1': 0, 'oyuncu2': 0, 'oyuncu3': 0, 'oyuncu4': 0}
    oyuncular_Keys = list(oyuncular.keys())
    for i in range(4):
        if oyun_skor[oyuncular_Keys[i-1]] == tahminler[oyuncular_Keys[i-1]]:
            skor_toplam.update({oyuncular_Keys[i-1]:tahminler[oyuncular_Keys[i-1]]*10})
        elif oyun_skor[oyuncular_Keys[i-1]] < tahminler[oyuncular_Keys[i-1]]:
            skor_toplam.update({oyuncular_Keys[i-1]:((tahminler[oyuncular_Keys[i-1]]*10)+(oyun_skor[oyuncular_Keys[i-1]] - tahminler[oyuncular_Keys[i-1]]))})
        else:
            skor_toplam.update({oyuncular_Keys[i-1]:-10*tahminler[oyuncular_Keys[i-1]]})
    
    # if "oyuncu1" in sıralı_skor:
    #     if sıralı_skor.get("oyuncu1")==tahminler.get("oyuncu1"):
    #         skor_toplam.update({skor_toplam["oyuncu1"]:tahminler.get("oyuncu1")*10})
        
    #     else:
    #         skor_toplam.update({skor_toplam["oyuncu1"]:-10*tahminler.get("oyuncu1")})
        
    
        # tüm_oyun_skorları.append(sıralı_skor)
    print("Skor tablosu")
    print(skor_toplam)     
        #  list(tahminler.values()).sorted
        # (oyuncu_tahmin[oyuncu1]*

















    # sorted_by_keys = dict(sorted(oyun_skor.items()))
    # tüm_oyun_skorları.append(oyun_skor)
    # #Skor toplama
    # skor_toplam = {'oyuncu1': 0, 'oyuncu2': 0, 'oyuncu3': 0, 'oyuncu4': 0}
    # for i in range(2):
    #     if tahminler[oyuncular[i]] == sorted_by_keys[i]:
    #         değer=tahminler[oyuncu[i]]*10
    #         skor_toplam.update({oyuncu[i]:değer})
    #     else:  
    #         print("hello world")




# for i in range(tursayısı):
#     print(f"{i+1}. eleman: {tüm_oyun_skorları[i]}")


   