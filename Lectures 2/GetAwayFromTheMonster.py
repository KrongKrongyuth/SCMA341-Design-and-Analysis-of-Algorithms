import pygame
import math


pygame.init()
clock = pygame.time.Clock()
dt = clock.tick(60)

size = (1000, 700)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Circle Following Cursor")
radius = 300
smallRadius = 3
human_speed = 0.005/2
monster_speed = 0.00108/2

x = size[0] / 2
y = size[1] / 2

human_x = x
human_y = y

mon_x = x+radius
mon_y = y

pool_color = (0, 150, 200)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    mouse_x, mouse_y = pygame.mouse.get_pos()
    distance = ((mouse_x - x) ** 2 + (mouse_y - y) ** 2) ** 0.5

    screen.fill((255, 255, 255))
    
    pygame.draw.circle(screen, pool_color, (int(x), int(y)), int(radius), 0)
    pygame.draw.circle(screen, (0, 50, 50), (int(x), int(y)), 5, 0)


    # Mouse is too far away from center
    if distance > 1.7*radius:
        human_x = x
        human_y = y
    
    # human is out of the pool, can run extremely fast
    elif ((human_x - x) ** 2 + (human_y - y) ** 2) ** 0.5> radius: 
        unit = math.sqrt((mouse_x - human_x)**2 + (mouse_y - human_y)**2 )
        human_x = human_x + 10*human_speed*dt * (mouse_x - human_x)/unit
        human_y = human_y + 10*human_speed*dt * (mouse_y - human_y)/unit
    
    # human is in the pool, swim at normal speed
    else: 
        unit = math.sqrt((mouse_x - human_x)**2 + (mouse_y - human_y)**2 )
        human_x = human_x + human_speed*dt * (mouse_x - human_x)/unit
        human_y = human_y + human_speed*dt * (mouse_y - human_y)/unit
    pygame.draw.circle(screen, (255, 0, 0), (int(human_x), int(human_y)), int(smallRadius), 0)
    
    
    


    goalMon_x = 0
    goalMon_y = 0
    
    
    unit = math.sqrt((human_x - x)**2 + (human_y - y)**2 )
    if unit != 0 :
        goalMon_x = (human_x - x) * radius/unit + x
        goalMon_y = (human_y - y) * radius/unit + y
    
    
    # find target angle
    target_angle  = math.atan2(((human_y - y)),((human_x - x)+0.01))
    
    # choose direction
    current_angle = math.atan2(((mon_y - y)),((mon_x - x)+0.01))
    diff_angle = target_angle - current_angle + 4*math.pi
    
    while diff_angle > 2*math.pi:
        diff_angle -= 2*math.pi
        
    
    if diff_angle < 2*math.pi-diff_angle:
        mon_angle = current_angle + monster_speed 
    
    else:
        mon_angle = current_angle - monster_speed 
    
    
    mon_x = math.cos(mon_angle)*radius + x
    mon_y = math.sin(mon_angle)*radius + y
    
    pygame.draw.circle(screen, (255, 0, 0), (int(mon_x), int(mon_y)), int(3*smallRadius), 0)
    
    
    
    
    caught = math.sqrt((mon_x - human_x)**2+(mon_y-human_y)**2)
    if caught < 2:
        pool_color = (255, 0, 0)
    
    if distance < 30:
        pool_color = (0, 150, 200)
    
    pygame.display.flip()


pygame.quit()