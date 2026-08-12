from tkinter import *
import random
import string

root = Tk()
root.geometry("400x200")
root.title("Gerador de Senhas")

passstr = StringVar()
pwd_len = IntVar()

#função para gerar senha
def get_pass():
    senha1 = string.ascii_letters + string.digits + string.punctuation
    senha = ""

    for x in range(pwd_len.get()):
        senha = senha + random.choice(senha1)
    passstr.set(senha)

Label(root, text= "gerador de senhas", font= "arial 20 bold").pack()
Label(root, text= " tamanho da senha", font= "arial 10 bold").pack(pady= 5)
Entry(root, textvariable= pwd_len).pack(pady= 5)
Button(root, text= "gerar senha", command= get_pass).pack(pady= 5)
Entry(root, textvariable= passstr).pack(pady= 5)

root.mainloop()