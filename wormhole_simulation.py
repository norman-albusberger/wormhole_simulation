import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Listen von Radien, exotischen Materiedichten und Drehimpulsen
r0_values = [50, 100]  # Beispielwerte für Radien
exotic_matter_densities = [-0.5, -2, -4, -6, -10]  # Exotische Materiedichten
angular_momenta = [0, 0.5, 1, 2]  # Beispielwerte für Drehimpuls (J)


# Funktion zur Berechnung der Raumzeitkrümmung unter Berücksichtigung der Rotation (Kerr-Effekt)
def kerr_wormhole_equations(y, r, r0, exotic_matter_density, J):
    phi, dphi_dr = y
    # Zusatzterm für den Kerr-Effekt (Rotation)
    kerr_effect = J ** 2 / (r ** 4)
    dydr = [dphi_dr, (2 / r) * dphi_dr + (8 * np.pi * exotic_matter_density) * np.exp(2 * phi) - kerr_effect]
    return dydr


# Iteriere über verschiedene Kombinationen von r0, exotischer Materie und Drehimpuls
for r0 in r0_values:
    for exotic_matter_density in exotic_matter_densities:
        for J in angular_momenta:
            # Anfangsbedingungen
            phi_0 = [0, 0]  # Anfangswerte für phi und dphi/dr

            # Definitionsbereich für die r-Koordinate (radiale Entfernung)
            r_values = np.linspace(r0, 1.5 * r0, 1000)

            # Lösung der Differentialgleichungen
            solution = odeint(kerr_wormhole_equations, phi_0, r_values, args=(r0, exotic_matter_density, J))

            # Extrahieren der Lösungen
            phi_values = solution[:, 0]

            # Visualisierung der Raumzeitkrümmung
            plt.figure(figsize=(10, 6))
            plt.plot(r_values, np.exp(2 * phi_values), label=f'ρ={exotic_matter_density}, r0={r0}, J={J}')
            plt.xlabel('Radiale Entfernung r')
            plt.ylabel(r'$\exp(2\phi(r))$')
            plt.title(f'Raumzeitkrümmung: Exotische Materiedichte={exotic_matter_density}, Radius={r0}, J={J}')
            plt.legend()
            plt.grid(True)

            # Speichern des Plots
            plt.savefig(f'Kerr_Wurmloch_r0_{r0}_density_{exotic_matter_density}_J_{J}.png')
            plt.close()

print("Plots für Kerr-Wurmlöcher wurden erzeugt und gespeichert.")
