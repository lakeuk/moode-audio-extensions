#!/usr/bin/env python2

import os

os.system("cp /home/pi/myapp/gpio-moode-audio-i2c.service /usr/lib/systemd/system")
os.system("cp /home/pi/myapp/gpio-moode-audio-i2c-Rotary.service /usr/lib/systemd/system")
os.system("cp /home/pi/myapp/ePaper-moode-audio.service /usr/lib/systemd/system")

os.system("systemctl start gpio-moode-audio-i2c")
os.system("systemctl start gpio-moode-audio-i2c-Rotary")
os.system("systemctl start ePaper-moode-audio")

os.system("systemctl enable gpio-moode-audio-i2c")
os.system("systemctl enable gpio-moode-audio-i2c-Rotary")
os.system("systemctl enable ePaper-moode-audio")
