#!/usr/bin/env python
 
import pigpio
from time import sleep
 
# -----------
pi=pigpio.pi();
pi.set_mode(17,pigpio.OUTPUT)

pi.write(17,1)
sleep(1)
pi.write(17,0)

pi.stop()