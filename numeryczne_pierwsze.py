# This is a sample Python script.
import numpy as np
import matplotlib.pyplot as plt

# Ilość bitów dla wykładnika (stała)
exponent_bits = 8

# Zakres ilości bitów dla mantysy
mantissa_bits_range = range(8, 53)

# Inicjalizacja list na wyniki
machine_epsilon_values = []

# Obliczanie machine epsilon dla różnych ilości bitów mantysy
for mantissa_bits in mantissa_bits_range:
    machine_epsilon = 2.0 ** (-mantissa_bits)
    machine_epsilon_values.append(machine_epsilon)

# Tworzenie wykresu
plt.figure(figsize=(10, 6))
plt.plot(mantissa_bits_range, machine_epsilon_values, marker='o', linestyle='-')
plt.title("Machine Epsilon vs. Ilość bitów mantysy")
plt.xlabel("Ilość bitów mantysy")
plt.ylabel("Machine Epsilon")
plt.yscale("log")  # Ustawienie skali logarytmicznej na osi Y
plt.grid(True)

# Wyświetlenie wykresu
plt.show()
