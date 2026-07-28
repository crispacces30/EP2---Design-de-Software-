from funções import *
from base_questoes import questoes

VERDE = "\033[92m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
AZUL = "\033[94m"
ROXO = "\033[95m"
CIANO = "\033[96m"
NEGRITO = "\033[1m"
RESET = "\033[0m"

premios = [
    1000,
    5000,
    10000,
    30000,
    50000,
    100000,
    300000,
    500000,
    1000000
]

print(ROXO + NEGRITO + "========================================")
print("        BEM-VINDO AO FORTUNA DESSOFT")
print("========================================" + RESET)

jogar_novamente = "sim"

while jogar_novamente == "sim":
    nome = input(CIANO + "Digite o seu nome: " + RESET)

    print()
    print(ROXO + NEGRITO + "Olá, " + nome + "!" + RESET)
    print()
    print(ROXO + NEGRITO + "MANUAL DO JOGO" + RESET)
    print("- Responda usando A, B, C ou D.")
    print("- Você possui 3 pulos.")
    print("- Você possui 2 ajudas.")
    print("- Uma resposta errada elimina todo o seu prêmio.")
    print("- Após acertar, você pode parar e levar o prêmio.")
    print("- O prêmio máximo é de R$ 1.000.000.")
    print()

    erros_base = valida_questoes(questoes)
    base_valida = True

    for erros in erros_base:
        if len(erros) > 0:
            base_valida = False

    if base_valida == False:
        print(VERMELHO + NEGRITO + "A base de questões contém erros." + RESET)
        print(VERMELHO + str(erros_base) + RESET)

    else:
        base_transformada = transforma_base(questoes)
        questoes_sorteadas = []
        pulos = 3
        ajudas = 2
        indice_premio = 0
        premio_atual = 0
        perdeu = False
        parou = False

        while indice_premio < len(premios) and perdeu == False and parou == False:
            if indice_premio < 3:
                nivel = "facil"
            elif indice_premio < 6:
                nivel = "medio"
            else:
                nivel = "dificil"

            questao = sorteia_questao_inedita(
                base_transformada,
                nivel,
                questoes_sorteadas
            )

            usou_ajuda_nesta_questao = False
            questao_finalizada = False

            print()
            print(AZUL + NEGRITO + "Prêmio atual: R$ " + str(premio_atual) + RESET)
            print(AZUL + "Próximo prêmio: R$ " + str(premios[indice_premio]) + RESET)
            print(CIANO + "Pulos restantes: " + str(pulos) + RESET)
            print(CIANO + "Ajudas restantes: " + str(ajudas) + RESET)
            print(CIANO + "Nível da questão: " + nivel.upper() + RESET)
            print()
            print(questao_para_texto(questao, indice_premio + 1))
            print()

            while questao_finalizada == False:
                resposta = input(
                    CIANO + "Digite A, B, C, D, AJUDA ou PULA: " + RESET
                ).strip().upper()

                while resposta != "A" and resposta != "B" and resposta != "C" and resposta != "D" and resposta != "AJUDA" and resposta != "PULA":
                    print(VERMELHO + NEGRITO + "Opção inválida!" + RESET)
                    resposta = input(
                        CIANO + "Digite novamente A, B, C, D, AJUDA ou PULA: " + RESET
                    ).strip().upper()

                if resposta == "AJUDA":
                    if ajudas == 0:
                        print(AMARELO + NEGRITO + "Você não possui mais ajudas." + RESET)
                    elif usou_ajuda_nesta_questao == True:
                        print(AMARELO + "Você já utilizou ajuda nesta questão." + RESET)
                    else:
                        print()
                        print(AMARELO + NEGRITO + gera_ajuda(questao) + RESET)
                        print()
                        ajudas -= 1
                        usou_ajuda_nesta_questao = True
                        print(CIANO + "Ajudas restantes: " + str(ajudas) + RESET)

                elif resposta == "PULA":
                    if pulos == 0:
                        print(AMARELO + NEGRITO + "Você não possui mais pulos." + RESET)
                    else:
                        pulos -= 1
                        print()
                        print(AMARELO + NEGRITO + "Questão pulada!" + RESET)
                        print(CIANO + "Pulos restantes: " + str(pulos) + RESET)
                        questao_finalizada = True

                elif resposta == "A" or resposta == "B" or resposta == "C" or resposta == "D":
                    if resposta == questao["correta"]:
                        premio_atual = premios[indice_premio]

                        print()
                        print(VERDE + NEGRITO + "Resposta correta!" + RESET)
                        print(VERDE + "Seu prêmio agora é R$ " + str(premio_atual) + RESET)

                        indice_premio += 1
                        questao_finalizada = True

                        if premio_atual == 1000000:
                            print()
                            print(VERDE + NEGRITO + "PARABÉNS!" + RESET)
                            print(VERDE + NEGRITO + "Você ganhou R$ 1.000.000!" + RESET)
                        else:
                            continuar = input(
                                CIANO + "Deseja PARAR ou CONTINUAR? " + RESET
                            ).strip().upper()

                            while continuar != "PARAR" and continuar != "CONTINUAR":
                                print(VERMELHO + "Opção inválida." + RESET)
                                continuar = input(
                                    CIANO + "Digite PARAR ou CONTINUAR: " + RESET
                                ).strip().upper()

                            if continuar == "PARAR":
                                parou = True

                    else:
                        print()
                        print(VERMELHO + NEGRITO + "Resposta errada!" + RESET)
                        print(
                            VERMELHO
                            + "A resposta correta era "
                            + questao["correta"]
                            + "."
                            + RESET
                        )
                        perdeu = True
                        premio_atual = 0
                        questao_finalizada = True

        print()
        print(ROXO + NEGRITO + "========================================")

        if perdeu == True:
            print(VERMELHO + NEGRITO + nome + ", você perdeu o jogo." + RESET)
            print(VERMELHO + "Prêmio final: R$ 0" + RESET)

        elif parou == True:
            print(AMARELO + NEGRITO + nome + ", você decidiu parar." + RESET)
            print(VERDE + "Prêmio final: R$ " + str(premio_atual) + RESET)

        elif premio_atual == 1000000:
            print(
                VERDE
                + NEGRITO
                + nome
                + ", você venceu o Fortuna DesSoft!"
                + RESET
            )
            print(VERDE + NEGRITO + "Prêmio final: R$ 1.000.000" + RESET)

        print(ROXO + NEGRITO + "========================================" + RESET)
        print()

    jogar_novamente = input(
        CIANO + "Deseja jogar novamente? Digite SIM ou NAO: " + RESET
    ).strip().lower()

    while jogar_novamente != "sim" and jogar_novamente != "nao":
        print(VERMELHO + "Opção inválida." + RESET)
        jogar_novamente = input(
            CIANO + "Digite SIM ou NAO: " + RESET
        ).strip().lower()

print()
print(ROXO + NEGRITO + "Obrigado por jogar!" + RESET)