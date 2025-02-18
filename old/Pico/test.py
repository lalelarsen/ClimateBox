from rotary_irq_rp2 import RotaryIRQ
import time

start_time = time.time()
run_time = 20

rotary_encoder = RotaryIRQ(pin_num_clk=12, 
              pin_num_dt=13, 
              min_val=0, 
              max_val=3, 
              reverse=False, 
              range_mode=RotaryIRQ.RANGE_WRAP)
            
val_old = rotary_encoder.value()

while time.time() < (start_time+run_time):
    
    print(rotary_encoder.value())
    
    time.sleep(0.2)