from conta import Conta
from cliente import Cliente
import datetime
from pymongo import MongoClient
import hashlib

"""
Conectando com o banco de dados.

"""

MONGO_URI = 'mongodb://localhost'
client = MongoClient(MONGO_URI)
db = client['sistema_bancario']
contas = db["contas"]
login = db["login"]
historicos = db["historicos"]


class Banco:

    """
    A classe banco irá conter os métodos que irão realizar as operações requisitadas pelo cliente na sua
    determinada conta.

    """

    def adciona_conta(self, conta):
        """
        O método irá passar os dados do objeto para o banco de dados.
        
        Parameters
        -----------
        conta : object
            Recebe a conta de um cliente.

        """
        hash = hashlib.sha256(conta._senha.encode('utf-8')).hexdigest()
        contas.insert_one({"Número": conta._numero, "Nome": conta._titular._nome, "CPF": conta._titular._cpf, 
                             "Saldo": conta._saldo, "Usuário": conta._usuario, "Senha": hash, "Limite": conta._limite})
        
    def remove_conta(self, cpf):
        """
        O método irá receber o cpf de um cliente, e logo após irá deletar sua conta do banco de dados, através do CPF.
        
        Parameters
        -----------
        cpf : str
            Recebe o cpf do cliente.

        """
        contas.delete_one({'CPF': cpf})

    def verifica_numero_conta(self, numero):
        """
        O método irá receber o número de uma conta, e logo após irá verificar se a mesma já está cadastrada 
        no banco de dados.
        
        Parameters
        -----------
        numero : str
            Recebe o número da conta de um cliente.

        """
        aux = contas.find_one({"Número": numero})
        if(aux == None):
            return True
        else:
            return False
    
    def verifica_cpf(self, cpf):
        """
        O método irá receber o número do cpf de uma cliente, e logo após irá verificar se o mesmo já está cadastrado 
        no banco de dados.
        
        Parameters
        -----------
        cpf : str
            Recebe o número do cpf de um cliente.

        """
        aux = contas.find_one({"CPF": cpf})
        if(aux == None):
            return True
        else:
            return False
    
    def verifica_conta_login(self, usuario, senha):
        """
        O método irá receber o usuário e senha de um cliente, e logo após irá verificar se o cliente já está cadastrado 
        no banco de dados.
        
        Parameters
        -----------
        usuario: str
            Recebe o nome do usuário de um cliente.
        
        senha: str
            Recebe a senha de um cliente.

        """
        hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        aux = contas.find_one({'Usuário': usuario, 'Senha': hash})
        if(aux != None):
            return aux
        else:
            return False

    def saca(self, cpf, valor):
       """
        O método irá receber o cpf de um cliente e o valor do saque, e logo após irá verificar se o cliente está cadastrado 
        no banco de dados, caso esteja, será feito o saque do valor passado.
        
        Parameters
        -----------
        cpf: str
            Recebe o cpf de um cliente.
        
        valor: float
            Recebe o valor do saque.

        """
       aux1 = contas.find_one({'CPF': cpf})
       if(aux1.get('Saldo') >= valor):
            valor1 = aux1.get('Saldo') - valor
            contas.update_one({'CPF': cpf}, {'$set':{'Saldo': valor1}})
            self.adciona_transacao(aux1.get('CPF'), 'saque', valor)
            return True
       else:
           return False

    def deposita(self, cpf, valor):
        """
        O método irá receber o cpf de um cliente e o valor do depósito, e logo após irá verificar se o cliente está 
        cadastrado no banco de dados, caso esteja, será feito o depósito do valor passado.
        
        Parameters
        -----------
        cpf: str
            Recebe o cpf de um cliente.
        
        valor: float
            Recebe o valor do depósito.

        """
        aux1 = contas.find_one({'CPF': cpf})
        if(aux1 != None):
            valor1 = aux1.get('Saldo') + valor
            contas.update_one({'CPF': cpf}, {'$set':{'Saldo': valor1}})
            self.adciona_transacao(aux1.get('CPF'), 'deposito', valor)
            return True
        else:
            return False

    def transfere(self, cpf, destino, valor):
        """
        O método irá receber o cpf de um cliente, o valor da transferência, e o número da conta de destino, 
        e logo após irá verificar se a conta de origem e destino estão cadastradas no banco de dados, caso esteja, 
        será feita a transferência do valor passado.
        
        Parameters
        -----------
        cpf: str
            Recebe o cpf da conta de origem.
        
        destino: str
            Recebe o número da conta de destino.

        valor: float
            Recebe o valor da transferência.
            
        """
        aux = self.saca(cpf, valor)
        if(aux):
            aux1 = contas.find_one({'Número': destino})
            if(aux1 != None):
                valor_dep = aux1.get('Saldo') + valor
                contas.update_one({'CPF': aux1.get('CPF')}, {'$set':{'Saldo': valor_dep}})
                self.adciona_transf(cpf, aux1.get('Número'), valor)
                return 1
            else:
                return 0
        else:
            return 2

    def extrato(self, cpf):
        """
        O método irá receber o cpf de um cliente, e logo após irá verificar se o cliente está cadastrado 
        no banco de dados, caso esteja, será capturado o nome, número da conta e o saldo do cliente, e retornado
        no formato de uma string, separados por vírgula.
        
        Parameters
        -----------
        cpf: str
            Recebe o cpf de um cliente.
        
        """
        aux1 = contas.find_one({'CPF': cpf})
        if(aux1 != None):
            lista = [aux1.get('Nome'),aux1.get('Número'),str(aux1.get('Saldo'))]
            dados = ','.join(lista)
            self.adciona_transacao(aux1.get('CPF'), 'extrato', aux1.get('Saldo'))
            return dados
        else:
            return False
    
    def adciona_transacao(self, user, tipo, valor):
        """
        O método irá receber o cpf de um cliente, o tipo de transação e o valor do saque. Logo após, a transação será 
        adcionada ao banco de dados.
        
        Parameters
        -----------
        user: str
            Recebe o cpf de um cliente.

        tipo:
            Recebe o tipo da transação.
        
        valor:
            Recebe o valor da transação.
        
        """
        data = datetime.datetime.today()
        if(tipo == 'saque'):
            historicos.insert_one({'id_user': user, 'Transação': 'saque de {} - Data: {}'.format(valor, data)})
        elif(tipo == 'deposito'):
            historicos.insert_one({'id_user': user, 'Transação': 'Depósito de {} - Data: {}'.format(valor, data)})
        elif(tipo == 'extrato'):
            historicos.insert_one({'id_user': user, 'Transação': 'Tirou extrato - Saldo:{} - Data: {}'.format(valor, data)})
        
    def adciona_transf(self, origem, destino, valor):
        """
        Método irá receber o cpf da conta de origem, o número da conta de destino e o valor da transferência, e logo
        após, será inserida a transferência no banco de dados.

        Parameters

        origem: str
            Recebe o CPF da conta de origem.
        
        destino: str
            Recebe o número da conta de destino.
        
        valor: float
            Recebe o valor da transferência.

        """
        aux = contas.find_one({'Número': destino})
        aux1 = contas.find_one({'CPF': origem})
        data = datetime.datetime.today()
        historicos.insert_one({'id_user': origem, 'Transação': 'Transferência de {} para conta {} - Data: {}'.format(valor, destino, data)})
        historicos.insert_one({'id_user': aux.get('CPF'), 'Transação': 'Transferência de {} recebda da conta {}- Data: {}'.format(valor, aux1.get('Número'), data)})

    def retorna_historico(self, cpf):
        """
        Método recebe o cpf da conta a ser retornado o histórico, e logo após, será feita uma busca do histórico 
        no banco de dados, daquele determinado cpf. E por fim, será retornada uma lista cotendo todas as transações.

        Parameters
        
        cpf: str
            Recebe o CPF da conta a ser buscado o histórico.
        """
        lista = []
        for i in historicos.find({'id_user': cpf}, {'Transação': 1}):
            lista.append(str(i))
        aux = len(lista)
        if(aux == 0):
            return False
        return lista
