from gtts import gTTS
import os 

def say(input): #using google text-to-speech library 
    gTTS(text=input, lang='pt', slow=False).save("precario.mp3")
    os.system("mpg123 precario.mp3")

say("Olá!")
say("O meu nome é Luís Morais e não gosto de ouvir a minha voz. ")
say("Excluindo essa parte, gostava de agradecer por muita coisa") 
say("mas vou concentrar-me no principal.")
say("Obrigado por toda a atenção e cuidado.")
say("Obrigado pelos momentos de humor")
say("Obrigado pelo sermão, por vezes indesejado")
say("Obrigado pelo amor")
