#!/usr/bin/env python
 
import pigpio
from time import sleep
 
# -----------
pi=pigpio.pi();
pi.set_mode(18,pigpio.OUTPUT)

pi.write(18,1)
sleep(1)
pi.write(18,0)

pi.stop()