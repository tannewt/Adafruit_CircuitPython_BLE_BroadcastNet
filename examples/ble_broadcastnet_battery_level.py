import adafruit_ble_broadcastnet
import analogio
import board
import math
import microcontroller
import time

print("This is BroadcastNet sensor:", adafruit_ble_broadcastnet.device_address)

battery = analogio.AnalogIn(board.VOLTAGE_MONITOR)
divider_ratio = 2

while True:
    measurement = adafruit_ble_broadcastnet.AdafruitSensorMeasurement()
    battery_voltage = battery.value / 2**16 * divider_ratio * battery.reference_voltage
    measurement.battery_voltage = int(battery_voltage * 1000)
    measurement.temperature = microcontroller.cpu.temperature
    print(measurement)
    adafruit_ble_broadcastnet.broadcast(measurement)

    time.sleep(30)