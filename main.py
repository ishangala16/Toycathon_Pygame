import pygame
import time
#initialization
pygame.init()
points = 0
bonus = 0 

clock = pygame.time.Clock()
#create screen (window)
screen = pygame.display.set_mode((1280,720))

#images & icons
pygame.display.set_caption("Toycathon")

bg = pygame.image.load('question.jpeg')
# bg = pygame.transform.scale(bg, (800, 600))

home = pygame.image.load('home.png')
ho1 = pygame.image.load('how1.png')
ho2 = pygame.image.load('how2.png')

r1l1 = pygame.image.load('r1l1.jpeg')
# r1l1 = pygame.transform.scale(r1l1, (800, 600))
#icon = pygame.image.load('.png')
#pygame.display.set_icon(icon)
font = pygame.font.SysFont('comicsans', 40)


class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

def how1(screen):
    running = True
    prev1 = button((203,254,51),373,69,100,37,'BACK')
    next1 = button((203,254,51),816,69,100,37,'NEXT') 
    while running:
        screen.fill((255,255,255))
        screen.blit(ho1, (0,0))
        prev1.draw(screen, (0,0,0))
        next1.draw(screen, (0,0,0))
        # mainscreen image and start button
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if prev1.isOver(pos):
                        main_menu(screen)
                        print('Back Clicked')
                    if next1.isOver(pos):
                        how2(screen)
                        print('Next Clicked')
            if event.type == pygame.MOUSEMOTION:
                if prev1.isOver(pos):
                    prev1.color = (255,255,255)
                else:
                    prev1.color = (203,254,51)
                if next1.isOver(pos):
                    next1.color = (255,255,255)
                else:
                    next1.color = (203,254,51)

def how2(screen):
    running = True
    prev1 = button((203,254,51),373,37,100,33,'PREV')
    while running:
        screen.fill((255,255,255))
        screen.blit(ho2, (0,0))
        prev1.draw(screen, (0,0,0))
        # mainscreen image and start button
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if prev1.isOver(pos):
                        how1(screen)
                        print('Back Clicked')
            if event.type == pygame.MOUSEMOTION:
                if prev1.isOver(pos):
                    prev1.color = (255,255,255)
                else:
                    prev1.color = (203,254,51)

def main_menu(screen):
    running = True
    start1 = button((203,254,51),759,236,192,70,'PLAY')
    how = button((203,254,51),537,637,200,65,'HOW TO PLAY') 
    while running:
        screen.fill((255,255,255))
        screen.blit(home, (0,0))
        start1.draw(screen, (0,0,0))
        how.draw(screen, (0,0,0))
        # mainscreen image and start button
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            # if event.type == pygame.KEYDOWN:
            #     rapidfire(screen)
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if start1.isOver(pos):
                        rapidfire(screen)
                        print('Play Clicked')
                    if how.isOver(pos):
                        how1(screen)
                        print('How to Play Clicked')
            if event.type == pygame.MOUSEMOTION:
                if start1.isOver(pos):
                    start1.color = (255,255,255)
                else:
                    start1.color = (203,254,51)
                if how.isOver(pos):
                    how.color = (255,255,255)
                else:
                    how.color = (203,254,51)
    pygame.display.quit()

