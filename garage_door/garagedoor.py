import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BCM)

TRIG = 24
ECHO = 23
MAX_DISTANCE = int(input("Enter the number of feet for trigger: ")) * 12

def main():
    try:
        print("")
        print("Distance measurement in progress...")
        pin_setup()
        print("Waiting for sensor")
        time.sleep(1)
        print("Starting Loop...")
        distance = get_distance()
        time.sleep(1)
        while distance < MAX_DISTANCE:
            distance = get_distance()
            print(f"Distance: {distance}in")
            if distance > MAX_DISTANCE:
                print("Door is open...")
                distance = send_notification("garage_open", distance)
                send_notification("garage_closed", distance)
            time.sleep(1)
    except KeyboardInterrupt:
        print("KeyboardInterrupt raised. Exiting...")
    except ValueError:
        print("ValueError. Exiting...")
    finally:
        GPIO.cleanup()


def pin_setup():
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.output(TRIG, False)
    
    
def get_distance()
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150 / 2.54
    return round(distance, 2)


def send_notification(event, distance):
    r = requests.post(f"https://maker.ifttt.com/trigger/{event}/with/key/dyfnszqFl0wfKtRnjhQh_I",
                      params={"value1":f"{distantce}"})
    time.sleep(1)
    while distance > MAX_DISTANCE:
        distance = get_distance()
        time.sleep(1)
    return distance
