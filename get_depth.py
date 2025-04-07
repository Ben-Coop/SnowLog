import RPi.GPIO as GPIO
import time 
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG = 23
ECHO = 24
log_fn = "depth_log.txt"

mount_height = 45 #height that the sensor is mounted (cm)
wait_interval = 10 #time between scans (seconds)

def get_depth():
    print("Distance Measurement In Progress:")
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG, False)
    print("Waiting For Sensor To Settle")
    time.sleep(2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input (ECHO)==0:
        pulse_start = time.time()
    while GPIO.input (ECHO)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance)
    print("Distance:", distance, "cm")
    print("Depth:", mount_height-distance, "cm")
    return mount_height-distance


while True:
    depth = get_depth()

    timestamp = time.strftime("%B %d, %Y %I:%M %p")
    
    # Append to depth_log.txt
    try:
        with open(log_fn, "a") as f:
            f.write(f"{timestamp}: {depth}cm\n")
        print("Appended to depth_log.txt:", timestamp, depth, "cm")
    except Exception as e:
        print("Error writing to depth_log.txt:", e)
    
    # Wait time between depth readings
    time.sleep(wait_interval)
