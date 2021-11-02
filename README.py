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
    # testando o codigo
v_g=pessas_pociveis([(8,4),(4,8)],destribui_pecas(criando_as_pecas(),4)[2]["jogador 1"])
# fim da função
# criando função que adiciona a pessas no tabuleiro

def adicionando_pessas(tabuleiro,banco,pessas_podem,computador):
    if len(pessas_podem)>0:
        print(f"suas pessas:{pessas_podem}")
        # time.sleep(2)
        melhor_pessa=[]
        numero_de_pontos=0
        for k in pessas_podem:
            soma=k[1]+k[0]
            if soma>numero_de_pontos:
                numero_de_pontos=soma
                melhor_pessa.append(k)
        m_pessa=melhor_pessa[len(melhor_pessa)-1]
        print(f"melhor pessa:{m_pessa}")
        if computador==1 and len(tabuleiro)==0:
            tabuleiro.append(m_pessa)
            print(f"pessa adicionada:{m_pessa}")
            pessas_podem.remove(m_pessa)
        elif len(tabuleiro)!=0 and computador==1:
            nipe_final_tab=tabuleiro[len(tabuleiro)-1][1]
            nipe_inicial_tab=tabuleiro[0][0]
            if nipe_final_tab==m_pessa[0]:
                tabuleiro.append(m_pessa)
                print(f" pessa adicionada:{m_pessa}")
                pessas_podem.remove(m_pessa)
            elif nipe_inicial_tab==m_pessa[1]:
                pessa_no_inicio=tabuleiro.copy()
                tabuleiro.clear()
                tabuleiro.append(m_pessa)
                tabuleiro=tabuleiro+pessa_no_inicio
                pessas_podem.remove(m_pessa)
                print(f" pessa adicionada:{m_pessa}")
            elif nipe_final_tab==m_pessa[1]:
                pessa_env=(m_pessa[1],m_pessa[0])
                tabuleiro.append(pessa_env)
                pessas_podem.remove(m_pessa)
                print(f"pessa adicionada:{pessa_env}")
            else:
                pessas_podem.remove(m_pessa)
                pessa_env=(m_pessa[1],m_pessa[0])
                print(f" pessa adicionada:{pessa_env}")
                pessa_no_inicio=tabuleiro.copy()
                tabuleiro.clear()
                tabuleiro.append(pessa_env)
                tabuleiro=tabuleiro+pessa_no_inicio
        elif computador==0 and len(tabuleiro)==0:
            altenticador=0
            while altenticador==0:
                nipe_1=int(input("digite um dos valores da pessa que quer escolher"))
                nip_2=int(input("digite o outro valor da pessa"))
                pessa_montada=(nipe_1,nip_2)
                pessa_montada_inv=(nip_2,nipe_1)
                if pessa_montada in pessas_podem:
                    print("pessa adicionada")
                    pessas_podem.remove(pessa_montada)
                    tabuleiro.append(pessa_montada)
                    altenticador=1
                elif pessa_montada_inv in pessas_podem:
                    pessas_podem.remove(pessa_montada_inv)
                    tabuleiro.append(pessa_montada_inv)
                    altenticador=1
                    print("pessa adicionada ao tabuleiro")
                else:
                    print("pessa inesistente")
        elif computador==0 and len(tabuleiro)!=0:
            altenticador=0
            while altenticador==0:
                nipe_1=int(input("digite um dos valores da pessa que quer escolher"))
                nip_2=int(input("digite o outro valor da pessa"))
                pessa_montada=(nipe_1,nip_2)
                pessa_montada_inv=(nip_2,nipe_1)
                if pessa_montada in pessas_podem:
                    altenticador=1
                    print("pessa adicionada")
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
                    print("pessa adicionada")
                    pessas_podem.remove(pessa_montada_inv)
                    if pessa_montada_inv[0]==tabuleiro[len(tabuleiro)-1][1]:
                        tabuleiro.append(pessa_montada_inv)
                    else:
                        inicio_do_jogo=tabuleiro.copy()
                        tabuleiro.clear()
                        tabuleiro.append(pessa_montada_inv)
                        tabuleiro+=inicio_do_jogo
                else:
                    print("pessa invalida")
        return [tabuleiro,banco,pessas_podem,computador]
    elif len(pessas_podem)==0 and len(banco)>0:
        uma_pessa_adicionada=banco[0]
        pessas_podem.append(uma_pessa_adicionada)
        banco.remove(uma_pessa_adicionada)
        print(f"o jogador comprou a pessa:{uma_pessa_adicionada} do banco")
        return [tabuleiro,banco,pessas_podem,computador]
    elif len(pessas_podem)==0 and len(banco)==0:
        print("pulando a sua vez porque você não tem pessas validas e o banco esta vazil")
        return [tabuleiro,banco,pessas_podem,computador]
