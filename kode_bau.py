"""Demonstrasi fungsi dengan kondisi sederhana."""


def print_sum_when_conditions_match(first_value, second_value, third_value):
    """Cetak jumlah dua nilai jika kondisi yang diberikan terpenuhi."""
    if first_value and not second_value and third_value is None:
        print(first_value + second_value)


print_sum_when_conditions_match(True, False, None)
