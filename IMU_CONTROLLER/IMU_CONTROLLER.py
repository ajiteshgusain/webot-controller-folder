from controller import Robot, Keyboard, GPS, InertialUnit

robot = Robot()
TIME_STEP = 64

# --- Setup Motors ---
wheels = []
wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
for i in range(4):
    wheels.append(robot.getDevice(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)

# --- Setup Sensors ---
gps = robot.getDevice("global")
gps.enable(TIME_STEP)

imu = robot.getDevice("imu") 
imu.enable(TIME_STEP)

keyboard = Keyboard()
keyboard.enable(TIME_STEP)

print("System Initialized: GPS, IMU, and Teleoperation are active.")

# --- Main Loop ---
while robot.step(TIME_STEP) != -1:
    # 1. Handle Keyboard Movement
    key = keyboard.getKey()
    leftSpeed = 0.0
    rightSpeed = 0.0
    
    if key == Keyboard.UP:
        leftSpeed, rightSpeed = 2.0, 2.0
    elif key == Keyboard.DOWN:
        leftSpeed, rightSpeed = -2.0, -2.0
    elif key == Keyboard.LEFT:
        leftSpeed, rightSpeed = -1.0, 1.0
    elif key == Keyboard.RIGHT:
        leftSpeed, rightSpeed = 1.0, -1.0
    
    # Apply velocities (Fixed missing parenthesis here)
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)
    
    # 2. Get GPS Coordinates
    pos = gps.getValues()
    
    # 3. Get IMU Readings
    angles = imu.getRollPitchYaw() 
    
    # Print data to console
    print(f"GPS: X:{pos[0]:.2f} Y:{pos[1]:.2f} Z:{pos[2]:.2f} | " 
          f"IMU Yaw: {angles[2]:.2f}")
          