"""
DISCLAIMER: Esse código não resolve questões de Mecânica-A algebricamente!!!

DISCLAIMER: Esse código não resolve questões de Mecânica-A algebricamente!!!

DISCLAIMER: Esse código não resolve questões de Mecânica-A algebricamente!!!
"""

#-----------------------------------------------------------------------------------------------------------------------
# Criação e inicialização da classe pme.
from functools import reduce

class pme:
    def __init__(self):
        return

    #-------------------------------------------------------------------------------------------------------------------
    # Funções relacionadas ao numero associado ao versor do vetor.

    def teste_versor(versor):
        # Testa se a entrada é um versor válido. Não aceita letras em maiúsculo.

        return versor in ["i","j","k","-i","-j","-k"]
    
    def teste_numero(item):
        # Testa se o valor de entrada é um item do tipo float ou int.

        return (type(item) == int) or (type(item) == float)

    def tira_zero(b): return True if (b[1] != 'zero') and (b[0] != 0) else False

    def soma(a, b): return a + b

    #-------------------------------------------------------------------------------------------------------------------
    # Funções relacionadas aos versores do vetor.

    def soma_versores_iguais(lista):
        array_i = list(filter(lambda item: True if item[1] == "i" else False, lista))
        array_j = list(filter(lambda item: True if item[1] == "j" else False, lista))
        array_k = list(filter(lambda item: True if item[1] == "k" else False, lista))

        print("\nSepara em arrays todos versores 'i', 'j' e 'k'.")
        print(array_i)
        print(array_j)
        print(array_k)

        array_i_soma = reduce(lambda a, b: a + b, map(lambda a: a[0], array_i))
        array_j_soma = reduce(lambda a, b: a + b, map(lambda a: a[0], array_j))
        array_k_soma = reduce(lambda a, b: a + b, map(lambda a: a[0], array_k))

        print("\nSoma os números associados aos 'i', 'j' e 'k' dos arrays.")
        print(array_i_soma)
        print(array_j_soma)
        print(array_k_soma)

        return (array_i_soma, array_j_soma, array_k_soma)

    def norm_versor(vetor): 
        if vetor[1][0] == "-":
            vetor[0] = -vetor[0]
            vetor[1] = vetor[1:]

        return vetor

    def prod_versor(mult):
        # Obtém os resultados das multiplicações entre dois versores.

        match mult:
            case "ii": return "zero"
            case "jj": return "zero"
            case "kk": return "zero"

            case "-ii": return "zero"
            case "-jj": return "zero"
            case "-kk": return "zero"

            case "i-i": return "zero"
            case "j-j": return "zero"
            case "k-k": return "zero"

            case "-i-i": return "zero"
            case "-j-j": return "zero"
            case "-k-k": return "zero"

            case "ij": return "k"
            case "ji": return "-k"
            case "ki": return "j"
            case "ik": return "-j"
            case "jk": return "i"
            case "kj": return "-i"

            case "-i-j": return "k"
            case "-j-i": return "-k"
            case "-k-i": return "j"
            case "-i-k": return "-j"
            case "-j-k": return "i"
            case "-k-j": return "-i"

            case "-ij": return "-k"
            case "-ji": return "k"
            case "-ki": return "-j"
            case "-ik": return "j"
            case "-jk": return "-i"
            case "-kj": return "i"

            case "i-j": return "-k"
            case "j-i": return "k"
            case "k-i": return "-j"
            case "i-k": return "j"
            case "j-k": return "-i"
            case "k-j": return "i"

    def soma_versor(soma):
        # Obtém o resultado da soma entre dois versores.

        match soma:
            case "ii": return ["i", True]
            case "jj": return ["j", True]
            case "kk": return ["k", True]

            case "-i-i": return ["i", True]
            case "-j-j": return ["j", True]
            case "-k-k": return ["k", True]
            
            case "-ii": return ["-i", True]
            case "-jj": return ["-j", True]
            case "-kk": return ["-k", True]

            case "i-i": return ["-i", True]
            case "j-j": return ["-j", True]
            case "k-k": return ["-k", True]

            case _: return [soma, False]

    #-------------------------------------------------------------------------------------------------------------------
    # Funções relacionadas ao vetor dado.

    def cria_vetor(a, b, c):
    # Cria um vetor, na formatação correta (em i, j e k), a partir de dados int.

        versores = [a, b, c]
        letras = ["i", "j", "k"]
        vetor = []

        for index, item in enumerate(versores): # Essa função cria uma matriz de arrays, com indices e itens.
            if item != 0:
                vetor.append([item, letras[index]]) # Pega o indice para somar com a letra de mesmo indice.

        return vetor
    #-------------------------------------------------------------------------------------------------------------------
    # Funções que calculam as componentes de poisson, e faz o cálculo de poisson.

    def abc_vp(omega, dist, vetor_vq):
        omega = [[2, 'i'], [2, 'i'], [2, 'i']]
        dist = [[2, 'i'], [2, 'i'], [2, 'i']]
        vetor_vq = [[2, 'i'], [2, 'i'], [2, 'i']]

        return

    def poisson_vp(omega, omega_vrs, dist, dist_vrs, vq, vq_vrs):
        # Resolve poisson para a velocidade do polo "normal" (vp):
            # vp = vq + pme.campo_velocidades(omega, omega_vrs, dist, dist_vrs)

        if not pme.teste_numero(vq): return "'vq' não é número."
        if not pme.teste_versor(vq_vrs): return "'vq_vrs' não é versor."

        #pme.not_zero(numero): (True if numero != "0" else False)

        prod_vetorial = pme.campo_velocidades(omega, omega_vrs, dist, dist_vrs)
        mult_versores = pme.soma_versor(vq_vrs + prod_vetorial[1])

        dir = mult_versores[0] if (mult_versores[1] == True) else ([vq_vrs, prod_vetorial[1]])
        num = vq + int(prod_vetorial[0]) if (mult_versores[1] == True) else ([vq, prod_vetorial[0]])

        return [num, dir]
    
    def poisson_vq(omega, omega_vrs, dist, dist_vrs, vp, vp_vrs):
        # Resolve poisson para a velocidade do outro polo (vq):
            # vq = vp - pme.campo_velocidades(omega, omega_vrs, dist, dist_vrs)

        if not pme.teste_numero(vp): return "'vp' não é número."
        if not pme.teste_versor(vp_vrs): return "'vp_vrs' não é versor."

        prod_vetorial = pme.campo_velocidades(omega, omega_vrs, dist, dist_vrs)
        mult_versores = pme.soma_versor(vp_vrs + prod_vetorial[1])

        dir = mult_versores[0] if (mult_versores[1] == True) else ([vp_vrs, prod_vetorial[1]])
        num = vp - int(prod_vetorial[0]) if (mult_versores[1] == True) else ([vp, prod_vetorial[0]])

        return [num, dir]
    
    def poisson_omega(vp, vp_vrs, vq, vq_vrs, dist, dist_vrs):
        # Resolve poisson para a componente da velocidade angular (omega):
            # pme.campo_velocidades(omega, omega_vrs, dist, dist_vrs) = vp - vq
            # (omega)/(dist) = (vp - vq)/(dist)

        if not pme.teste_numero(vq): return "'vq' não é número."
        if not pme.teste_versor(vq_vrs): return "'vq_vrs' não é versor."

        if not pme.teste_numero(vp): return "'vp' não é número."
        if not pme.teste_versor(vp_vrs): return "'vp_vrs' não é versor."

        prod_vetorial = pme.campo_velocidades(vp, vp_vrs, dist, dist_vrs)
        mult_versores = pme.soma_versor(vq_vrs + prod_vetorial[1])

        dir = mult_versores[0] if (mult_versores[1] == True) else ([vq_vrs, prod_vetorial[1]])
        num = vp - int(prod_vetorial[0]) if (mult_versores[1] == True) else ([vq, prod_vetorial[0]])

        return [num, dir]
    
    def campo_velocidades_vp(omega, dist, vq):
        # Resolve o produto vetorial entre a velocidade angular e a distância na fórmula de poisson.

        for vetor in omega:
            if not pme.teste_numero(vetor[0]): return "'omega_vetor[0]' não é número."
            if not pme.teste_versor(vetor[1]): return "'omega_vetor[1]' não é número."

        for vetor in dist:
            if not pme.teste_numero(vetor[0]): return "'dist_vetor[0]' não é número."
            if not pme.teste_versor(vetor[1]): return "'dist_vetor[1]' não é número."
        
        for vetor in vq:
            if not pme.teste_numero(vetor[0]): return "'vq_vetor[0]' não é número."
            if not pme.teste_versor(vetor[1]): return "'vq_vetor[1]' não é número."

        grupo = []

        for vo in omega:
            for vd in dist:
                grupo.append([vo[0] * vd[0], pme.prod_versor(vo[1] + vd[1])])

        print("\nLista com o resultado do produto vetorial.")
        print(grupo)

        grupo_sem_zero = list(filter(pme.tira_zero, grupo))
        
        print("\nElimina os termos nulos da lista grupo.")
        print(grupo_sem_zero)
        
        grupo_normalizado = list(map(pme.norm_versor, grupo_sem_zero))

        print("\nAltera os sinais '-' do versor para o número associado.")
        print(grupo_normalizado)

        grupo_final = pme.soma_versores_iguais(grupo_normalizado)

        print("\nJunta todos arrays de versores em uma única lista.")
        print(grupo_final)

        vp = []

        for i, valor in enumerate(grupo_final):
            vp_numero = valor + vq[i][0]
            vp.append(str(vp_numero)+vq[i][1])
        
        print(f"""\nSoma os valores dos versores iguais entre a lista grupo_final e o vetor vq no vetor vp.
              \nO valor da velocidade no polo p é:\nV(P) = {vp}""")

    #-------------------------------------------------------------------------------------------------------------------
    # Funções associadas à formatação do retorno.

    def formata_poisson_vp_e_vq(poi_res_vp, poi_res_vq):
        # Formata o resultado obtido pela função poisson_vp(omega, omega_vrs, dist, dist_vrs, vq, vq_vrs), e também
        # o da função poisson_vq(omega, omega_vrs, dist, dist_vrs, vp, vp_vrs).
        
        if pme.teste_numero(poi_res_vp[0]) and pme.teste_numero(poi_res_vq[0]):
            
            poi_res_vp[0] = str(poi_res_vp[0])
            poi_res_vq[0] = str(poi_res_vq[0])

            poi_f1 = "".join(poi_res_vp)
            poi_f2 = "".join(poi_res_vq)
            
            # Os () permitem escrever em mais linhas. Além disso, cada linha corresponde a uma das velocidades.
            return (f"""\nA velocidade nos dois polos é:
            - Poisson a partir de V(Q) e de omega: V(P) = {poi_f1}
            
            - Poisson a partir de V(P) e de omega: V(Q) = {poi_f2}\n""")
        
        elif not pme.teste_numero(poi_res_vp[0]) and not pme.teste_numero(poi_res_vq[0]):

            poi_f3 = poi_res_vp[0] + poi_res_vp[1]
            poi_f4 = poi_res_vq[0] + poi_res_vq[1]
            
            return (f"""\nA velocidade nos dois polos é:
            - Poisson a partir de V(Q) e de omega: V(P) = {poi_f3[0]}{poi_f3[2]} + {poi_f3[1]}{poi_f3[3]}
            
            - Poisson a partir de V(P) e de omega: V(Q) = {poi_f4[0]}{poi_f4[2]} - {poi_f4[1]}{poi_f4[3]}\n""")
