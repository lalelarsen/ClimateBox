from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from rotary_irq_rp2 import RotaryIRQ
from config import getTargetTemperature, setTargetTemperature, getTargetHumidity, setTargetHumidity
import time

# Initialize I2C (adjust pins and frequency as needed for your board)
i2c = I2C(0, scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c)

# Menu options
menu_options = [
    ["Temperature", getTargetTemperature, setTargetTemperature, 1, 0, 50],
    ["Humidity", getTargetHumidity, setTargetHumidity, 1, 0, 50]
    ]
in_menu = True
in_pause_mode = True
pause_timer = time.time()
time_until_paused = 7
current_option = 0

rotary_encoder = RotaryIRQ(pin_num_clk=12, pin_num_dt=13)

# Variables to handle button debounce
last_button_press_time = time.ticks_ms()
button_cooldown = 300
encoder_button = Pin(10, Pin.IN, Pin.PULL_DOWN)

rotary_encoder.set(value=current_option, min_val=0, max_val=len(menu_options)-1, reverse=False, range_mode=RotaryIRQ.RANGE_WRAP)
current_option = rotary_encoder.value()

def handleMenu():
    global current_option, in_pause_mode, in_menu, pause_timer, time_until_paused
    oled.fill(0)
    
    if in_pause_mode:
        if rotary_encoder.value() != current_option or not encoder_button.value():
            in_pause_mode = False
    else:    
        if pause_timer+time_until_paused < time.time():
            in_pause_mode = True
        if in_menu:
            for index, option in enumerate(menu_options):
                text = "> " + option[0] if index == current_option else "  " + option[0]
                oled.text(text, 5, index*12, 1)
            
            if current_option != rotary_encoder.value():
                pause_timer = time.time()
                current_option = rotary_encoder.value()
        else:
            option = menu_options[current_option]
            option[2](rotary_encoder.value())
            oled.text(str(option[1]()), 5, 0, 1)
        
        handle_encoder_button()
    
    oled.show()
    
def handle_encoder_button():
    if not encoder_button.value():
        global in_menu, last_button_press_time, pause_timer
        pause_timer = time.time()
        current_time = time.ticks_ms()
        
        if time.ticks_diff(current_time, last_button_press_time) > button_cooldown:
            last_button_press_time = current_time  # Update last button press time
                
            if in_menu:
                in_menu = False
                option = menu_options[current_option]
                rotary_encoder.set(value=option[1](), min_val=option[4], max_val=option[5], reverse=False, range_mode=RotaryIRQ.RANGE_WRAP)
                
            else:
                in_menu = True
                rotary_encoder.set(value=current_option, min_val=0, max_val=len(menu_options)-1, reverse=False, range_mode=RotaryIRQ.RANGE_WRAP)