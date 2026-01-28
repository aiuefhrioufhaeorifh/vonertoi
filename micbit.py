# This is my tutorial for python learning on micro:bit.
# While True is a must for a microbit block
from microbit import *

display.scroll("hello world")
# That will scrool the words in the LED screen.
display.show("Image.HAPPY")
# There are also some useful built-in kmages for you to choose.
# Create an image
boat = Image("00505:"
             "05050:"
             "05505:"
             "55555:"
             "50005")
display.show(boat)
# In this situation the `"`is not needed.
# Pay attention to the `:` at the end of each line.
# You can also use this function to display a set of pics enclosed by `[]` like this:
set_boot = [boot1, boot2, boot3]
display.show(set_boot, loop = True, delay = 200)
# The delay shows how long between the two pictures in this set.
# Sleep for 1000 miliseconds.
sleep(1000)
# The function below can hold True or False that judge whether a button is pressed or not.
button_a.is_pressed()
# Get the acceleration in each coordinate.
accelerometer.get_x()
accelerometer.get_y()
accelerometer.get_z()
# Get direction from the compass
compass.heading()
# Other parameters can be hired from their correspomding sensors
temperature()
light.read_light_level()
running_time()
# Music playing
import music
import audio
music.play(music.NAME) # Playing a music
# IO pins
# The usual state of pins is 1 or 0 corresponds on and off
pin0
