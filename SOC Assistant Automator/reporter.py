import os
import json
from jinja2 import Environment, FileSystemLoader

RESULTS_DIR = "scans/results"
REPORTS_DIR = "reports"
TEMPLATE_DIR = os.path.join(REPORTS_DIR, "templates")
os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)
os.makedirs(TEMPLATE_DIR, exist_ok=True)

def save_json(data):
    ip_sanitized = data["target"].replace('.', '_')
    output_path = os.path.join(RESULTS_DIR, f"{ip_sanitized}_scan_full.json")
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"[+] Results saved to {output_path}")

def render_html_report(scan_data):
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template("report_template.j2")
    html_output = template.render(data=scan_data)

    html_path = os.path.join(REPORTS_DIR, f"{scan_data['target'].replace('.', '_')}_report.html")
    with open(html_path, "w") as f:
        f.write(html_output)

    print(f"[+] HTML report saved to {html_path}")