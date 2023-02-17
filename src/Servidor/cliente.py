class Cliente:
    """
    Uma classe para representar o cliente.

    ...

    Attributes 
    -----------
    nome : str
        Recebe o nome do cliente.

    cpf : str
        Recebe o CPF do cliente.
    
    Constructor
    ------------
    Parameteres
    ------------

    nome: str
        Recebe o nome do cliente.

    cpf: str
        Recebe o CPF do cliente.

    Methods
    --------

    def nome(self):
        Método para retornar o nome do cliente.
    
    def nome(self, nome):
        Método para alterar o nome do cliente.

    def cpf(self):
        Método para retornar o CPF do cliente.
    
    def cpf(self, cpf):
        Metodo para alterar o CPF do cliente.

    """
    __slots__ = ['_nome', '_cpf']

    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf

        @property
        def nome(self):
            return self._nome

        @nome.setter
        def nome(self, nome):
            self._nome = nome

        @property
        def cpf(self):
            return self._cpf

        @cpf.setter
        def cpf(self, cpf):
            self._cpf = cpf
