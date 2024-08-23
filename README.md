Project: NGINX-CMD

Description: This project is a Python application that provides a command-line interface for managing Nginx configurations.

+ Generate requirements.txt
    # pip freeze > requirements.txt

Requirements:
 + Python 3.6 or higher
 + The following packages, which can be installed using 
    # pip install -r requirements.txt

Run as dev:
    # python3 app.py

Install Python using the package manager
    + Update the package index:
        # sudo apt update
    + Install Python using the following command:
        For Python 3.x: 
        # sudo apt install python3
    + Python version: 
        # python3 --version

Set Hosting app on ubunto
+ Create a systemd service file to manage your app:
    - Create a file at /etc/systemd/system/<whatapp-broadcast.service> with the following contents:
        [Unit]
        Description=Whatapp Broadcast build from Python
        After=network.target

        [Service]
        WorkingDirectory=/var/www/html/whatapp-broadcast
        ExecStart=/usr/bin/python3 app.py
        Restart=always
        RestartSec=30
        StandardOutput=journal
        StandardError=journal

        [Install]
        WantedBy=multi-user.target

    <!-- - Replace <your_username> with your actual username. -->
    - Reload the systemd daemon: 
        <sudo systemctl daemon-reload>
    - Start and enable the service: 
        <sudo systemctl restart whatapp-broadcast.service>
    - Make sure you are already enable
        <sudo systemctl enable whatapp-broadcast>
    - Check the service status: <sudo systemctl status whatapp-broadcast>