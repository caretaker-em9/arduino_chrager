

from pyfirmata import Arduino, util
import psutil
import time

relay_pin=12
led_pin=10

board = Arduino('COM3')
board.digital[relay_pin].write(0)
board.digital[led_pin].write(0)

print("<-----cheching----->")
print("******************")
def check_board():
    board.digital[led_pin].write(1)
    time.sleep(0.3)
    board.digital[led_pin].write(0)
    time.sleep(0.2)
for i in range(10):
    check_board()
board.digital[relay_pin].write(1)
time.sleep(5)
board.digital[relay_pin].write(0)

def check_battery(relay_pin, led_pin, board):
    print("=======================================")
    print("            working !                  ")
    print("=======================================")

    while True:
        battery = psutil.sensors_battery()
        print(battery.percent)
        if battery.percent <= 25 and not battery.power_plugged:
            board.digital[relay_pin].write(1)
            board.digital[led_pin].write(1)
            

        elif battery.percent == 100 and battery.power_plugged:
            board.digital[relay_pin].write(0)
            board.digital[led_pin].write(0)

            print("""

              +------------------+  
              |                  |
              | fully charged..! |  
              |                  |
              +------------------+   
                """)
            time.sleep(5)
            if battery.power_plugged == False:
                print("-----charger disconnected-----")



        time.sleep(60)
        print(battery.percent)

check_battery(relay_pin, led_pin, board)

