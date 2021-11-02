# EP2
Guido Alvaro e João Victor

import random as rd
def criando_as_pecas():
    lista_pecas=[(6,6),(6,5),(6,4),(6,3),(6,2),(6,1),(6,0),(5,5),(5,4),(5,3),(5,2),(5,1),(5,0),(4,4),(4,3),(4,2),(4,1),(4,0),(3,3),(3,2),(3,1),(3,0),(2,2),(2,1),(2,0),(1,1),(1,0),(0,0)]
    rd.shuffle(lista_pecas)
    return lista_pecas

def destribui_pecas(lista_pecas,num_participantes):
    dicionario_mesa={}
    lista_copia=lista_pecas.copy()
    if num_participantes not in (2,3,4):
        return "False"
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
        inicio_do_jogo =dicionario_mesa
    elif num_participantes==3:
        pessas_jogador_3=[]
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
        inicio_do_jogo =dicionario_mesa
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
        inicio_do_jogo=dicionario_mesa
                inicio_do_jogo= dicionario_mesa
    if "banco" in dicionario_mesa.keys()    :
        dicionario_banco={"banco":dicionario_mesa["banco"]}
        dicionario_mesa.popitem()
    lista_inbaralhar_chaves=[]
    for i in dicionario_mesa.keys():
        lista_inbaralhar_chaves.append(i)
    rd.shuffle(lista_inbaralhar_chaves)
    dicionario_ordem_jogadores={}
    for i2 in lista_inbaralhar_chaves:
        dicionario_ordem_jogadores[i2]=dicionario_mesa[i]
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
# função verifica movimietos pocíveis
# função recebe([tabuleiro],[lista de pessas],computador v=1 or0)
# retorna: lista de pessas pociveis
def pessas_pociveis(jogo,um_jogador_e_suas_pessas):
    pessas_pociveis=[]
    if len(jogo)==0:
        return um_jogador_e_suas_pessas
    else:
        nipe_final=jogo[(len(jogo)-1)][1]
        nipe_inicial=jogo[0][0]
        for k in um_jogador_e_suas_pessas:
            if nipe_final in k or nipe_inicial in k:
                pessas_pociveis.append(k)
        retorno=pessas_pociveis
        return retorno

