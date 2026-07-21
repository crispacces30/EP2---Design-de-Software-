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
