import pygame
import time
import random

pygame.init()
# Định nghĩa một số màu sử dụng trong trò chơi
black = (0, 0, 0)
red = (213, 50, 80)
blue = (50, 153, 213)
# Định nghĩa kích thước của cửa sổ trò chơi
dis_width = 800
dis_height = 650
#Hình nền 
background = pygame.image.load('background.png')
# Tạo cửa sổ trò chơi với kích thước và tiêu đề tương ứng
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game-Nhóm 2')
dis.blit(background, (0,0))
bg_width, bg_height = background.get_size()
x = dis_width/2 - bg_width/2  
y = dis_height/2 - bg_height/2
dis.blit(background, (x, y)) 
# Khởi tạo đối tượng clock để giới hạn tốc độ khung hình của trò chơi
clock = pygame.time.Clock()
# Định nghĩa kích thước của mỗi khối con rắn và tốc độ di chuyển của rắn
snake_block = 30
snake_speed = 8
apple_block = 30
block_size = snake_block
#Hình trái táo
apple_image = pygame.transform.scale(pygame.image.load('Apple.png'), (apple_block, apple_block))
#Đầu rắn
# 333 Hình ảnh đầu rắn 
head_img = pygame.image.load('headSNAKE.png')
head_img = pygame.transform.scale(head_img, (block_size, block_size)) 
# Đuôi rắn
body1_img = pygame.image.load('body.png')
body1_img = pygame.transform.scale(body1_img, (block_size, block_size)) 
body_imgs=[body1_img]

#leg_img = pygame.transform.scale(leg_img, (block_size, block_size)) 

# Định nghĩa font chữ cho điểm số và thông báo trò chơi
font_style = pygame.font.SysFont(None, 50) 
score_font = pygame.font.SysFont(None, 35)


def Your_score(score):
     # Hiển thị điểm số lên màn hình
    value = score_font.render("Your Score: " + str(score), True, red)
    dis.blit(value, [0, 0])

def show_high_score():
   high_score = get_high_score()
   value = score_font.render("High Score: " + str(high_score), True, green)
   dis.blit(value, [0, 50])

def save_score(score):
   # Khai báo hàm lưu high score:
  with open('highscore.txt', 'w') as f:
    f.write(str(score))

#Kiểm tra high score mới và cập nhật nếu cao hơn:
def get_high_score():
   try:
      with open('highscore.txt', 'r') as f:
         return int(f.read())
   except: 
      return 0

def update_high_score(score):
   high_score = get_high_score()
   if score > high_score:
    save_score(score)


# Khởi tạo đối tượng clock để giới hạn tốc độ khung hình của trò chơi
clock = pygame.time.Clock()

# Định nghĩa font chữ cho điểm số và thông báo trò chơi
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

#def our_snake(snake_block, snake_list):
    # Vẽ rắn lên màn hình ver0
    # #for x in snake_list:
    #    #pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 # Vẽ rắn lên màn hình ver1 tọa độ 1;2
    #for x in snake_list:
        #pygame.draw.rect(dis, black, [x[1], x[2], snake_block, snake_block]) 
# 333
    # Tạo phần tử mới
 

def our_snake(snake_block, snake_list):
  # Vẽ từng phần tử trong danh sách rắn  
  # for i, x in enumerate(snake_list):  
  for i in range(len(snake_list)-1, -1, -1):
    x = snake_list[i]  
    if i == len(snake_list)-1:  
      # Đầu rắn sẽ ở phần tử đầu
      dis.blit(head_img, (x[0], x[1]))
    else:  
      # Vẽ cho thân rắn
      if i > 0:
        img = random.choice(body_imgs)
        dis.blit(img, (x[0], x[1]))

      else:
      # Vẽ thân, đuôi 
        pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    # Hiển thị thông báo lên màn hình
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def draw():
   #dis.fill(blue) # Làm mới màn hình trước khi vẽ
     # Load background mỗi lần vẽ
   background = pygame.image.load('background.png')  
   dis.blit(background, (0,0))
   pygame.display.update()

def gameLoop():
    #Khai báo biến sử dụng snake_speed.
    global snake_speed
    global high_score
    game_over = False
    game_close = False
    # Khởi tạo vị trí ban đầu của đầu rắn
    x1 = dis_width / 2
    y1 = dis_height / 2
    # Khởi tạo thay đổi vị trí ban đầu của rắn
    x1_change = 0
    y1_change = 0
    # Khởi tạo danh sách chứa các khối của rắn và độ dài ban đầu của rắn
    snake_List = []
    Length_of_snake = 1
    # Đặt vị trí ngẫu nhiên của thức ăn ban đầu
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    while not game_over:
        while game_close:
            # Vòng lặp khi trò chơi kết thúc
            draw()
            dis.blit(apple_image, (foodx, foody))
            our_snake(snake_block, snake_List) 
            #dis.fill(blue)
            message("You lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            show_high_score()
            pygame.display.update()
            # Xử lý sự kiện khi người chơi nhấn nút
            for event in pygame.event.get():
                # Xử lý sự kiện khi người chơi nhấn nút
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        snake_speed = 10
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            # Kiểm tra nếu rắn chạm vào biên màn hình, kết thúc trò chơi
            game_close = True
        x1 += x1_change
        y1 += y1_change
        draw()
        dis.blit(apple_image, (foodx, foody))
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            # Kiểm tra nếu rắn tự cắn vào mình, kết thúc trò chơi
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        update_high_score(Length_of_snake - 1)
        high_score = get_high_score()
        pygame.display.update()

        if foodx <= x1 <= foodx + apple_block and foody <= y1 <= foody + apple_block:
        # Kiểm tra nếu rắn ăn thức ăn, tăng điểm và đặt lại vị trí của thức ăn
            foodx = round(random.randrange(0, dis_width - apple_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - apple_block) / 10.0) * 10.0
            #snake_List.reverse()
            
            Length_of_snake += 5
             
    # Tăng tốc +1 mỗi lần ăn được mồi
            snake_speed += 5
            
        clock.tick(snake_speed)     
    
    while not game_over:
   #game logic
        show_high_score()
        # Cập nhật high score 
        update_high_score(Length_of_snake - 1)
        draw()
        dis.blit(apple_image, (foodx, foody))
        our_snake(snake_block, snake_List) 


    pygame.quit()
    high_score = get_high_score()
    save_score(high_score)

gameLoop()
