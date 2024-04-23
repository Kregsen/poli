"""
DISCLAIMER: Esse código não resolve questões de MecânicaA algebricamente!!!
"""
"""
DISCLAIMER: Esse código não resolve questões de MecânicaA algebricamente!!!
"""
"""
DISCLAIMER: Esse código não resolve questões de MecânicaA algebricamente!!!
"""

class pme:
    def __init__(self):
        return

    def teste_versor(versor):
        # Testa se a entrada é um versor válido. Não aceita letras em maiúsculo.

        return versor in ["i","j","k","-i","-j","-k"]
    
    def teste_numero(numero):
        # Testa se o valor de entrada é um numero do tipo float ou int.

        return (type(numero) == int) or (type(numero) == float)
    
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

            case "-i-i": return ["-i", True]
            case "-j-j": return ["-j", True]
            case "-k-k": return ["-k", True]
            
            case "-ii": return ["-i", True]
            case "-jj": return ["-j", True]
            case "-kk": return ["-k", True]

            case "i-i": return ["-i", True]
            case "j-j": return ["-j", True]
            case "k-k": return ["-k", True]

            case _: return [soma, False]
    
    def comp_prod_vetorial(omega, omega_v, dist, dist_v):
        # Resolve o produto vetorial entre a velocidade angular e a distância na fórmula de poisson.

        if not pme.teste_numero(omega): return "'omega' não é número."
        if not pme.teste_numero(dist): return "'dist' não é número."
        
        if omega < 0: return "'omega' não pode ser negativo."
        if dist <= 0: return "'dist' não pode ser negativo nem zero."

        if not pme.teste_versor(omega_v): return "'omega_v' não é versor."
        if not pme.teste_versor(dist_v): return "'dist_v' não é versor."

        comp_int = omega * dist 
        comp_str = pme.prod_versor(omega_v + dist_v)
       
        if comp_str == "zero": return [0, "zero"]
        else: return [comp_int, comp_str]

    def poisson_vp(omega, omega_vrs, dist, dist_vrs, vq, vq_vrs):
        # Resolve poisson para a velocidade do polo "normal" (vp):
            # vp = vq + pme.comp_prod_vetorial(omega, omega_vrs, dist, dist_vrs)

        if not pme.teste_numero(vq): return "'vq' não é número."
        if not pme.teste_versor(vq_vrs): return "'vq_vrs' não é versor."

        prod_vetorial = pme.comp_prod_vetorial(omega, omega_vrs, dist, dist_vrs)
        mult_versores = pme.soma_versor(vq_vrs + prod_vetorial[1])

        dir = mult_versores[0] if (mult_versores[1] == True) else ([vq_vrs, prod_vetorial[1]])
        num = vq + int(prod_vetorial[0]) if (mult_versores[1] == True) else ([vq, prod_vetorial[0]])

        return [num, dir]
    
    def poisson_vq(omega, omega_vrs, dist, dist_vrs, vp, vp_vrs):
        # Resolve poisson para a velocidade do outro polo (vq):
            # vq = vp - pme.comp_prod_vetorial(omega, omega_vrs, dist, dist_vrs)

        if not pme.teste_numero(vp): return "'vp' não é número."
        if not pme.teste_versor(vp_vrs): return "'vp_vrs' não é versor."

        prod_vetorial = pme.comp_prod_vetorial(omega, omega_vrs, dist, dist_vrs)
        mult_versores = pme.soma_versor(vp_vrs + prod_vetorial[1])

        dir = mult_versores[0] if (mult_versores[1] == True) else ([vp_vrs, prod_vetorial[1]])
        num = vp - int(prod_vetorial[0]) if (mult_versores[1] == True) else ([vp, prod_vetorial[0]])

        return [num, dir]
    
    def poisson_omega(vp, vp_vrs, vq, vq_vrs, dist, dist_vrs):
        # Resolve poisson para a componente da velocidade angular (omega):
            # pme.comp_prod_vetorial(omega, omega_vrs, dist, dist_vrs) = vp - vq
            # (omega)/(dist) = (vp - vq)/(dist)

        if not pme.teste_numero(vq): return "'vq' não é número."
        if not pme.teste_versor(vq_vrs): return "'vq_vrs' não é versor."

        if not pme.teste_numero(vp): return "'vp' não é número."
        if not pme.teste_versor(vp_vrs): return "'vp_vrs' não é versor."

        prod_vetorial = pme.comp_prod_vetorial(vp, vp_vrs, dist, dist_vrs)
        mult_versores = pme.soma_versor(vq_vrs + prod_vetorial[1])

        dir = mult_versores[0] if (mult_versores[1] == True) else ([vq_vrs, prod_vetorial[1]])
        num = vp - int(prod_vetorial[0]) if (mult_versores[1] == True) else ([vq, prod_vetorial[0]])

        return [num, dir]

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
