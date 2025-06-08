def verificar_palindromo(texto):
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

# Exemplos de uso:
print(verificar_palindromo("Ame a ema"))           # Sim
print(verificar_palindromo("Python"))              # Não
print(verificar_palindromo("A sogra má e amargosa"))  # Sim
