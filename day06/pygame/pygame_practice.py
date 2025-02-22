# pygame
# 간단한 게임을 만들기 위한 라이브러리로
# GUI를 몰라도 쉽게 다룰 수 있다.
# 설치
# pip install pygame
import pygame

# 레이저 클래스 호출
from laser import Laser

# 적 클래스 호출
from enemy import Enemy

class Player(pygame.sprite.Sprite):
    def __init__(self,all_sprites):
        super().__init__()
        self.all_sprites =all_sprites
        # 이미지 추가
        self.image =pygame.Surface((50,50))
        # 초록생 우주선 추가
        self.image.fill((0,255,0))
        # 객체
        self.rect = self.image.get_rect()
        self.rect.centerx =400
        self.rect.bottom =580

        # 레이저 그룹 생성
        self.lasers =pygame.sprite.Group()
        self.all_sprites.add(self.lasers)
        self.all_sprites.add(self)

    # 키보드를 입력했을 때 화면을 update하는
    # 메서드 구현
    def update(self):
                self.move()
    def move(self):
        # 키보드 입력 감지
        keys =pygame.key.get_pressed()
        # 왼쪽 화살표 키를 누르면 왼쪽으로 이동
        if keys[pygame.K_LEFT]:
            self.rect.x -= 2 # 왼쪽으로 2만큼 이동
        if keys[pygame.K_RIGHT]:
            self.rect.x += 2 # 오른쪽으로 2만큼 이동
        if keys[pygame.K_SPACE]:
            print("pressed space")
            # self.shoot()
            
    # 총 쏘는 모션을 구현하는 메서드
    def shoot(self):
        # 레이저 발사
        laser =Laser(self.rect.centerx+1,self.rect.top)
        self.lasers.add(laser)
        # all_sprites.add(laser)
    # def


if __name__=="__main__":
    # 스프라이트 그룹생성
    all_sprites = pygame.sprite.Group()
    # 게임 객체(플레이어) 초기화
    player =Player(all_sprites)
    # 플레이어를 스프라이트 그룹에 추가
    # all_sprites.add(player)
    # all_sprites.add(player.lasers)
    
    e=Enemy()
    all_sprites.add(e)

    # pygame 초기화
    pygame.init()
    # 게임화면 생성(800X600)
    width,height =800,600
    screen =pygame.display.set_mode((width,height))
    pygame.display.set_caption("Space Shooter")

    # 메인 게임 루프(반복) 실행
    running =True # 실행중인지 여부를 담을 변수
    while running:
        #이벤트 처리(게임 종료 등)
        for event in pygame.event.get():
            # 전달받은 이벤트가 QUIT이라면
            if event.type ==pygame.QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    player.shoot()

        # 모든 스프라이트 업데이트
        all_sprites.update()

        # 화면 그리기
        screen.fill((0,0,0)) # 검은색 배경
        all_sprites.draw(screen) # 스프라이트 그리기
        pygame.display.flip() # 화면 업데이트
        pass
    pygame.quit()