import string

import string

print("--- Brookshear Makine Dili Yorumlayıcısı ---")
print("Çıkış yapmak için 'exit', 'cikis' veya 'çıkış' yazabilirsiniz.\n")

while True:
    # Kullanıcıdan veriyi alıyorum ve büyük harfe çeviriyorum.
    # .strip() ile baştaki/sondaki boşlukları siliyorum, .upper() ile de küçük harf girilse bile büyütüyorum.
    giris = input("Onaltılık (Hex) kodu giriniz (Örn: 14A3): ").strip().upper()

    # Çıkış kontrolü yapıyorum.
    # Kullanıcı 'exit', 'cikis' veya Türkçe karakterle 'çıkış' yazarsa döngüyü kırıp çıkıyorum.
    cikis_kelimeleri = ["EXIT", "CIKIS", "ÇIKIŞ", "ÇIKIS", "EXİT"]
    if giris in cikis_kelimeleri:
        print("Programdan çıkılıyor...")
        break

    # Hata Kontrollerini yapıyorum.
    
    # Uzunluk kontrolü: Kodun tam olarak 4 karakter olup olmadığına bakıyorum.
    if len(giris) != 4:
        print("HATA: Lütfen tam olarak 4 haneli bir kod giriniz!")
        continue
    
    # Karakter kontrolü: Sadece onaltılık (Hex) karakterler mi var diye kontrol ediyorum.
    gecerli_karakterler = string.hexdigits # "0123456789abcdefABCDEF" listesini getiriyorum.
    
    # Girilen her bir harfi tek tek geziyorum, eğer listede olmayan bir harf varsa hata veriyorum.
    if not all(char in gecerli_karakterler for char in giris):
        print("HATA: Sadece 0-9 arası rakamlar ve A-F arası harfler kullanabilirsiniz!")
        continue

    # Kodu anlamlı parçalara ayırıyorum.
    # Brookshear mimarisinde her hanenin yerinin bir anlamı var, bunları değişkenlere atıyorum.
    
    islem_kodu = giris[0]   # İlk hane: Ne yapacağımı söyleyen kod (Op-code).
    yazmac     = giris[1]   # İkinci hane: İşlemin yapılacağı hedef yazmaç (Register).
    
    # Bazı komutlar son iki haneyi bir adres veya sayı değeri olarak kullanır, onları birleştiriyorum.
    adres_veya_sayi = giris[2] + giris[3] 
    
    # Bazı komutlar (Toplama gibi) son iki haneyi iki ayrı kaynak yazmaç olarak kullanır.
    kaynak_yazmac_1 = giris[2]
    kaynak_yazmac_2 = giris[3]

    # İşlem koduna göre ne yapacağıma karar veriyorum (Match-Case Yapısı).
    match islem_kodu:
        case '1': # LOAD: Bellekten veriyi alıp yazmaca yüklüyorum.
            print(f"SONUÇ: {adres_veya_sayi} adresindeki veriyi alıyorum, {yazmac} numaralı Register'a kopyalıyorum.")
            
        case '2': # LOAD: Verilen sayıyı doğrudan yazmaca yüklüyorum.
            print(f"SONUÇ: {adres_veya_sayi} sayısını (değerini), doğrudan {yazmac} numaralı Register'a yüklüyorum.")
            
        case '3': # STORE: Yazmaçtaki veriyi belleğe kaydediyorum.
            print(f"SONUÇ: {yazmac} numaralı Register'daki veriyi alıp, {adres_veya_sayi} bellek adresine yazıyorum.")
            
        case '4': # MOVE: Bir yazmaçtaki veriyi diğerine kopyalıyorum.
            print(f"SONUÇ: {kaynak_yazmac_1} numaralı kaydedicideki veriyi alıp, {kaynak_yazmac_2} numaralı Register'a kopyalıyorum.")
            
        case '5': # ADD: İki tam sayıyı topluyorum.
            print(f"SONUÇ: {kaynak_yazmac_1} ve {kaynak_yazmac_2} numaralı kaydedicilerdeki tam sayıları topluyorum, sonucu {yazmac} numaralı Register'a yazıyorum.")
            
        case '6': # ADD: İki ondalıklı (floating point) sayıyı topluyorum.
            print(f"SONUÇ: {kaynak_yazmac_1} ve {kaynak_yazmac_2} numaralı kaydedicilerdeki ondalıklı sayıları topluyorum, sonucu {yazmac} numaralı Register'a yazıyorum.")
            
        case '7': # OR: Mantıksal VEYA işlemi yapıyorum.
            print(f"SONUÇ: {kaynak_yazmac_1} ve {kaynak_yazmac_2} numaralı kaydedicilere OR (VEYA) işlemi uyguluyorum, sonucu {yazmac} numaralı Register'a yazıyorum.")
            
        case '8': # AND: Mantıksal VE işlemi yapıyorum.
            print(f"SONUÇ: {kaynak_yazmac_1} ve {kaynak_yazmac_2} numaralı kaydedicilere AND (VE) işlemi uyguluyorum, sonucu {yazmac} numaralı Register'a yazıyorum.")
            
        case '9': # XOR: Mantıksal ÖZEL VEYA işlemi yapıyorum.
            print(f"SONUÇ: {kaynak_yazmac_1} ve {kaynak_yazmac_2} numaralı kaydedicilere XOR işlemi uyguluyorum, sonucu {yazmac} numaralı Register'a yazıyorum.")
            
        case 'A': # ROTATE: Bitleri sağa doğru döndürüyorum.
            print(f"SONUÇ: {yazmac} numaralı kaydedicideki veriyi alıp, {kaynak_yazmac_2} adım kadar sağa döndürüyorum (Rotate Right).")
            
        case 'B': # JUMP: Koşullu atlama yapıyorum.
            print(f"SONUÇ: Kontrol ediyorum; eğer {yazmac} numaralı kaydedici ile 0 numaralı kaydedici eşitse, program akışını {adres_veya_sayi} adresine atlatıyorum (Jump).")
            
        case 'C': # HALT: Programı durduruyorum.
            print("SONUÇ: Tüm işlemleri bitirip programı durduruyorum (HALT).")
            
        case _: # Tanımsız Kod: Geçersiz bir işlem kodu girildiyse uyarıyorum.
            print(f"HATA: Girdiğiniz '{islem_kodu}' kodu geçerli bir işlem değildir. Lütfen 1-C arası bir kod giriniz.")

    print("-" * 30) # Görsel olarak adımları ayırmak için çizgi çekiyorum.
