import csv
import sys
from dende_statistics import Statistics

def carregar_spotify(caminho):
    schema = {
        'track_duration_min': float,
        'track_popularity': int,
        'artist_followers': int,
        'artist_popularity': int
    }
    cols = list(schema.keys()) + ['explicit', 'artist_name', 'album_type']
    corpus = {c: [] for c in cols}

    try:
        with open(caminho, mode='r', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                for col in cols:
                    val = linha.get(col, "")
                    tipo = schema.get(col, str)
                    try:
                        corpus[col].append(tipo(val))
                    except (ValueError, TypeError):
                        corpus[col].append(0 if tipo == int else (0.0 if tipo == float else "N/A"))
        return corpus
    except FileNotFoundError:
        print("Erro: Arquivo CSV não encontrado.")
        return None

def dashboard(stats):
    print("="*45)
    print("         DADOS ESTATÍSTICOS BRUTOS")
    print("="*45)
    
    print("\n[ Duração da Faixa (Minutos) ]")
    print(f"Média:   {stats.mean('track_duration_min'):.2f}")
    print(f"Mediana: {stats.median('track_duration_min'):.2f}")

    print("\n[ Popularidade da Faixa (0 a 100) ]")
    q_pop = stats.quartiles('track_popularity')
    print(f"Q1: {q_pop['Q1']}")
    print(f"Q2: {q_pop['Q2']} (Mediana)")
    print(f"Q3: {q_pop['Q3']}")

    print("\n[ Seguidores do Artista ]")
    print(f"Média:         {stats.mean('artist_followers'):.2f}")
    print(f"Desvio Padrão: {stats.stdev('artist_followers'):.2f}")

    print("\n[ Covariância ]")
    cov_val = stats.covariance('artist_popularity', 'track_popularity')
    print(f"Fama do Artista x Sucesso da Música: {cov_val:.2f}")

    print("\n[ Nome do Artista ]")
    moda_artista = stats.mode('artist_name')[0]
    freq_abs_artista = stats.absolute_frequency('artist_name').get(moda_artista, 0)
    print(f"Moda: {moda_artista}")
    print(f"Frequência Absoluta (da Moda): {freq_abs_artista}")

    print("\n[ Tipo de Álbum ]")
    moda_album = stats.mode('album_type')[0]
    rel_freq_album = stats.relative_frequency('album_type')
    print(f"Moda: {moda_album}")
    print(f"Freq. Relativa ('album'): {rel_freq_album.get('album', 0):.4f} ({rel_freq_album.get('album', 0)*100:.2f}%)")

    print("\n[ Conteúdo Explícito (True/False) ]")
    rel_freq_explicit = stats.relative_frequency('explicit')
    for chave, valor in rel_freq_explicit.items():
        print(f"Freq. Relativa ('{chave}'): {valor:.4f} ({valor*100:.2f}%)")
    
    print("\n" + "="*45)

if __name__ == "__main__":
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')

    dados = carregar_spotify('spotify_data_clean.csv')
    if dados:
        analisador = Statistics(dados)
        dashboard(analisador)
