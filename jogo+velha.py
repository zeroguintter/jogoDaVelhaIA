#print("Jogo da Velha")
#layout
#   ║   ║   
#═══╬═══╬═══
#   ║   ║   
#═══╬═══╬═══
#   ║   ║   
#skins = ☺ ♂ ♀ x ○
def skin(s):
    global x
    if s=="1":
        x="☺"
    elif s=="2":
        x="♂"
    elif s=="3":
        x="♀"
    elif s=="4":
        x="x"
    elif s=="5":
        x="o"
    elif s=="6":
        x="■"
    elif s=="0":
        x="&"

def skin2(s):
    global x,cor
    if s=="0":
        cor=f"\033[47m {x} \033[m"
    elif s=="1":
        cor=f"\033[41m {x} \033[m"
    elif s=="2":
        cor=f"\033[42m {x} \033[m"
    elif s=="3":
        cor=f"\033[43m {x} \033[m"
    elif s=="4":
        cor=f"\033[44m {x} \033[m"
    elif s=="5":
        cor=f"\033[45m {x} \033[m"
    elif s=="6":
        cor=f"\033[46m {x} \033[m"


def ocupado(u,t,m):
    global ii,al,turno
    if o[u-1]==0:
        o[u-1]=1
        j[u-1]=t
        al=False 
        turno+=1
        compar(t,m)
        if ii==0:
            mm[u-1]=1
        else:
            mm[u-1]=-1
        ii+=1
    else:
        print("\n\t\033[41m - Local já ocupado tente outro - \033[m")
        al=True

def compar(t,m):
    global inud
    if j[0]==t and j[1]==t and j[2]==t or j[3]==t and j[4]==t and j[5]==t or j[6]==t and j[7]==t and j[8]==t or j[0]==t and j[3]==t and j[6]==t or j[1]==t and j[4]==t and j[7]==t or j[2]==t and j[5]==t and j[8]==t or j[0]==t and j[4]==t and j[8]==t or j[6]==t and  j[4]==t and j[2]==t:
        print('\n')
        historico()
        print("\n\t╔════════════════════════════════════╗")
        print(f" \t║   PARABENS {t} VOCÊ GANHOU!!!!!!   ║")
        print(" \t╚════════════════════════════════════╝\n")
        print(f"\t\033[34m Vulgo {m}.\033[m\n")
        o[0]=9
        inud=False 
    
def cadastro(press):
    
    i=0
    while i<press:
        nom=str(input(f"\nEscolha um nome jogador {i+1}: "))
        nomes[i]=nom
        aa=True
        while aa==True:
            print("\t┌─────────────────────────┐")
            print("\t│        • Tabela •       │")
            print("\t├───────────┬─────────────┤")
            print("\t│    Skin   │   Numero    │")
            print("\t├───────────┼─────────────┤")
            print("\t│        ☺  │   1         │")
            print("\t│        ♂  │   2         │")
            print("\t│        ♀  │   3         │")
            print("\t│        x  │   4         │")
            print("\t│        ○  │   5         │")
            print("\t│        ■  │   6         │")
            print("\t└───────────┴─────────────┘")
            sk=str(input(f" Diga o numero da skin desejada {nomes[i]}: "))
            if sk=="0" or sk=="1" or sk=="2" or sk=="3" or sk=="4" or sk=="5" or sk=="6":
                skin(sk)
                ratinhoo=True
                while ratinhoo==True:
                    print("\t┌───────────────────────────┐")
                    print("\t│         • Tabela •        │")
                    print("\t├─────────────┬─────────────┤")
                    print("\t│     cor     │   Numero    │")
                    print("\t├─────────────┼─────────────┤")
                    print("\t\033[47m│   branco    │      0      │\033[m")
                    print("\t\033[41m│   vermelho  │      1      │\033[m")
                    print("\t\033[42m│   verde     │      2      │\033[m")
                    print("\t\033[43m│   amarelo   │      3      │\033[m")
                    print("\t\033[44m│   azul      │      4      │\033[m")
                    print("\t\033[45m│   roxo      │      5      │\033[m")
                    print("\t\033[46m│   ciano     │      6      │\033[m")
                    print("\t└─────────────┴─────────────┘")
                    skk=str(input(f" Diga o numero da cor desejada {nomes[i]}: "))
                    if skk=="0" or skk=="1" or skk=="2" or skk=="3" or skk=="4" or skk=="5" or skk=="6":      
                        skin2(skk)      
                        ss[i]=cor
                        if ss[0]!= ss[1]:
                            print("skin selecionada: ",ss[i])
                            i+=1
                            aa=False
                            ratinhoo=False
                        else:
                            ratinhoo=True
                            print("\n\t\033[41m A skin \033[m",ss[1],"\033[41m corresponde a outro jogador, tente novamente. \033[m\n") 

                    else:
                        print("\n\t\033[41m Valor invalido tente novamente. \033[m\n") 
            else:
                print("\n\t\033[41m Valor invalido tente novamente. \033[m\n")

    
