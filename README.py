# EP2
Guido Alvaro e João Victor

import random as rd
import random as rd
import time
# fim das bibliotecas
# função cria peças retorna peças embaralhadas em forma de lista com tuplas

def criando_as_pecas():
    lista_pecas=[(6,6),(6,5),(6,4),(6,3),(6,2),(6,1),(6,0),(5,5),(5,4),(5,3),(5,2),(5,1),(5,0),(4,4),(4,3),(4,2),(4,1),(4,0),(3,3),(3,2),(3,1),(3,0),(2,2),(2,1),(2,0),(1,1),(1,0),(0,0)]
    rd.shuffle(lista_pecas)
    return lista_pecas
# print(criando_as_pecas())
# print(len(criando_as_pecas()))
# fim da  função
# função inicia jogo
# parametros: lista de pessas,numero de participantes
# retorno lista com [[pozição0 tabuleiro vazil],pozição1:{"banco":[lista de pessas no banco]},pozição2:{nome do jogador:[pessas do jogador]}] or "False"

def destribui_pecas(lista_pecas,num_participantes):
    dicionario_mesa={}
    lista_copia=lista_pecas.copy()
    if num_participantes not in (2,3,4):
        return ["False","False","False"]
    elif num_participantes==2:
        listabanco=[]
        pessas_jogador_1=[]
        pessas_jogador_2=[]
        for k in range(0,7):
            valor_j1=lista_pecas[k]
            pessas_jogador_1.append(valor_j1)
            lista_copia.remove(valor_j1)
            valor_j2=lista_pecas[k+7]
            pessas_jogador_2.append(valor_j2)
            lista_copia.remove(valor_j2)
        dicionario_mesa["jogador 1"]=pessas_jogador_1
        dicionario_mesa["jogador 2"]=pessas_jogador_2
        dicionario_mesa["banco"]=lista_copia
        inicio_do_jogo = dicionario_mesa
    elif num_participantes==3:
        pessas_jogador_3=[]
        pessas_jogador_1=[]
        pessas_jogador_2=[]
        for k in range(0,7):
            valor_j3=lista_pecas[k+14]
            pessas_jogador_3.append(valor_j3)
            lista_copia.remove(valor_j3)
            valor_j1=lista_pecas[k]
            pessas_jogador_1.append(valor_j1)
            lista_copia.remove(valor_j1)
            valor_j2=lista_pecas[k+7]
            pessas_jogador_2.append(valor_j2)
            lista_copia.remove(valor_j2)
        dicionario_mesa["jogador 1"]=pessas_jogador_1
        dicionario_mesa["jogador 2"]=pessas_jogador_2
        dicionario_mesa["jogador 3"]=pessas_jogador_3
        dicionario_mesa["banco"]=lista_copia
        inicio_do_jogo =dicionario_mesa
    elif num_participantes==4:
        pessas_jogador_3=[]
        pessas_jogador_1=[]
        pessas_jogador_2=[]
        for k in range(0,7):
            valor_j3=lista_pecas[k+14]
            pessas_jogador_3.append(valor_j3)
            lista_copia.remove(valor_j3)
            valor_j1=lista_pecas[k]
            pessas_jogador_1.append(valor_j1)
            lista_copia.remove(valor_j1)
            valor_j2=lista_pecas[k+7]
            pessas_jogador_2.append(valor_j2)
            lista_copia.remove(valor_j2)
        dicionario_mesa["jogador 1"]=pessas_jogador_1
        dicionario_mesa["jogador 2"]=pessas_jogador_2
        dicionario_mesa["jogador 3"]=pessas_jogador_3
        dicionario_mesa["jogador 4"]=lista_copia
        dicionario_mesa["banco"]=lista_copia
        inicio_do_jogo=dicionario_mesa
                inicio_do_jogo=dicionario_mesa
    if "banco" in dicionario_mesa.keys():
        dicionario_banco={"banco":dicionario_mesa["banco"]}
        dicionario_mesa.popitem()
    lista_inbaralhar_chaves=[]
    for i in dicionario_mesa.keys():
        lista_inbaralhar_chaves.append(i)
    rd.shuffle(lista_inbaralhar_chaves)
    dicionario_ordem_jogadores={}
    for i2 in lista_inbaralhar_chaves:
        dicionario_ordem_jogadores[i2]=dicionario_mesa[i2]
    if num_participantes==4:
        dicionario_banco={"banco":[]}
        jogo=[]
        return [jogo,dicionario_banco,dicionario_ordem_jogadores]
    else:
        jogo=[]
        return [jogo,dicionario_banco,dicionario_ordem_jogadores]
