"""5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;"""


palavra = "Pedro Falcão"
palavra_invertida = ""

for caractere in palavra:
    palavra_invertida = caractere + palavra_invertida
print(palavra_invertida)

