from vpython import *
from time import *



mRadius=1

wallThickness=1

roomWidth=25
roomDepth=12
roomHeight=20

floor=box(pos=vector(0,-roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white)
ceiling=box(pos=vector(0,roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white)
backWall=box(pos=vector(0,0,-roomDepth/2),size=vector(roomWidth,roomHeight,wallThickness), color=color.white)
leftWall=box(pos=vector(-roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white)
rightWall=box(pos=vector(roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white)

marble1 = sphere(radius = mRadius, color = color.red)
marble2 = sphere(radius = mRadius, color = color.green)
marble3 = sphere(radius = mRadius, color = color.blue)

deltaX1 = 0.1
deltaY1 = 0.1
deltaZ1 = 0.1

xPos1 = 0
yPos1 = 1
zPos1 = -1
# -------------
deltaX2 = 0.2
deltaY2 = 0.3
deltaZ2 = -0.1

xPos2 = 0
yPos2 = 0.5
zPos2 = -2
# --------------
deltaX3 = -0.1
deltaY3 = 0.4
deltaZ3 = 0.3

xPos3 = 2
yPos3 = -1
zPos3 = 0

while True:
    rate(25)
    
    xPos1 = xPos1 + deltaX1
    yPos1 = yPos1 + deltaY1
    zPos1 = zPos1 + deltaZ1
    
    Xrme1=xPos1 + mRadius
    Xlme1=xPos1 - mRadius
    
    Ytme1 = yPos1 + mRadius
    Ybme1 = yPos1 - mRadius
    
    Zbme1 = zPos1 - mRadius
    Zfme1 = zPos1 + mRadius
    
    #---------------------
    
    xPos2 = xPos2 + deltaX2
    yPos2 = yPos2 + deltaY2
    zPos2 = zPos2 + deltaZ2
    
    Xrme2=xPos2 + mRadius
    Xlme2=xPos2 - mRadius
    
    Ytme2 = yPos2 + mRadius
    Ybme2 = yPos2 - mRadius
    
    Zbme2 = zPos2 - mRadius
    Zfme2 = zPos2 + mRadius
    
    #-----------------------
    
    xPos3 = xPos3 + deltaX3
    yPos3 = yPos3 + deltaY3
    zPos3 = zPos3 + deltaZ3
    
    Xrme3=xPos3 + mRadius
    Xlme3=xPos3 - mRadius
    
    Ytme3 = yPos3 + mRadius
    Ybme3 = yPos3 - mRadius
    
    Zbme3 = zPos3 - mRadius
    Zfme3 = zPos3 + mRadius
    
    #-------------------------
    
    Rwe= roomWidth / 2 - wallThickness/2
    Lwe= -roomWidth / 2 + wallThickness/2
    
    Cwe = roomHeight / 2 - wallThickness / 2
    Floorwe = -roomHeight / 2 + wallThickness / 2
    
    Bwe = -roomDepth / 2 + wallThickness / 2
    Fwe = roomDepth / 2 - wallThickness / 2
    
    if (Xrme1 >= Rwe or Xlme1 <= Lwe):
        deltaX1 = -deltaX1
    
    if (Ytme1 >= Cwe or Ybme1 <= Floorwe):
        deltaY1 = -deltaY1
    
    if (Zfme1 >= Fwe or Zbme1 <= Bwe):
        deltaZ1 = -deltaZ1
    #-----------------------------
    if (Xrme2 >= Rwe or Xlme2 <= Lwe):
        deltaX2 = -deltaX2
    
    if (Ytme2 >= Cwe or Ybme2 <= Floorwe):
        deltaY2 = -deltaY2
    
    if (Zfme2 >= Fwe or Zbme2 <= Bwe):
        deltaZ2 = -deltaZ2
    
    #-----------------------------
    if (Xrme3 >= Rwe or Xlme3 <= Lwe):
            deltaX3 = -deltaX3
    
    if (Ytme3 >= Cwe or Ybme3 <= Floorwe):
        deltaY3 = -deltaY3
    
    if (Zfme3 >= Fwe or Zbme3 <= Bwe):
        deltaZ3 = -deltaZ3
        
    marble1.pos=vector(xPos1, yPos1, zPos1)
    marble2.pos=vector(xPos2, yPos2, zPos2)
    marble3.pos=vector(xPos3, yPos3, zPos3)