# Ball directions:
# Left, Right,
# Upleft, Upright,
# Downleft, Downright
import pygame

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong!")

game_over = False

white = (255, 255, 255)
black = (0, 0, 0)

player_width = 10
player_height = 70

score = [0, 0]

# Player directions:
# Up, down
left_player_pos = [50, 100]
left_player_direction = ""
right_player_pos = [750, 100]
right_player_direction = ""
speed = 2

ball_size = 50
ball_pos = [100, 100]
ball_speed = 1
ball_direction = "left"

def update_ball_pos(direction, pos):
	if direction == "left":
		pos[0] -= ball_speed
	elif direction == "right":
		pos[0] += ball_speed

def detect_collision(player, ball):
    p_x = player[0]
    p_y = player[1]
    b_x = ball[0]
    b_y = ball[1]

    if (b_x >= p_x and b_x < (p_x + player_width)) or (p_x >= b_x and p_x < (b_x + ball_size)):
        if (b_y >= p_y and b_y < (p_y + player_width)) or (p_y >= b_y and p_y < (b_y + ball_size)):
            return True

def give_points():
	pass # For now

while not game_over:
	keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True

	if keys[pygame.K_w]:
		left_player_pos[1] -= speed
		left_player_direction = "up"

	if keys[pygame.K_s]:
		left_player_pos[1] += speed
		left_player_direction = "down"

	if keys[pygame.K_UP]:
		right_player_pos[1] -= speed
		right_player_direction = "up"

	if keys[pygame.K_DOWN]:
		right_player_pos[1] += speed
		right_player_direction = "down"

	if left_player_pos[1] < 0:
		left_player_pos[1] = 0

	if left_player_pos[1] > HEIGHT - player_height:
		left_player_pos[1] = HEIGHT - player_height

	if right_player_pos[1] < 0:
		right_player_pos[1] = 0

	if right_player_pos[1] > HEIGHT - player_height:
		right_player_pos[1] = HEIGHT - player_height

	if ball_pos[0] > WIDTH:
		score[0] += 1

	if ball_pos[0] < 0:
		score[1] += 1

	if detect_collision(left_player_pos, ball_pos):
		ball_direction = "right"

	if detect_collision(right_player_pos, ball_pos):
		ball_direction = "left"

	update_ball_pos(ball_direction, ball_pos)
	screen.fill(black)
	pygame.draw.rect(screen, white, (left_player_pos[0], left_player_pos[1], player_width, player_height))
	pygame.draw.rect(screen, white, (right_player_pos[0], right_player_pos[1], player_width, player_height))
	pygame.draw.rect(screen, white, (ball_pos[0], ball_pos[1], ball_size, ball_size))
	pygame.display.update()

pygame.quit()