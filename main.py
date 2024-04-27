def main():
    from pme import pme
    
    # Cria os versores correspondentes aos vetores.
    versor_i_omega = int(input("Digite a intensidade (número) do vetor omega na direção i: "))
    versor_j_omega = int(input("Digite a intensidade (número) do vetor omega na direção j: "))
    versor_k_omega = int(input("Digite a intensidade (número) do vetor omega na direção k: "))
    
    versor_i_dist = int(input("\nDigite a intensidade (número) do vetor dist na direção i: "))
    versor_j_dist = int(input("Digite a intensidade (número) do vetor dist na direção j: "))
    versor_k_dist = int(input("Digite a intensidade (número) do vetor dist na direção k: "))    
    
    versor_i_vq = int(input("\nDigite a intensidade (número) do vetor vq na direção i: "))
    versor_j_vq = int(input("Digite a intensidade (número) do vetor vq na direção j: "))
    versor_k_vq = int(input("Digite a intensidade (número) do vetor vq na direção k: "))
    #-------------------------------------------------------------------------------------------------------------------

    vetor_omega = pme.cria_vetor(versor_i_omega, versor_j_omega, versor_k_omega)
    dist = pme.cria_vetor(versor_i_dist, versor_j_dist, versor_k_dist)
    # vetor_vp = pme.cria_vetor(versor_i_vp, versor_j_vp, versor_k_vp)
    vetor_vq = pme.cria_vetor(versor_i_vq, versor_j_vq, versor_k_vq)
    #-------------------------------------------------------------------------------------------------------------------

    return pme.campo_velocidades_vp(vetor_omega, dist, vetor_vq)
main()