# testando a função
# print(destribui_pecas(criando_as_pecas(),4))
# fim da função
# função verifica movimietos possíveis
# função recebe([tabuleiro],[lista de peças],computador v=1 or0)
# retorna: lista de peças pociveis
def pessas_pociveis(jogo,um_jogador_e_suas_pessas):
    pessas_pociveis=[]
    if len(jogo)==0:
        return um_jogador_e_suas_pessas
    else:
        nipe_final=jogo[(len(jogo)-1)][1]
        nipe_inicial=jogo[0][0]
        c=[x for x in um_jogador_e_suas_pessas if x not in jogo]
        for k in c:
            if nipe_final in k or nipe_inicial in k:
                pessas_pociveis.append(k)
        retorno=pessas_pociveis
        return retorno
# testando o codigo
v_g=pessas_pociveis([(8,4),(4,8)],destribui_pecas(criando_as_pecas(),4)[2]["jogador 1"])
# fim da função
# criando função que adiciona a pessas no tabuleiro

def adicionando_pessas(tabuleiro,banco,pessas_podem,computador):
    if len(pessas_podem)>0:
        print(f"suas peças:{pessas_podem}")
        # time.sleep(2)
        melhor_pessa=[]
        numero_de_pontos=0
        for k in pessas_podem:
            soma=k[1]+k[0]
            if soma>numero_de_pontos:
                numero_de_pontos=soma
                melhor_pessa.append(k)
        m_pessa=melhor_pessa[len(melhor_pessa)-1]
        print(f"melhor peça:{m_pessa}")
        if computador==1 and len(tabuleiro)==0:
            tabuleiro.append(m_pessa)
            print(f"peça adicionada:{m_pessa}")
            pessas_podem.remove(m_pessa)
        elif len(tabuleiro)!=0 and computador==1:
            nipe_final_tab=tabuleiro[len(tabuleiro)-1][1]
            nipe_inicial_tab=tabuleiro[0][0]
            if nipe_final_tab==m_pessa[0]:
                tabuleiro.append(m_pessa)
                print(f" peça adicionada:{m_pessa}")
                pessas_podem.remove(m_pessa)
            elif nipe_inicial_tab==m_pessa[1]:
                pessa_no_inicio=tabuleiro.copy()
                tabuleiro.clear()
                tabuleiro.append(m_pessa)
                tabuleiro=tabuleiro+pessa_no_inicio
                pessas_podem.remove(m_pessa)
                print(f" peça adicionada:{m_pessa}")
            elif nipe_final_tab==m_pessa[1]:
                pessa_env=(m_pessa[1],m_pessa[0])
                tabuleiro.append(pessa_env)
                pessas_podem.remove(m_pessa)
                print(f"peça adicionada:{pessa_env}")
            else:
                pessas_podem.remove(m_pessa)
                pessa_env=(m_pessa[1],m_pessa[0])
                print(f" peça adicionada:{pessa_env}")
                pessa_no_inicio=tabuleiro.copy()
                tabuleiro.clear()
                tabuleiro.append(pessa_env)
                tabuleiro=tabuleiro+pessa_no_inicio
        elif computador==0 and len(tabuleiro)==0:
            altenticador=0
            while altenticador==0:
                nipe_1=int(input("digite um dos valores da peça que quer escolher"))
                nip_2=int(input("digite o outro valor da peça"))
                pessa_montada=(nipe_1,nip_2)
                pessa_montada_inv=(nip_2,nipe_1)
                if pessa_montada in pessas_podem:
                    print("peça adicionada")
                    pessas_podem.remove(pessa_montada)
                    tabuleiro.append(pessa_montada)
                    altenticador=1
                elif pessa_montada_inv in pessas_podem:
                    pessas_podem.remove(pessa_montada_inv)
                    tabuleiro.append(pessa_montada_inv)
                    altenticador=1
                    print("peça adicionada ao tabuleiro")
                else:
                    print("peça inexistente")
        elif computador==0 and len(tabuleiro)!=0:
            altenticador=0
            while altenticador==0:
                nipe_1=int(input("digite um dos valores da peça que quer escolher"))
                nip_2=int(input("digite o outro valor da peça"))
                pessa_montada=(nipe_1,nip_2)
                pessa_montada_inv=(nip_2,nipe_1)
                if pessa_montada in pessas_podem:
                    altenticador=1
                    print("peça adicionada")
                    pessas_podem.remove(pessa_montada)
                    if pessa_montada[0]==tabuleiro[len(tabuleiro)-1][1]:
                        tabuleiro.append(pessa_montada)
                    else:
                        inicio_do_jogo=tabuleiro.copy()
                        tabuleiro.clear()
                        tabuleiro.append(pessa_montada)
                        tabuleiro+=inicio_do_jogo
                elif pessa_montada_inv in pessas_podem:
                    altenticador=1
                    print("peça adicionada")
                    pessas_podem.remove(pessa_montada_inv)
                    if pessa_montada_inv[0]==tabuleiro[len(tabuleiro)-1][1]:
                        tabuleiro.append(pessa_montada_inv)
                    else:
                        inicio_do_jogo=tabuleiro.copy()
                        tabuleiro.clear()
                        tabuleiro.append(pessa_montada_inv)
                        tabuleiro+=inicio_do_jogo
                else:
                    print("peça inválida")
        return [tabuleiro,banco,pessas_podem,computador]
    elif len(pessas_podem)==0 and len(banco)>0:
        uma_pessa_adicionada=banco[0]
        pessas_podem.append(uma_pessa_adicionada)
        banco.remove(uma_pessa_adicionada)
        print(f"o jogador comprou a peça:{uma_pessa_adicionada} do banco")
        return [tabuleiro,banco,pessas_podem,computador]
    elif len(pessas_podem)==0 and len(banco)==0:
        print("pulando a sua vez porque você não tem pessas válidas e o banco esta vazio")
        return [tabuleiro,banco,pessas_podem,computador]
    
