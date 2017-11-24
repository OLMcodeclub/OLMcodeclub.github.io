#compilation of code entered to astropi competition

from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
sense.set_rotation(270)

# MDF

bc = (0, 0, 205)
tc = (255,165,0)
c = 0

sense.clear(bc)

while c < 280:
  sense.set_pixel(randint(0,7), randint(0,7), randint(0,255), randint(0,255), randint(0,255))
  c = c + 1
  sleep(0.03)

t1 = round( sense.get_temperature(), 1 )
t2 = round( sense.get_temperature_from_pressure(), 3)
sense.show_message( str(t1) + " C or " + str(t2) + " C" , text_colour=tc, back_colour=bc)

c = 0
while c < 280:
  sense.set_pixel(randint(0,7), randint(0,7), randint(0,255), randint(0,255), randint(0,255))
  c = c + 1
  sleep(0.03)

#constance and william
sense.show_message("Hello how boring is it in space?")

w = (32,178,170)

b = (0, 0, 0)

picture = [
    b, b, b, b, b, b, b, b,
    b, b, w, w, b, w, w, b,
    b, b, w, w, b, w, w, b,
    b, w, b, b, b, b, b, w,
    b, w, w, w, w, w, w, w,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b
]
sense.set_pixels(picture)

temp = round( sense.get_temperature(), 1 )

sense.show_message( str(temp) )

#oscar and juliette

bc = (17, 173, 48)
tc = (173, 17, 17)
c = 0

sense.clear(bc)

while c < 280:
  sense.set_pixel(randint(0,7), randint(0,7), randint(0,255), randint(0,255), randint(0,255))
  c = c + 1
  sleep(0.03)

t1 = round( sense.get_temperature(), 1 )
t2 = round( sense.get_temperature_from_pressure(), 3)
sense.show_message( str(t1) + " C or " + str(t2) + " C" , text_colour=tc, back_colour=bc)

c = 0
while c < 280:
  sense.set_pixel(randint(0,7), randint(0,7), randint(0,255), randint(0,255), randint(0,255))
  c = c + 1
  sleep(0.03)

# charlotte and grace

temp = round( sense.get_temperature(), 1 )
sense.show_message( str(temp) )
red = (255,0,0)
sense.show_message("Greetings from earth" ,text_colour=red, scroll_speed=0.05)
w = (255, 255, 255)
b = (0, 0, 0)
picture = [
    b, b, b, b,b, b, b, b,
    b, w, w, b, b, w, w, b,
    b, w, w, b, b, w, w, b,
    b, b, b, b, b, b, b, b,
    w, b, b, b, b, b, b, w,
    w, w, w, w, w, w, w, w,
    b, w, w, w, w, w, w, b,
    b, b, b, b, b, b, b, b
]
sense.set_pixels(picture)

# grace and charlotte

d = (139, 0, 139)
sense.show_message("OLM are in space!", text_colour=d, scroll_speed= 0.06 )
a = (0, 250, 154)
b = (255, 255, 0)
c = (238, 154, 0)
de = (255, 255, 255)
e = (0, 0, 0)
picture = [
 e, e, e, e, e, e, e, e,
 e, de, a, e, e, de, a, e,
 e, a, a, e, e, a, a, e,
 e, e, e, e, e, e, e, e,
 c, c, e, e, e, e, c, c,
 e, c, c, c, c, c, c, e,
 e, e, c, c, c, c, e, e,
 e, e, e, e, e, e, e, e,
 ]
sense.set_pixels(picture)
sleep(3)

r = (255, 255, 255)
x = (255 ,14 ,6)
temp = sense.get_temperature()
temp = round( sense.get_temperature(), 1 )
sense.show_message( str(temp) )
sense.show_message( "It is " + str(temp) + " degrees", text_colour=r, back_colour=x )

# pilar

sense.show_message("Astro Pi")
b=(0,0,0)
w=(44,63,94)
picture = [
    b, b, w, w, w, w, b, b,
    b, w, b, b, b, b, w, b,
    b, w, b, w, w, b, w, b,
    b, w, b, b, b, b, w, b,
    b, b, w, w, w, w, b, b,
    b, b, w, w, w, w, b, b,
    b, w, w, w, w, w, w, b,
    b, w, w, w, w, w, w, b
]

sense.set_pixels(picture)
sleep(2)

