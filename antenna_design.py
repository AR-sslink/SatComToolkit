import numpy as np
import matplotlib.pyplot as plt

# Define Constants
c = 299792458  # Speed of light in meters per second
freq = 2.4e9  # Frequency in Hertz (e.g., 2.4 GHz for Wi-Fi)

# Calculate Wavelength
wavelength = c / freq

# Define Dipole Length
dipole_length = wavelength / 2

# Generate Theta Angles (Polar Angle)
theta = np.linspace(0, np.pi, 180)

# Calculate Radiation Pattern
radiation_pattern = (np.cos(np.pi * np.cos(theta))) ** 2

# Normalize the Radiation Pattern
radiation_pattern /= radiation_pattern.max()

# Plot the Radiation Pattern
plt.figure()
plt.plot(theta * 180 / np.pi, radiation_pattern)
plt.title('Dipole Antenna Radiation Pattern')
plt.xlabel('Theta (degrees)')
plt.ylabel('Normalized Radiation Pattern')
plt.grid(True)
plt.show()