# testando a função
# tabuleiro,banco,pessa_restantes,computador=adicionando_pessas([(3,6)],[],[],0)
# fim da função
# função soma os valores das peças de um jogador recebe como parametro um conjunto de peças e retorna como rezultado um valor
def soma_p_v(lista_pessas):
    valor=0
    a=type(0)
    if type(lista_pessas)==a:
        return valor
    for k in lista_pessas:
        valor+=k[0]
        valor+=k[1]
    return valor
# fim da função
# função atualiza a lista de pessas de um jogador resebe como parametros lista_inicial,lista_pociveis e lista_restantes
def atualiza_patrimonho(lista_inicial,lista_pociveis,lista_resto):
    for k in lista_pociveis:
        lista_inicial.remove(k)
    lista_inicial+=lista_resto
    print(f"""sobraram as peças: {lista_inicial}
    sobra de pontos: {soma_p_v(lista_inicial)}""")
    return lista_inicial
    # fim da função
# função recebe um dicionario com jogadores e seus pontos e retorna nome do jogador que tem menos pontos
def jogador_m_pontos(placar_jogadores):
    menor_num=4**10
    nome=""
    for k in placar_jogadores.keys():
        somatorio=soma_p_v(placar_jogadores[k])
        if somatorio<menor_num:
            menor_num=somatorio
            nome=k
        elif menor_num==somatorio:
            nome="empate"
    print("calculando o vencedor")
    print('aguarde...')
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    print(nome)
    return nome

# função roda o jogo, recebe como parametros jogo,dicionario_banco,dicionario_ordem_jogadores
# retorna jogo terminado, rezultado que vai ser adicionado em um arquivo
# mostra interação com o usuario

