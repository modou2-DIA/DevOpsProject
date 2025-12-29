
```markdown
# DevSecOps Backend Project – End-to-End Implementation

## 📌 Overview

This project demonstrates an **end-to-end DevSecOps workflow** applied to a lightweight REST API.
The objective is to design, secure, observe, containerize, automate, and deploy a backend service
using modern DevOps and Cloud-Native best practices.

This repository is intended to showcase **real-world DevOps skills** to technical recruiters and engineers.

---

## 🧱 Architecture Overview

- **Backend**: Python (Flask)
- **CI/CD**: GitHub Actions
- **Containerization**: Docker (multi-stage, non-root)
- **Security**: SAST + DAST + Image Scanning
- **Observability**: Structured logs, request tracing
- **Orchestration**: Kubernetes (Minikube)
- **Registry**: Docker Hub

---

## 🚀 Backend Service

- Lightweight REST API (<150 lines)
- Health endpoint: `/health`
- Designed for containerized environments
- Stateless & production-ready

---

## 🔁 CI/CD Pipeline (GitHub Actions)

The CI/CD pipeline automates **quality checks, security scans, container build and publication**.

### Pipeline Stages

### 1️⃣ Code Quality & Tests
- `flake8` for linting
- `pytest` for unit testing

### 2️⃣ Static Application Security Testing (SAST)
- **Bandit**: detects insecure Python patterns
- **Safety**: detects vulnerable dependencies (CVEs)
- Reports generated in JSON and uploaded as artifacts

### 3️⃣ Container Build & Image Scanning
- Docker image built locally using Buildx
- **Trivy** scans the image for CRITICAL and HIGH vulnerabilities
- Pipeline fails on critical findings

### 4️⃣ Dynamic Application Security Testing (DAST)
- Application started inside Docker
- **OWASP ZAP (baseline scan)** executed against the running API
- HTML report generated and stored as artifact

### 5️⃣ Image Publication
- Image pushed to Docker Hub **only if all checks pass**
- Tags:
  - `latest`
  - commit SHA (traceability)

📦 Docker image:
```

docker pull diamodou1968/devops-api:latest

````

---

## 🔐 Security Practices Implemented

- SAST (Bandit, Safety)
- DAST (OWASP ZAP)
- Container vulnerability scanning (Trivy)
- Non-root Docker container
- No secrets hardcoded
- Minimal base images

Security reports are available as CI artifacts.

---

## 📊 Observability

### Logs
- Structured JSON logs
- Log levels (INFO, ERROR)
- Timestamped entries
- Request context included

Example:
```json
{
  "timestamp": "2025-12-29T22:18:43Z",
  "level": "INFO",
  "request_id": "05e0d509-5776",
  "method": "GET",
  "path": "/health",
  "status_code": 200,
  "duration_ms": 0.35
}
````

### Tracing

* Unique Request ID generated per request
* Propagated through logs
* Returned in response headers (`X-Request-ID`)

### Metrics

* Health endpoint implemented
* Prometheus metrics endpoint planned as next improvement

---

## 🐳 Docker

### Best Practices Applied

* Multi-stage build
* Slim base image
* Non-root user
* Healthcheck
* Small attack surface

Build locally:

```bash
docker build -t devops-api .
docker run -p 8080:8080 devops-api
```

---

## ☸️ Kubernetes Deployment

### Environment

* Minikube (local cluster)

### Kubernetes Resources

* Namespace
* Deployment (2 replicas)
* Service (NodePort)
* ConfigMap
* Ingress (optional)
* Liveness & Readiness probes
* Resource requests & limits

### Commands

```bash
minikube start
kubectl create namespace devops-project
kubectl apply -f k8s/ -n devops-project
kubectl get all -n devops-project
minikube service devops-api-service -n devops-project
```

---

## 📦 Deliverables Checklist

✅ Source code & manifests
✅ CI/CD pipeline with security scans
✅ Docker image published
✅ Application deployed on Kubernetes
✅ Observability (logs + tracing)
✅ SAST & DAST evidence
✅ Recruiter-ready documentation

---

## 🧠 Lessons Learned

* Security must be automated early in CI/CD
* Observability is not optional in production systems
* Kubernetes requires health-aware applications
* DevOps is about **reliability, not scripts**
* Failing fast is a feature, not a bug

---

## 📈 Possible Improvements

* Prometheus `/metrics` endpoint
* Grafana dashboard
* Kubernetes-native DAST
* Cloud deployment (GKE / EKS)
* Alerting rules

---

## 👤 Author

**Modou DIA**
DevOps / Backend / Cloud Engineering Student
Focused on secure, observable, production-grade systems

```

---


