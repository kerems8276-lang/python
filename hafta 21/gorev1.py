import play

play.set_backdrop("white")

karakter = play.new_circle(color="red", radius=35, border_color="black", border_width=5)



@play.when_key_pressed("d","a","w","s")
def haraket(tus):
    if tus == "d":
        karakter.x = min(350,karakter.x+5)

    elif tus == "a":
        karakter.x = max(-350,karakter.x-5)

    elif tus == "w":
        karakter.y = min(250,karakter.y+5)

    elif tus == "s":
        karakter.y = max(-250,karakter.y-5)
play.start_program()