def historico():
    print(f" {j[0]} ║ {j[1]} ║ {j[2]} ")
    print("═════╬═════╬═════")
    print(f" {j[3]} ║ {j[4]} ║ {j[5]} ")
    print("═════╬═════╬═════")
    print(f" {j[6]} ║ {j[7]} ║ {j[8]} ")

def iacore(jii):
    ocupado(jii,ss[2],nomes[2])
    print(f"\n\t\033[45m A maquina jogou na posição {jii} \033[m")
    compar(ss[2],nomes[2])

def cerebro1():
    uu=True
    while uu==True:
        jii=random.randint(1,9)
        iacore(jii)
        uu=al

def cerebro2(nn,inv,index,x,kj):
        global inud
        kk=inv
        uiui=0
        #print("-------------")
        while uiui<3:
            #print(uiui)
            #print(kk)
            #print(inv)
            #print("-->",kj)
            #print("--",inud)
            if x==1:
             #   print(f"mm[{kk}]+mm[{kk}+{nn}])=={kj} o[{kk}+{nn}+{nn}]")
                if (mm[kk]+mm[kk+nn])==kj and o[kk+nn+nn]==0:
                    core(kk+nn+nn)
                    j[kk+nn+nn]=ss[2]
                    o[kk+nn+nn]=1
                    uiui=3
                    mm[kk+nn+nn]=-1
                else:
                    kk+=index
                    uiui+=1
            elif x==2:
              #  print("--",inud)
               # print(f"mm[{kk}]+mm[{kk}+{nn}+{nn}])=={kj} o[{kk}+{nn}]")
                if (mm[kk]+mm[kk+nn+nn])==kj and o[kk+nn]==0:
                    core(kk+nn)
                    j[kk+nn]=ss[2]
                    o[kk+nn]=1
                    uiui=3
                    mm[kk+nn]=-1
                else:
                    kk+=index
                    uiui+=1

def cerebro3(kj,x):
    global inud
    kk=0
    nn=8
    uiui=0
    while uiui<4:
        #print(uiui)
        #print(kk)
        #print(nn)
        #print("-->",kj)
        #print("--",inud)
        if x==1:
            #print(f"mm[{kk}]+mm[4])==kj and o[{nn}]==0:")
            if (mm[kk]+mm[4])==kj and o[nn]==0:
                core(nn)
                j[nn]=ss[2]
                o[nn]=1
                uiui=4
                mm[nn]=-1
            if (mm[nn]+mm[4])==kj and o[kk]==0:
                #print(f"mm[{nn}]+mm[4])==kj and o[{kk}]==0:")
                core(kk)
                j[kk]=ss[2]
                o[kk]=1
                uiui=4
                mm[nn]=-1
            else:
                kk+=2
                nn-=2
                uiui+=1
        elif x==2:
            #print(f"mm[{kk}]+mm[{nn}]==kj and o[4]==0:")
            if (mm[kk]+mm[nn])==kj and o[4]==0:
                core(4)
                j[4]=ss[2]
                o[4]=1
                uiui=4
                mm[4]=-1
            else:
                kk+=2
                nn-=2
                uiui+=1

def core(num):
    global inud
    print(f"\n \t\033[45m A maquina jogou na posição {num+1} \033[m")
    ocupado(num+1,ss[2],nomes[2])
    inud=False



import random 

