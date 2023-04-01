# Kütüphaneler
import pygame
import random as rastgele

# Hız tanımlamaları
yilanhizi = 20
hizlandirmahizi = 35

# Pencere Boyutu
pencerex = 1440
pencerey = 900

# Renk Tanımları
siyah = pygame.Color(0, 0, 0)
beyaz = pygame.Color(255, 255, 255)
kirmizi = pygame.Color(255, 0, 0)
yesil = pygame.Color(0, 255, 0)
mavi = pygame.Color(0, 0, 255)

# Pygame Tanımlama
pygame.init()

# Oyun Penceresi Tanımlama
pygame.display.set_caption('Yılan Oyunu - fromNyvrane')
oyunpenceresi = pygame.display.set_mode((pencerex, pencerey))

# FPS Tanımlama
fps = pygame.time.Clock()

# Varsayılan Yılan Pozisyonu
yilanpozisyonu = [100, 50]

# Yılan Body Tanımlama
yilanvucudu = [[100, 50],
               [90, 50],
               [80, 50],
               [70, 50]
               ]
# Meyve Pozisyonu
meyvepozisyonu = [rastgele.randrange(1, (pencerex // 10)) * 10,
                  rastgele.randrange(1, (pencerey // 10)) * 10]

meyveuretme = True

# Varsayılan Yönü Sağa Ayarlama
yon = 'SAG'
degistir = yon

# Başlangıç Skoru
skor = 0


# Skor Gösterme
def skorgoster(renk, yazi, boyut):
    # Skor İçin Font Oluşturma
    skoryazisi = pygame.font.SysFont(yazi, boyut)

    # Görüntü Yüzeyi Nesnesi Oluşturma - Skor Arayüzü
    skorarayuzu = skoryazisi.render('Skor : ' + str(skor), True, renk)

    # Metin İçin Dikdörtgen Nesne Arayüzü
    skornesnearayuzu = skorarayuzu.get_rect()

    # Görüntü Metni
    oyunpenceresi.blit(skorarayuzu, skornesnearayuzu)


# Oyunu Yeniden Başlatma Fonksiyonu
def yenidenbasla():
    global yilanpozisyonu, yilanvucudu, meyvepozisyonu, meyveuretme, yon, degistir, skor, yilanhizi
    yilanpozisyonu = [100, 50]
    yilanvucudu = [[100, 50],
                   [90, 50],
                   [80, 50],
                   [70, 50]
                   ]
    meyvepozisyonu = [rastgele.randrange(1, (pencerex // 10)) * 10,
                      rastgele.randrange(1, (pencerey // 10)) * 10]
    meyveuretme = True
    yon = 'SAG'
    degistir = yon
    skor = 0
    yilanhizi = 15


# Oyun Bitiminde Çıkış Yapılması halinde Oyunun Kapanması
def oyuncikis():
    pygame.quit()
    quit()


# Oyun Bitti Fonksiyonu
def oyunbitti():
    global yilanhizi
    # Yazı Objesi Oluşturma
    oyunbittifont = pygame.font.SysFont('arial', 50)

    # Üzerinde Metin Bulunan Bir Yüzey Oluşturma
    oyunbittiarayuzu = oyunbittifont.render("Oyun Bitti! Skorunuz : " + str(skor), True, kirmizi)

    # Metin İçin Dikdörtgen Nesne Arayüzü
    oyunbittinesnearayuzu = oyunbittiarayuzu.get_rect()

    # Metnin Pozisyonunu Ayarlama
    oyunbittinesnearayuzu.midtop = (pencerex / 2, pencerey / 4)

    # Metni Ekranda Çizdirme
    oyunpenceresi.blit(oyunbittiarayuzu, oyunbittinesnearayuzu)
    pygame.display.flip()

    # 4 Saniye Sonra Oyun Kendini Kapatacak
    yilanhizi = 0.00001
    pygame.time.delay(4000)

    # Oyun Yeniden Başlatılmadıysa Pygame Kütüphanesini Kapatma
    for eylem2 in pygame.event.get():
        if eylem2.type == pygame.KEYDOWN:
            if eylem2.key == pygame.K_1:
                yenidenbasla()

    for eylem3 in pygame.event.get():
        if eylem3.type != pygame.KEYDOWN:
            if eylem3.key != pygame.K_1:
                oyuncikis()


puandegisti = False

# Ana Fonksiyon
while True:
    # Yön Tuşu Aktiviteleri
    for eylem in pygame.event.get():
        if eylem.type == pygame.KEYDOWN:
            if eylem.key == pygame.K_ESCAPE:
                oyunbitti()
            if eylem.key == pygame.K_1:
                yenidenbasla()
            if eylem.key == pygame.K_UP:
                degistir = 'YUKARI'
            if eylem.key == pygame.K_DOWN:
                degistir = 'ASAGI'
            if eylem.key == pygame.K_LEFT:
                degistir = 'SOL'
            if eylem.key == pygame.K_RIGHT:
                degistir = 'SAG'
            if eylem.key == pygame.K_LSHIFT:
                yilanhizi += hizlandirmahizi

        if eylem.type == pygame.KEYUP:
            if eylem.key == pygame.K_LSHIFT:
                yilanhizi -= hizlandirmahizi

    # Yılan Zıt Yöne Gitmediği Sürece Yön Değiştirmesini Sağlama
    if degistir == 'YUKARI' and yon != 'ASAGI':
        yon = 'YUKARI'
    if degistir == 'ASAGI' and yon != 'YUKARI':
        yon = 'ASAGI'
    if degistir == 'SOL' and yon != 'SAG':
        yon = 'SOL'
    if degistir == 'SAG' and yon != 'SOL':
        yon = 'SAG'

    # Yılanı Hareket Ettirme
    if yon == 'YUKARI':
        yilanpozisyonu[1] -= 10
    if yon == 'ASAGI':
        yilanpozisyonu[1] += 10
    if yon == 'SOL':
        yilanpozisyonu[0] -= 10
    if yon == 'SAG':
        yilanpozisyonu[0] += 10

    # Yılanın Vücudunun Büyüme Fonksiyonu - Yılan Meyveyi Yediğinde 10 Puan Artışı

    yilanvucudu.insert(0, list(yilanpozisyonu))
    if yilanpozisyonu[0] == meyvepozisyonu[0] and (yilanpozisyonu[1] == meyvepozisyonu[1]):
        skor += 10
        puandegisti = True
        meyveuretme = False
    else:
        yilanvucudu.pop()

    if not meyveuretme:
        meyvepozisyonu = [rastgele.randrange(1, (pencerex // 10)) * 10,
                          rastgele.randrange(1, (pencerey // 10)) * 10]

    meyveuretme = True
    oyunpenceresi.fill(siyah)

    for yer in yilanvucudu:
        pygame.draw.rect(oyunpenceresi, yesil,
                         pygame.Rect(yer[0], yer[1], 10, 10))
    pygame.draw.rect(oyunpenceresi, beyaz, pygame.Rect(
        meyvepozisyonu[0], meyvepozisyonu[1], 10, 10))

    # Oyun Bitiş Şartları
    if yilanpozisyonu[0] < 0 or yilanpozisyonu[0] > pencerex - 10:
        oyunbitti()
    if yilanpozisyonu[1] < 0 or yilanpozisyonu[1] > pencerey - 10:
        oyunbitti()

    # Yılan Vücuduna Temas Durumu
    for vucut in yilanvucudu[1:]:
        if yilanpozisyonu[0] == vucut[0] and yilanpozisyonu[1] == vucut[1]:
            oyunbitti()

    if puandegisti:
        if skor % 10 == 0:
            yilanhizi += 0.4
    puandegisti = False

    # Oyun Bitiminde Skor Gösterimi
    skorgoster(beyaz, 'arial', 20)

    # Oyun Ekranını Yenileme
    pygame.display.update()

    # Yenileme Oranı/FPS
    fps.tick(yilanhizi)
