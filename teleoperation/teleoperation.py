from controller import Robot, Keyboard

# Initialize the robot
robot = Robot()

# Set up the simulation time step (64ms is standard)
TIME_STEP = 64

# --- Setup Motors ---
# Ensure the 'name' field of each RotationalMotor in your Scene Tree
# matches exactly 'wheel1', 'wheel2', 'wheel3', and 'wheel4'
wheels = []
wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
for i in range(4):
    wheels.append(robot.getDevice(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)

# --- Setup Distance Sensors ---
ds = []
dsNames = ['ds_right', 'ds_left']
for i in range(2):
    ds.append(robot.getDevice(dsNames[i]))
    ds[i].enable(TIME_STEP)

# --- Setup Keyboard ---
keyboard = Keyboard()
keyboard.enable(TIME_STEP)

print("Teleoperation Started: Use Arrow Keys to move.")

# --- Main Loop ---
while robot.step(TIME_STEP) != -1:
    # Read the keyboard input
    key = keyboard.getKey()
    
    # Optional: Print key to console if pressed
    if key != -1:
        print(f"Key pressed: {key}")

    # Initialize speeds
    leftSpeed = 0.0
    rightSpeed = 0.0
    
    # Check key codes and map to movement
    if key == Keyboard.UP:
        leftSpeed = 2.0
        rightSpeed = 2.0
    elif key == Keyboard.DOWN:
        leftSpeed = -2.0
        rightSpeed = -2.0
    elif key == Keyboard.LEFT:
        leftSpeed = -1.0
        rightSpeed = 1.0
    elif key == Keyboard.RIGHT:
        leftSpeed = 1.0
        rightSpeed = -1.0
    
    # Apply velocities to motors
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)
    
    # Read and print sensor values to the Console
    left_val = ds[0].getValue()
    right_val = ds[1].getValue()
    
    # This print statement helps you calibrate your sensors
    print(f"Left Sensor: {left_val:.2f} | Right Sensor: {right_val:.2f}")