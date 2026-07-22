# Questão 1
def transforma_base(questoes):
    base_transformada = {}
    i = 0
    while i < len(questoes):
        nivel = questoes[i]["nivel"]

        # If esse nível ainda não existe no dicionário,
        # criando uma lista vazia 
        if nivel not in base_transformada:
            base_transformada[nivel] = []

        # Colocar a questão na lista do seu nível
        base_transformada[nivel].append(questoes[i])
        i += 1
    return base_transformada

# Questão 2
def valida_questao(questao):
    erros = {}
    # Verificar se as quatro obrigatórias existem
    if "titulo" not in questao:
        erros["titulo"] = "nao_encontrado"
    if "nivel" not in questao:
        erros["nivel"] = "nao_encontrado"
    if "opcoes" not in questao:
        erros["opcoes"] = "nao_encontrado"
    if "correta" not in questao:
        erros["correta"] = "nao_encontrado"

    # Verificar se o dic principal tem ext 4 chaves
    if len(questao) != 4:
        erros["outro"] = "numero_chaves_invalido"
    # Só verifica o título caso a chave exista
    if "titulo" in questao:
        # strip() remove espaços, tabulações e quebras de linha
        if questao["titulo"].strip() == "":
            erros["titulo"] = "vazio"

    # Só verifica o nível caso a chave exista
    if "nivel" in questao:
        if questao["nivel"] != "facil" and questao["nivel"] != "medio" and questao["nivel"] != "dificil":
            erros["nivel"] = "valor_errado"

    # Só verifica as opções caso a chave exista
    if "opcoes" in questao:
        opcoes = questao["opcoes"]
        # Verificar se existem exatamente quatro opções
        if len(opcoes) != 4:
            erros["opcoes"] = "tamanho_invalido"
        else:
            # Como já sabemos que existem exatamente quatro chaves, verificar se A, B, C e D estão presentes
            if "A" not in opcoes or "B" not in opcoes or "C" not in opcoes or "D" not in opcoes:
                erros["opcoes"] = "chave_invalida_ou_nao_encontrada"
            else:
                # Guarda as opções que estiverem vazias
                opcoes_vazias = {}
                letras = ["A", "B", "C", "D"]
                i = 0
                while i < len(letras):
                    letra = letras[i]
                    if opcoes[letra].strip() == "":
                        opcoes_vazias[letra] = "vazia"
                    i += 1

                # Adiciona ao dicionário de erros se houver opção vazia
                if len(opcoes_vazias) > 0:
                    erros["opcoes"] = opcoes_vazias
    # Só verifica a resposta correta caso a chave exista
    if "correta" in questao:
        if questao["correta"] != "A" and questao["correta"] != "B" and questao["correta"] != "C" and questao["correta"] != "D":
            erros["correta"] = "valor_errado"

    return erros

