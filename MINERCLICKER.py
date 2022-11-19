TITLE = "MINERCLICKER"
WIDTH = 960
HEIGHT = 550
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

kilof = Actor("kilof")
kilof_pozycja = (WIDTH - 220) / 2
kilof.pos = kilof_pozycja, CENTER_Y
punkty = 60000
ulepszenie = 0
koszt_auto_kilofa = 10
liczba_auto_kilofow = 0
koszt_btt1 = 200
koszt_btt2 = 1500
koszt_btt3 = 4000
koszt_btt4 = 12000
koszt_btt5 = 25000
kup_autoclicker = Actor("autoclicker")
kup_autoclicker.pos = 35, 515
liniag = Actor("liniag")
liniag.pos = CENTER_X, CENTER_Y / 4
liniad = Actor("liniad")
liniad.pos = WIDTH - 220, CENTER_Y

dwojka = Actor("button1")
dwojka.pos = WIDTH - 215 / 2, 100

czworka = Actor("button2")
czworka.pos = WIDTH - 215 / 2, 200

osemka = Actor("button3")
osemka.pos = WIDTH - 215 / 2, 300

szesnastka = Actor("button4")
szesnastka.pos = WIDTH - 215 / 2, 400

trzydziestka = Actor("button5")
trzydziestka.pos = WIDTH - 215 / 2, 500

koniec = Actor("koniec")
koniec.pos = 70, CENTER_Y / 4 + 53

wygrana = Actor("wygrana")
wygrana.pos = CENTER_X, CENTER_Y

wyjdz = Actor("wyjdz")
wyjdz.pos = CENTER_X, CENTER_Y * 1.5

zmk = 0


def draw():
    global funkoniec, zmk
    screen.clear()
    screen.fill("white")
    kilof.draw()
    screen.draw.text(str("Punkty:  ") + str(punkty),[kilof_pozycja - 100, CENTER_Y - 150],color="black",fontsize=50)
    kup_autoclicker.draw()
    screen.draw.text(str(koszt_auto_kilofa), [80, 500], color="black", fontsize=60)
    liniag.draw()
    liniad.draw()
    dwojka.draw()
    czworka.draw()
    osemka.draw()
    szesnastka.draw()
    trzydziestka.draw()
    koniec.draw()
    screen.draw.text(str("MINER CLICKER"), [150, 10], color="black", fontsize=80)
    screen.draw.text(str("UPGRADES"), [WIDTH - 210, 10], color="black", fontsize=50)
    screen.draw.text(str("Liczba autokilofow: ") + str(liczba_auto_kilofow),[350, 500],color="black",fontsize=50)
    if zmk == 1:
        screen.clear()
        koniec.draw()
        wyjdz.draw()
        koniec.image = 'wygrana'
        koniec.pos = CENTER_X, CENTER_Y


def on_mouse_down(pos):
    global punkty, liczba_auto_kilofow, koszt_auto_kilofa, koszt_btt1, koszt_btt2, koszt_btt3, koszt_btt4, koszt_btt5, ulepszenie, zmk
    if kilof.collidepoint(pos):
        kilof.image = "kilofclick"
        sounds.kamien.play()
    if kup_autoclicker.collidepoint(pos):
        if punkty >= koszt_auto_kilofa:
            kup_autoclicker.image = "autoclicked"
            punkty -= koszt_auto_kilofa
            koszt_auto_kilofa *= 2
            liczba_auto_kilofow += 5
    if dwojka.collidepoint(pos):
        if punkty >= koszt_btt1:
            dwojka.image = "kupione"
            punkty -= koszt_btt1
            ulepszenie = 1
    if czworka.collidepoint(pos):
        if punkty >= koszt_btt2:
            czworka.image = "kupione"
            punkty -= koszt_btt2
            ulepszenie = 2
    if osemka.collidepoint(pos):
        if punkty >= koszt_btt3:
            osemka.image = "kupione"
            punkty -= koszt_btt3
            ulepszenie = 3
    if szesnastka.collidepoint(pos):
        if punkty >= koszt_btt4:
            szesnastka.image = "kupione"
            punkty -= koszt_btt4
            ulepszenie = 4
    if trzydziestka.collidepoint(pos):
        if punkty >= koszt_btt5:
            trzydziestka.image = "kupione"
            punkty -= koszt_btt5
            ulepszenie = 5
    if koniec.collidepoint(pos):
        if punkty >= 60000:
            zmk+=1
    if wyjdz.collidepoint(pos):
        exit()


def on_mouse_up(pos):
    if kilof.collidepoint(pos):
        global punkty, ulepszenie
        kilof.image = "kilof"
        if ulepszenie == 0:
            punkty += 1
        if ulepszenie == 1:
            punkty += 2
        if ulepszenie == 2:
            punkty += 4
        if ulepszenie == 3:
            punkty += 8
        if ulepszenie == 4:
            punkty += 16
        if ulepszenie == 5:
            punkty += 32
    if kup_autoclicker.collidepoint(pos):
        kup_autoclicker.image = "autoclicker"


def dodaj_autoclicker():
    global punkty
    punkty += liczba_auto_kilofow
    clock.schedule(dodaj_autoclicker, 1)


dodaj_autoclicker()
