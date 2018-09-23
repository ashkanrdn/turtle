import rhinoscriptsyntax as rs

#allObjs = rs.AllObjects()
#rs.DeleteObjects(allObjs)



class Turtle:
    def __init__(self, pos = [0,0,0], heading = [1,0,0]):
        self.heading = heading
        self.point = rs.AddPoint(pos)
        self.draw = True
        pointPos = rs.PointCoordinates(self.point)
        self.direction = rs.VectorCreate(heading,pointPos)
        self.lines = []
    
    def forward(self,magnitude):
        print self.direction
        movement = rs.VectorScale(self.direction,magnitude)
        prevPos = rs.PointCoordinates(self.point)
        rs.MoveObject(self.point,movement)
        currentPos = rs.PointCoordinates(self.point)
#        rs.AddLine(prevPos,currentPos)
        self.drawLine(prevPos, currentPos)
        
    def left(self,angle):
        self.direction = rs.VectorRotate(self.direction, angle, [0,0,1])
        print(self.direction)
        
    def right(self,angle):
        self.direction = rs.VectorRotate(self.direction, -angle, [0,0,1])
        print(self.direction)
    
    def goto(self, x, y,z=0):
        prevPos = rs.PointCoordinates(self.point)
        movement = rs.VectorCreate([x,y,z],prevPos)
        rs.MoveObject(self.point,movement)
        currentPos = rs.PointCoordinates(self.point)
#        rs.AddLine(prevPos,currentPos)
        l = self.drawLine(prevPos, currentPos)
        
    
    def drawLine(self, p1, p2):
        if self.draw:
            l=rs.AddLine(p1,p2)
            return l
        else:
            pass
    def penUp(self):
        self.draw = False
    
    def penDown(self):
        self.draw = True
        
    def grid(self , sqr,x ,y):
        xpldCrv = rs.ExplodeCurves(sqr)
        rs.ReverseCurve(xpldCrv[0])
        rs.ReverseCurve(xpldCrv[3])
        crvPoints = []
        for i in range(len(xpldCrv)):
            curve = xpldCrv[i]
            if i % 2 == 0:
                crvPoints.append(rs.DivideCurve(curve,x))
            else:
                crvPoints.append(rs.DivideCurve(curve,y))
            #divide up the curve into points based on x and y
            #add the resulting points to the curvePoints List. Each of the resulting points sets are a list themsleves
        for p1, p2 in zip(crvPoints[0], crvPoints[2]):
            #draw a line between p1, p2
            print(p1)
            #rs.AddLine(p1,p2)
            self.penUp()
            self.goto(p1[0],p1[1],p1[2])
            self.penDown()
            self.goto(p2[0],p2[1],p2[2])
        for p1, p2 in zip(crvPoints[1], crvPoints[3]):
            #draw a line between p1, p2
#            rs.AddLine(p1,p2)
            self.penUp()
            l = self.goto(p1[0],p1[1],p1[2])
            #rs.ObjectColor(l,"red")
            self.penDown()
            self.goto(p2[0],p2[1],p2[2])

rect = rs.GetObject("Select an object")
divx=int(input("number of x side"))
divy=int(input("number of y side"))
t = Turtle()
t.grid(rect,divx,divy)
t.goto(20,45,23)