def rapidfire(screen):
    question1(screen)

    # running = True
    # screen.blit(r1l1, (0,0))
    # pygame.display.update()
    # pygame.time.delay(5000)

    # option1 = button((255,255,255),28,536,300,50,'Option 1')
    # option2 = button((255,255,255),28,596,300,50,'Option 2')
    # option3 = button((255,255,255),440,536,300,50,'Option 3')
    # option4 = button((255,255,255),440,596,300,50,'Option 4')

    # counter, text = 5, '5'
    # pygame.time.set_timer(pygame.USEREVENT, 1000)
    
    # while running:
    #     screen.fill((255,255,255))
    #     screen.blit(bg, (0,0))
    #     option1.draw(screen, (0,0,0))
    #     option2.draw(screen, (0,0,0))
    #     option3.draw(screen, (0,0,0))
    #     option4.draw(screen, (0,0,0))
    #     for event in pygame.event.get():
    #         pos = pygame.mouse.get_pos()
    #         if event.type == pygame.USEREVENT:                    
    #             text = str(counter) if counter > 0 else ''
    #             counter -= 1
    #             # if counter < 0:
    #             #     counter = 5
    #             # if counter == 0:
    #             #     main_menu(screen)
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             if option1.isOver(pos):
    #                 print('Option 1 Selected')
    #             if option2.isOver(pos):
    #                 print('Option 2 Selected')
    #             if option3.isOver(pos):
    #                 print('Option 3 Selected')
    #             if option4.isOver(pos):
    #                 print('Option 4 Selected')


    #         if event.type == pygame.MOUSEMOTION:
    #             if option1.isOver(pos):
    #                 option1.color = (0,255,0)
    #             else:
    #                 option1.color = (255,255,255)
    #             if option2.isOver(pos):
    #                 option2.color = (0,255,0)
    #             else:
    #                 option2.color = (255,255,255)
    #             if option3.isOver(pos):
    #                 option3.color = (0,255,0)
    #             else:
    #                 option3.color = (255,255,255)
    #             if option4.isOver(pos):
    #                 option4.color = (0,255,0)
    #             else:
    #                 option4.color = (255,255,255)    
    #         if event.type == pygame.QUIT:
    #             running = False
    #             pygame.quit()
    #             quit()
    #     font1 = pygame.font.SysFont('comicsans', 35)
    #     font2 = pygame.font.SysFont('comicsans', 35)
    #     screen.blit(font1.render(text, True, (0, 0, 0)), (73, 52))
    #     screen.blit(font2.render(ques1, True, (0, 0, 0)), (602, 38))
    #     pygame.display.update()
    #     clock.tick(60)
    
def question1(screen):
    running = True
    ques1 = '1. Physics'
    q1a = 'a) Refractive Index'
    q1b = 'b) Gravity '
    q1c = 'c) Isaac Newton'
    q1d = 'd) None'

    option1 = button((255,255,255),28,536,300,50,q1a)
    option2 = button((255,255,255),28,596,300,50,q1b)
    option3 = button((255,255,255),440,536,300,50,q1c)
    option4 = button((255,255,255),440,596,300,50,q1d)

    
    
    counter, text = 5, '5'
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    flag = 0
    flag2 = 0

    while running:
        screen.fill((255,255,255))
        screen.blit(bg, (0,0))
        option1.draw(screen, (0,0,0))
        option2.draw(screen, (0,0,0))
        option3.draw(screen, (0,0,0))
        option4.draw(screen, (0,0,0))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.USEREVENT:                    
                text = str(counter) if counter > 0 else ''
                counter -= 1
                print(counter)
                # print(counter)
                if counter == 0:
                    question2(screen)
                # if counter == 0:
                #     main_menu(screen)
            if flag2 == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if option1.isOver(pos):
                        option1.color = (255,0,0)
                        flag = 1
                        flag2 =1
                        print('Option 1 Selected')
                    if option2.isOver(pos):
                        option2.color = (255,0,0)
                        flag = 1
                        flag2 =1
                        print('Option 2 Selected')
                    if option3.isOver(pos):
                        option3.color = (0,255,0)
                        pygame.display.update()
                        global points 
                        points= points + 1
                        print(points)
                        flag = 1
                        flag2 =1
                        print('Option 3 Selected')
                    if option4.isOver(pos):
                        option4.color = (255,0,0)
                        flag = 1
                        flag2 =1
                        print('Option 4 Selected')
            
                
            if flag == 0:
                if event.type == pygame.MOUSEMOTION:
                    if option1.isOver(pos):
                        option1.color = (192,192,192)
                    else:
                        option1.color = (255,255,255)
                    if option2.isOver(pos):
                        option2.color = (192,192,192)
                    else:
                        option2.color = (255,255,255)
                    if option3.isOver(pos):
                        option3.color = (192,192,192)
                    else:
                        option3.color = (255,255,255)
                    if option4.isOver(pos):
                        option4.color = (192,192,192)
                    else:
                        option4.color = (255,255,255)    
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        font1 = pygame.font.SysFont('comicsans', 35)
        font2 = pygame.font.SysFont('comicsans', 65)
        font3 = pygame.font.SysFont('comicsans', 45)
        screen.blit(font1.render(text, True, (0, 0, 0)), (73, 52))
        screen.blit(font2.render(ques1, True, (0, 0, 0)), (100,302))
        point = str(points)
        screen.blit(font2.render(point, True, (0, 0, 0)), (602,35))
        pygame.display.update()
        clock.tick(60)

