import random
import time

TEMP_LIMIT = 30

for i in range(10):
    temperature = random.randint(20, 40)

    print("Temperature:", temperature, "°C")

    if temperature > TEMP_LIMIT:
        print("ALERT: High Temperature Detected!")
        print("Action: Cooling System ON")
    else:
        print("Status: Normal")
        print("Action: Cooling System OFF")

    print("-------------------")
    time.sleep(2)