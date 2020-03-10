import numpy

R=2
C=5
Y="IMPOSSIBLE"

Casillas=numpy.zeros((R,C,2))

for i in range(R):
    for j in range(C):
        Casillas[i][j][0]=int(i+1)
        Casillas[i][j][1]=int(j+1)
        

count=0
Path=[[]]
print(len(Path))
Change=True


while Change:
    Change=False
    for i in range (R):
        for j in range (C):
            #Coordenada inicial        
            if len(Path)<C*R:
                Path=[[]] #Si vuelve aquí es que no ha ido y se reescribe
                r=Casillas[i,j,0]
                c=Casillas[i,j,1]
                Place=[r,c]
                Path.append(Place)
                Path.pop(0)
                rp=r
                cp=c
                Changing=True
                while Changing:  #Para que pueda iterar en coordenadas de i,j ya usadas
                    Changing=False
                    for i in range (R):
                        for j in range (C):
                            #Demás coordenadas
                            r=Casillas[i,j,0]
                            c=Casillas[i,j,1]
                            if not (r==rp or c==cp or r-c==rp-cp or r+c==rp+cp or [r,c] in Path):
                                #Añade coordenada si cumple condiciones
                                Place=[r,c]
                                Path.append(Place)
                                rp=r
                                cp=c
                                Changing=True
    
                        
            else:
                Y="POSSIBLE"
                L=Path                    


print("Y=",Y)
print("L=",L)

    
        
        
        

        