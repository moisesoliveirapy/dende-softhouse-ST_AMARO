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
        """
        Calcula a média aritmética de uma coluna.
        """
        if column not in self.dataset:
            raise ValueError(f"Coluna '{column}' não encontrada no dataset.")

        valores = self.dataset[column]

        if len(valores) == 0:
            raise ValueError(f"Coluna '{column}' está vazia.")

        for v in valores:
            if not isinstance(v, (int, float)):
                raise TypeError("Média só funciona com valores numéricos (int ou float).")

        soma = 0
        for v in valores:
            soma += v

        return soma / len(valores)




    def median(self, column):
        """
        Calcula a mediana de uma coluna.
        """
        # validação: coluna existe
        if column not in self.dataset:
            raise ValueError(f"Coluna '{column}' não encontrada no dataset.")

        valores = self.dataset[column]

        # validação: coluna não vazia
        if len(valores) == 0:
            raise ValueError(f"Coluna '{column}' está vazia.")

        # validação: somente números
        for v in valores:
            if not isinstance(v, (int, float)):
                raise TypeError("Mediana só funciona com valores numéricos (int ou float).")

        # ordena uma cópia para não alterar o dataset original
        ordenados = list(valores)

        # ordenação (bubble sort simples; sem usar sorted())
        n = len(ordenados)
        for i in range(n):
            for j in range(0, n - i - 1):
                if ordenados[j] > ordenados[j + 1]:
                    ordenados[j], ordenados[j + 1] = ordenados[j + 1], ordenados[j]

        meio = n // 2

        # se n for ímpar, retorna o do meio
        if n % 2 != 0:
            return ordenados[meio]

        # se n for par, média dos dois centrais
        return (ordenados[meio - 1] + ordenados[meio]) / 2

    def mode(self, column):
        """
        Encontra a moda (ou modas) de uma coluna.
        Retorna uma lista com o(s) valor(es) mais frequente(s).
        """
        # validação: coluna existe
        if column not in self.dataset:
            raise ValueError(f"Coluna '{column}' não encontrada no dataset.")

        valores = self.dataset[column]

        if len(valores) == 0:
            return []

        # conta frequências (sem Counter)
        freq = {}
        for v in valores:
            if v in freq:
                freq[v] += 1
            else:
                freq[v] = 1

        # encontra a maior frequência
        maior = 0
        for k in freq:
            if freq[k] > maior:
                maior = freq[k]

        # junta todas as modas (empates)
        modas = []
        for k in freq:
            if freq[k] == maior:
                modas.append(k)

        return modas


    def variance(self, column):
       coluna = self.dataset[column]
       n = len(coluna)

       #validacao
       if not isinstance(coluna[0], (int, float)):
           raise TypeError("Variação so funciona com numeros")
       
       media = self.mean(column)
       soma = 0

       for valor in coluna:
           soma += (valor - media) ** 2

       variancia = soma / n
       return variancia

    def stdev(self, column):
         variancia = self.variance(column)
         return variancia ** 0.5

    def covariance(self, column_a, column_b):
      coluna_a = self.dataset[column_a]
      coluna_b = self.dataset[column_b]

      #validação
      if len(column_a) != len(column_b):
          raise TypeError("As colunas devem ter o mesmo tamanho")
      if not isinstance(coluna_a[0], (int, float)) or not isinstance(coluna_b[0], (int, float)):
          raise TypeError("Variação so funciona com numeros")
      
      media_a = self.mean(column_a)
      media_b = self.mean(column_b)

      soma = 0

      for i in range(len(coluna_a)):
          soma += (coluna_a[i] - media_a) * (coluna_b[i] - media_b)

      return soma / len(coluna_a)

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
        if (frequency_method).lower() not in ('absolute', 'relative'):
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

        if frequency_method.lower().strip() == 'absolute':
            return lista_de_itens
        elif frequency_method.lower().strip() == 'relative':

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

        # Validação da coluna
        if column not in self.dataset:
            raise ValueError(f"Coluna '{column}' não encontrada no dataset.")

        valores = self.dataset[column]
        print(valores)
        # Validação de bins
        if bins <= 0:
            raise ValueError("O número de bins deve ser maior que zero.")

        menor_valor = min(valores)
        maior_valor = max(valores)
        print(bins)
        print(menor_valor)
        print(maior_valor)

        # Caso todos os valores sejam iguais
        if menor_valor == maior_valor:
           return {"Se os valores forem iguais": {(menor_valor, maior_valor): len(valores)}}


        tamanho_bin = (maior_valor - menor_valor) / bins
        print(f"tamanho bin: {tamanho_bin}")
        # Criando os limites
        limites = []
        for i in range(bins + 1):
            print(i)
            ponto = menor_valor + (i * tamanho_bin)
            limites.append(ponto)
            print(limites)

        # Criando estrutura do histograma
        histograma = {}
        for i in range(bins):
            intervalo = (limites[i], limites[i + 1])
            print(limites[i])
            print(limites[i + 1])
            print(intervalo)
            histograma[intervalo] = 0

        # Contagem dos valores
        for valor in valores:
            """ print(valor) """
            indice = int((valor - menor_valor) / tamanho_bin)
            
            """ 50,30,70,20,80,30,25,75,20,65 """
            # Ajuste para incluir o valor máximo no último intervalo
            if indice == bins:
                indice -= 1

            intervalo = (limites[indice], limites[indice + 1])
            print(f'intervalo v2{intervalo}')
            histograma[intervalo] += 1
            print(f'histograma v2: {histograma}')

        return histograma
    pass




