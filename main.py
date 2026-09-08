import subprocess

cmd = """
wget -qO- https://raw.githubusercontent.com/komari-monitor/komari-agent/refs/heads/main/install.sh |
sudo bash -s -- -e https:// --auto-discovery yU
"""

subprocess.run(cmd, shell=True, check=True)
