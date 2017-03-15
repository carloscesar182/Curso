from tkinter import *
import pygame.mixer

sounds = pygame.mixer
sounds.init()

s_correct = sounds.Sound("correct.wav")
s_wrong = sounds.Sound("wrong.wav")

number_correct = 0
number_wrong = 0


def play_correct_sound():
    global number_correct
    number_correct += 1
    s_correct.play()


def play_wrong_sound():
    global number_wrong
    number_wrong += 1
    s_wrong.play()


def prompt():
    print(str(number_correct) + " were correctly answered.")
    print(str(number_wrong) + " were answered incorrectly.")


app = Tk()  # cria uma janela chamada "app"
app.title("TVN Game Show")  # dá um nome para a janela
app.geometry('300x100+200+100')  # configura a coordenada e o tamanho da janela

b1 = Button(app, text = "Correct!", width = 10, command = play_correct_sound)  # adiciona o botao
b1.pack(side = 'left', padx = 10, pady = 10)  # linka o botão com a janela

b2 = Button(app, text = "Wrong!", width = 10, command = play_wrong_sound)
b2.pack(side = 'right', padx = 10, pady = 10)

b3 = Button(app, text = "Quit", width = 10, command = prompt)
b3.pack(side = 'bottom', padx = 10, pady = 10)

app.mainloop()  # inicia o evento
