import sqlite3
import os
import subprocess

# Hardcoded secret - Gitleaks should catch this
API_KEY = "sk-prod-9x8y7z6w5v4u3t2s1r0q"
DB_PASSWORD = "SuperSecret123!"

def get_user(username):
    # SQL Injection - Semgrep should catch this
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()

def ping_host(hostname):
    # Command Injection - Semgrep should catch this
    output = os.system("ping -c 4 " + hostname)
    return output

def run_command(cmd):
    # Dangerous subprocess usage - Semgrep should catch this
    result = subprocess.run(cmd, shell=True)
    return result