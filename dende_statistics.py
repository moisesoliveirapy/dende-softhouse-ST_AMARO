class Statistics:
    def __init__(self, dataset):
        if not isinstance(dataset, dict):
            raise TypeError("O dataset deve ser um dicionário.")
        
        self.dataset = dataset 
        
        colunas = list(self.dataset.keys())

        if not colunas:
            return
        
        primeira_chave = colunas[0]
        if not isinstance(self.dataset[primeira_chave], list):
            raise ValueError(f"A coluna '{primeira_chave}' deve conter uma lista.")

        tamanho_esperado = len(self.dataset[primeira_chave])

        for rotulo in colunas:
            lista_dados = self.dataset[rotulo]

            if not isinstance(lista_dados, list):
                raise ValueError(f"A entrada '{rotulo}' não é uma lista válida.")

            if len(lista_dados) != tamanho_esperado:
                raise ValueError(f"Inconsistência: A coluna '{rotulo}' tem tamanho diferente.")

            if tamanho_esperado > 0:
                tipo_da_coluna = type(lista_dados[0])
                for elemento in lista_dados:
                    if type(elemento) is not tipo_da_coluna:
                        raise ValueError(f"Tipo misto na coluna '{rotulo}'.")
        
        
    def mean(self, column):
        if column not in self.dataset:
            return None
        
        dados = self.dataset[column]
        
        quantidade = len(dados)
        if quantidade == 0:
            return 0

        if not isinstance(dados[0], (int, float)):
            return None

        soma_total = 0
        for valor in dados:
            soma_total += valor
        
        if quantidade == 0:
            return 0
        
        mean = soma_total / quantidade
        return mean




    def median(self, column):
        if column not in self.dataset:
            return None
        
        dados = self.dataset[column]
        
        column_size = len(dados)
        if column_size == 0:
            return None

        if not isinstance(dados[0], (int, float)):
            return None 

        sorted_column = sorted(dados)
        middle_position = column_size // 2

        if column_size % 2 != 0:
            return sorted_column[middle_position]

        return (sorted_column[middle_position - 1] + sorted_column[middle_position]) / 2

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
        column = self.dataset[column]
        frequency = {}

        for value in column:
            if value in frequency:
                frequency[value] += 1
            else:
                frequency[value] = 1
                
        return frequency


    def relative_frequency(self, column):
        relative_frequency = self.absolute_frequency(column)
        total = 0

        for key in relative_frequency:
            total = total + int(relative_frequency[key])

        for key in relative_frequency:
            relative_frequency[key] = int(relative_frequency[key]) / total

        return relative_frequency


    def cumulative_frequency(self, column, frequency_method='absolute'):
        if frequency_method.lower().strip() not in ['absolute', 'relative']:
            return 'Frequência Inválida'
    
        item_anterior = 0
        
        if frequency_method == 'absolute':
            base_frequency = self.absolute_frequency(column)
        else:
            base_frequency = self.relative_frequency(column)

        base_frequency_sorted = ["baixa", "media", "alta"] if "baixa" in base_frequency and "media" in base_frequency else sorted(base_frequency.keys())

        cumulative_frequency = {}

        for key in base_frequency_sorted:
            if key in base_frequency:
                valor_atual = base_frequency[key] + item_anterior
                cumulative_frequency[key] = valor_atual
                item_anterior = valor_atual
        
        return cumulative_frequency


    def conditional_probability(self, column, value1, value2):
        column = self.dataset[column]
        conditional_probability = 0
        total = 0
        conditione = 0
        for i in range(0, len(column) - 1):
            if column[i] == value2:
                total += 1
                if column[i+1] == value1:
                    conditione += 1
        
        if total != 0:
            conditional_probability = conditione / total
        else:
            return 0

        return conditional_probability

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

        # Recebendo os valores do dataset
        valores = sorted(self.dataset[column])
        print(valores)
        tamanho_valores = len(valores)
        print(tamanho_valores)

        # Caso a quantidade de valores for igual a zero
        if tamanho_valores == 0:
            return {"Q1": 0, "Q2": 0, "Q3": 0}

        # Cálculo do Q2 (Mediana)
        mediana = tamanho_valores // 2
        if tamanho_valores % 2 == 0:
            q2 = (valores[mediana - 1] + valores[mediana]) / 2
            print(valores[mediana])
            print(mediana)
            print(q2)
            # O fatiamento começa do início até o meio
            primeira_metade = valores[:mediana]
            # O fatiamento começa do meio até o final
            segunda_metade  = valores[mediana:]
        else:
            q2 = valores[mediana]
            # Para n ímpar, a mediana (Q2) é excluída de ambas as metades
            primeira_metade = valores[:mediana]
            segunda_metade  = valores[mediana + 1:]

        # Cálculo do Q1 (Mediana da Metade Inferior)
        tamanho_inferior = len(primeira_metade)
        mediana_1 = tamanho_inferior // 2
        if tamanho_inferior % 2 == 0:
            q1 = (primeira_metade[mediana_1 - 1] + primeira_metade[mediana_1]) / 2
        else:
            q1 = (primeira_metade[mediana_1])

        # Cálculo do Q3 (Mediana da Metade Superior
        tamanho_superior = len(segunda_metade)
        mediana_2 = tamanho_superior // 2
        if tamanho_superior % 2 == 0:
            q3 = (segunda_metade [mediana_2 - 1] + segunda_metade [mediana_2]) / 2
        else:
            q3 = (segunda_metade [mediana_2])

        return {"Q1": q1, "Q2": q2, "Q3": q3}
    
     
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
            return { f"Se os valores forem iguais: ({menor_valor}, {maior_valor})": len(valores)}


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




