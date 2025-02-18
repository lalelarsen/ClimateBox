import time


time_on = 0
last_time = 0
duty_length = 0

def getDuty(pulse_length, latest_duty_length):
    global time_on
    global last_time
    global duty_length

    current_time = time.time()
    
    if(time_on == 0):
        duty_length = latest_duty_length
        time_on = duty_length * pulse_length
        last_time = current_time

        return 1
    
    if(current_time - last_time <= time_on):
        return 1
    
    if(current_time - last_time <= duty_length):
        return 0
    else:
        duty_length = latest_duty_length
        time_on = duty_length * pulse_length
        last_time = current_time
        return 1

def getPulseLength(value, error_post_gain_max):
    return min(max(value/error_post_gain_max, 0), 1)