sense.show_message("the current temp is",scroll_speed=0.05)
temp = round( sense.get_temperature(), 1 )
sense.show_message("it is"+ str(temp) )
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
hot = [
  b, b, b, b, b, y, y, b,
  b, b, b, b, y, y, y, y,
  b, b, b, b, b, y, y, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g,
  g, g, g, g, g, g, g, g
]


cold = [
  b, b, w, b, b, b, w, b,
  b, b, b, b, b, w, b, b,
  b, w, b, b, b, b, b, w,
  b, b, b, b, w, b, b, b,
  w, b, b, w, b, b, w, b,
  b, b, b, b, b, b, b, b,
  w, w, w, w, w, w, w, w,
  w, w, w, w, w, w, w, w
]
temp = sense.get_temperature()
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)
    
bc = (0, 0, 205)
tc = (255,165,0)
c = 0

# william and storm

sense.show_message("hello I like science!!!!")
b = (0,0,0)
y = (255,255,0)
r = (255,0,0)



picture = [
  b, b, b, b, b, b, b, b,
  b, y, y, b, b, y, y, b, 
  b, y, y, b, b, y, y, b,  
  y, y, y, y, y, y, y, y, 
  y, y, b, y, y, b, y, y, 
  y, r, y, b, b, y, r, y, 
  y, y, y, y, y, y, y, y, 
  b, y, y, y, y, y, y, b,
]
sense.set_pixels(picture)
sleep(2)
sense.show_message("picachu!")
temp = sense.get_temperature()
sense.show_message( str(temp) )

# peterzac scooby tiga

sense.show_message("The tempratue is", scroll_speed=0.01)
temp = sense.get_temperature()
sense.show_message( str(temp) )
w = (255, 255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 0)
temp = sense.get_temperature()
hot = [
  b, b, b, b, b, y, y, b,
  b, b, b, b, y, y, y, y,
  b, b, b, b, b, y, y, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g,
  g, g, g, g, g, g, g, g
]
cold = [
  b, b, w, b, b, b, w, b,
  b, b, b, b, b, w, b, b,
  b, w, b, b, b, b, b, w,
  b, b, b, b, w, b, b, b,
  w, b, b, w, b, b, w, b,
  b, b, b, b, b, b, b, b,
  w, w, w, w, w, w, w, w,
  w, w, w, w, w, w, w, w
]
temp = sense.get_temperature()
if temp >= 20:
    sense.set_pixels(hot)
else:
    sense.set_pixels(cold)

sleep(2)
sense.show_message("bye astronauts", scroll_speed=0.01)
    
picture = [
  b, b, b, b, b, b, b, b,
  b, b, w, w, w, w, b, b,
  b, b, w, y, y, w, b, b,
  b, b, w, y, y, w, b, b,
  b, b, w, w, w, w, b, b,
  w, w, w, w, w, w, w, w,
  w, b, w, w, w, w, b, w,
  b, b, w, b, b, w, b, b, 
]
sense.set_pixels(picture)

# arun adam

green = (0,255,0)
sense.show_message("This is for all the code clubs around the UK", scroll_speed=0.0, text_colour= green)

w = (255,215,0)
b = (255,0,255)

picture = [
    w, w, w, w, w, w, w, w,
    w, w, b, w, w, b, w, w,
    w, w, w, w, w, w, w, w,
    b, w, w, b, b, w, w, b,
    b, b, w, w, w, w, b, b,
    w, b, b, w, w, b, b, w,
    w, w, b, w, w, b, w, w,
    w, w, b, b, b, b, w, w,
]
sense.set_pixels(picture)
sleep(2)
temp = round( sense.get_temperature(), 1 )
sense.show_message( str(temp) )

# adam arun
temp= sense.get_temperature()
blue= (0,206,209)
sense.show_message("space",text_colour=blue, scroll_speed=0.1)

w = (255, 255, 255)
b = (0, 0, 0)

picture = [
    b, b, b,w, w, w, b, b,
    b, b, w, b, w, b, w, b,
    b, b, w, w, w, w, w, b,
    b, b, w, b, b, b, w, b,
    b, b, w, b, b, b, w, b,
    b, b, w, b, b, b, w, b,
    b, b, b, w, b, w, b, b,
    b, b, b, b, w, b, b, b
]

sense.set_pixels(picture)

