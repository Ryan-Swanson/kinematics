from math import * 
import numpy as np
import threading
import matplotlib.pyplot as plt

def vel(t):
    return v0 + a * t

def pos(t):
    return x0 + v0 * t + 1/2 * a * t**2

def accel(t):
    return a

def plotter():
  xcoord_position = []
  for x in range(0,10):
      xcoord_position.append(x)
  ycoord_position = []
  for x in range(0, 10):
      ycoord_position.append(pos(x))

  xcoord_velocity = []
  for x in range(0,10):
      xcoord_velocity.append(x)
  ycoord_velocity = []
  for x in range(0, 10):
      ycoord_velocity.append(vel(x))

  xcoord_accel = []
  for x in range(0,10):
      xcoord_accel.append(x)
  ycoord_accel = []
  for x in range(0, 10):
      ycoord_accel.append(accel(x))
      
  plt.style.use("dark_background")
  plt.ylabel('Position / Velocity')
  plt.xlabel('Time')
  plt.plot(xcoord_position,ycoord_position, label="Position")
  plt.plot(xcoord_velocity,ycoord_velocity, label="Velocity")
  plt.plot(xcoord_accel,ycoord_accel, label="Acceleration")

  plt.legend()
  plt.show()


x0 = float(input("Enter the initial position: "))
v0 = float(input("Enter the initial velocity: "))
a = float(input("Enter the acceleration: "))

plot = threading.Thread(plotter())
plot.start()

user = input("Enter a time (q to quit): ") 

def pos_time():
  while user != 'q':
    try:
        t = float(user)
        print("The position is "+str(pos(t)))
        print("The velocity is "+str(vel(t)))
    except ValueError:
        print("That's not a time or q.")
    user = input("Enter a time (q to quit): ")
    
