import Adafruit_DHT
from RPLCD.i2c import CharLCD
import time

SENSOR_TYPE = Adafruit_DHT.DHT22
DHT_PIN = 22

# Initialize the LCD with backlight enabled
lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2, backlight_enabled=True)

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR_TYPE, DHT_PIN)
        if humidity is not None and temperature is not None:
            temp_str = f"Temp: {temperature:.2f}C"
            lcd.cursor_pos = (0, 0)
            lcd.write_string(temp_str)
            lcd.cursor_pos = (1, 0)
            lcd.write_string(f"Humidity: {humidity:.2f}%")
            print(temp_str, f"Humidity: {humidity:.2f}%")
        else:
            lcd.cursor_pos = (0, 0)
            lcd.write_string("Failed to retrieve data")
            print("Failed to retrieve data")
        time.sleep(2)  # Wait for 2 seconds before the next reading

except KeyboardInterrupt:
    pass

finally:
    # Turn off the backlight and close the LCD
    lcd.backlight_enabled = False
    lcd.close()
