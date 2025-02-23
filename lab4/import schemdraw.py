import schemdraw
import schemdraw.elements as elm

# Create a new schematic drawing
d = schemdraw.Drawing()

# ESP32 Microcontroller
esp32 = d.add(elm.Rect().label("ESP32\nMicrocontroller")).at((0, 0))

# Wireless Module (NRF24L01)
nrf = d.add(elm.Rect().label("NRF24L01\nWireless Module")).at((0, 3))

# Motor Drivers (L298N)
md1 = d.add(elm.Rect().label("L298N\nMotor Driver 1")).at((-3, -3))
md2 = d.add(elm.Rect().label("L298N\nMotor Driver 2")).at((3, -3))

# Motors
m1 = d.add(elm.Motor().label("Motor 1")).at((-5, -6))
m2 = d.add(elm.Motor().label("Motor 2")).at((-3, -6))
m3 = d.add(elm.Motor().label("Motor 3")).at((3, -6))
m4 = d.add(elm.Motor().label("Motor 4")).at((5, -6))

# Power Supply (LiPo Battery)
battery = d.add(elm.BatteryCell().label("LiPo Battery\n11.1V - 14.8V")).at((0, -8))

# Connections using explicit positions
d.add(elm.Line().at(esp32.center).to(md1.center))  # ESP32 to Motor Driver 1
d.add(elm.Line().at(esp32.center).to(md2.center))  # ESP32 to Motor Driver 2
d.add(elm.Line().at(md1.center).to(m1.center))  # Motor Driver 1 to Motor 1
d.add(elm.Line().at(md1.center).to(m2.center))  # Motor Driver 1 to Motor 2
d.add(elm.Line().at(md2.center).to(m3.center))  # Motor Driver 2 to Motor 3
d.add(elm.Line().at(md2.center).to(m4.center))  # Motor Driver 2 to Motor 4
d.add(elm.Line().at(battery.center).to(md1.center))  # Battery to Motor Driver 1
d.add(elm.Line().at(battery.center).to(md2.center))  # Battery to Motor Driver 2
d.add(elm.Line().at(battery.center).to(esp32.center))  # Battery to ESP32
d.add(elm.Line().at(nrf.center).to(esp32.center))  # NRF to ESP32

# Display the schematic
d.draw()