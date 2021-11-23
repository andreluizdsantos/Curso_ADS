#programa para substituir prefixo de e-mail para *, exemplo: teste@teste.com em *@teste.com
from re import sub
prov = ['gmail.com', 'hotmail.com', 'outlook.com', '@live.com', 'zap.com', 'yahoo.com',
'icloud.com', 'terra.com', '@bol.com', '@uol.com', '@ig.com', '@pop.com', 'brturbo.com',
'netvision.com', 'expresso.com', 'protonmail.com', 'zoho.com', 'gmx.com', 'fastmail.com', 
'inbox.com', 'lavabit.com', 'myspace.com', 'hotpotmail.com', 'yandex.com', 'tutanota.com', 
'lockbin.com', 'aol.com', 'qq.com']
end = ['@', '.', ',', '-', '_', '+', '*', '!', '%', 
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.co', '.ru']
valid = True
reg = False
i = 0
j = 0
with open("contatos.vcf", "r", encoding = 'utf8') as arquivo: #abre o arquivo, "r" read "leitura"
    contatos = arquivo.readlines() #guarda o conteudo do arquivo na variavel contatos

for linha in contatos: #caminha por todas as linhas
    l = sub(r'(\s)|(;)|(:)|(=)|(EMAIL)|(TYPE)|(INTERNET)|(OTHER)|(HOME)|(WORK)|(FN)', '', linha).lower()
    l = sub(r'(@htmail)|(@gmial)|(@gnail)|(sdvrecft.com)', '', l)
    # l recebe o conteudo de cada linha elimilnado espaços, alguns caracteres e informações desnecessárias
    if "@" in l:
        while i < len(end):
            if l.endswith(end[i]):
                valid = False
                print(f"Inválido: {l}")
                i = len(end)
            else:
                valid = True
            i = i+1

        if valid:
            while j < len(prov):
                if prov[j] in l:
                    resultado = l
                    print(resultado) #exibe a linha alterada
                    with open("resultado.txt", "a") as arquivo2: # abre o arquivo que receberá os dados,
                                            # "a" refere a append "adicionar" dados ao arquivo
                        arquivo2.write('\n' + resultado) #grava os dados no arquivo linha a linha
                    j = len(prov)
                    reg = True
                elif reg == False and j == (len(prov) - 1):
                    if '*@' in l:
                        resultado = l
                    else:
                        resultado = sub(r'(\w.*)@', '*@', l) #substitui o prefixo do email por *
                    reg = True
                    print(resultado) #exibe a linha alterada
                    with open("resultado.txt", "a") as arquivo2:# abre o arquivo que receberá os dados,
                                                            # "a" refere a append "adicionar" dados ao arquivo
                        arquivo2.write('\n' + resultado) #grava os dados no arquivo linha a linha
                j = j+1
        else:
            print(f"{l} Não é um e-mail válido!")
        reg = False
        j = 0
        i = 0
