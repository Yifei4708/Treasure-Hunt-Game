
#between 0 and 100
#radom(100)
#Determine a radom x and y position on the screen to determine
#where treasure is

x = random(800)
y = random(600)
buttonPressed = False
pressedP = False
def setup():
    #set window to 800 by 600
    size(800,600)
    #set color of background
    ##background(204,204,255)
    noStroke()
    
def draw():
    #global x, y
    #line(0,0,width, height)
    #rect(x,y,0,0)
#this function gets called when the mouse is clicked   
    global buttonPressed, pressedP
    if buttonPressed == False and pressedP == False:
    
        fill(255)
        rect(width/2 - 100/2 ,height/2 - 50/2,100,50)
        fill(0)
        text("Play!", width/2 - 20 , height/2 + 5  )


      
def mouseClicked():
    global buttonPressed
    #check if you click the bottom
    #if mousePressed and mouseX > width/2 - 100/2 and mouseX < width/2 - 100/2 + 100 and mouseY > height/2 - 50/2 and mouseY < height/2 + 50/2  :
    if buttonPressed == False and mouseX > width/2 - 100/2 and mouseX < width/2 - 100/2 + 100 and mouseY > height/2 - 50/2 and mouseY < height/2 + 50/2  :
        print("Yes")
        buttonPressed = True
        background(204,204,255)
    elif buttonPressed == True:    
        #distance between two points
        d = dist(x,y,mouseX,mouseY)
        #d = sqrt((mouseY-y)**2 + (mouseX-x)**2)
        print(d)
        #value = distance of guess / farthest you can be
        value = d / 1000
        fill((value) * 255, (1-value) *255,0)
        ellipse(mouseX, mouseY,10,10)
        #you win when you are 25 or ferwer pixefls away
        if d < 25:
            fill(0)
            textSize(20)
            text("you found the treasure!", 5, 20)
            #print("you found the treasure!")
            #fill(255,255,0)
            
            #black for the line
            stroke(0)
            line(mouseX,mouseY,x,y)
            noStroke()
            
            #green circle 
            #rect(x,y,10,10)
            fill(0)
            ellipse(mouseX,mouseY,10,10)
            
            #yellow cicle treasure is 
            fill(255,255,0)
            ellipse(x,y,10,10)
            print("you were", d, "distance away")

def keyPressed():
    global pressedP
    if key == 'p':
        pressedP = True
    
