# https://git-scm.com/book/pt-br/v1/Primeiros-passos-No%C3%A7%C3%B5es-B%C3%A1sicas-de-Git
# Este é um progama para codificar em CN (Códogo Numerico)

alfabeto = {'!':'!','?':'?','.':'.',',':',',':':':',';':';','(':'(',')':')','a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'*10*','k':'*11*','l':'*12*','m':'*13*','n':'*14*','o':'*15*','p':'*16*','q':'*17*','r':'*18*','s':'*19*','t':'*20*','u':'*21*','v':'*22*','w':'*23*','y':'*25*','z':'*26*','x':'*27*','ç':'*28*','ã':'*30*'}

for chave,valor in alfabeto.items():

    print('valor: '+str(valor))


print('Digite a frase que quer  codificar sem ascentos ou caracteres especiais (@,#,$,%,\",\',\):')
entrada = input().lower().strip()
print(entrada)








    
