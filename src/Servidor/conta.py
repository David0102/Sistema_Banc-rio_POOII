from cliente import Cliente
import datetime


class Conta:
    """
    Uma classe para representar a conta.

    ...

    Attributes  
    -----------
    numero : str
        Recebe número da conta. 

    titular : object
        Recebe um objeto do tipo cliente.

    saldo : float
        Recebe o valor do saldo da conta. 

    usuario : str
        Recebe o nome de usuário da conta.

    senha : str
        Recebe senha do usuário da conta. 

    limite : float
        Recebe o valor do limite da conta.

    data_transacao : date
        Recebe a data de uma determinada transação.

    Constructor
    ------------
    Parameters
    -----------
    Constrói todos os atributos necessários para o objeto cliente.

    numero : str
        Recebe o número da conta. 

    cliente : object
        Recebe um objeto do tipo cliente.

    usuario : str
            Recebe o nome de usuário da conta.

    senha : str
            Recebe senha do usuário da conta. 

    limite : float
            Recebe um valor limite por padrão.

    saldo : float
            Recebe o valor "0" por padrão.
    
    Methods
    --------

    def numero(self):
        Método para retornar o número da conta.
    
    def numero(self, numero):
        Método para alterar o número da conta.
    
    def usuario(self):
        Método para retornar o usuário.
    
    def usuario(self, usuario):
        Método para alterar o nome de usuário.

    def senha(self):
        Método para retornar a senha da conta.
    
    def senha(self, senha):
        Método para alterar a senha da conta.
    
    """

    __slots__ = ['_numero', '_titular', '_saldo', '_usuario', '_senha', '_limite', 'historico', 'data_transacao']

    def __init__(self, numero, cliente, usuario, senha, limite=10000, saldo = 0):
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self._usuario = usuario
        self._senha = senha
        self.data_transacao = datetime.datetime.today()

        @property
        def numero(self):
            return self._numero

        @numero.setter
        def numero(self, numero):
            self._numero = numero
        
        @property
        def usuario(self):
            return self._usuario

        @usuario.setter
        def usuario(self, usuario):
            self._usuario = usuario

        @property
        def senha(self):
            return self._senha

        @senha.setter
        def senha(self, senha):
            self._senha = senha