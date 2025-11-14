import time, random

def get_price():
    return round(80 + random.uniform(-1, 1), 4)

if __name__ == "__main__":
    while True:
        print("USD/INR:", get_price())
        time.sleep(1)
