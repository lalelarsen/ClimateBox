from machine import Pin, I2C
import ssd1306
# Initialize I2C (adjust pins and frequency as needed for your board)
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)  # Adjust for your board's I2C pins

# Initialize the OLED display with width=128 and height=64
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

def drawDisplay(header, value):
    # Clear the display
    oled.fill(0)
    
    
    # Draw a rectangle (optional example)
    oled.rect(1, 1, 125, 61, 1)
    oled.text("<", 6, 28, 1)
    oled.text(">", 113, 28, 1)
    oled.text("-", 32, 45, 1)
    oled.text("+", 83, 45, 1)
    oled.rect(31, 5, 66, 31, 1)
    oled.text(header, 40, 11, 1)
    oled.text(str(value), 40, 23, 1)
    
    # Show the content on the display
    oled.show()


