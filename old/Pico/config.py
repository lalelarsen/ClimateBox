import time

upload_data = True

# Humidity
currentHumidity = 0
targetHumidity = 30

# Temperature
duty_length = 10
currentTemperature = 0
targetTemperature = 37
error_post_gain_max = 70

Kp = 6.5 # Proportional gain
Ki = 0.0035 # Integral gain
Kd = 10 # Derivative gain

integral_frequence = 2
integral = 0

def getTargetTemperature():
    global targetTemperature
    return targetTemperature
def getTargetHumidity():
    global targetHumidity
    return targetHumidity

def setTargetTemperature(value):
    global targetTemperature
    targetTemperature = value
def setTargetHumidity(value):
    global targetHumidity
    targetHumidity = value

last_integral_calculation_time = 0
def calculateIntegral(value):
    current_time = time.time()
    global last_integral_calculation_time
    
    if(current_time - last_integral_calculation_time >= integral_frequence or last_integral_calculation_time == 0):
        global integral
        integral += value

    return integral
