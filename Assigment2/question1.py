import numpy as np
import matplotlib.pyplot as plt


v0 = 7  #(m/s)
theta = np.radians(60)  
x_hoop = 4.6  #M
y_hoop = 3.05  # (m)
y0 = 2.2  #(m)
g = 9.81  # (m/s^2)

t_flight = (v0 * np.sin(theta) + np.sqrt((v0 * np.sin(theta))**2 + 2 * g * y0)) / g

t = np.linspace(0, t_flight, num=100)

x = v0 * np.cos(theta) * t  # Horizontal distance
y = y0 + v0 * np.sin(theta) * t - 0.5 * g * t**2  # Vertical height

plt.figure(figsize=(8, 5))
plt.plot(x, y, 'g--', label="Ball Trajectory")  # Green dashed line


plt.axhline(y=0, color='black', linewidth=1)
plt.scatter(x_hoop, y_hoop, color='red', s=100, label="Basketball Hoop")

plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.title("Basketball Free Throw Trajectory")
plt.legend()
plt.grid()

plt.show()
