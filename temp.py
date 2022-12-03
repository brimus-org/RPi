#!/usr/bin/python
# for reading the si7021 and printing it out on the 128x32 display (ssd1306 controlled)

import smbus
import time

import subprocess

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

import platform
import socket
import os

# Get I2C bus - si7021
bus = smbus.SMBus(1)

# Create the I2C interface - ssd1306.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 9)

h1 = socket.gethostname()
h2 = platform.node()
h3 = os.uname()[1]
h4 = os.uname()

print("socket = " + h1)
print("platfor = " + h2)
print("os = " + h3)
print("os full = " + h3)


while True:

    # SI7021 address, 0x40(64)
    # 0xF5(245) Select Relative Humidity NO HOLD master mode
    bus.write_byte(0x40, 0xF5)

    time.sleep(0.3)

    # SI7021 address, 0x40(64)
    # Read data back, 2 bytes, Humidity MSB first
    data0 = bus.read_byte(0x40)
    data1 = bus.read_byte(0x40)

    # Convert the data
    humidity = round(((data0 * 256 + data1) * 125 / 65536.0) - 6, 2)

    time.sleep(0.3)

    # SI7021 address, 0x40(64)
    # 0xF3(243) Select temperature NO HOLD master mode
    bus.write_byte(0x40, 0xF3)

    time.sleep(0.3)

    # SI7021 address, 0x40(64)
    # Read data back, 2 bytes, Temperature MSB first
    data0 = bus.read_byte(0x40)
    data1 = bus.read_byte(0x40)

    # Convert the data
    cTemp = round(((data0 * 256 + data1) * 175.72 / 65536.0) - 46.85, 2)
    fTemp = round(cTemp * 1.8 + 32, 2)
    
    # Output data to screen
    print ("Relative Humidity is : %.2f %%" %humidity)
    print ("Temperature in Celsius is : %.2f C" %cTemp)
    print ("Temperature in Fahrenheit is : %.2f F" %fTemp)

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Shell scripts for system monitoring from here:
    # https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
    cmd = "hostname -I | cut -d' ' -f1"
    IP = subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = 'cut -f 1 -d " " /proc/loadavg'
    CPU = subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%s MB  %.2f%%\", $3,$2,$3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = 'df -h | awk \'$NF=="/"{printf "Disk: %d/%d GB  %s", $3,$2,$5}\''
    Disk = subprocess.check_output(cmd, shell=True).decode("utf-8")

    # Write four lines of text.

    draw.text((x, top + 0), "IP: " + IP, font=font, fill=255)
    # draw.text((x, top + 8), "Humidity: " + str(humidity) + " %", font=font, fill=255)
    draw.text((x, top + 8), "Hostname: " + str(h1), font=font, fill=255)
    draw.text((x, top + 16), "Temperature F: " + str(fTemp), font=font, fill=255)
    draw.text((x, top + 25), "Temperature C: " + str(cTemp), font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.show()
    time.sleep(10)
    
    
