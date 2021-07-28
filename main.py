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

  for t in range(0, 30):
    xcoord.append(t)
    ycoord_position.append(pos(t))
    ycoord_velocity.append(vel(t))
    ycoord_accel.append(accel(t))

  plt.style.use("fivethirtyeight")
  plt.ylabel('Position | Velocity')
  plt.xlabel('Time (seconds)')
  plt.plot(xcoord, ycoord_position, label="Position")
  plt.plot(xcoord, ycoord_velocity, label="Velocity")
  plt.plot(xcoord, ycoord_accel, label="Acceleration")

  plt.legend()

  # plt.yscale('log') # Uncheck for log scale
  plt.tight_layout()
  plt.show(block=False)

def get_time_data():
  t = input("Enter a time (q to quit): ")
  while t != 'q':
    try:
        t = float(t)
        print("The position is "+ str(pos(t)) )
        print("The velocity is "+ str(vel(t)) )
        plt.plot(t)
    except ValueError: 
        print("That's not a time or q.")
    t = input("Enter a time (q to quit): ")

if __name__ == "__main__":
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

