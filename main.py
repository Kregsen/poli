def main():
    from pme import pme

    # poisson_para = input("Digite 1 para encontrar V(P), 2 para encontrar V(Q) ou 3 para encontrar omega: ")

    # dist_nr = int(input("Digite a intensidade do vetores distância: "))
    # dist_vers = int(input("Digite o versor do vetor distância: "))

    # vq_nr = int(input("Digite a intensidade do vetor V(Q) (dado no enunciado do exercício): "))
    # vq_vers = int(input("Digite o versor do vetor V(Q) (dado no enunciado do exercício): "))

    # vp_nr = int(input("Digite a intensidade do vetor V(P) (dado no enunciado do exercício): "))
    # vp_vers = int(input("Digite o versor do vetor V(P) (dado no enunciado do exercício): "))

    # omega_nr = int(input("Digite a intensidade dos vetor omega (dado no enunciado do exercício): "))
    # omega_vers = int(input("Digite o versor do vetor omega (dado no enunciado do exercício): "))

    # print("\nEscolha o programa que vai rodar: \n")
    # print("1: Poisson em V(P).")
    # print("2: Poisson em V(Q).")
    # print("3: Poisson em omega.")
    # print("\n")

    # Encontra os valores das velocidades no polo q e no polo p por poisson.
    resultado_vp = pme.poisson_vp(2, "-i", 6, "k", 12, "-k")
    resultado_vq = pme.poisson_vq(2, "-i", 6, "k", 12, "-k")

    resultado_formatado_vp = pme.formata_poisson(resultado_vp)
    resultado_formatado_vq = pme.formata_poisson(resultado_vq)

    print("A velocidade no polo p, por poisson, é:", resultado_formatado_vp)
    print("A velocidade no polo q, por poisson, é:", resultado_formatado_vq)

    