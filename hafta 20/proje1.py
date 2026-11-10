import turtle

ekran = turtle.Screen()
ekran.title("Dijital Çizim Tahtası")

kalem = turtle.Turtle()
kalem.speed(0)
kalem.pensize(3)


# Görev 1: Fareyle çizim fonksiyonu oluştur.

def haraket_et(x, y):
    kalem.goto(x, y)

ekran.onscreenclick(haraket_et)
# Görev 2: Renk değiştirme fonksiyonları ekle.
def kirmizi():
    kalem.pencolor("red")
def mavi():
    kalem.pencolor("blue")
def yesil():
    kalem.pencolor("green")
def siyah():
    kalem.pencolor("black")
# Görev 3: Ekranı temizleme özelliği ekle.
def clear():
    kalem.clear()
    kalem.penup()
    kalem.goto(0,0)
    kalem.pendown()
# Görev 4: Klavye olaylarını tanımla.

ekran.onkey(kirmizi, "r")

ekran.onkey(mavi, "b")

ekran.onkey(yesil, "g")

ekran.onkey(siyah, "s")

ekran.onkey(clear, "c")


# bonus Görev: 1, 2 ve 3 tuşlarına basıldığında kalemin kalınlığını değiştiren özellik ekle.
def ince():
    kalem.pensize(1)

ekran.onkey(ince, "1")

def kalin():
    kalem.pensize(10)

ekran.onkey(kalin, "2")

def  normal():
    kalem.pensize(3)

ekran.onkey(normal, "3")

def kaldir():
    kalem.penup()

ekran.onkey(kaldir, "u")

def indir():
    kalem.pendown()

ekran.onkey(indir, "d")

ekran.listen()
ekran.mainloop()
