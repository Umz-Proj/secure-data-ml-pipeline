# Threat Model – Secure Data ML Pipeline

## 1. System Components

- External API (data source)
- ETL Service (Python container)
- Processed Data Storage
- ML API Service
- Docker Engine
- GitHub CI/CD Pipeline

---

## 2. Assets to Protect

- API keys
- Processed dataset
- ML model file
- Container images
- Source code
- Logs

---

## 3. Potential Threats

- Hardcoded secrets in code
- API data manipulation
- Data poisoning attacks
- Container vulnerabilities
- Supply chain attacks
- Unauthorized API access
- Log tampering

---

## 4. Planned Security Controls

- Environment variables for secrets
- Input validation in ETL & API
- Container vulnerability scanning
- Static code analysis (SAST)
- Logging and monitoring
- Authentication for ML API