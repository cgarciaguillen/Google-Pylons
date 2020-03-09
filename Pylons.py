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

if Y=="IMPOSSIBLE":
    for i in range (R):
        for j in range (C):
                    
            if len(Path)<C*R:
                count=count+1
                Path=[[]]
                r=Casillas[i,j,0]
                c=Casillas[i,j,1]
                Place=[r,c]
                Path.append(Place)
                Path.pop(0)
                rp=r
                cp=c
                m=0
                while m<=R:
                    for i in range (R):
                        for j in range (C):
                            m=m+1
                            r=Casillas[i,j,0]
                            c=Casillas[i,j,1]
                            if not (r==rp or c==cp or r-c==rp-cp or r+c==rp+cp or [r,c] in Path):
                                Place=[r,c]
                                Path.append(Place)
                                rp=r
                                cp=c
    
                        
            else:
                Y="POSSIBLE"
                L=Path                    

else:
    print("Y=",Y)
    print("L=",L)

    
        
        
        

        