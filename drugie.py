def ieee754_to_float(bit_string):
    binary = int(bit_string, 2)
    mantissa = binary & ((1 << 23) - 1)  # Wyizoluj mantysę
    exponent = (binary >> 23) & 0xFF  # Wyizoluj eksponentę

    # Oblicz wartość float
    sign = (-1) ** (binary >> 31)
    value = sign * (1 + mantissa / (1 << 23)) * (2 ** (exponent - 127))

    return value

# Przykładowa bitowa reprezentacja liczby w formacie IEEE-754 (32-bit)
bit_string = "10111110011000000000000000000000"

# Wywołanie funkcji do konwersji
float_value = ieee754_to_float(bit_string)

print(f"Liczba float w systemie dziesiętnym: {float_value}")
