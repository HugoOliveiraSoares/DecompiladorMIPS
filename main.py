from Tabelas import Funct, Registradores


instrucao = input("Digite uma instrução:\n")

def converterb_d(n):
    decimal = 0
    n = str(n)
    n = n[::-1]
    tam = len(n)
    for i in range(tam):
        if n[i] == "1":
            decimal = decimal + 2**i
    return decimal



if instrucao.startswith("000000"):
    rs = instrucao[6:11]
    rt = instrucao[11:16]
    rd = instrucao[16:21]
    funct = instrucao[26:]
    print(rs)
    print(rt)
    print(rd)
    print(funct)
    comando = '{} ${}, ${}, ${} '
    print(comando.format(Funct(funct), Registradores(rd), Registradores(rs), Registradores(rt)))

else:
    opcode = instrucao[:6]
    rs = instrucao[6:11]
    rt = instrucao[11:16]
    offset = converterb_d(instrucao[16:])
    print(opcode)
    print(rs)
    print(rt)
    print(offset)
    comando = '{} ${}, {}(${}) '
    print(comando.format(Funct(opcode), Registradores(rt), offset, Registradores(rs)))
