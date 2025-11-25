# emulator.py
import time, json, random, requests
from datetime import datetime, timezone

API_URL = "http://127.0.0.1:8000/telemetry"
vehicle_id = "corolla_2019"

def generate_point():
    rpm = random.randint(700, 2500)
    speed = random.randint(0, 70)
    coolant = random.randint(120, 200)
    return {
        "ts": datetime.now(timezone.utc).isoformat(),
        "vehicle_id": vehicle_id,
        "rpm": rpm,
        "coolant_temp_c": coolant,
        "speed_mph": speed
    }

if __name__ == "__main__":
    while True:
        point = generate_point()
        try:
            r = requests.post(API_URL, json=point, timeout=2)
            print("sent", r.status_code, point)
        except Exception as e:
            print("error sending:", e)
        time.sleep(1)
