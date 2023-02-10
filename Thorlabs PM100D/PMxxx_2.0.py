# from ctypes import cdll,c_long, c_ulong, c_uint32,byref,create_string_buffer,c_bool,c_char_p,c_int,c_int16,c_double, sizeof, c_voidp
# import clr
import time
# from TLPM import TLPM
# from datetime import datetime
from Instrumental_Con_PM100D import ThorlabsPM100D
import matplotlib as plt
import numpy as np 

#%%
"""         ----------------------           """
"""         -----  BUSCAR !  -----           """
"""         ----------------------           """

tlPM = ThorlabsPM100D()
tlPM.connected_devices()

#%%
"""         ----------------------           """
"""         ----- CONECCION !-----           """
"""         ----------------------           """
resourceName = ''
tlPM.connect_to(resourceName)

#%%
"""         ----------------------           """
"""         ----- MEDICION ! -----           """
"""         ----------------------           """

tlPM.set_wave_lenght(1064)
tlPM.set_AutoRange(1) ; tlPM.set_PowerUnits(0);
potencias = tlPM.get_PowerMeasurement(150, 0.1)

#%%
corriente=[0,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.9,2.0,2.1,2.2,2.3,2.05,1.85,1.75,1.65,1.7,1.8,1.62,1.61]
np.savetxt( f'{corriente[26]}A.txt',potencias)
#corriente=[,,,,,,,,,,,,]

#%%
distancia=[29.5,34.5,42,50,57,63]
np.savetxt( f'distanciasensor/{distancia[5]}CM.txt',potencias)
#corriente=[,,,,,,,,,,,,]

