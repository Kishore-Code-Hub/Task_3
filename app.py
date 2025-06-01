from flask import Flask, render_template, request
from modules import port_scanner, vuln_scanner, brute_forcer, network_sniffer
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    target = request.form.get("target")
    action = request.form.get("action")
    result = ""

    def run_tool():
        nonlocal result
        if action == "port_scan":
            result = port_scanner.scan_ports(target)
        elif action == "vuln_scan":
            result = vuln_scanner.scan_vulnerabilities(target)
        elif action == "brute_force":
            # ✅ Get username & password from user input
            username = request.form.get("username")
            password = request.form.get("password")
        elif action == "sniff":
            result = network_sniffer.sniff_packets()
        else:
            result = "Invalid action."

    # Run the tool in a thread to avoid blocking
    thread = threading.Thread(target=run_tool)
    thread.start()
    thread.join()

    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
