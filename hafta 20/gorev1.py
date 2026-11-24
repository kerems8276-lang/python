import turtle
dongu = 0

turtle.penup()
turtle.goto(100,250)
turtle.pendown()
while dongu != 3:
    dongu += 1
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)
turtle.forward(200)
turtle.exitonclick()
# 1 -DEĞİLİ YÖNTEM

dongu1 = 0

while dongu1 != 10:
    print("Burak")
    dongu1 += 1 # dongu1 = dongu1 + 1

# 2 - SAYAÇ YÖNETİMİ

dongu2 = 0

while dongu2 <= 10:
    print("Kerem")
    dongu2 += 1 #

# 3 - For

for i in range(5,10): # FOR i değişkenine belirlenen aralğıa kadaar 0 dan başlayarak değer atar ve kodunu o şekilde çalıştırır.
    print("Kodlama!", i)

# FOR TEKRAR SAYISINI BİLDİĞİMİZ GÖREVLERDE KULLANILIR. WHİLE İSE TEKRAR SAYISINDAN EMİN OLMADIĞIMIZ GÖREVLERDE KULLANILIR.

puanlar = [10,50,100,50,100,50,100,50,100,50,100,50,100,50,100,50,100,50,100,50,100,50,100,50,100,50,100]
print(len(puanlar))
for x in puanlar:
    print("Puanım:", x)