def question2(screen):
    running = True
    ques2 = '2. Metalloids'
    q2a = 'a) Graphite '
    q2b = 'b) Silicon '
    q2c = 'c) Periodic Table'
    q2d = 'd) None'

    option1 = button((255,255,255),28,536,300,50,q2a)
    option2 = button((255,255,255),28,596,300,50,q2b)
    option3 = button((255,255,255),440,536,300,50,q2c)
    option4 = button((255,255,255),440,596,300,50,q2d)

    
    
    counter, text = 5, '5'
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    flag = 0
    flag2 = 0
    

    while running:
        screen.fill((255,255,255))
        screen.blit(bg, (0,0))
        option1.draw(screen, (0,0,0))
        option2.draw(screen, (0,0,0))
        option3.draw(screen, (0,0,0))
        option4.draw(screen, (0,0,0))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.USEREVENT:                    
                text = str(counter) if counter > 0 else ''
                counter -= 1
                # print(counter)
                if counter == 0:
                    question3(screen)
            if flag2 == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if option1.isOver(pos):
                        option1.color = (255,0,0)
                        flag = 1
                        flag2 =1
                        print('Option 1 Selected')
                    if option2.isOver(pos):
                        option2.color = (255,0,0)
                        flag = 1
                        flag2 =1
                        print('Option 2 Selected')
                    if option3.isOver(pos):
                        option3.color = (0,255,0)
                        global points 
                        points= points + 1
                        print(points)
                        flag = 1
                        flag2 =1
                        print('Option 3 Selected')
                    if option4.isOver(pos):
                        option4.color = (255,0,0)
                        flag = 1
                        flag2 =1
                        print('Option 4 Selected')
            if flag == 0:
                if event.type == pygame.MOUSEMOTION:
                    if option1.isOver(pos):
                        option1.color = (192,192,192)
                    else:
                        option1.color = (255,255,255)
                    if option2.isOver(pos):
                        option2.color = (192,192,192)
                    else:
                        option2.color = (255,255,255)
                    if option3.isOver(pos):
                        option3.color = (192,192,192)
                    else:
                        option3.color = (255,255,255)
                    if option4.isOver(pos):
                        option4.color = (192,192,192)
                    else:
                        option4.color = (255,255,255)    
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        font1 = pygame.font.SysFont('comicsans', 35)
        font2 = pygame.font.SysFont('comicsans', 65)
        font3 = pygame.font.SysFont('comicsans', 45)
        screen.blit(font1.render(text, True, (0, 0, 0)), (73, 52))
        screen.blit(font2.render(ques2, True, (0, 0, 0)), (100,302))
        point = str(points)
        screen.blit(font2.render(point, True, (0, 0, 0)), (602,35))
        pygame.display.update()
        clock.tick(60)

