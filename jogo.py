from funções import *
from base_questoes import questoes


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


print("========================================")
print("        BEM-VINDO AO FORTUNA DESSOFT")
print("========================================")

jogar_novamente = "sim"

while jogar_novamente == "sim":

    nome = input("Digite o seu nome: ")

    print()
    print("Olá, " + nome + "!")
    print()
    print("MANUAL DO JOGO")
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
        print("A base de questões contém erros.")
        print(erros_base)

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

            while questao_finalizada == False:

                print()
                print("Prêmio atual: R$ " + str(premio_atual))
                print("Próximo prêmio: R$ " + str(premios[indice_premio]))
                print("Pulos restantes: " + str(pulos))
                print("Ajudas restantes: " + str(ajudas))
                print()

                print(questao_para_texto(questao, indice_premio + 1))
                print()

                resposta = input(
                    "Digite A, B, C, D, AJUDA ou PULA: "
                ).strip().upper()

                if resposta == "AJUDA":

                    if ajudas == 0:
                        print("Você não possui mais ajudas.")

                    elif usou_ajuda_nesta_questao == True:
                        print("Você já utilizou ajuda nesta questão.")

                    else:
                        print()
                        print(gera_ajuda(questao))
                        ajudas -= 1
                        usou_ajuda_nesta_questao = True

                elif resposta == "PULA":

                    if pulos == 0:
                        print("Você não possui mais pulos.")

                    else:
                        pulos -= 1
                        questao_finalizada = True

                elif resposta == "A" or resposta == "B" or resposta == "C" or resposta == "D":

                    if resposta == questao["correta"]:
                        premio_atual = premios[indice_premio]

                        print()
                        print("Resposta correta!")
                        print("Seu prêmio agora é R$ " + str(premio_atual))

                        indice_premio += 1
                        questao_finalizada = True

                        if premio_atual == 1000000:
                            print()
                            print("PARABÉNS!")
                            print("Você ganhou R$ 1.000.000!")

                        else:
                            continuar = input(
                                "Deseja PARAR ou CONTINUAR? "
                            ).strip().upper()

                            while continuar != "PARAR" and continuar != "CONTINUAR":
                                print("Opção inválida.")
                                continuar = input(
                                    "Digite PARAR ou CONTINUAR: "
                                ).strip().upper()

                            if continuar == "PARAR":
                                parou = True

                    else:
                        print()
                        print("Resposta errada!")
                        print("A resposta correta era " + questao["correta"] + ".")
                        perdeu = True
                        premio_atual = 0
                        questao_finalizada = True

                else:
                    print()
                    print("Opção inválida.")
                    print("Digite A, B, C, D, AJUDA ou PULA.")

        print()
        print("========================================")

        if perdeu == True:
            print(nome + ", você perdeu o jogo.")
            print("Prêmio final: R$ 0")

        elif parou == True:
            print(nome + ", você decidiu parar.")
            print("Prêmio final: R$ " + str(premio_atual))

        elif premio_atual == 1000000:
            print(nome + ", você venceu o Fortuna DesSoft!")
            print("Prêmio final: R$ 1.000.000")

        print("========================================")
        print()

    jogar_novamente = input(
        "Deseja jogar novamente? Digite SIM ou NAO: "
    ).strip().lower()

    while jogar_novamente != "sim" and jogar_novamente != "nao":
        print("Opção inválida.")
        jogar_novamente = input(
            "Digite SIM ou NAO: "
        ).strip().lower()

print()
print("Obrigado por jogar!")