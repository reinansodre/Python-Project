# Reescreva a função leiaint(), incluindo agora a possibilidade da digitação de um número de tipo
# invalid, aproveite e crie uma função leiaFloat() com a mesma funcionalidade.

def leiaint():
    try:
        ni = int(input("Digite um número inteiro: "))
    except (ValueError, TypeError):
        return f"O valor digitado não é um número inteiro."
    else:
        return f"O valor inteiro digitado foi {ni}"

def leiafloat():
    try:
        nf = float(input("Digite um número real: "))
    except (ValueError, TypeError):
        return f"O valor digitado não é um número real."
    else:
        return f"O valor real digitado foi {nf}"

if __name__ == '__main__':
    x = leiaint()
    y = leiafloat()
    print(f"{x} \n{y}")
