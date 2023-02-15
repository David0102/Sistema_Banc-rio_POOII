class Cliente:
    """
    Uma classe para representar o cliente.

    ...

    Atributos 
    ---------
    nome : str
        Recebe o nome do cliente.

    cpf : str
        Recebe o CPF do cliente.
    
    """

    __slots__ = ['_nome', '_cpf']

    def __init__(self, nome, cpf):
        """
        Constrói todos os atributos necessarios para o objeto cliente.

        Parâmetros
        ---------
            nome : str
                Recebe o nome do cliente.

            cpf : str
                Recebe o CPF do cliente.

        """
        self._nome = nome
        self._cpf = cpf

        @property
        def nome(self):
            """
            Método
            ------
            Método para retornar o nome do cliente.

            """
            return self._nome

        @nome.setter
        def nome(self, nome):
            """
            Método
            ------
            Método para alterar o nome do cliente.

            """
            self._nome = nome

        @property
        def cpf(self):
            """
            Método
            ------
            Método para retornar o CPF do cliente.

            """
            return self._cpf

        @cpf.setter
        def cpf(self, cpf):
            """
            Método
            ------
            Metodo para alterar o CPF do cliente.

            """
            self._cpf = cpf
