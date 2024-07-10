"""Use the selfmade complex class to plot the Jullia fractal."""

from math import log10

import matplotlib.pyplot as plt

from my_code import Complex

if __name__ == "__main__":

    def julia(z: Complex, c: Complex) -> Complex:
        """Evaluate a julia step."""
        square = z.multiply(z)
        return square.add(c)

    c = Complex(-0.07, 0.652)

    mesh = []
    steps = 100
    for y in range(steps):
        row = []
        for x in range(steps):
            sx = 1 * (x * 1.0 / steps) - 0.5
            sy = 1 * (y * 1.0 / steps) - 0.5
            z = Complex(sx, sy)
            counter = 0
            while z.radius() < 1.0:
                z = julia(z, c)
                counter += 1
            row.append(counter)
        mesh.append(row)

    scaled = [[log10(val + 1e-12) for val in row] for row in mesh]

    # TODO: use plt.imshow and plt.plot to explore the scaled values.
    # TODO: combine plt.imshow and plt.colorbar.
