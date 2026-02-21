#2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação).
#Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.

def eh_palindromo(texto):
    texto_limpo = ""
    
    for caractere in texto:
        if caractere.isalnum():
            texto_limpo += caractere.lower()
    
    return texto_limpo == texto_limpo[::-1]

frase = input("Digite uma palavra ou frase: ")

if eh_palindromo(frase):
    print("Sim")
else:
    print("Não")