

````markdown
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
- **Security**: SAST, DAST, Container Image Scanning
- **Observability**: Structured logs, request tracing
- **Orchestration**: Kubernetes (Minikube)
- **Container Registry**: Docker Hub

---

## 🚀 Backend Service

- Lightweight REST API (**< 150 lines of code**)
- Health check endpoint: `/health`
- Stateless and container-friendly
- Designed for Kubernetes readiness and scalability

---

## 🔁 CI/CD Pipeline (GitHub Actions)

The CI/CD pipeline automates **code quality checks, security scans, containerization, and publication**.

### Pipeline Stages

#### 1️⃣ Code Quality & Testing
- `flake8` for linting and code consistency
- `pytest` for unit testing

#### 2️⃣ Static Application Security Testing (SAST)
- **Bandit**: detects insecure Python code patterns
- **Safety**: scans dependencies for known CVEs
- Reports generated in JSON format and uploaded as CI artifacts

#### 3️⃣ Container Build & Image Security Scan
- Docker image built locally using Docker Buildx
- **Trivy** scans the image for CRITICAL and HIGH vulnerabilities
- Pipeline fails if critical vulnerabilities are detected

#### 4️⃣ Dynamic Application Security Testing (DAST)
- Application started in a Docker container
- **OWASP ZAP (baseline scan)** executed against the running API
- HTML security report generated and stored as artifact

#### 5️⃣ Image Publication
- Docker image pushed **only if all previous steps succeed**
- Image tags:
  - `latest`
  - Commit SHA (for traceability)

📦 Docker image available on Docker Hub:
```bash
docker pull diamodou1968/devops-api:latest
````

---

## 🔐 Security Practices Implemented

* Static code analysis (Bandit)
* Dependency vulnerability scanning (Safety)
* Container image scanning (Trivy)
* Dynamic runtime security testing (OWASP ZAP)
* Non-root Docker containers
* No hardcoded secrets
* Minimal and hardened base images

📁 All security reports are available as CI/CD artifacts.

---

## 📊 Observability

### Logs

* Structured **JSON logs**
* Standard log levels (INFO, ERROR)
* Timestamped entries
* Request context included (method, path, status, duration)

Example log entry:

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
```

### Tracing

* Unique **Request ID** generated per request
* Propagated through the application lifecycle
* Returned to the client via response header: `X-Request-ID`

### Metrics

* Health endpoint implemented
* Prometheus `/metrics` endpoint identified as next improvement

---

## 🐳 Docker

### Best Practices Applied

* Multi-stage builds
* Slim Python base images
* Non-root execution
* Docker healthcheck
* Reduced attack surface

### Local Build & Run

```bash
docker build -t devops-api .
docker run -p 8080:8080 devops-api
```

---

## ☸️ Kubernetes Deployment

### Environment

* Local Kubernetes cluster using **Minikube**

### Kubernetes Resources

* Namespace
* Deployment (2 replicas)
* Service (NodePort)
* ConfigMap
* Ingress (optional)
* Liveness & Readiness probes
* CPU & memory requests/limits

### Deployment Commands

```bash
minikube start
kubectl create namespace devops-project
kubectl apply -f k8s/ -n devops-project
kubectl get all -n devops-project
minikube service devops-api-service -n devops-project
```

---

## 📦 Deliverables Checklist

* ✅ Source code and Kubernetes manifests
* ✅ Automated CI/CD pipeline with security scans
* ✅ Docker image published on Docker Hub
* ✅ Application deployed on Kubernetes
* ✅ Observability (logs and tracing)
* ✅ SAST and DAST evidence
* ✅ Recruiter-ready documentation

---

## 🧠 Lessons Learned

* Security must be integrated early in CI/CD pipelines
* Observability is mandatory for production-grade systems
* Kubernetes requires health-aware applications
* DevOps focuses on **reliability and automation**
* Fast feedback and failure detection improve system quality

---

## 📈 Possible Improvements

* Prometheus `/metrics` endpoint
* Grafana dashboards
* Kubernetes-native DAST scanning
* Cloud deployment (GKE, EKS, DigitalOcean)
* Alerting and incident response workflows

---

## 👤 Author

**Modou DIA**
DevOps / Backend / Cloud Engineering Student
Focused on secure, observable, and production-grade systems

```

---


```
