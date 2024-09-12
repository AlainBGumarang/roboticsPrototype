# ----------------------------------------------------------------------------- #
#                                                                               #        
#    Project:        Right-Hand Arcade Control                                  #
#    Module:         main.py                                                    #
#    Author:         VEX                                                        #
#    Created:        Fri Aug 05 2022                                            #
#    Description:    This example will use the right X/Y Controller             #
#                    axis to control the Clawbot.                               #
#                                                                               #                                                                          
#    Configuration:  V5 Clawbot (Individual Motors)                             #
#                    Controller                                                 #
#                    Left Motors in Ports 11, 20                                #
#                    Right Motors in Ports 1, 10                                #
#                    Arm Motor in Port 9                                        #
#                    Claw Motor in Port 2                                       #
#                    Balance Motor in Port 8                                    #
#                                                                               #                                                                          
# ----------------------------------------------------------------------------- #

# Library imports
from vex import *
MAX_SPEED = 50
# Brain should be defined by default
brain=Brain()

# Robot configuration code
# Arm motor, claw motor, and controller
claw_motor = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
arm_motor = Motor(Ports.PORT9, GearSetting.RATIO_18_1, False)
controller_1 = Controller(PRIMARY)

# Drive motors and balance motor
left_drive_1 = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
left_drive_2 = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
right_drive_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
right_drive_2 = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
motorUpandDown = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)

# setup the claw motor
claw_motor.set_max_torque(25, PERCENT)
claw_motor.set_stopping(HOLD)

# setup the arm motor
arm_motor.set_stopping(HOLD)

# Begin project code
# Main Controller loop to set motors to controller axis postiions
while True:
    # Controlling arm and claw
    control_l1  = (controller_1.buttonL1.pressing() - controller_1.buttonL2.pressing()) * MAX_SPEED
    control_r1  = (controller_1.buttonR1.pressing() - controller_1.buttonR2.pressing()) * MAX_SPEED
    control_l2  = (controller_1.buttonUp.pressing() - controller_1.buttonDown.pressing()) * MAX_SPEED
    control_r2  = (controller_1.buttonA.pressing() - controller_1.buttonB.pressing()) * MAX_SPEED

    control_A = (controller_1.buttonA.pressing() - controller_1.buttonB.pressing()) * MAX_SPEED
    control_B = (controller_1.buttonB.pressing() - controller_1.buttonA.pressing()) * MAX_SPEED

    # Controlling movement of robot
    left_drive_1.set_velocity((controller_1.axis3.position() + controller_1.axis1.position()), PERCENT)
    right_drive_1.set_velocity((controller_1.axis3.position() - controller_1.axis1.position()), PERCENT)
    left_drive_2.set_velocity((controller_1.axis3.position() + controller_1.axis1.position()), PERCENT)
    right_drive_2.set_velocity((controller_1.axis3.position() - controller_1.axis1.position()), PERCENT)

    left_drive_1.spin(FORWARD)
    left_drive_2.spin(FORWARD)
    right_drive_1.spin(FORWARD)
    right_drive_2.spin(FORWARD)

    # Claw and Arm motors
    arm_motor.spin(FORWARD, control_l1, PERCENT)
    claw_motor.spin(FORWARD, control_r1, PERCENT)

    motorUpandDown.spin(FORWARD, control_A, PERCENT)

    wait(5, MSEC)