def rodando_o_jogo(jogo,dicionario_banco,dicionario_ordem_jogadores):
    fim_de_jogo=0
    dicionario_usuario={}
    somatorio_d_g={}
    for k in dicionario_ordem_jogadores.keys():
        if k=="jogador 1":
            dicionario_usuario["humano"]=dicionario_ordem_jogadores[k]
            somatorio_d_g["humano"]=soma_p_v(dicionario_ordem_jogadores[k])
        else:
            dicionario_usuario[k]=dicionario_ordem_jogadores[k]
            somatorio_d_g[k]=soma_p_v(dicionario_ordem_jogadores[k])
    while fim_de_jogo==0:
        jogadas_foram_i=0
        for k in dicionario_usuario.keys():
            if k=="humano":
                computador=0
                print(" jogada do humano")
            else:
                computador=1
                print(f"vez do jogador {k}")
            # lista_de_pessas_validas=pessas_pociveis(jogo,dicionario_usuario[k])
            parou_de_comprar=0
            while parou_de_comprar==0:
                lista_de_pessas_validas=pessas_pociveis(jogo,dicionario_usuario[k])
                loop_tabuleiro,loop_banco,loop_pessas_restantes,computador=adicionando_pessas(jogo,dicionario_banco["banco"],lista_de_pessas_validas,computador)
                if loop_banco==dicionario_banco["banco"] and loop_tabuleiro==jogo:
                    parou_de_comprar+=3
                    jogadas_foram_i+=1.2
                elif jogo!=loop_tabuleiro:
                    parou_de_comprar=3
                    jogo.clear()
                    jogo=loop_tabuleiro.copy()
                    dicionario_usuario[k]=atualiza_patrimonho(dicionario_usuario[k],lista_de_pessas_validas,loop_pessas_restantes)
                elif loop_banco!=dicionario_banco["banco"]:
                    dicionario_banco["banco"]=loop_banco
                    media=dicionario_usuario[k].copy()
                    media+=loop_pessas_restantes
                    loop_pessas_restantes.clear()
                    dicionario_usuario[k]=media
                print("---")
                os.system("cls")    
                print("peças jogadas")
                print(jogo)
                print("---")
            somatorio_d_g[k]=soma_p_v(dicionario_usuario[k])
            if somatorio_d_g[k]==0:
                print(f"""fim do jogo
                vitória do jogador: {k}""")
                return k
            elif jogadas_foram_i>=len(dicionario_usuario.keys()):
                vitoria=jogador_m_pontos(somatorio_d_g)
                if vitoria=="empate":
                    print("empate")
                    return "empate"
                else:
                    print(f"""fim do jogo
                    vitória do jogador {vitoria}""")
                    return vitoria
                    # fim da função
# teste macro
         # teste macro
# retorna lista de pessas

lista_de_pessas=criando_as_pecas()
# print(f""" lista de pessas :{lista_de_pessas}
# tipo:{type(lista_de_pessas)}""")
# jogo cria um tabuleiro com lista ou "False", dicionario_banco:cria um dicionario com chave:"banco e valor:pessas ou "False" e dicionario de nome do jogador e pessas como valores ou "False"
# boas vindas
print("Bem Vindo ao dominó")
pode_jogar="False"
while pode_jogar=="False":
    numero_de_jogadores=int(input("Com quantos jogadores você quer jogar? máximo 4"))
    jogo,dicionario_banco,dicionario_ordem_jogadores=destribui_pecas(lista_de_pessas,numero_de_jogadores)
    pode_jogar=dicionario_ordem_jogadores
print("Começando o jogo em 4 segundos")
time.sleep(2)
print("Começando o jogo em 2 segundos")
time.sleep(2)
print("O jogo foi iniciado!")
rodando_o_jogo(jogo,dicionario_banco,dicionario_ordem_jogadores)



    # macro print com cada um dos valores da lista
# print(f"""tabuleiro:{jogo}
# tipo:{type(jogo)}
 # banco:{dicionario_banco}
 # tipo:{type(dicionario_banco)}
 # jogadores e suas pessas:{dicionario_ordem_jogadores}
 # tipo:{type(dicionario_ordem_jogadores)}""")
 # função recebe 2 listas , jogo e lista de pessas de um jogador
 # capiturando uma lista de pessas por jogador
uma_lista_para_um_jogador=dicionario_ordem_jogadores["jogador 1"]
jogo=[(7,7)]
# antes de paçar para pessas são puciveis pociveis? precisa garantir que numero de jogadores e verdadeiro
pessas__puciveis=pessas_pociveis(jogo,uma_lista_para_um_jogador)
print(f"""peças possíveis:{pessas__puciveis}
tipo: {type(pessas__puciveis)}
tamanho: {len(pessas__puciveis)}""")
# fim do teste macro


