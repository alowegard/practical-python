# bounce.py
#
# Exercise 1.5
ball_height = 100 # ball height in meters
bounce = 1 # number of bounces

while bounce < 11:
    ball_height = ball_height * 0.6 # ball height changes to 3/5 the current height
    print(bounce,round(ball_height,4)) # print the bounce number and the current height
    bounce += 1 
