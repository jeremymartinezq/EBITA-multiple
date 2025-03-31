def ebitda_multiple_valuation(ebitda, multiple):
    enterprise_value = ebitda * multiple
    return enterprise_value


# Example inputs
ebitda = 25  # EBITDA in millions
multiple = 8  # Industry multiple

enterprise_value = ebitda_multiple_valuation(ebitda, multiple)
print(f"Enterprise Value: ${enterprise_value:.2f} million")


