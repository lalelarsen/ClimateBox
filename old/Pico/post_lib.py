import network
import urequests
import time

# Replace with your Wi-Fi credentials
SSID = "CableBox-EA99"
PASSWORD = "emmkdzy2yz"
last_posted_time = 0

# Connect to Wi-Fi
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to network...')
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            time.sleep(1)
    print('Connected!')

# Make POST request
def post_data(data, timed):

    current_time = time.time()
    global last_posted_time
    
    if(current_time - last_posted_time >= timed or last_posted_time == 0):
        last_posted_time = current_time
        url = "http://192.168.0.25:5000/submit"  # Replace with your server URL
        headers = {'Content-Type': 'application/json'}
        data = str(data)  # Example JSON payload

        try:
            response = urequests.post(url, data=data, headers=headers)
            print('Response:', response.text)
            response.close()
        except Exception as e:
            print('Error making POST request:', e)

