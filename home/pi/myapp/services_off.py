#!/usr/bin/env python2

import os

os.system("systemctl disable gpio-moode-audio-i2c")
os.system("systemctl disable gpio-moode-audio-i2c-Rotary")
os.system("systemctl disable ePaper-moode-audio")

os.system("systemctl stop gpio-moode-audio-i2c")
os.system("systemctl stop gpio-moode-audio-i2c-Rotary")
os.system("systemctl stop ePaper-moode-audio")

os.system("rm /usr/lib/systemd/system/gpio-moode-audio-i2c.service")
os.system("rm /usr/lib/systemd/system/gpio-moode-audio-i2c-Rotary.service")
os.system("rm /usr/lib/systemd/system/ePaper-moode-audio.service")