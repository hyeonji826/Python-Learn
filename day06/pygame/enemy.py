# 슈팅 게임에서 적을 등장시킨다.
# 충돌 이벤트 등을 정의한다.

from .__init__ import*
import random
# 적 우주선 클래스 정의
class Enemy(pygame.sprite.Sprite):
  def __inite__(self):
    super().__init__()

    # 적 이미지와 초기 위치 설정
    self.image=pygame.Surface((40,40))
    self.image.fill((255,0,0)) # 빨간색으로 설정

    self.rect =self.image.get_rect()

    self.gernerate()

  def gernerate(self,change_speed:bool=True):
    # 랜덤한 시작 위치 설정
    self.rect.x =random.randrange(0,760)
    self.rect.y =random.randrange(-100,-40)
    if change_speed: # 속도를 바꾸어서 위치를 이동할 것인지 여부
      # 랜덤한 이동 속도 설정
      self.speedy=random.randrange(1,3)

  def update(self):
    # 적 우주선을 아래로 이동
    self.rect.y +=self.speedy

    # 화면 아래로 나가면 다시 위에서 시작
    if self.rect.top > 600:
      self.gernerate(False)
    