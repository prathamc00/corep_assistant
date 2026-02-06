def validate_corep(report_json, scenario_text):
    flags = []

    # crude extraction from scenario for demo purposes
    shares = 50
    earnings = 10
    intangibles = 5

    expected_cet1 = shares + earnings - intangibles

    for field in report_json["fields"]:
        if field["code"] == "010":
            if field["value"] != expected_cet1:
                flags.append(
                    f"CET1 calculation mismatch. Expected {expected_cet1} based on deductions, got {field['value']}."
                )

    return flags
