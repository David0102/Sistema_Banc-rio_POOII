import socket
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Login():
    """
    A classe irá representar o login do usuário.

    Atributes
    ----------
    login_user : str
        Login_user irá receber o cpf do usuário logado para realizar as operações requisitadas.
    """
    
    login_user = None

def main():
    """
    O método main irá criar o socket, com o ip e a porta requisitada.

    Methods
    --------
    
    def fazer_login():
        O método irá enviar o valor 0 para o servidor, para indicar que será realizado um login.

        O método irá enviar o usuário e senha capturados da tela de login, para o servidor no formato de uma string,
        separados por vírgula.

    def chama_logout():
        O método irá deslogar o usuário, ou seja, a variável login_user da classe login irá receber None.
    
    def chama_tela_cadastro():
        O método irá fechar a tela de cadastro e abrir a tela de login.
    
    def cadastrar():
        O método irá enviar o valor 1 para o servidor, para indicar que será realizado um cadastro.

        O método irá enviar os dados capturados dos campos da tela de cadastro, e logo após irá fazer o envio dos mesmos
        para o servidor, no formato de string, e separados por vírgula.
    
    def chama_tela_saque():
        O método irá fechar a tela do dashboard, e logo após irá abrir a tela de saque.
    
    def sacar():
        O método irá enviar o valor 4 para o servidor, para indicar que será realizado um saque.
        
        O método irá capturar o valor do saque da tela de saque, logo após irá enviar ao servidor no formato
        de uma string.
    
    def chama_tela_dashboard():
        O método irá fechar a tela de saque, e abrir a tela do dashboard.
    
    def chama_tela_deposito():
        O método irá fechar a tela do dashboard, e abrir a tela de depósito.
    
    def chama_deposito():
        O método irá enviar o valor 5 para o servidor, para indicar que será realizado um depósito.

        O método irá capturar o valor do depósito da tela de saque, logo após irá enviar ao servidor no formato
        de uma string.
    
    def chama_tela_transferencia():
        O método irá fechar a tela do dashboard, e abrir a tela de transferência.
    
    def transferir():
        O método irá enviar o valor 6 para o servidor, para indicar que será realizado uma transferência.

        O método irá capturar o número da conta e o valor da transferência da tela de transferência, e logo após
        irá enviar para o servidor no formato de uma string, separados por vírgula.
    
    def chama_tela_extrato():
        O método irá enviar o valor 7 para o servidor, para indicar que será requisitado o extrato da conta.
    
    def voltar_extrato_dashboard():
        O método irá fechar a tela de extrato, e abrir a tela do dashboard.
    
    def deletar_conta():
        O método irá enviar o valor 8 para o servidor, para indicar que uma conta será deletada.
    
    def voltar_transferencia_dashboard():
        O método irá fechar a tela de tranferência, e abrir a tela do dashboard.
    
    def voltar_deposito_dashboard():
        O método irá fechar a tela de deposito, e abrir a tela do dashboard.

    def voltar_cadastro_login():
        O método irá fechar a tela de cadastro, e abrir a tela de login.
    
    def chama_tela_historico():
        O método irá enviar o valor 9 para o servidor, para indicar que será requisitado o histórico da conta.
    
    def voltar_historico_dashboard():
        O método irá fechar a tela de histórico, e abrir a tela do dashboard.
    
    def finalizar():
        O método irá enviar o valor 0 para o servidor, indicando para desconectar o cliente. O socket será fechado, e 
        a será exibida a tela de login.
    """

    ip = '192.168.1.16'
    port = 3000
    addr = (ip, port)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    login1 = Login()

    try:
        client_socket.connect(addr)
    except:
        print("\nNão foi possível conectar ao servidor!\n")
        exit()



    def fazer_login():
        usuario = login.lineEdit.text()
        senha = login.lineEdit_2.text()
        if(usuario == "" or senha == ""):
            QMessageBox.information(None, "Alerta!", "Preencha todos os campos!")
        else:
            client_socket.send('2'.encode())
            lista_dados = [usuario,senha]
            dados = ','.join(lista_dados)
            client_socket.send(dados.encode())
            retorno = client_socket.recv(1024).decode()
            if(retorno != '0'):
                ret = retorno.split(',')
                login1.login_user = ret[0]
                login.close()
                dashboard.show()
                dashboard.label.setText("Olá {}".format(ret[1]))
                QMessageBox.information(None, "Alerta!", "Login realizado com sucesso!")

            elif(retorno == '0'):
                QMessageBox.information(None, "Alerta!", "Usuário ou senha incorreta!")

    def chama_logout():
            login1.login_user = None
            dashboard.close()
            login.show()
            QMessageBox.information(None, "Aviso!", "Logout realizado com sucesso!")


    def chama_tela_cadastro():
        login.close()
        cadastro.show()

    def cadastrar():
        nome = cadastro.lineEdit.text()
        cpf = cadastro.lineEdit_2.text()
        numConta = cadastro.lineEdit_3.text()
        usuario = cadastro.lineEdit_5.text()
        senha = cadastro.lineEdit_6.text()

        if(nome == "" or cpf == "" or numConta == "" or usuario == "" or senha == ""):
            QMessageBox.information(None, "Alerta!", "Preencha todos os campos!")
        else:
            client_socket.send('1'.encode())
            lista_dados = [nome,cpf,numConta,usuario,senha]
            dados = ','.join(lista_dados)
            client_socket.send(dados.encode())

            retorno = int(client_socket.recv(1024).decode())
            
            if(retorno == 1):
                cadastro.close()
                login.show()
                QMessageBox.information(None, "Aviso!", "Cadastro realizado com sucesso!")

            elif(retorno == 0):
                QMessageBox.information(None, "Aviso!", "CPF ou Número da conta já cadastrado!")

    def chama_tela_saque():
        dashboard.close()
        saque.show()

    def sacar():
        valor = str(saque.lineEdit.text())
        if(valor == '0'):
            QMessageBox.information(None, "Aviso!", "Valor inválido!")
        else:
            client_socket.send('4'.encode())
            lista_saque = [login1.login_user,valor]
            aux = ','.join(lista_saque)
            client_socket.send(aux.encode())

            retorno = int(client_socket.recv(1024).decode())
                
            if(retorno == 1):
                saque.close()
                dashboard.show()
                QMessageBox.information(None, "Aviso!", "Saque realizado com sucesso!")

            elif(retorno == 0):
                QMessageBox.information(None, "Aviso!", "Saldo insuficiente!")
            
    def chama_tela_dashboard():
        saque.close()
        dashboard.show()

    def chama_tela_deposito():
        dashboard.close()
        deposito.show()

    def chama_deposito():
        valor = str(deposito.lineEdit.text())
        if(valor == '0'):
            QMessageBox.information(None, "Aviso!", "Valor inválido!")
        else:
            client_socket.send('5'.encode())
            aux = [login1.login_user,valor]
            lista_deposito = ','.join(aux)
            client_socket.send(lista_deposito.encode())

            retorno = int(client_socket.recv(1024).decode())
                
            if(retorno == 1):
                deposito.close()
                dashboard.show()
                QMessageBox.information(None, "Aviso!", "Depósito realizado com sucesso!")
            elif(retorno == 0):
                QMessageBox.information(None, "Aviso!", "Erro ao realizar depósito!")
        

    def chama_tela_transferencia():
        dashboard.close()
        transferencia.show()

    def transferir():
        numConta = transferencia.lineEdit.text()
        valor = transferencia.lineEdit_2.text()
        if(valor == '0'):
            QMessageBox.information(None, "Aviso!", "Valor inválido!")
        else:
            client_socket.send('6'.encode())
            lista_dados = [login1.login_user,numConta,valor]
            dados = ','.join(lista_dados)
            client_socket.send(dados.encode())
        
            retorno = int(client_socket.recv(1024).decode())
                
            if(retorno == 1):
                transferencia.close()
                dashboard.show()
                QMessageBox.information(None, "Aviso!", "Transferência realizada com sucesso!")

            elif(retorno == 0):
                QMessageBox.information(None, "Aviso!", "Número da conta inválido!")

            elif(retorno == 2):
                QMessageBox.information(None, "Aviso!", "Saldo insuficiente!")

    def chama_tela_extrato():
        client_socket.send('7'.encode())
        user = login1.login_user
        client_socket.send(user.encode())
        dashboard.close()
        extrato.show()

        retorno = client_socket.recv(1024).decode()

        if(retorno != '0'):
            lista_dados = retorno.split(',')
            extrato.lineEdit.setText(lista_dados[0])
            extrato.lineEdit_2.setText(lista_dados[1])
            extrato.lineEdit_3.setText(lista_dados[2])
        else:
            QMessageBox.information(None, "Aviso!", "Erro ao mostrar extrato!")

    def voltar_extrato_dashboard():
        extrato.close()
        dashboard.show()

    def deletar_conta():
        client_socket.send('8'.encode())
        user_deletar = login1.login_user
        client_socket.send(user_deletar.encode())
        retorno = int(client_socket.recv(1024).decode())
        if(retorno == 1):
            dashboard.close()
            login.show()
            QMessageBox.information(None, "Aviso!", "Conta excluída com sucesso!")

    def voltar_transferencia_dashboard():
        transferencia.close()
        dashboard.show()

    def voltar_deposito_dashboard():
        deposito.close()
        dashboard.show()

    def voltar_cadastro_login():
        cadastro.close()
        login.show()

    def chama_tela_historico():
        client_socket.send('9'.encode())
        user_historico = login1.login_user
        client_socket.send(user_historico.encode())
        retorno = client_socket.recv(1024).decode()
        if(retorno != '0'):
            dashboard.close()
            historico.show()
            lista = retorno.replace(",","\n")
            historico.label_3.setText(lista)
        else:
            QMessageBox.information(None, "Aviso!", "O histórico está vazio!")

    def voltar_historico_dashboard():
        historico.close()
        dashboard.show()

    def finalizar():
        client_socket.send('0'.encode())
        client_socket.close()
        login.close()

    app = QtWidgets.QApplication([])
    login = uic.loadUi("Telas/login.ui")
    cadastro = uic.loadUi("Telas/cadastro.ui")
    dashboard = uic.loadUi("Telas/dashboard.ui")
    saque = uic.loadUi("Telas/saque.ui")
    deposito = uic.loadUi("Telas/deposito.ui")
    transferencia = uic.loadUi("Telas/transferencia.ui")
    extrato = uic.loadUi("Telas/extrato.ui")
    historico = uic.loadUi("Telas/historico.ui")



    login.pushButton.clicked.connect(fazer_login)
    login.pushButton_2.clicked.connect(chama_tela_cadastro)
    cadastro.pushButton_2.clicked.connect(cadastrar)
    cadastro.pushButton_3.clicked.connect(voltar_cadastro_login)
    dashboard.pushButton_2.clicked.connect(chama_tela_saque)
    dashboard.pushButton_3.clicked.connect(chama_tela_deposito)
    dashboard.pushButton_5.clicked.connect(chama_tela_extrato)
    dashboard.pushButton_6.clicked.connect(chama_tela_historico)
    dashboard.pushButton_7.clicked.connect(chama_logout)
    dashboard.pushButton_4.clicked.connect(chama_tela_transferencia)
    saque.pushButton_8.clicked.connect(sacar)
    saque.pushButton_9.clicked.connect(chama_tela_dashboard)
    deposito.pushButton_8.clicked.connect(chama_deposito)
    deposito.pushButton_9.clicked.connect(voltar_deposito_dashboard)
    transferencia.pushButton_8.clicked.connect(transferir)
    transferencia.pushButton_9.clicked.connect(voltar_transferencia_dashboard)
    extrato.pushButton_8.clicked.connect(voltar_extrato_dashboard)
    dashboard.pushButton_8.clicked.connect(deletar_conta)
    historico.pushButton_6.clicked.connect(voltar_historico_dashboard)
    login.pushButton_3.clicked.connect(finalizar)

    login.show()
    app.exec()

if __name__ == "__main__":
    main()