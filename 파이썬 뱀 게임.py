import pygame ##파이게임 모듈 임포트
import sys ##종료하기 위해서 창끄는 거
import time
import random

from pygame.locals import *

window_width = 800
window_height = 600
grid_size = 20 ##픽셀을 기준으로 하면 너무 작기 때문에 좀 더 크게
grid_width = window_width/grid_size
grid_height = window_height/grid_size

white = (255,255,255)
green = (0, 50, 0)
orange = (250, 150, 0)

up = (0,-1)
down = (0,1)
left = (-1,0)
right = (1,0)

fps = 10

class Python(object):
    def __init__(self):
        self.create()
        self.color = green

    def create(self):
        self.length = 2 ##처음 생성된 뱀의 길이
        self.positions = [((window_width)/2,(window_height)/2)] ##처음에 생성이 되고 어디에 위치 시킬것인지(중앙에 배치)
        self.direction = random.choice([up,down,left,right]) ##방향 리스트 중 랜덤으로 하나 결정 →처음에 랜덤으로 방향 설정

    def control(self, xy):
        if (xy[0] * -1, xy[1] * -1) == self.direction:
            return
        else:
            self.direction = xy

    def move(self):
        cur = self.positions[0] ##positions[0] = 뱀의 머리
        x, y = self.direction
        new = (((cur[0] + (x*grid_size))%window_width), (cur[1] + (y*grid_size))%window_height)##뱀이 윈도우 창을 넘어가지 않도록
        if new in self.positions[2:]:##뱀이 자기 자신을 먹지 못하게
            self.create()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def eat(self):
        self.length +=1

    def draw(self, surface):
        for p in self.positions:
            draw_object(surface, self.color, p)

class feed(object):
    def __init__(self):
        self.color = orange##먹이 색깔
        self.create()

    def create(self):
        self.position = (random.randint(0, grid_width - 1) * grid_size, random.randint(0, grid_height - 1) * grid_size)

    def draw(self, surface):
        draw_object(surface, self.color, self.position)

def draw_object(surface, color, pos):
    r = pygame.Rect(int((pos[0]),(pos[1])),(grid_size,grid_size))##사각형 모양을 그리기 위함
    pygame.draw.rect(surface, color, r)##사각형 그리기

def check_eat(python, feed):
    if python.positions[0] == feed.position:##뱀의 머리가 먹이의 위치와 같아졌다면
        python.eat()##파이썬이 먹이를 먹었다는 표현을 해줌
        feed.create()##먹이가 없어졌으니까 다시 먹이 생성

if __name__=="__main__":
    python = Python()
    feed = feed()
    
    pygame.init()##pygame을 초기화시켜줌 그래야 라이브러리를 쓸 수 있음
    window = pygame.display.set_mode((window_width, window_height)) ##game을 돌릴 창
    pygame.display.set_caption("Python Game")##window 이름 정해주기
    surface = pygame.Surface(window.get_size())
    surface = surface.convert()
    surface.fill(white)##바탕에 white색 채워주기
    clock = pygame.time.Clock()
    pygame.key.set_repeat(1,40)
    window.blit(surface,(0,0))

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    python.control(up)
                elif event.key == pygame.K_DOWN:
                    python.control(down)
                elif event.key == pygame.K_LEFT:
                    python.control(left)
                elif event.key == pygame.K_RIGHT:
                    python.control(right)

        surface.fill(white)
        python.move()
        check_eat(python, feed)
        speed = (fps + python.length) / 2##뱀이 점점 빨라지도록
        python.draw(surface)
        feed.draw(surface)
        window.blit(surface, (0, 0))
        pygame.display.flip()
        pygame.display.update()
        clock.tick(speed)##tick단위로 컴퓨터가 움직임
