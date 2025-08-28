#!/usr/bin/env python3
"""
Robot Dog Dance Routine
A fun dance sequence using the available control functions
"""

import time
from Control import *
from Buzzer import *

def robot_dance():
    """
    Main dance routine with multiple movements and 5 repetitions each
    """
    print("🤖 Starting Robot Dog Dance! 🕺")
    
    # Start with a musical buzzer beat
    dance_music()
    
    # Dance Sequence 1: Forward-Backward Groove (5 reps)
    print("Movement 1: Forward-Backward Groove")
    for i in range(5):
        forward()
        time.sleep(0.3)
        backWard()
        time.sleep(0.3)
        print(f"  Groove step {i+1}/5")
    
    # Brief pause with attitude adjustment
    attitude(0, 0, 0)  # Reset position
    time.sleep(0.5)
    
    # Dance Sequence 2: Side Shuffle (5 reps each direction)
    print("Movement 2: Side Shuffle")
    for i in range(5):
        setpLeft()
        time.sleep(0.4)
        print(f"  Left shuffle {i+1}/5")
    
    for i in range(5):
        setpRight()
        time.sleep(0.4)
        print(f"  Right shuffle {i+1}/5")
    
    # Dance Sequence 3: Spinning Action (5 reps each direction)
    print("Movement 3: Spinning Action")
    for i in range(5):
        turnLeft()
        time.sleep(0.3)
        print(f"  Left spin {i+1}/5")
    
    # Brief pause
    time.sleep(0.5)
    
    for i in range(5):
        turnRight()
        time.sleep(0.3)
        print(f"  Right spin {i+1}/5")
    
    # Dance Sequence 4: Body Wave (5 reps)
    print("Movement 4: Body Wave")
    for i in range(5):
        # Roll left and right
        attitude(15, 0, 0)   # Roll right
        time.sleep(0.3)
        attitude(-15, 0, 0)  # Roll left
        time.sleep(0.3)
        attitude(0, 0, 0)    # Center
        time.sleep(0.2)
        print(f"  Body wave {i+1}/5")
    
    # Dance Sequence 5: Up-Down Bounce (5 reps)
    print("Movement 5: Up-Down Bounce")
    for i in range(5):
        upAndDown()  # This should adjust height
        time.sleep(0.4)
        print(f"  Bounce {i+1}/5")
    
    # Dance Sequence 6: Forward-Backward Lean (5 reps)
    print("Movement 6: Forward-Backward Lean")
    for i in range(5):
        beforeAndAfter()  # Body forward/backward movement
        time.sleep(0.4)
        print(f"  Lean {i+1}/5")
    
    # Dance Sequence 7: Pitch Dance (5 reps)
    print("Movement 7: Pitch Dance")
    for i in range(5):
        attitude(0, 20, 0)   # Pitch up
        time.sleep(0.3)
        attitude(0, -20, 0)  # Pitch down
        time.sleep(0.3)
        attitude(0, 0, 0)    # Center
        time.sleep(0.2)
        print(f"  Pitch move {i+1}/5")
    
    # Dance Sequence 8: Yaw Wiggle (5 reps)
    print("Movement 8: Yaw Wiggle")
    for i in range(5):
        attitude(0, 0, 25)   # Yaw right
        time.sleep(0.3)
        attitude(0, 0, -25)  # Yaw left
        time.sleep(0.3)
        attitude(0, 0, 0)    # Center
        time.sleep(0.2)
        print(f"  Yaw wiggle {i+1}/5")
    
    # Final Sequence: Complex Combo (5 reps)
    print("Movement 9: Grand Finale Combo")
    for i in range(5):
        # Complex movement combining multiple actions
        forward()
        time.sleep(0.2)
        attitude(10, 0, 15)  # Roll and yaw
        time.sleep(0.3)
        turnLeft()
        time.sleep(0.2)
        attitude(-10, 0, -15) # Opposite roll and yaw
        time.sleep(0.3)
        backWard()
        time.sleep(0.2)
        attitude(0, 0, 0)    # Reset
        time.sleep(0.2)
        print(f"  Finale combo {i+1}/5")
    
    # End with a flourish
    print("Movement 10: Victory Pose")
    attitude(0, 15, 0)  # Proud pitch up pose
    victory_music()
    time.sleep(2)
    
    # Return to neutral position
    attitude(0, 0, 0)
    stop()
    
    print("🎉 Dance complete! Robot dog is ready for applause! 🎉")

def dance_music():
    """
    Create a musical intro with the buzzer
    """
    print("🎵 Playing intro music...")
    for i in range(8):
        run(1)  # Buzzer on
        time.sleep(0.1)
        run(0)  # Buzzer off
        time.sleep(0.1)

def victory_music():
    """
    Victory sound sequence
    """
    print("🎵 Victory music!")
    for i in range(3):
        run(1)
        time.sleep(0.3)
        run(0)
        time.sleep(0.1)
        run(1)
        time.sleep(0.1)
        run(0)
        time.sleep(0.2)

def quick_dance():
    """
    A shorter version of the dance for testing
    """
    print("🤖 Quick Dance Test!")
    
    # Forward-back (3 reps)
    for i in range(3):
        forward()
        time.sleep(0.3)
        backWard()
        time.sleep(0.3)
    
    # Left-right (3 reps each)
    for i in range(3):
        setpLeft()
        time.sleep(0.4)
    for i in range(3):
        setpRight()
        time.sleep(0.4)
    
    # Spins (3 reps each)
    for i in range(3):
        turnLeft()
        time.sleep(0.3)
    for i in range(3):
        turnRight()
        time.sleep(0.3)
    
    # Body attitude finale
    attitude(15, 15, 15)
    time.sleep(1)
    attitude(0, 0, 0)
    stop()
    
    print("✅ Quick dance complete!")

if __name__ == "__main__":
    try:
        # Ask user which dance to perform
        print("Robot Dog Dance Options:")
        print("1. Full Dance Routine (about 2-3 minutes)")
        print("2. Quick Dance Test (about 30 seconds)")
        
        choice = input("Enter your choice (1 or 2): ").strip()
        
        if choice == "1":
            robot_dance()
        elif choice == "2":
            quick_dance()
        else:
            print("Invalid choice. Running quick dance...")
            quick_dance()
            
    except KeyboardInterrupt:
        print("\n🛑 Dance interrupted by user")
        stop()
        run(0)  # Make sure buzzer is off
    except Exception as e:
        print(f"❌ Error during dance: {e}")
        stop()
        run(0)  # Make sure buzzer is off
