from animes import *

# Exemplo de uso da classe pai
anime = Anime("Naruto", "Masashi Kishimoto", 2002, "123-456-789", "Studio Pierrot")
print(anime.exibir_informacoes())
print(anime.exibir_codigo_interno())

# Exemplo de uso da classe herdeira
anime_streaming = AnimeStreaming("Attack on Titan", "Hajime Isayama", 2013, "987-654-321", "Wit Studio", "Crunchyroll", 75, True)
print(anime_streaming.exibir_detalhes())
print(anime_streaming.verificar_legendado())