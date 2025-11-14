import time, random

def read_sensor():
    return {
        "temperature": round(random.uniform(20,30),2),
        "humidity": round(random.uniform(30,50),2)
    }

if __name__ == "__main__":
    while True:
        print("Sensor Data:", read_sensor())
        time.sleep(1)
