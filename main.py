import matplotlib.pyplot as plt


def pos(t):
    return x0 + v0 * t + 1/2 * a * t**2

def vel(t):
    return v0 + a * t

def accel(t):
    return a

def plotter():
  plt.clf()
  xcoord = []
  ycoord_position, ycoord_velocity, ycoord_accel = [], [], []

  for x in range(0, 30):
    xcoord.append(x)
    ycoord_position.append(pos(x))
    ycoord_velocity.append(vel(x))
    ycoord_accel.append(accel(x))

  plt.style.use("fivethirtyeight")
  plt.ylabel('Position / Velocity')
  plt.xlabel('Time (seconds)')
  plt.plot(xcoord, ycoord_position, label="Position")
  plt.plot(xcoord, ycoord_velocity, label="Velocity")
  plt.plot(xcoord, ycoord_accel, label="Acceleration")

  plt.legend()

  # plt.yscale('log') # Uncheck for log scale
  plt.tight_layout()
  plt.show(block=False)

def get_time_data():
  user = input("Enter a time (q to quit): ")
  while user != 'q':
    try:
        t = float(user)
        print("The position is "+ str(pos(t)) )
        print("The velocity is "+ str(vel(t)) )
        plt.plot(t)
    except ValueError: 
        print("That's not a time or q.")
    user = input("Enter a time (q to quit): ")

user = ""
while user.lower() != 'n':
    try:
      x0 = float(input("Enter the initial position: "))
      v0 = float(input("Enter the initial velocity: "))
      a =  float(input("Enter the acceleration: "))
      plotter()
      get_time_data()
    except ValueError:
      print("Not a valid value")
    user = input("Would you like to enter another set (y/n)? ")

