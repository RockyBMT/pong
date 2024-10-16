import pygame
pygame.init()

BLACK =(0,0,0)
WHITE =(255,255,255)

size=(800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PONG")

clock = pygame.time.Clock()

font = pygame.font.SysFont('Calibri', 50, True, False)
font2 = pygame.font.SysFont('Calibri', 25, True, False)


done = False
xspeed=-3
yspeed=3
x_coord=385
y_coord=285

pscore=0
cscore=0

mainmenu=True

aix = 760
aiy = 0
aiyspeed=0

px=10
py=0
pspeed=0
tim=0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done =True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and py <= 500:
                pspeed+=6
            elif event.key== pygame.K_UP and py>= -1:
                pspeed-=6
            elif event.key== pygame.K_SPACE:
                mainmenu=False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pspeed = 0
            elif event.key == pygame.K_UP:
                pspeed = 0
    if mainmenu== True:
        screen.fill(BLACK)
        menutext= font.render("PONG",True,WHITE)
        screen.blit(menutext, [330, 20])
        menutext= font2.render("Made by Boris Tchakarski",True,WHITE)
        screen.blit(menutext, [265, 100])
        menutext= font.render("Press Space to Start",True,WHITE)
        screen.blit(menutext, [190, 400])
    else:
        score1 = font.render(str(pscore),True,WHITE)
        score2 = font.render(str(cscore),True,WHITE)
        if py> 500:
            py=499
        if py<-1:
            py=0
        if py < 500 and py> -1:
            py+=pspeed
        if y_coord > aiy+30:
            aiyspeed =5
        elif y_coord<aiy+30:
            aiyspeed=-5
        if x_coord >= 800:
            x_coord=385
            y_coord=285
            tim=0
            xspeed=-3
            pscore+=1
            #xspeed=-3-tim
        elif x_coord <= 0:
            x_coord=385
            y_coord=285
            tim=0
            xspeed=-3
            #xspeed=3+tim
            cscore+=1
        if y_coord >= 590:
            yspeed=-3-tim
        elif y_coord <= 0:
            yspeed=3+tim
        elif x_coord <= 40 and y_coord >=py and y_coord<=py+100:
            tim+=0.3
            xspeed=3+tim
        elif x_coord >= 750 and y_coord >=aiy and y_coord<=aiy+100:
            tim+=0.3
            xspeed=-3-tim
        aiy+=aiyspeed
        x_coord+= xspeed
        y_coord+=yspeed
        screen.fill(BLACK)
        pygame.draw.rect(screen,WHITE,[x_coord,y_coord,10,10],0)
        pygame.draw.rect(screen,WHITE,[px,py,30,100],0)
        pygame.draw.rect(screen,WHITE,[aix,aiy,30,100],0)
        pygame.draw.rect(screen,WHITE,[397,0,6,600],0)

        screen.blit(score1, [325, 20])
        screen.blit(score2, [450, 20])

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()