# !python3

# Exercise 31 - Karvonen Heart Rate

def calculate_heart_rate(a,rh):
    intensity = 55
    print("Resting pulse: {} Age: {}".format(rh,a))
    while intensity < 100:
        targetHeartRate = round((((220 - a) - rh) * intensity / 100) + rh)
        print("Intensity: {}% ----------- Rate: {}bpm" . format(intensity, targetHeartRate))
        intensity += 5

age = int(input("What is your age?: \n"))
resting_heart_rate = int(input("What is your resting heart rate?: \n"))

calculate_heart_rate(age, resting_heart_rate)
