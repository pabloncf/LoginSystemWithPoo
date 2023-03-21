from Data import Data
import time

class Signup:         
    def __init__(self):

        print("##################")
        print("#### CADASTRO ####")
        print("##################")

        self.usernameInput = input("Digite seu usuário:")
        time.sleep(1)

        self.passwordInput = input("Digite sua senha:")
        time.sleep(1)
        
        self.checkPass = input("Confirme sua senha:")

        if(self.checkPass != self.passwordInput):
            print("As senhas não se conhecidem. Por favor, tente novamente")
            Signup()
        elif(self.checkPass == self.passwordInput):
            Data.insertData(self.usernameInput, self.passwordInput)
            
            print("Cadastro realizado com sucesso!")
            time.sleep(1)
        
        