def question3(screen):
    running = True
    ques3 = '3. Government'
    q3a = 'a) Narendra Modi'
    q3b = 'b) Law'
    q3c = 'c) College'
    q3d = 'd) All of the above'

    option1 = button((255,255,255),28,536,300,50,q3a)
    option2 = button((255,255,255),28,596,300,50,q3b)
    option3 = button((255,255,255),440,536,300,50,q3c)
    option4 = button((255,255,255),440,596,300,50,q3d)

    
    
    counter, text = 5, '5'
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    flag = 0
    flag2 = 0
    

    while running:
        screen.fill((255,255,255))
        screen.blit(bg, (0,0))
        option1.draw(screen, (0,0,0))
        option2.draw(screen, (0,0,0))
        option3.draw(screen, (0,0,0))
        option4.draw(screen, (0,0,0))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.USEREVENT:                    
                text = str(counter) if counter > 0 else ''
                counter -= 1
                # print(counter)
                if counter == 0:
                    question4(screen)
            if flag2 == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if option1.isOver(pos):
                        option1.color = (255,0,0)
                        flag = 1
                        flag2 =1
                        print('Option 1 Selected')
                    if option2.isOver(pos):
                        option2.color = (0,255,0)
                        global points 
                        points= points + 1
                        print(points)
                        flag = 1
                        flag2 =1
                        print('Option 2 Selected')
                    if option3.isOver(pos):
                        option3.color = (255,0,0)
                        flag = 1
                        flag2 =1
                        print('Option 3 Selected')
                    if option4.isOver(pos):
                        option4.color = (255,0,0)
                        flag = 1
                        flag2 =1
                        print('Option 4 Selected')
            if flag == 0:
                if event.type == pygame.MOUSEMOTION:
                    if option1.isOver(pos):
                        option1.color = (192,192,192)
                    else:
                        option1.color = (255,255,255)
                    if option2.isOver(pos):
                        option2.color = (192,192,192)
                    else:
                        option2.color = (255,255,255)
                    if option3.isOver(pos):
                        option3.color = (192,192,192)
                    else:
                        option3.color = (255,255,255)
                    if option4.isOver(pos):
                        option4.color = (192,192,192)
                    else:
                        option4.color = (255,255,255)    
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        font1 = pygame.font.SysFont('comicsans', 35)
        font2 = pygame.font.SysFont('comicsans', 65)
        font3 = pygame.font.SysFont('comicsans', 45)
        screen.blit(font1.render(text, True, (0, 0, 0)), (73, 52))
        screen.blit(font2.render(ques3, True, (0, 0, 0)), (100,302))
        point = str(points)
        screen.blit(font2.render(point, True, (0, 0, 0)), (602,35))
        pygame.display.update()
        clock.tick(60)

def question4(screen):
    running = True
    ques4 = '4. Continents'
    q4a = 'a) Asia'
    q4b = 'b) Water'
    q4c = 'c) India'
    q4d = 'd) America'

    option1 = button((255,255,255),28,536,300,50,q4a)
    option2 = button((255,255,255),28,596,300,50,q4b)
    option3 = button((255,255,255),440,536,300,50,q4c)
    option4 = button((255,255,255),440,596,300,50,q4d)

    
    
    counter, text = 5, '5'
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    flag = 0
    flag2 = 0
    

    while running:
        screen.fill((255,255,255))
        screen.blit(bg, (0,0))
        option1.draw(screen, (0,0,0))
        option2.draw(screen, (0,0,0))
        option3.draw(screen, (0,0,0))
        option4.draw(screen, (0,0,0))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.USEREVENT:                    
                text = str(counter) if counter > 0 else ''
                counter -= 1
                # print(counter)
                if counter == 0:
                    question5(screen)
            if flag2 == 0: 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if option1.isOver(pos):
                        option1.color = (0,255,0)
                        global points 
                        points= points + 1
                        print(points)
                        flag = 1
                        flag2 = 1
                        print('Option 1 Selected')
                    if option2.isOver(pos):
                        option2.color = (255,0,0)
                        flag = 1
                        flag2 = 1
                        print('Option 2 Selected')
                    if option3.isOver(pos):
                        option3.color = (255,0,0)
                        flag = 1
                        flag2 = 1
                        print('Option 3 Selected')
                    if option4.isOver(pos):
                        option4.color = (255,0,0)
                        flag = 1
                        flag2 = 1
                        print('Option 4 Selected')
            if flag == 0:
                if event.type == pygame.MOUSEMOTION:
                    if option1.isOver(pos):
                        option1.color = (192,192,192)
                    else:
                        option1.color = (255,255,255)
                    if option2.isOver(pos):
                        option2.color = (192,192,192)
                    else:
                        option2.color = (255,255,255)
                    if option3.isOver(pos):
                        option3.color = (192,192,192)
                    else:
                        option3.color = (255,255,255)
                    if option4.isOver(pos):
                        option4.color = (192,192,192)
                    else:
                        option4.color = (255,255,255)    
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        font1 = pygame.font.SysFont('comicsans', 35)
        font2 = pygame.font.SysFont('comicsans', 65)
        font3 = pygame.font.SysFont('comicsans', 45)
        screen.blit(font1.render(text, True, (0, 0, 0)), (73, 52))
        screen.blit(font2.render(ques4, True, (0, 0, 0)), (100,302))
        point = str(points)
        screen.blit(font2.render(point, True, (0, 0, 0)), (602,35))
        pygame.display.update()
        clock.tick(60)

