import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Parameters
duration = 10  # Duration in seconds
fps = 60  # Frames per second
num_points = duration * fps  # Total frames
t = np.linspace(0, 4 * np.pi, num_points)  # Time array

# Electric field components for linear, circular, and elliptical polarization
Ex_linear = np.cos(t)  # Linear polarization (x-component)
Ey_linear = np.zeros_like(t)  # Linear polarization (y-component)

Ex_circular = np.cos(t)  # Circular polarization (x-component)
Ey_circular = np.sin(t)  # Circular polarization (y-component)

Ex_elliptical = np.cos(t)  # Elliptical polarization (x-component)
Ey_elliptical = 0.5 * np.sin(t)  # Elliptical polarization (y-component)

# Create the figure and 3D subplots
fig = plt.figure(figsize=(14, 8))
ax1 = fig.add_subplot(131, projection='3d')  # Linear polarization
ax2 = fig.add_subplot(132, projection='3d')  # Circular polarization
ax3 = fig.add_subplot(133, projection='3d')  # Elliptical polarization

# Set titles for each subplot
ax1.set_title('Linear Polarization')
ax2.set_title('Circular Polarization')
ax3.set_title('Elliptical Polarization')

# Set axis labels for all subplots
for ax in [ax1, ax2, ax3]:
    ax.set_xlabel('Ex')
    ax.set_ylabel('Ey')
    ax.set_zlabel('Time')

# Set axis limits for all subplots
for ax in [ax1, ax2, ax3]:
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_zlim(0, 4 * np.pi)

# Initialize lines for each subplot
(line_linear,) = ax1.plot([], [], [], lw=2, color='blue')
(line_circular,) = ax2.plot([], [], [], lw=2, color='green')
(line_elliptical,) = ax3.plot([], [], [], lw=2, color='red')

# Update function for animation
def update(frame):
    # Update linear polarization
    line_linear.set_data(Ex_linear[:frame], Ey_linear[:frame])
    line_linear.set_3d_properties(t[:frame])

    # Update circular polarization
    line_circular.set_data(Ex_circular[:frame], Ey_circular[:frame])
    line_circular.set_3d_properties(t[:frame])

    # Update elliptical polarization
    line_elliptical.set_data(Ex_elliptical[:frame], Ey_elliptical[:frame])
    line_elliptical.set_3d_properties(t[:frame])

    return line_linear, line_circular, line_elliptical

# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_points, interval=10, blit=True)

# Display the animation
plt.tight_layout()
plt.show()

# Save the animation as a 10-second video
ani.save('10_second_polarization_animation.mp4', writer='ffmpeg', fps=600)
print("Animation saved as '10_second_polarization_animation.mp4'")