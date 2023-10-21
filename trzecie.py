import math

def approximate_e(target_error):
    e_approximation = 1.0  # Początkowa przybliżona wartość e
    n = 1  # Numer składnika w szeregu Maclaurina
    current_term = 1.0  # Wartość aktualnego składnika
    relative_error = 100.0  # Początkowy błąd względny

    while relative_error > target_error:
        n += 1
        current_term *= 1.0 / n  # Oblicz kolejny składnik
        e_approximation += current_term  # Dodaj składnik do przybliżonej wartości e

        # Oblicz błąd względny
        previous_e_approximation = e_approximation - current_term
        relative_error = abs((e_approximation - previous_e_approximation) / e_approximation) * 100

    return e_approximation, n

# Oblicz przybliżoną wartość liczby e z błędem względnym < 1%
target_error = 1.0  # 1% błąd względny
e_approx, n_terms = approximate_e(target_error)

print(f"Przybliżona wartość liczby e z błędem < 1% to: {e_approx}")
print(f"Ilość składników potrzebnych do osiągnięcia tej dokładności: {n_terms}")
print(f"Rzeczywista wartość liczby e: {math.e}")
