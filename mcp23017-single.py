#!/usr/bin/python3
import time

import Adafruit_GPIO as GPIO
import Adafruit_GPIO.MCP230xx as MCP230xx

mcp = MCP230xx.MCP23017()  # This assumes the MCP23017 is at the default address 0x20, if not pass in an argument with the actual address in hex.

# Setup pin 1 as an output and pin 2 as an input, very similar to RPi.GPIO library.
mcp.setup(0, GPIO.OUT)
mcp.setup(1, GPIO.OUT)
mcp.setup(2, GPIO.OUT)
mcp.setup(3, GPIO.OUT)
mcp.setup(4, GPIO.OUT)
mcp.setup(5, GPIO.OUT)
mcp.setup(6, GPIO.OUT)
mcp.setup(7, GPIO.OUT)
mcp.setup(8, GPIO.OUT)
mcp.setup(9, GPIO.OUT)
mcp.setup(10, GPIO.OUT)
mcp.setup(11, GPIO.OUT)
mcp.setup(12, GPIO.OUT)

# Loop forever blinking pin 1 high and low every second.
mcp.output(0, GPIO.HIGH)
time.sleep(1.0)
mcp.output(0, GPIO.LOW)
time.sleep(5.0)

