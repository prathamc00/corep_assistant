def render_corep_table(report_json: dict):
    print("\nCOREP C01.00 — Own Funds\n")
    print(f"{'Code':<10}{'Field':<35}{'Value':<10}")
    print("-" * 60)

    for field in report_json["fields"]:
        print(f"{field['code']:<10}{field['name']:<35}{field['value']:<10}")

    print("\nJustifications:\n")
    for field in report_json["fields"]:
        print(f"Field {field['code']}: {field['justification']}")
        print(f"Rules used: {', '.join(field['rules_used'])}\n")
