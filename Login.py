import time
from Data import Data

class Login:
    def __init__(self):

        print("#################")
        print("##### LOGIN #####")
        print("#################")

        time.sleep(2)
        self.usernameInput = input("Digite o nome de usuário:")
        time.sleep(1)
        self.passwordInput = input("Digite sua senha:")
        time.sleep(1)

        data = Data.data
        
        if(data[0] != self.usernameInput or data[1] != self.passwordInput):
            print("Usuário ou senha inválido")
            self.usernameInput = input("Digite o nome de usuário:")
            time.sleep(1)
            self.passwordInput = input("Digite sua senha:")
            time.sleep(1)
            Login()
        else:
           time.sleep(2)
           print("Bem vindo ao sistema!")
