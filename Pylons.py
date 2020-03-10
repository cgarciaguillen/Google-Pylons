import numpy

R=5
C=2
Y="IMPOSSIBLE"

Casillas=numpy.zeros((R,C,2))

for i in range(R):
    for j in range(C):
        Casillas[i][j][0]=int(i+1)
        Casillas[i][j][1]=int(j+1)
        

count=0
Path=[[]]
Change=True


while Change:
    Change=False
    for i in range (R):
        for j in range (C):
            #Coordenada inicial   
            
            if len(Path)==C*R:
                Y="POSSIBLE"
                L=Path   
            
                                
            else:
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
                    for ii in range (R):
                        for jj in range (C):
                            #Demás coordenadas
                            r=Casillas[ii,jj,0]
                            c=Casillas[ii,jj,1]
                            if not (r==rp or c==cp or r-c==rp-cp or r+c==rp+cp or [r,c] in Path):
                                #Añade coordenada si cumple condiciones
                                Place=[r,c]
                                Path.append(Place)
                                rp=r
                                cp=c
                                Changing=True
                if len(Path) == C*R or (i==5 and j==5):
                    Change=False
                else:
                    Change=True
    
                                          
print("Y=",Y)
if Y=="POSSIBLE":
    print("L=",L)



    
        
        
        

        