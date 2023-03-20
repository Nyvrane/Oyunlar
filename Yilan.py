# Kütüphaneler
import pygame
import time as sure
import random as rastgele

yilanhizi = 15

# Pencere Boyutu
pencerex = 720
pencerey = 480

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


# Oyun Bitti Fonksiyonu
def oyunbitti():
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

    # 2 Saniye Sonra Oyun Kendini Kapatacak
    sure.sleep(2)

    # Pygame Kütüphanesini Kapatma
    pygame.quit()

    # Programdan Çıkış
    quit()


# Ana Fonksiyon
while True:

    # Yön Tuşu Aktiviteleri
    for eylem in pygame.event.get():
        if eylem.type == pygame.KEYDOWN:
            if eylem.key == pygame.K_UP:
                degistir = 'YUKARI'
            if eylem.key == pygame.K_DOWN:
                degistir = 'ASAGI'
            if eylem.key == pygame.K_LEFT:
                degistir = 'SOL'
            if eylem.key == pygame.K_RIGHT:
                degistir = 'SAG'

    # İki Tuşa Aynı Anda Basılırsa Yılanın İkiye Ayrılmaması İçin Eşzamanlı Yön Ayarlama
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
    if yilanpozisyonu[0] == meyvepozisyonu[0] and yilanpozisyonu[1] == meyvepozisyonu[1]:
        skor += 10
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

    # Oyun Bitiminde Skor Gösterimi
    skorgoster(beyaz, 'arial', 20)

    # Oyun Ekranını Yenileme
    pygame.display.update()

    # Yenileme Oranı/FPS
    fps.tick(yilanhizi)
