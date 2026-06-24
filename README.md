\# DevSecOps Pipeline Demo



A CI/CD security pipeline built with GitHub Actions that automatically

scans for vulnerabilities on every push — blocking builds when security

issues are detected before code reaches production.



\## What this demonstrates

\- Automated SAST scanning integrated into a CI/CD pipeline

\- Secrets detection across the entire codebase

\- Pipeline configured to fail on findings — blocking insecure code

&#x20; from being merged

\- Real-world tool usage: Semgrep and Gitleaks



\---



\## Pipeline Jobs



\### 1. Semgrep SAST

Scans source code for insecure coding patterns using the OWASP Top 10

and Python security rulesets. Runs on every push to main.



\*\*Finding detected:\*\*



app/vulnerable\_app.py



python.lang.security.audit.subprocess-shell-true — BLOCKING



Found 'subprocess' function 'run' with 'shell=True'. This is dangerous



because this call will spawn the command using a shell process, making



it easier for a malicious actor to execute arbitrary commands.



Line 23: result = subprocess.run(cmd, shell=True)



Rules run: 209 | Files scanned: 5 | Findings: 1 blocking



!\[Semgrep Finding](./screenshots/semgrep-finding.png)



\---



\### 2. Gitleaks Secrets Scan

Scans all files for hardcoded credentials, API keys, and tokens.

Runs on every push with full git history depth.



\*\*Findings detected — 5 total, 1 real, 4 false positives:\*\*



Real finding:

\- app/vulnerable\_app.py line 6 — hardcoded API key ✅



False positives suppressed:

\- README.md lines 42, 221, 223, 259 — example strings in 

&#x20; documentation, not live credentials. Confirmed false positives.

&#x20; Suppression via --gitleaks-ignore-path not applied in this demo 

&#x20; to preserve the false positive triage example.

devsecops-pipeline-demo/



.github/



workflows/



security.yml      ← GitHub Actions pipeline definition



app/



vulnerable\_app.py   ← Deliberately vulnerable target



screenshots/



semgrep-finding.png



gitleaks-finding.png



requirements.txt      ← Outdated dependencies with known CVEs



.gitleaksignore       ← Suppressed false positives with rationale



README.md

