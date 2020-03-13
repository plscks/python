# raspberry pi 3 I2C test
# Learning to use I2C on RPi3
# uses https://github.com/adafruit/Adafruit_CircuitPython_SSD1306 library
# sudo pip3 install adafruit-circuitpython-ssd1306
# Here we go!
import time
import subprocess

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
# Move left to right keeping track of the current x position for drawing shapes.
padding = -2
top = padding
bottom = height-padding
x = 0

# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
#font = ImageFont.truetype('/home/plscks/FiraCode-Regular.ttf', 9)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)


draw.text((x, top+0), 'Length test:', font=font, fill=255)
draw.text((x, top+8), '12345678901234567890', font=font, fill=255)
draw.text((x, top+16), 'Line 3', font=font, fill=255)
draw.text((x, top+24), 'Line 4', font=font, fill=255)
draw.text((x, top+32), 'Line 5', font = font, fill = 255)
draw.text((x, top+40), 'Line 6', font = font, fill = 255)
draw.text((x, top+48), 'Line 7', font = font, fill = 255)
draw.text((x, top+56), 'Line 8', font = font, fill = 255)
draw.text((x, top+64), 'Line 9', font = font, fill = 255)

# Display image.
disp.image(image)
disp.show()
