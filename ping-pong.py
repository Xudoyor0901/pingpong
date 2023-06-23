import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ping Pong")

# Set up the paddles
paddle1 = pygame.Rect(50, 250, 10, 100)
paddle2 = pygame.Rect(740, 250, 10, 100)

# Set up the ball
ball = pygame.Rect(395, 295, 10, 10)
ball_speed = [5, 5]

# Set up the score
score1 = 0
score2 = 0
font = pygame.font.Font(None, 50)

# Game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball.move_ip(ball_speed)

    # Handle collisions
    if ball.bottom >= 600 or ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball.left <= 0:
        score2 += 1
        ball.center = (395, 295)
        ball_speed = [5, 5]
    if ball.right >= 800:
        score1 += 1
        ball.center = (395, 295)
        ball_speed = [5, 5]
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed[0] = -ball_speed[0]

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.move_ip(0, -5)
    if keys[pygame.K_s] and paddle1.bottom < 600:
        paddle1.move_ip(0, 5)
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.move_ip(0, -5)
    if keys[pygame.K_DOWN] and paddle2.bottom < 600:
        paddle2.move_ip(0, 5)

    # Draw the screen
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), paddle1)
    pygame.draw.rect(screen, (255, 255, 255), paddle2)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    score_text = font.render(f"{score1} : {score2}", True, (255, 255, 255))
    screen.blit(score_text, (350, 50))
    pygame.display.flip()

# Quit Pygame
pygame.quit()
