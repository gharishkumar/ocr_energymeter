# sudo apt-get install i2c-tools python-smbus
# i2cdetect -y 1

import I2C_LCD_driver
mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_clear()
mylcd.lcd_display_string("POWER CUT", 1)