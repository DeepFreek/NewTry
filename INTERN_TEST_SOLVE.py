def regulator(error):
    if(error>=0):
        return 0
    else:
        return abs((0.4*error+0.006*(error**3))/25.6125)
Temperature_Sensor=0
Normal_Temperature=75
Power=0
while True:
    Temperature_Sensor=int(input())
    print(Temperature_Sensor-Normal_Temperature)
    print(regulator(Temperature_Sensor-Normal_Temperature))