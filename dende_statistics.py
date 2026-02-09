class Statistics:
    """
    Uma classe para realizar cálculos estatísticos em um conjunto de dados.

    Atributos
    ----------
    dataset : dict[str, list]
        O conjunto de dados, estruturado como um dicionário onde as chaves
        são os nomes das colunas e os valores são listas com os dados.
    """
    def __init__(self, dataset):
        """
        Inicializa o objeto Statistics.

        Parâmetros
        ----------
        dataset : dict[str, list]
            O conjunto de dados, onde as chaves representam os nomes das
            colunas e os valores são as listas de dados correspondentes.
        """
        self.dataset = dataset

    def mean(self, column):
            def mean(self, column):
        coluna = self.dataset[column]
        tamanho_coluna = len(coluna)
        soma_coluna = 0
        media = float

        for item in coluna:
            soma_coluna = soma_coluna + item
        
        media = soma_coluna/tamanho_coluna

        return media

    def median(self, column):
        """
        Calcula a mediana de uma coluna.

        A mediana é o valor central de um conjunto de dados ordenado.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            O valor da mediana da coluna.
        """
        pass

    def mode(self, column):
        """
        Encontra a moda (ou modas) de uma coluna.

        A moda é o valor que aparece com mais frequência no conjunto de dados.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        list
            Uma lista contendo o(s) valor(es) da moda.
        """
        pass

    def variance(self, column):
        """
        Calcula a variância populacional de uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            A variância dos valores na coluna.
        """
        pass

    def stdev(self, column):
        """
        Calcula o desvio padrão populacional de uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            O desvio padrão dos valores na coluna.
        """
        pass

    def covariance(self, column_a, column_b):
        """
        Calcula a covariância entre duas colunas.

        Parâmetros
        ----------
        column_a : str
            O nome da primeira coluna (X).
        column_b : str
            O nome da segunda coluna (Y).

        Retorno
        -------
        float
            O valor da covariância entre as duas colunas.
        """
        pass

    def itemset(self, column):
        """
        Retorna o conjunto de itens únicos em uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        set
            Um conjunto com os valores únicos da coluna.
        """
        pass

    def absolute_frequency(self, column):
        lista_de_itens = []
        coluna = self.dataset[column]
        dicionario_frequencia_absoluta = {}

        for valor in coluna:
            if valor not in lista_de_itens:
                lista_de_itens.append(valor)
                lista_de_itens.append(1)
                continue
            
            indice_incrementar = int(lista_de_itens.index(valor))

            lista_de_itens[indice_incrementar + 1] = lista_de_itens[indice_incrementar + 1] + 1

        for item in range(0, len(lista_de_itens), 2):
            chave = lista_de_itens[item]
            valor = lista_de_itens[item+1]
            dicionario_frequencia_absoluta[chave] = valor

        dicionario_frequencia_absoluta = {lista_de_itens[i]: lista_de_itens[i+1] for i in range(0, len(lista_de_itens), 2)}

        return dicionario_frequencia_absoluta

    def relative_frequency(self, column):
        lista_de_itens = []
        coluna = self.dataset[column]
        total_frequencia_absoluta = 0
        dicionario_frequencia_relativa = {}

        for valor in coluna:
            if valor not in lista_de_itens:
                lista_de_itens.append(valor)
                lista_de_itens.append(1)
                continue
            
            indice_incrementar = int(lista_de_itens.index(valor))

            lista_de_itens[indice_incrementar + 1] = lista_de_itens[indice_incrementar + 1] + 1

        contador = 0

        for frequencia_absoluta in lista_de_itens:
            if contador % 2 == 0:
                contador = contador + 1
                continue

            total_frequencia_absoluta = total_frequencia_absoluta + frequencia_absoluta
            contador = contador + 1

        for item in range(0, len(lista_de_itens), 2):
            chave = lista_de_itens[item]
            valor = lista_de_itens[item+1]



            dicionario_frequencia_relativa[chave] = valor/total_frequencia_absoluta

        dicionario_frequencia_absoluta = {lista_de_itens[i]: lista_de_itens[i+1] for i in range(0, len(lista_de_itens), 2)}

        return dicionario_frequencia_relativa

    def cumulative_frequency(self, column, frequency_method='absolute'):
                if (frequency_metody).lower() not in ('absolute', 'relative'):
            return 'Insira uma frequência válida!'

        lista_de_itens = []
        coluna = self.dataset[column]
        dicionario_frequencia_absoluta = {}
        valor_acumulativo = 0
        valor_total = 0
        

        for valor in coluna:
            if valor not in lista_de_itens:
                lista_de_itens.append(valor)
                lista_de_itens.append(1)
                continue
            
            indice_incrementar = int(lista_de_itens.index(valor))
            

            lista_de_itens[indice_incrementar + 1] = lista_de_itens[indice_incrementar + 1] + 1

        contador = 0

        for valor in lista_de_itens:
            if contador % 2 == 0:
                contador = contador + 1
                continue

            lista_de_itens[contador] = lista_de_itens[contador] + valor_acumulativo
            valor_acumulativo = lista_de_itens[contador]

            contador = contador + 1

        valor_total = lista_de_itens[-1]

        if frequency_metody.lower().strip() == 'absolute':
            return lista_de_itens
        elif frequency_metody.lower().strip() == 'relative':

            for indice in range(1, len(lista_de_itens), 2):
                lista_de_itens[indice] = lista_de_itens[indice] / valor_total
        else:
            return('Insira uma frequência válida!')

        return lista_de_itens


    def conditional_probability(self, column, value1, value2):
        """
        Calcula a probabilidade condicional P(X_i = value1 | X_{i-1} = value2).

        Este método trata a coluna como uma sequência e calcula a probabilidade
        de encontrar `value1` imediatamente após `value2`.

        Fórmula: P(A|B) = Contagem de sequências (B, A) / Contagem total de B

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).
        value1 : any
            O valor do evento consequente (A).
        value2 : any
            O valor do evento condicionante (B).

        Retorno
        -------
        float
            A probabilidade condicional, um valor entre 0 e 1.
        """
        pass

    def quartiles(self, column):
        """
        Calcula os quartis (Q1, Q2 e Q3) de uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        dict
            Um dicionário com os quartis Q1, Q2 (mediana) e Q3.
        """
        pass

    def histogram(self, column, bins):
        """
        Gera um histograma baseado em buckets (intervalos).

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).
        bins : int
            Número de buckets (intervalos).

        Retorno
        -------
        dict
            Um dicionário onde as chaves são os intervalos (tuplas)
            e os valores são as contagens.
        """
        pass

