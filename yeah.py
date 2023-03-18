from gtts import gTTS
import os
import pyautogui
from turtle import * 

def say(input):

    gTTS(text=input, lang='pt', slow=False).save("precario.mp3")
  
    play("precario")

def play(track):
    os.system("mpg123 " + track + ".mp3")
    
screen = Screen()
screen.setup(width = 1.0, height = 1.0)
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)
color("red")
speed(6)
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill()
color("white")
left(135)
right(180)
forward(200)
right(90)
forward(350)
begin_fill()
pensize(3)
color("black")
write("Feliz dia do pai!", font=("Comic Sans MS", 100, "normal"))
say("Feliz dia do pai!")
delay(2000)
end_fill()
os.system("open pai.mp4")
pyautogui.press('space')
say("Olá!")
say("O meu nome é Luís Morais e não gosto da minha voz. ")
say("Excluindo essa parte, gostava de agradecer por muita coisa") 
say("mas vou concentrar-me no principal.")
say("Obrigado por toda a atenção e cuidado.")
say("Obrigado pelos momentos de humor")
say("Obrigado pelo sermão, por vezes indesejado")
say("Obrigado pelo amor")


