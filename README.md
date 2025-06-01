Pentest Toolkit 🚀
The Pentest Toolkit is a powerful web-based penetration testing application designed to assist security professionals, ethical hackers, and system administrators in identifying vulnerabilities within networks. 
Built with Flask, this toolkit provides a simple yet effective interface for performing essential security analysis, including port scanning, vulnerability assessment, SSH brute-force attacks, and network sniffing. 
Its modular design ensures flexibility, allowing users to select the right tool for their cybersecurity needs.The toolkit includes several critical features. 
The Port Scanner helps identify open ports on a target system, providing insights into potential entry points for unauthorized access. 
The Vulnerability Scanner assesses systems for known security weaknesses, making it easier to pinpoint areas requiring remediation. 
The SSH Brute Force module allows ethical hackers to test password security by attempting login attempts using a dictionary of usernames and passwords. 
Finally, the Network Sniffer captures packets from the network, enabling users to analyze traffic patterns and potential threats.
Installing and using the Pentest Toolkit is simple. Users first clone the repository from GitHub and install dependencies using Python’s package manager. 
Once the setup is complete, the Flask application can be started, providing a user-friendly web interface accessible through a browser. 
From the dashboard, users can select a module, input their target details, and execute tests in real time.
The toolkit is designed with efficiency in mind. Using threading, it ensures non-blocking execution, allowing scans to run smoothly without affecting the interface's responsiveness. 
Additionally, it includes logging and error handling, providing clear feedback for users during testing. 
The modular architecture makes it easy to extend functionality, supporting further customization based on individual security requirements.

This project is intended for educational and ethical hacking purposes only.t is lightweight, easy to use, and fully customizable, making it ideal for security audits and learning cybersecurity principles.

⚡ Features
Port Scanner 🔍 - Scan open ports on a target system

Vulnerability Scanner 🛡️ - Identify security weaknesses

SSH Brute Forcer 🔑 - Test password security using brute-force methods

Network Sniffer 🌐 - Capture and analyze network packets

Web-Based UI 💻 - Simple and interactive interface

Threaded Execution ⏳ - Efficient scanning without blocking the application

🚀 Installation & Setup
1️⃣ Clone the Repository
sh
git clone https://github.com/Kishore-Code-Hub/Task_3.git
cd Task_3
2️⃣ Install Dependencies
Make sure you have Python installed. Then run:

sh
pip install -r requirements.txt
3️⃣ Run the Application
Start the Flask server using:

sh
python app.py
4️⃣ Access the Toolkit
Once the server is running, open your browser and visit:

http://127.0.0.1:5000
🛠️ Usage
1️⃣ Open the web interface 
2️⃣ Select a module (Port Scanner, Vulnerability Scanner, SSH Brute Force, or Network Sniffer) 
3️⃣ Provide the target details (IP, domain, username, password for brute force) 
4️⃣ Click "Execute" and view the results in real-time

📜 Requirements
The dependencies are listed in requirements.txt, which includes:
flask
paramiko
scapy
threading

🔥 Project Structure
plaintext
Task_3/
├── static/            # Contains CSS & JavaScript files
├── templates/         # HTML interface files
├── modules/           # Core pentest tools (port_scanner, vuln_scanner, etc.)
├── app.py             # Main Flask application
├── requirements.txt   # Required Python dependencies
├── README.md          # Documentation
⚖️ Legal Disclaimer
This toolkit is intended for educational and ethical hacking purposes only. 
⚠️ Unauthorized use against live systems without permission is illegal and punishable by law. 
Please ensure you have explicit authorization before testing any networks.




![Image](https://github.com/user-attachments/assets/da79c87a-e798-419b-acd2-3e3666b77add)
![Image](https://github.com/user-attachments/assets/2b5bbc37-1649-49f2-96ca-d75187ade466)
![Image](https://github.com/user-attachments/assets/e9ffc5a3-e54a-4c9e-af7c-1b5d9d02a7e5)
