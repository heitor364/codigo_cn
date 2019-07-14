# https://git-scm.com/book/pt-br/v1/Primeiros-passos-No%C3%A7%C3%B5es-B%C3%A1sicas-de-Git
# Este é um progama para codificar em CN (Códogo Numerico)

alfabeto = {'\\n':'\\n','*':'*','-':'-','+':'+',' ':'=','!':'!','?':'?','.':'.',',':',',':':':',';':';','(':'(',')':')','a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'*10*','k':'*11*','l':'*12*','m':'*13*','n':'*14*','o':'*15*','p':'*16*','q':'*17*','r':'*18*','s':'*19*','t':'*20*','u':'*21*','v':'*22*','w':'*23*','y':'*25*','z':'*26*','x':'*27*','ç':'*28*','ã':'*30*','é':'*31*','ê':'*32*','í':'*33*','â':'*34*','á':'*35*','õ':'*36*','ó':'*37*','ú':'*38*','ù':'*39*' }

codigo_pronto = ''
flag = 0
flag2 = True

while flag2 == True:


    while flag == 0:

        print('Digite a frase que quer codificar em CN (Codigo Numérico) sem caracteres especiais (=,@,#,$,%,\",\',\\):')
        entrada = input().lower().strip()

        if '@' in entrada or '#' in entrada or '$' in entrada or '%' in entrada or '"' in entrada or '\'' in entrada or '\\' in entrada or '/' in entrada or '=' in entrada:
            print('Seu burro e cego não pode ter caracteres especiais (=,@,#,$,%,\",\',\\) na frase. Na proxima a MOMO vai te levar! \n')
            entrada = ''
        else:
            flag = 1

    for i in range(len(entrada)):
        for k,v in alfabeto.items():
            if k == entrada[i]:
                codigo_pronto += v


    print('\ncodigo pronto:')
    print(codigo_pronto +'\n')
    print('aperte qualquer tecla para continuar')
    flag = 0
    input()










    
