import psutil as ps

battery = ps.sensors_battery() 

print(battery.percent)
print(battery.power_plugged)

if(not battery.power_plugged):
    if(int(battery.percent)>80):
        print("Please remove the battery")        
