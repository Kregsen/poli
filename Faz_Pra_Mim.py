import itertools

class pme:
    def __init__(self):
        return

    def teste_versor(versor):
        return versor in ["i","j","k","-i","-j","-k"]
    
    def teste_numero(numero):
        return (type(numero) == int) or (type(numero) == float)
    
    def prod_versor(mult):

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

    def poisson(omega, omega_v, dist, dist_v , numero, versor):
        if not pme.teste_numero(numero): return "'numero' não é número."
        if not pme.teste_versor(versor): return "'versor' não é versor."

        prod_vetorial = pme.comp_prod_vetorial(omega, omega_v, dist, dist_v)
        mult_versores = pme.soma_versor(versor + prod_vetorial[1])

        dir = mult_versores[0] if (mult_versores[1] == True) else ([versor, prod_vetorial[1]])
        num = numero + int(prod_vetorial[0]) if (mult_versores[1] == True) else ([numero, prod_vetorial[0]])

        return [num, dir]
    
    def formata_poisson(a):
        q = a
        if pme.teste_numero(a[0]):
            a[0] = str(a[0])
            b = "".join(a)
            return f"\nA velocidade por Poisson é: V(P) = {b}\n" 
        
        else:
            a = list(itertools.chain(a[0],a[1]))
            return f"\nA velocidade por Poisson é: V(P) = {a[0]}{a[2]} + {a[1]}{a[3]}\n" 

resultado = pme.poisson(1, "-k", 2, "-j", 0, "i")

resultado_formatado = pme.formata_poisson(resultado)

print(resultado_formatado)