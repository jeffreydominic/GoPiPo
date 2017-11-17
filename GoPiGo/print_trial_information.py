import time # Date and time information
import os.path

def print_output(initialDistance, encoder):
    # Output trial summary
    save_path = "/home/pi/Documents/GoPiGo/trial_outputs"
    fileName = 'trial_' + time.strftime("%m-%d-%Y") + "_" + time.strftime("%H-%M-%S")
    complete_name = os.path.join(save_path, fileName)
    with open(complete_name, 'w') as txt:
        print("\n\nTrial Summary\n")
        txt.write("Trial Summary\r")

        print("  Trial Information")
        print("    Date  " + time.strftime("%m/%d/%Y"))
        print("    Time  " + time.strftime("%H:%M:%S") + "\n")
        txt.write("  Trial Information")
        txt.write("    Date  " + time.strftime("%m/%d/%Y"))
        txt.write("    Time  " + time.strftime("%H:%M:%S") + "\r")

        print("  Distance Measurments")
        print("    Encoder Counts       " + str(encoder - initialDistance))
        print("    Wheel Rotations      " + str((encoder - initialDistance)/18))
        print("    Distance Travelled   %.3f m" % (((encoder - initialDistance)*0.21590)/18) + "\n")
        txt.write("  Distance Measurments")
        txt.write("    Encoder Counts       " + str(encoder - initialDistance))
        txt.write("    Wheel Rotations      " + str((encoder - initialDistance)/18))
        txt.write("    Distance Travelled   %.3f m" % (((encoder - initialDistance)*0.21590)/18) + "\r")

        print("  **Notes")
        print("    >Wheel Rotations = Encoder Counts / 18")
        print("    >Distance Travelled based on approximate wheel circumfrence of 21.590cm")
        txt.write("  **Notes")
        txt.write("    >Wheel Rotations = Encoder Counts / 18")
        txt.write("    >Distance Travelled based on approximate wheel circumfrence of 21.590cm")

        print("\n")