himperador=True
while himperador==True:

    o=[0,0,0,0,0,0,0,0,0]
    ss=['player1','palyer2',"\033[45m ▲ \033[m"]
    nomes=["player1","player2","Maquina"]
    dd=0
    menu = True 
    while menu == True:
        print("\t┌───────────────────────────────┐")
        print("\t│  # JOGO DA VELHA DO ROMIN #   │")
        print("\t└───────────────────────────────┘")
        print("\t┌───────────────────────────────┐")
        print("\t│            # MENU #           │")
        print("\t├───────────────────────────────┤")
        print("\t│ \033[31mcontra a maquina\033[m  #  Press 1  │")
        print("\t│       \033[31mPVP\033[m         #  Press 2  │")
        print("\t│       \033[4;31mSair\033[m        #  Press 3  │")
        print("\t└───────────────────────────────┘")
        press=int(input("-> "))
        if press != 1 and press !=2 and press !=3:
            print("\t\033[41m Valor invalido. \033[m")
        elif press==3:
            print("\t\033[34m Programa encerrado. \033[m")
            menu=False
            himperador=False
            o[0]=9

        elif press == 1:
            print("\t┌───────────────────────────────┐")
            print("\t│  # JOGO DA VELHA DO ROMIN #   │")
            print("\t└───────────────────────────────┘")
            print("\t┌───────────────────────────────┐")
            print("\t│  # Escolha sua dificuldade  # │")
            print("\t├───────────────────────────────┤")
            print("\t│       \033[31mizi\033[m      #  Press 1     │")
            print("\t│      \033[31mNormal\033[m    #  Press 2     │")
            print("\t├───────────────────────────────┤")
            print("\t│   \033[4;31m<< Voltar\033[m    #  Press 3     │")
            print("\t└───────────────────────────────┘")
            dd=str(input("->"))
            if dd=='1' or dd=='2':
                menu=False
                cadastro(press)
                
            elif dd=='3':
                menu=True

            elif dd!='1' and dd!='2':
                print("\033[41m Valor invalido vc foi realocado para o menu. \033[m")
            
        elif press == 2:
            menu=False
            cadastro(press)


    al=True
    inud=True
    mm=[0,0,0,0,0,0,0,0,0]
    j=[" 1 "," 2 "," 3 "," 4 "," 5 "," 6 "," 7 "," 8 "," 9 "]  

    turno=1
    while o[0]!=9 :
        
        ii=0
        while ii<press and o[0]!=9:

            if sum(o) < 9:
                print(f"\nEscolha sua jogada {nomes[ii]}\n")
                historico()
                y=True
                while y==True:
                    ji=int(input("\nColoque a posição desejada aki=>"))
                    if ji<10 and ji>0:
                        ocupado(ji,ss[ii],nomes[ii])
                        y=al
                    else:
                        print("\t\033[41m Posição invalida tente um numero correspondente: \033[m")

            if press==1 and sum(o) < 9:
                if dd=="1":
                    cerebro1()

                elif dd=="2":
                    if turno==2:
                        cerebro1()
                   
                    elif turno>=4:

                        inud=True
                        jjj=True
                        kj=-2

                        while jjj==True:
                            
                            if jjj == True:
                                #print("cerebro - 1")
                                cerebro2(1,0,3,1,kj)
                                jjj=inud
                            if jjj == True:
                                #print("cerebro - 2")
                                cerebro2(-1,8,-3,1,kj)
                                jjj=inud
                            if jjj == True:
                                #print("cerebro - 3")
                                cerebro2(3,0,1,1,kj)
                                jjj=inud
                            if jjj == True:   
                                #print("cerebro - 4")
                                cerebro2(-3,8,-1,1,kj)
                                jjj=inud
                            if jjj == True:
                                #print("DIAGONAL-1")
                                cerebro3(kj,1)
                                jjj=inud
                            if jjj == True:
                                #print("DIAGONAL- BURACOS")
                                cerebro3(kj,2)
                                jjj=inud
                            if jjj == True:
                                #print("BURACOS-1")
                                cerebro2(3,0,1,2,kj)
                                jjj=inud
                            if jjj == True:
                                #print("BURACOS-2")
                                cerebro2(1,0,3,2,kj)
                                jjj=inud

                            if jjj == True and kj==2:
                                #print("cerebro1 ativado")
                                cerebro1()
                                jjj=False

                            if jjj == True:
                                kj=2
                                    
        else:
            if sum(o)==9:
                historico()
                print("\n\t\033[1;41m ╔══════════════════════╗ \033[m")
                print(" \t\033[1;41m ║     \033[m\033[1;31;41mDeu velha :C\033[m\033[1;41m     ║ \033[m")
                print(" \t\033[1;41m ╚══════════════════════╝ \033[m\n")
                o[0]=9
   




















































# meu primeiro jogo :P
#               ~~romulin

#           .    ®    •        .    +      ○      *   
#    ♫    ♦  *      ○ '   ♪       ♦   ♫    ® '      ♪   •
#   ♦  ♫     a ya ya got this feeling, yeah, you know  ♪  ♫
#       ○ '  ♪     Where I'm losing all control  •  ♫    °
#    '   ♫  ® 'Cause there's magic in my bones    ♪ ♦  . '
#   . ♫       ♪     •    •  ♪      .    ♫      ○      ♪   ♦
#         *  ♪   °   '   +       ♦        *  °      *   •   



        
        

   