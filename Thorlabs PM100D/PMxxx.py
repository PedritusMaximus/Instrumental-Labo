from datetime import datetime
import clr
from ctypes import cdll,c_long, c_ulong, c_uint32,byref,create_string_buffer,c_bool,c_char_p,c_int,c_int16,c_double, sizeof, c_voidp
from TLPM import TLPM
import time
#%%
# Find connected power meter devices.
tlPM = TLPM()
deviceCount = c_uint32()
tlPM.findRsrc(byref(deviceCount))

print("Number of found devices: " + str(deviceCount.value))
#print("")
#%%
resourceName = create_string_buffer(1024)

for i in range(0, deviceCount.value):
    tlPM.getRsrcName(c_int(i), resourceName)
#    print("Resource name of device", i, ":", c_char_p(resourceName.raw).value)
#print("")
tlPM.close()

# Connect to last device.
tlPM = TLPM()
tlPM.open(resourceName, c_bool(True), c_bool(True))

message = create_string_buffer(1024)
tlPM.getCalibrationMsg(message)
print("Connected to device", i)
print("Last calibration date: ",c_char_p(message.raw).value)
#print("")

time.sleep(1)
#%%
# Set wavelength in nm.
wavelength = c_double(1064)
tlPM.setWavelength(wavelength)
#wave = tlPM.getWavelength(0,1064)
#print(wave)

# Enable auto-range mode.
# 0 -> auto-range disabled
# 1 -> auto-range enabled
tlPM.setPowerAutoRange(c_int16(1))

# Set power unit to Watt.
# 0 -> Watt
# 1 -> dBm
tlPM.setPowerUnit(c_int16(0))

# Take power measurements and save results to arrays.
power_measurements = []
times = []
count = 0
mediciones = [] 
while count < 150:
    power =  c_double()
    tlPM.measPower(byref(power))
    power_measurements.append(power.value)
    times.append(datetime.now())
    print(times[count], ":", power_measurements[count], "W")
#   print(power_measurements[count])
    count+=1
    time.sleep(0.1)
print("")

# Close power meter connection.
#tlPM.close()
print('End program')
#%%
import matplotlib as plt
import numpy as np 
corriente=[0,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.9,2.0,2.1,2.2,2.3,2.05,1.85,1.75,1.65,1.7,1.8,1.62,1.61]
np.savetxt( f'{corriente[26]}A.txt',power_measurements)
#corriente=[,,,,,,,,,,,,]

#%%
import matplotlib as plt
import numpy as np 
distancia=[29.5,34.5,42,50,57,63]
np.savetxt( f'distanciasensor/{distancia[5]}CM.txt',power_measurements)
#corriente=[,,,,,,,,,,,,]