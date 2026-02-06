import json
from llm.reporter import generate_report
from renderer.template_view import render_corep_table
from validator.rules import validate_corep

scenario = """
Bank has:
- £50m ordinary shares
- £10m retained earnings
- £5m intangible assets
"""

result = generate_report(scenario)

report_json = json.loads(result)

render_corep_table(report_json)
flags = validate_corep(report_json, scenario)

if flags:
    print("\nVALIDATION FLAGS:")
    for f in flags:
        print("-", f)
