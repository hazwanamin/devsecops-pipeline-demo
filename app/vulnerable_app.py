import sqlite3
import os
import subprocess

# Hardcoded secrets - Gitleaks target
API_KEY = "sk-prod-9x8y7z6w5v4u3t2s1r0q"
DB_PASSWORD = "SuperSecret123!"

def get_user(username):
    # SQL Injection - string concat into execute
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = '" + username + "'")
    return cursor.fetchone()

def ping_host(hostname):
    # Command Injection - os.system with user input
    output = os.system("ping -c 4 " + hostname)
    return output

def run_command(cmd):
    # Dangerous shell=True subprocess
    result = subprocess.run(cmd, shell=True)
    return result

def get_user_v2(user_id):
    # Another SQL injection pattern
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = " + str(user_id)
    cursor.execute(query)
    return cursor.fetchone()
    # running tests