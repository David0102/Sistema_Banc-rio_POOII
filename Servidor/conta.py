from cliente import Cliente
import datetime


class Conta:
    """
    Uma classe para representar a conta.

    ...

    Atributos 
    ---------
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

    
    """

    __slots__ = ['_numero', '_titular', '_saldo', '_usuario', '_senha', '_limite', 'historico', 'data_transacao']

    def __init__(self, numero, cliente, usuario, senha, limite=10000, saldo = 0):
        """
        Constrói todos os atributos necessários para o objeto cliente.

        Parâmetros
        ---------
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
            
        """
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self._usuario = usuario
        self._senha = senha
        self.data_transacao = datetime.datetime.today()

        @property
        def numero(self):
            """
            Método
            ------
            Método para retornar o número da conta.

            """
            return self._numero

        @numero.setter
        def numero(self, numero):
            """
            Método
            ------
            Método para alterar o número da conta.

            """
            self._numero = numero
        
        @property
        def usuario(self):
            """
            Método
            ------
            Método para retornar o usuário da conta.

            """
            return self._usuario

        @usuario.setter
        def usuario(self, usuario):
            """
            Método
            ------
            Método para alterar o usúario da conta.

            """
            self._usuario = usuario

        @property
        def senha(self):
            """
            Método
            ------
            Método para retornar a senha da conta.

            """
            return self._senha

        @senha.setter
        def senha(self, senha):
            """
            Método
            ------
            Método para alterar a senha da conta.

            """
            self._senha = senha