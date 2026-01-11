# BML101_24360859058_SumeyyeSimsek
BLM101 Bilgisayar Mühendisliğine Giriş - Dönem Projesi (4. Grup: Brookshear Makine Dili)

# BLM101 Dönem Projesi: Brookshear Makine Dili Yorumlayıcısı (4. Grup)

**Ad Soyad:** Sümeyye Şimşek
**Öğrenci No:** 24360859058
**Bölüm:** Bilgisayar Mühendisliği

##  Proje Sunum Videosu
Projemi anlattığım ve kodun çalışmasını gösterdiğim videoya aşağıdaki linkten ulaşabilirsiniz:
**[https://youtu.be/gl2fpbSs8C8]**



## Proje Hakkında
Bu proje, **Brookshear Mimarisi** için tasarlanmış basit bir makine dili yorumlayıcısıdır (Decoder). Proje, kullanıcıdan alınan onaltılık (Hexadecimal) makine kodlarını analiz eder ve bu kodların ne anlama geldiğini Türkçe olarak açıklar.

Proje kapsamında **Fetch (Getir) -> Decode (Çöz) -> Execute (Yürüt)** döngüsünün mantığı simüle edilmiştir.

## Özellikler
* **Hex Kontrolü:** Girilen kodun geçerli bir 4 haneli Hex formatında olup olmadığını denetler.
* **Op-code Analizi:** Kodun ilk hanesine bakarak yapılacak işlemi (LOAD, STORE, ADD vb.) belirler.
* **Operand Çözümleme:** Kodun geri kalan hanelerini (Register numarası veya Bellek adresi) parametre olarak işler.
* **Türkçe Çıktı:** Makine dilindeki karmaşık komutları anlaşılır Türkçe cümlelere çevirir.

## Nasıl Çalışır?
Program çalıştırıldığında kullanıcıdan bir komut beklenir.

**Örnek Senaryo:**
1.  Kullanıcı `14A3` kodunu girer.
2.  Program kodu parçalar:
    * **Op-code:** `1` (LOAD komutu)
    * **Register:** `4`
    * **Adres:** `A3`
3.  Program şu çıktıyı üretir:
    > *"A3 adresindeki bellek hücresinin içeriğini, 4 numaralı kaydediciye (Register) YÜKLE."*

## Dosya Yapısı
* `kodlar/main.py`: Projenin kaynak kodları.
* `sunum.pdf`: Proje konusunun teorik anlatımı ve sunum dosyası.
