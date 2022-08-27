import pygame
import random

pygame.init()               # 초기화 (중요)

# 화면 크기 설정
screen_width = 600          # 가로 
screen_height = 600         # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 회면 타이틀 설정
pygame.display.set_caption("DUDU")               # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("dudu.png") 
# 캐릭터1 이미지 불러오기
character = pygame.image.load("dddd.png")
# 빈공간 이미지 불러오기
groundPiece = pygame.image.load("duduground.png")

# 두더지 생성 개수
duTotal = 3
du_r_list = []

# 한두더지 땅 사이즈
duduPieceSize = 200

# 두더지 잡은 횟수(점수)
score = 0
# 두더지 점수판 폰트
moveFont = pygame.font.Font(None, 30)

# 두더지 변환속도 조절
time_count = 0

# 아래 두더지 위치들의 공식
# character1_size = character1.get_rect().size              # 이미지의 크기를 구해옴
# character1_width = character1_size[0]              # 캐릭터의 가로 크기
# character1_height = character1_size[1]
# character_x_pos = ((screen_width / 3) / 2) - (character1_width / 2) 
# character_y_pos = ((screen_height / 3) / 2) - (character1_height / 2)

character_x_list = [25, 225, 425, 25, 225, 425, 25, 225, 425]                       #  두더지 사진 x좌표
character_y_list = [25, 25, 25, 225, 225, 225, 425, 425, 425]

# character_list = [character ,character ,character ,character ,character ,character ,character ,character ,character]

# 이벤트 루프
running = True              # 게임이 진행 중인가?
while running:
       for event in pygame.event.get():          # 어떤 이벤트가 발생하였는가?
              if event.type == pygame.QUIT:             # 창이 단히는 이벤트가 발생하였는가?
                     running = False             # 게임이 진행 중이 아님
              elif event.type == pygame.MOUSEBUTTONDOWN:              # 마우스 버튼이 눌렸을 때
                     if event.button == 1:
                            mouseXPos= event.pos[0] // duduPieceSize                # 마우스 X값, Y값 구하기
                            mouseYPos = event.pos[1] // duduPieceSize
                            dudugroundPos = mouseXPos + 3 * mouseYPos               # (X 값의 규칙성을 공식)두더지 위치와 일치시키기 mn\\
                            if dudugroundPos in du_r_list:                      # 마우스가 두더지 위라면 두더지 삭제
                                   print("DUDU CUT")
                                   score += 100
                                   du_r_list.remove(dudugroundPos)
                            else:
                                   print("ISN'T DUDU")

       screen.blit(background, (0,0))            # 배경 그리기

       while len(du_r_list) < duTotal:                  # 두더지 3마리 중복되지 않게 생성
              a = random.randint(0,8)
              if not(a in du_r_list):
                     du_r_list.append(a)                # 랜덤값 3개를 두더지 리스트로 포함

       for i in range(9):
              if i in du_r_list:
                     screen.blit(character, (character_x_list[i], character_y_list[i]))           # 반복문으로 랜덤값에만 두더지 그리기
              else:
                     screen.blit(groundPiece, (character_x_list[i], character_y_list[i]))         # 배경조각 그리기
       #screen.blit(character1, (character_x_list[0], character_y_list[0])) 

       scoreText = moveFont.render("POINT : " + str(score) ,True,(255,255,255))                # 출력글, 글자색상 정의
       screen.blit(scoreText ,(15, 10))                            # 점수판 그리기

       pygame.display.update()            # 게임화면을 다시 그리기

       pygame.time.delay(100)
       time_count += 1
       if time_count > 8:
              du_r_list.clear()
              time_count = 0

pygame.quit()               # pygame 종료