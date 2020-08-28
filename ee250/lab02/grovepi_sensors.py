""" EE 250L Lab 02: GrovePi Sensors

Daniel Briones
Dfbrione@usc.edu

GitHub Repository Link: https://github.com/dfbrione/GrovePi-EE250.git
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time

# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
from grove_rgb_lcd import*

def splash_screen():
    setRGB(0,0,255) #Initialize the backlight as blue
    setText_norefresh("Lab02:\nGrovePi Sensors")
    time.sleep(2) #Pause for 2 seconds

def not_in_range_screen(threshold_value, curr_ranger_output):
    setRGB(0,255,0) #Set the backlight as green 
    setText_norefresh(" " + str(threshold_value) + "cm")
    setText_norefresh("\n " + str(curr_ranger_output) + "cm")

def in_range_screen(threshold_value, curr_ranger_output):
    setRGB(255,0,0)
    setText_norefresh(str(threshold_value) + "cm OBJ PRES")
    setText_norefresh("\n " + str(curr_ranger_output) + "cm")
    

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
    PORT = 4    # D4
    pot = 0 #Analog port A0
    grovepi.pinMode(pot, "INPUT")
    


    splash_screen()

    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)
        pot_value = grovepi.analogRead(pot)
        ranger_value = grovepi.ultrasonicRead(PORT)
        
        if ranger_value >=  pot_value:
            not_in_range_screen(pot_value, ranger_value)

        else:
            in_range_screen(pot_value,ranger_value)



       # print(grovepi.ultrasonicRead(PORT))
        
