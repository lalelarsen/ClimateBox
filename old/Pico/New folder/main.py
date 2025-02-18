from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from rotary_irq_rp2 import RotaryIRQ
from display_lib import handleMenu
import time

# Initialize I2C for the OLED display (GPIO 4 = SDA, GPIO 5 = SCL)
i2c = I2C(0, scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c)


# Define menu options and corresponding numbers
menu_options = ["Option 1", "Option 2", "Option 3", "Option 4"]
option_numbers = [42, 99, 123, 7]  # Numbers associated with each option
current_option = 0  # Start at the first menu option
in_menu = True  # Start in the menu view
in_pause_mode = False

start_time = time.time()
run_time = 30

while time.time() < (start_time+run_time):
    
    handleMenu()
    #print(rotary_encoder.value())
    time.sleep(0.1)

