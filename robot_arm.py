#20211159 Nguyen Thao Nhi
#Project 1. Robot Arm

# utils.py
import pygame
import numpy as np

def getRegularPolygon(N, radius=1):
    v = np.zeros((N,2))
    for i in range(N):
        deg = i * 360. / N
        rad = deg * np.pi / 180.
        x = radius * np.cos(rad)
        y = radius * np.sin(rad)
        v[i] = [x, y]
    return v

def getRectangle(width, height, x=0, y=0):
    points = np.array([ [0, 0], 
                        [width, 0], 
                        [width, height], 
                        [0, height]], dtype='float')
    points = points + np.array([x, y], dtype='float')

    return points

def get_circle(radius):
    return np.array([[0, 0], [0, radius]], dtype='float')

def get_triangle(point1, point2, point3):
    return np.array([point1, point2, point3], dtype='float')

def get_line(point1, point2):
    return np.array([point1, point2], dtype='float')

def Rmat(degree):
    # Rotation Matrix
    # Counter-clockwise rotation
    radian = np.deg2rad(degree)
    c = np.cos(radian)
    s = np.sin(radian)
    R = np.array([ [c, -s, 0], 
                   [s, c, 0], 
                   [0, 0, 1]], dtype='float')
    return R 

def Tmat(tx, ty):
    # Translation Matrix
    # Ma trận tịnh tiến.
    T = np.array([ [1, 0, tx], 
                   [0, 1, ty], 
                   [0, 0, 1]], dtype='float')
    return T 


def draw(screen, M, points, color=(0,0,0), p0=None, filled=False):
    R = M[0:2, 0:2]
    t = M[0:2, 2]

    points_transformed = ( R @ points.T ).T + t
    if filled:
        pygame.draw.polygon(screen, color, points_transformed)
    else:
        pygame.draw.polygon(screen, color, points_transformed, 2)
    if p0 is not None:
        pygame.draw.line(screen, (0,0,0), p0, points_transformed[0])

def draw_circle(screen, M, points, radius, color=(0,0,0), p0=None):
    R = M[0:2, 0:2]
    t = M[0:2, 2]

    p_transformed = (R @ points.T).T + t
    pygame.draw.circle(screen, color, p_transformed[0], radius)
    if p0 is not None:
        pygame.draw.line(screen, (0,0,0), p0, p_transformed[1])
    return p_transformed

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 800

# 색 정의
GREEN = (100, 200, 100)

pygame.init()  # 1! initialize the whole pygame system!
pygame.display.set_caption("Robot arm")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

center=(WINDOW_WIDTH/2., WINDOW_HEIGHT/2.)

center1 = [100, 300.]

angles = [0 for i in range(4)]

angles[0] = 20
width1 = 300
height1 = 100
rect1 = getRectangle(width1, height1)

gap12 = 30 #

angles[1] = 0
width2 = 280
height2 = 70
rect2 = getRectangle(width2, height2)

angles[2] = 0
width3 = 400
height3 = 150
rect3 = getRectangle(width3, height3)

# Create a gripper, with 2 parts create from 2 rectangles
# The gripper is attached to the end of the robot arm
# The gripper is controlled by one angle
gripper_width = 10
gripper_height = 30
gripper_points1 = getRectangle(gripper_height, gripper_width)
gripper_points2 = getRectangle(gripper_height, -gripper_width)

MAX_GRIPPER_ANGLE = 115
MIN_GRIPPER_ANGLE = 55
angle_gripper_between = 90
gripper_on = False

