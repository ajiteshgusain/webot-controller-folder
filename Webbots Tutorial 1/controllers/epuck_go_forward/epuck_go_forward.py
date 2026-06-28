from controller import Robot, Motor

# Match this to your WorldInfo basicTimeStep
TIME_STEP = 16 

robot = Robot()

leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')

# Set position to infinity for continuous rotation
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

# Set the velocity (speed)
leftMotor.setVelocity(2.0)
rightMotor.setVelocity(2.0)

# Main loop
while robot.step(TIME_STEP) != -1:
    pass