print("-----------------------------------------------------------------------------------------------------------------------------------")

class Anime:
    def __init__(self, titulo, criador, ano_lancamento, codigo_interno, studio):
        self.__codigo_interno = codigo_interno  # Atributo privado
        self._criador = criador  # Atributo protegido
        self.titulo = titulo  # Atributo público
        self.ano_lancamento = ano_lancamento  # Atributo público
        self.__studio = studio  # Atributo privado

    def exibir_informacoes(self):
        return f"Título: {self.titulo}, Criador: {self._criador}, Ano de Lançamento: {self.ano_lancamento}, Studio: {self.__studio}"

    def exibir_codigo_interno(self):
        return f"Código Interno: {self.__codigo_interno}"


class AnimeStreaming(Anime):
    def __init__(self, titulo, criador, ano_lancamento, codigo_interno, studio, plataforma, numero_episodios, legendado):
        super().__init__(titulo, criador, ano_lancamento, codigo_interno, studio)
        self.plataforma = plataforma  # Atributo público
        self._numero_episodios = numero_episodios  # Atributo protegido
        self._legendado = legendado  # Atributo protegido

    def exibir_detalhes(self):
        return f"Título: {self.titulo}, Criador: {self._criador}, Ano de Lançamento: {self.ano_lancamento}, Studio: {self.__studio}, Plataforma: {self.plataforma}, Episódios: {self._numero_episodios}, Legendado: {self._legendado}"

    def verificar_legendado(self):
        return f"Legendado: {self._legendado}"


print("-----------------------------------------------------------------------------------------------------------------------------------")