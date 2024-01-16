import pygame
import random

#Blob Game https://www.mathsisfun.com/games/blob-game.html
#Collaboration between Azad K. and Ethan R.

maxx = 7
maxy = 7
bsize = 75
dif = 5
p1 = []
p2=[]
border = [0,1,2,3,4,5,6,7,13,14,20,21,27,28,34,35,41,42,43,44,45,46,47,48]
r = True
abc = 0
win = 0
white = (255,255,255)
gray = (192,192,192)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue=(0,0,255)
gameover = False
turn = random.randint(1,2)

def make_board():
  global board
  board= [1] * dif + [2] * dif +[0]*((maxx*maxy)-2*dif)
  random.shuffle(board)
  for x in range(maxx):
      for y in range(maxy):
          pos = y*maxx+x
          if pos in border:
              board[pos] = 3
  for i in range(maxx):
      board.append(i)

          

  

def draw_board():
  p1.clear()
  p2.clear()
  for y in range(maxy):
    for x in range(maxx):
      pos = y*maxx+x 
      if board[pos]==0:
        c = gray
      elif board[pos]==1:
        c = red
        if pos not in p1:
             p1.append(pos)
      elif board[pos] == 2:
        c = blue
        if pos not in p2:
            p2.append(pos)
      elif board[pos] == 3:
          c = green
      pygame.draw.rect(screen,c,(x*bsize,y*bsize,bsize,bsize))
      pygame.draw.rect(screen,black,(x*bsize,y*bsize,bsize,bsize),2)
      # value = afont.render(str(pos), True, black)
      # screen.blit(value, [x*bsize+50, y*bsize+50])

pygame.init()
afont = pygame.font.SysFont("comicsansms", 15)
 
window_width=bsize*maxx    
window_height= bsize*maxy

screen = pygame.display.set_mode((window_width, window_height + 50))

def score(p1,p2):
    pygame.draw.rect(screen,black,(0,window_height,window_width,50))
    a = afont.render("P1 score " + str(p1), True, red)
    b = afont.render("P2 score " + str(p2), True, blue)
    if turn == 2:
        c = afont.render("Its blue's turn!" , True, blue)
    elif turn == 1:
        c = afont.render("Its red's turn!" , True, red)
    if win == 0:
     screen.blit(a, [5,window_height+25])
     screen.blit(b, [190,window_height+25])
     screen.blit(c, [400,window_height+25])
    elif win == 1: 
        c = afont.render("Red wins!" , True, red)
        screen.blit(c, [400,window_height+25])
    elif win == 2:
        c = afont.render("Blue wins!" , True, blue)
        screen.blit(c, [400,window_height+25])
    pygame.display.flip()

def close_borders():
   line = 0
   for y in range(maxy):
    for x in range(maxx):
        pos = y*maxx+x
        if board[pos]:
            board[pos]=3

make_board()


while gameover == False:
  draw_board()
  for event in pygame.event.get():      
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    if turn == 1:
     if event.type == pygame.KEYDOWN:
          #P1 is arrow
          #P2 is WASD
          if event.key == pygame.K_LEFT:
              turn = 2
              for i in p1:
                if i-1 in border:
                    if board[i] == 1:
                        board[i] = 0
                    
                else:
                    if board[i]==1:
                        board[i]=0
                        board[i -1] = 1
          elif event.key == pygame.K_RIGHT:
              turn = 2
              for i in p1:
                if i+1 in border:
                    if board[i] == 1:
                        board[i] = 0
                    
                else:
                    if board[i]==1:
                        board[i]=0
                        board[i + 1] = 1
          elif event.key == pygame.K_UP:
              turn = 2
              for i in p1:
                if i-maxy in border:
                    if board[i] == 1:
                        board[i] = 0
                    
                else:
                    if board[i]==1:
                        board[i]=0
                        board[i - maxy] = 1
          elif event.key == pygame.K_DOWN:
              turn = 2
              for i in p1:
                if i+maxy in border:
                    if board[i] == 1:
                        board[i] = 0
                else:
                    if board[i]==1:
                        board[i]=0
                        board[i + maxy] = 1
                            
    if turn == 2:
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_a:
              turn = 1
              for i in p2:
                if i-1 in border:
                    if board[i] == 2:
                        board[i] = 0
                else:
                    if board[i]==2:
                        board[i]=0
                        board[i -1] = 2
          elif event.key == pygame.K_d:
              turn = 1
              for i in p2:
                if i+1 in border:
                    if board[i] == 2:
                        board[i] = 0
                
                else:
                    if board[i]==2:
                        board[i]=0
                        board[i + 1] = 2
          elif event.key == pygame.K_w:
              turn = 1
              for i in p2:
                if i-maxy in border:
                    if board[i] == 2:
                        board[i] = 0
                    
                else:
                    if board[i]==2:
                        board[i]=0
                        board[i -maxy] = 2
          elif event.key == pygame.K_s:
              turn = 1
              for i in p2:
                if i + maxy in border:
                    if board[i] == 2:
                        board[i] = 0
                    
                else:
                    if board[i]==2:
                        board[i]=0
                        board[i + maxy] = 2
          elif event.key == pygame.K_SPACE:
              print(p1,'||',p2)


      

  if len(p1) == 0:
      gameover = True
      win = 2
  elif len(p2) == 0:
      gameover = True
      win = 1
  draw_board()
  score(len(p1),len(p2))
  pygame.display.flip()