index_current_angle = 0
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse Button Pressed!")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if index_current_angle >= 0:
                    index_current_angle -= 1
            elif event.key == pygame.K_RIGHT:
                if index_current_angle + 1 < len(angles):
                    index_current_angle += 1
            elif event.key == pygame.K_UP:
                angles[index_current_angle] -= 5
            elif event.key == pygame.K_DOWN:
                angles[index_current_angle] += 5
            elif event.key == pygame.K_SPACE:
                gripper_on = not gripper_on
        #
    screen.fill(GREEN)

    if gripper_on and angle_gripper_between > MIN_GRIPPER_ANGLE:
        angle_gripper_between -= 1
    if not gripper_on and angle_gripper_between < MAX_GRIPPER_ANGLE:
        angle_gripper_between += 1
    
    # draw Robot Arm
    # Red rectangle
    M1 = np.eye(3) @ Tmat(center1[0], center1[1]) @ Rmat(angles[0]) @ Tmat(0, -height1/2.)
    draw(screen, M1, rect1, (255, 0, 0))
    # Yellow rectangle
    M2 = M1 @ Tmat(width1, 0) @ Tmat(0, height1/2.) @ Tmat(gap12, 0) @ Rmat(angles[1]) @ Tmat(0, -height2/2.)
    draw(screen, M2, rect2, (255, 255, 0))
    # pygame.draw.circle(screen, (0,0,0), center1, 4)
    
    # Green rectangle
    M3 = M2 @ Tmat(width2, 0) @ Tmat(0, height2/2.) @ Tmat(gap12, 0) @ Rmat(angles[2]) @ Tmat(0, -height3/2.)
    draw(screen, M3, rect3, (0, 255, 0))
    # pygame.draw.circle(screen, (0,0,0), center1, 4)

    C = M1 @ Tmat(width1, 0) @ Tmat(0, height1/2.)
    center2 = C[0:2, 2]
    pygame.draw.circle(screen, (0,0,0), center2, 5)
    # print("C ---")
    # print(C) 
    
    C1 = C @ Tmat(gap12, 0)
    center3 = C1[0:2, 2]
    pygame.draw.circle(screen, (0,0,0), center3, 5)
    # print("C2 -----")
    # print(C2)
    
    pygame.draw.line(screen, (0,0,0), center2, center3, 1)
    
    C2 = M2 @ Tmat(width2, 0) @ Tmat(0, height2/2.)
    center4 = C2[0:2, 2]
    pygame.draw.circle(screen, (0,0,0), center4, 5)

    C3 = C2 @ Tmat(gap12, 0)
    center5 = C3[0:2, 2]
    pygame.draw.circle(screen, (0,0,0), center5, 5)

    pygame.draw.line(screen, (0,0,0), center4, center5, 1)

    C4 = M3 @ Tmat(width3, 0) @ Tmat(0, height3/2.)
    center6 = C4[0:2, 2]
    pygame.draw.circle(screen, (0,0,0), center6, 5)

    C5 = C4 @ Tmat(gap12, 0)
    center7 = C5[0:2, 2]
    pygame.draw.circle(screen, (0,0,0), center7, 5)

    pygame.draw.line(screen, (0,0,0), center6, center7, 1)

    # Upper part of gripper
    M_gripper_up = Tmat(center7[0], center7[1]) @ Rmat(angles[3]-angle_gripper_between/2)
    draw(screen, M_gripper_up, gripper_points1, (0,0,0), filled=True)
    M_gripper = M_gripper_up @ Tmat(gripper_height, 0) @ Rmat(50) # @ Tmat(-gripper_width, -gripper_height)
    # draw(screen, M_gripper, gripper_points, (0,0,0))
    draw(screen, M_gripper, gripper_points1, (0,0,0), filled=True)

    # # Lower part of gripper
    M_gripper_down = Tmat(center7[0], center7[1]) @ Rmat(angles[3]+angle_gripper_between/2) # @ Tmat(-gripper_width, -gripper_height)
    draw(screen, M_gripper_down, gripper_points2, (0,0,0), filled=True)
    M_gripper_2 = M_gripper_down @ Tmat(gripper_height, 0) @ Rmat(-50) # @ Tmat(-gripper_width, -gripper_height)
    draw(screen, M_gripper_2, gripper_points2, (0,0,0), filled=True)
    
    # update screen
    pygame.display.flip()
    clock.tick(60)

# 게임 종료
pygame.quit()
