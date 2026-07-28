import random 
# Questão 1
def transforma_base(questoes):
    base_transformada = {}
    i = 0
    while i < len(questoes):
        nivel = questoes[i]["nivel"]
        if nivel not in base_transformada:
            base_transformada[nivel] = []
        base_transformada[nivel].append(questoes[i])
        i += 1
    return base_transformada

# Questão 2
def valida_questao(questao):
    erros = {}
    if "titulo" not in questao:
        erros["titulo"] = "nao_encontrado"
    if "nivel" not in questao:
        erros["nivel"] = "nao_encontrado"
    if "opcoes" not in questao:
        erros["opcoes"] = "nao_encontrado"
    if "correta" not in questao:
        erros["correta"] = "nao_encontrado"
    if len(questao) != 4:
        erros["outro"] = "numero_chaves_invalido"
    if "titulo" in questao:
        if questao["titulo"].strip() == "":
            erros["titulo"] = "vazio"
    if "nivel" in questao:
        if questao["nivel"] != "facil" and questao["nivel"] != "medio" and questao["nivel"] != "dificil":
            erros["nivel"] = "valor_errado"
    if "opcoes" in questao:
        opcoes = questao["opcoes"]
        if len(opcoes) != 4:
            erros["opcoes"] = "tamanho_invalido"
        else:
            if "A" not in opcoes or "B" not in opcoes or "C" not in opcoes or "D" not in opcoes:
                erros["opcoes"] = "chave_invalida_ou_nao_encontrada"
            else:
                opcoes_vazias = {}
                letras = ["A", "B", "C", "D"]
                i = 0
                while i < len(letras):
                    letra = letras[i]
                    if opcoes[letra].strip() == "":
                        opcoes_vazias[letra] = "vazia"
                    i += 1
                if len(opcoes_vazias) > 0:
                    erros["opcoes"] = opcoes_vazias
    if "correta" in questao:
        if questao["correta"] != "A" and questao["correta"] != "B" and questao["correta"] != "C" and questao["correta"] != "D":
            erros["correta"] = "valor_errado"
            
    return erros

# Questão 3
def valida_questoes(questoes):
    resultado = []
    for questao in questoes:
        erros = valida_questao(questao)
        resultado.append(erros)

    return resultado

# Questão 4
def sorteia_questao(questoes, nivel):
    lista_questoes = questoes[nivel]
    questao_sorteada = random.choice(lista_questoes)

    return questao_sorteada

# Questão 5
def sorteia_questao_inedita(questoes, nivel, questoes_sorteadas):
    questao = sorteia_questao(questoes, nivel)
    while questao in questoes_sorteadas:
        questao = sorteia_questao(questoes, nivel)
    questoes_sorteadas.append(questao)

    return questao

# Questão 6
def questao_para_texto(questao, id):
    text = "----------------------------------------\n"
    text += "QUESTAO " + str(id) + "\n\n"
    text += questao["titulo"] + "\n\n"
    text += "RESPOSTAS:\n"

    letras = ["A", "B", "C", "D"]
    i = 0

    while i < len(letras):
        letra = letras[i]
        text += letra + ": " + questao["opcoes"][letra]
        if i < len(letras) - 1:
            text += "\n"
        i += 1

    return text

# Questão 7
def gera_ajuda(questao):
    respostas_erradas = []
    correta = questao["correta"]
    opcoes = questao["opcoes"]
    for letra in opcoes:
        if letra != correta:
            respostas_erradas.append(opcoes[letra])
    quantidade = random.randint(1, 2)
    sorteadas = random.sample(respostas_erradas, quantidade)

    texto = "DICA:\n"
    texto += "Opções certamente erradas: "
    texto += " | ".join(sorteadas)
    return texto
