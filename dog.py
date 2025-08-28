# Robot Dance Routine - "The Electric Shuffle"
# Using the provided robot control functions

import time
from Buzzer import *
from Control import *
from Led import *
from Servo import *

def robot_dance():
    """
    A choreographed dance routine combining movement, lights, and sound
    Each movement repeated 5+ times for substantial motion as requested
    """
    
    # Initialize components
    print("🤖 Starting Robot Dance: 'The Electric Shuffle' 🎵")
    
    # === INTRO: Light Show ===
    print("🌈 Intro: Rainbow light show...")
    for i in range(3):
        rainbowCycle(strip, 100)  # Rainbow breathing effect
        time.sleep(0.5)
    
    # === VERSE 1: Forward March with Beat ===
    print("🎵 Verse 1: Forward March...")
    for rep in range(8):  # 8 reps for substantial forward movement
        forward()
        time.sleep(0.3)
        run(1)  # Buzzer beat
        time.sleep(0.2)
        ledIndex(0, 255, 0, 0)  # Red LED flash
        time.sleep(0.1)
        ledIndex(0, 0, 0, 0)    # LED off
    stop()
    
    # === CHORUS: Spin Dance ===
    print("🌀 Chorus: The Spin Spectacular...")
    # Right spin sequence
    for rep in range(6):  # 6 reps for full rotation effect
        turnRight()
        time.sleep(0.3)
        theaterChaseRainbow(strip, 50)  # Chase lights during spin
        run(1)  # Buzzer on beat
        time.sleep(0.2)
    stop()
    
    # Brief pause with attitude adjustment
    attitude(0, 0, 180)  # Dramatic pose
    time.sleep(0.5)
    
    # Left spin sequence  
    for rep in range(6):  # 6 reps for full counter-rotation
        turnLeft()
        time.sleep(0.3)
        LED_TYPR(255, 255, 0)  # Yellow chase during left spins
        run(0)  # Different buzzer tone
        time.sleep(0.2)
    stop()
    
    # === VERSE 2: Side Steps ===
    print("⬅️➡️ Verse 2: Side Step Groove...")
    for rep in range(5):  # 5 reps each direction
        # Step right sequence
        setpRight()
        time.sleep(0.4)
        ledIndex(1, 0, 255, 0)  # Green LED
        time.sleep(0.1)
        
        # Step left sequence  
        setpLeft()
        time.sleep(0.4)
        ledIndex(1, 0, 0, 255)  # Blue LED
        run(1)
        time.sleep(0.1)
    
    # === BRIDGE: Body Wave ===
    print("🌊 Bridge: Body Wave...")
    for rep in range(4):  # 4 wave cycles
        # Wave up
        upAndDown()
        time.sleep(0.3)
        attitude(15, 0, 0)  # Slight forward tilt
        rainbowCycle(strip, 80)
        time.sleep(0.2)
        
        # Wave down
        upAndDown()  
        time.sleep(0.3)
        attitude(-15, 0, 0)  # Slight backward tilt
        time.sleep(0.2)
    
    # Return to neutral
    attitude(0, 0, 0)
    
    # === FINAL CHORUS: Backward Moonwalk ===
    print("🌙 Final: Robot Moonwalk...")
    LED_TYPR(255, 255, 255)  # White spotlights
    for rep in range(7):  # 7 reps for dramatic backward movement
        backWard()
        time.sleep(0.4)
        run(1)  # Steady beat
        time.sleep(0.1)
        run(0)
        time.sleep(0.1)
    stop()
    
    # === GRAND FINALE ===
    print("🎆 Grand Finale: 360 Light Spectacular...")
    
    # Final spin with full light show
    for rep in range(8):  # 8 spins for full rotation
        turnRight()
        time.sleep(0.25)
        
        # Cycling through different light patterns
        if rep % 4 == 0:
            rainbowCycle(strip, 50)
        elif rep % 4 == 1:
            theaterChaseRainbow(strip, 30)
        elif rep % 4 == 2:
            LED_TYPR(255, 0, 0)  # Red
        else:
            LED_TYPR(0, 255, 0)  # Green
            
        run(1)
        time.sleep(0.1)
    
    # Final pose
    stop()
    attitude(0, 0, 0)  # Return to center
    
    # Victory light show
    for i in range(5):
        rainbowCycle(strip, 30)
        run(1)
        time.sleep(0.2)
        run(0)
        time.sleep(0.2)
    
    # All lights off, final buzzer flourish
    ledIndex(0, 0, 0, 0)
    run(1)
    time.sleep(0.5)
    run(0)
    
    print("🎉 Dance complete! The robot has performed 'The Electric Shuffle'!")

# Optional: Individual dance move functions for modular choreography

def robot_wave(reps=5):
    """Body wave movement"""
    for i in range(reps):
        upAndDown()
        attitude(10, 0, 0)
        time.sleep(0.3)
        upAndDown()
        attitude(-10, 0, 0) 
        time.sleep(0.3)
    attitude(0, 0, 0)

def spin_combo(direction='right', reps=6):
    """Spinning combination with lights"""
    turn_func = turnRight if direction == 'right' else turnLeft
    for i in range(reps):
        turn_func()
        theaterChaseRainbow(strip, 50)
        run(1)
        time.sleep(0.3)
    stop()

def march_forward(reps=5):
    """Forward marching with rhythm"""
    for i in range(reps):
        forward()
        ledIndex(i % 2, 255, 0, 0)  # Alternating LEDs
        run(1)
        time.sleep(0.4)
    stop()

# Execute the main dance routine
if __name__ == "__main__":
    robot_dance()