def question5(screen):
    running = True
    ques5 = '5. Family'
    q5a = 'a) Love'
    q5b = 'b) Support & Strength'
    q5c = 'c) Parents'
    q5d = 'd) Fun'

    option1 = button((255,255,255),28,536,300,50,q5a)
    option2 = button((255,255,255),28,596,300,50,q5b)
    option3 = button((255,255,255),440,536,300,50,q5c)
    option4 = button((255,255,255),440,596,300,50,q5d)

    
    
    counter, text = 5, '5'
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    flag = 0
    flag2 = 0
    

    while running:
        screen.fill((255,255,255))
        screen.blit(bg, (0,0))
        option1.draw(screen, (0,0,0))
        option2.draw(screen, (0,0,0))
        option3.draw(screen, (0,0,0))
        option4.draw(screen, (0,0,0))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.USEREVENT:                    
                text = str(counter) if counter > 0 else ''
                counter -= 1
                # print(counter)
                # if counter == 0:
                #     question3(screen)
            if flag2 == 0: 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if option1.isOver(pos):
                        option1.color = (255,0,0)
                        
                        flag = 1
                        flag2 = 1
                        print('Option 1 Selected')
                    if option2.isOver(pos):
                        option2.color = (0,255,0)
                        global points 
                        points= points + 1
                        print(points)
                        flag = 1
                        flag2 = 1
                        print('Option 2 Selected')
                    if option3.isOver(pos):
                        option3.color = (255,0,0)
                        flag = 1
                        flag2 = 1
                        print('Option 3 Selected')
                    if option4.isOver(pos):
                        option4.color = (255,0,0)
                        flag = 1
                        flag2 = 1
                        print('Option 4 Selected')
            if flag == 0:
                if event.type == pygame.MOUSEMOTION:
                    if option1.isOver(pos):
                        option1.color = (192,192,192)
                    else:
                        option1.color = (255,255,255)
                    if option2.isOver(pos):
                        option2.color = (192,192,192)
                    else:
                        option2.color = (255,255,255)
                    if option3.isOver(pos):
                        option3.color = (192,192,192)
                    else:
                        option3.color = (255,255,255)
                    if option4.isOver(pos):
                        option4.color = (192,192,192)
                    else:
                        option4.color = (255,255,255)    
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        font1 = pygame.font.SysFont('comicsans', 35)
        font2 = pygame.font.SysFont('comicsans', 65)
        font3 = pygame.font.SysFont('comicsans', 45)
        screen.blit(font1.render(text, True, (0, 0, 0)), (73, 52))
        screen.blit(font2.render(ques5, True, (0, 0, 0)), (100,302))
        point = str(points)
        screen.blit(font2.render(point, True, (0, 0, 0)), (602,35))
        pygame.display.update()
        clock.tick(60)
    
main_menu(screen)        