settings = {
    # Temperature
    "Temperature": 0,
    "Temperature_Proportional": 0,
    "Temperature_Integral": 0,
    "Temperature_Derivative": 0,
    "Temperature_kP": 0,
    "Temperature_kI": 0,
    "Temperature_kD": 0,

    # Humidity
    "Humidity": 0,
    "Humidity_Proportional": 0,
    "Humidity_Integral": 0,
    "Humidity_Derivative": 0,
    "Humidity_kP": 0,
    "Humidity_kI": 0,
    "Humidity_kD": 0,

    # Data posting (WiFi)
    "SSID": "CableBox-EA99",
    "PASSWORD": "emmkdzy2yz",

    # Pins
    "OLED_CLK": 21,
    "OLED_DT": 20,

    "Rotary_Encoder_CLK": 20,
    "Rotary_Encoder_DT": 28,
    "Rotary_Encoder_BUTTON": 27,
}

def getSettings():
    global settings
    return settings