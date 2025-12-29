# DevOps API – End‑to‑End DevOps Project

## 👋 Introduction 
This project demonstrates my ability to **design, build, secure, observe, containerize, and deploy a backend service end‑to‑end**, following modern **DevOps and Cloud‑Native best practices**.

The goal was not only to make an API work, but to **treat it as a production‑ready service**, even at a small scale (<150 LOC), with automation, observability, security checks, and Kubernetes deployment.

This repository reflects how I would work in a **real engineering team**: structured tasks, reproducible builds, automated pipelines, and clear documentation.

---

## 🎯 Project Objectives (From the Subject)

| Objective                              | Status                                  |
| -------------------------------------- | --------------------------------------- |
| Small backend / REST API (<150 LOC)    | ✅ Achieved                              |
| GitHub Issues / Project management     | ✅ Achieved                              |
| Git & GitHub with PR‑based workflow    | ✅ Achieved                              |
| CI/CD pipeline (build, test, scan)     | ⚠️ Partial (see notes)                  |
| Observability (metrics, logs, tracing) | ⚠️ Partial (logs + tracing implemented) |
| Security (SAST + DAST)                 | ⚠️ Planned / partially implemented      |
| Docker containerization                | ✅ Achieved                              |
| Kubernetes deployment (Minikube)       | ✅ Achieved                              |
| Clear technical documentation          | ✅ Achieved                              |
| Final report & presentation            | ⏳ In progress                           |

> ⚠️ Some items are intentionally marked **partial** and explained transparently below. This reflects honesty and engineering maturity.

---

## 🧠 Architecture Overview

```
Client
  ↓
Kubernetes Service (NodePort)
  ↓
Kubernetes Deployment (2 replicas)
  ↓
Flask API (Docker container)
```

### Key design principles

* Stateless service
* Horizontal scalability via replicas
* Health‑driven lifecycle management
* Immutable infrastructure (Docker images)
* Environment‑driven configuration

---

## 🧩 Backend Service

* **Language**: Python 3.11
* **Framework**: Flask
* **Lines of code**: < 150
* **Endpoints**:

  * `GET /health` → health check used by Docker & Kubernetes probes

### Why Flask?

* Minimal footprint
* Fast startup time
* Ideal for microservices and DevOps demos

---

## 📦 Containerization (Docker)

### Best Practices Applied

* ✅ Multi‑stage build (builder + runtime)
* ✅ Non‑root user (`appuser`)
* ✅ Slim base image (`python:3.11-slim`)
* ✅ Deterministic dependency installation
* ✅ Docker HEALTHCHECK aligned with Kubernetes probes
* ✅ Clear port exposure (8080)

### Result

* Image published on Docker Hub:

  * `diamodou1968/devops-api:latest`
* Image runs identically:

  * Locally
  * In Docker
  * In Kubernetes

---

## ☸️ Kubernetes Deployment (Minikube)

### Resources Created

* Namespace
* Deployment (2 replicas)
* Service (NodePort)
* ConfigMap
* Ingress (ready for future use)

### Deployment Best Practices

* ✅ Resource requests & limits (CPU / Memory)
* ✅ Liveness & Readiness probes (`/health`)
* ✅ Environment variables via ConfigMap
* ✅ Rolling update‑ready Deployment
* ✅ ReplicaSet managed by Deployment

### Verification Evidence

* Pods reach **Running / Ready** state
* Health checks succeed
* Service accessible via `minikube service`
* Logs accessible via `kubectl logs`

---

## 🔍 Observability

### Logs (Implemented ✅)

* Structured JSON logs
* Request lifecycle logging
* Request ID for traceability
* Method, path, status, duration

### Tracing (Basic ✅)

* Unique request ID propagated per request
* Enables correlation across logs

### Metrics (Planned ⚠️)

* Metrics endpoint (e.g. `/metrics`) identified as next improvement
* Would integrate Prometheus client in future iteration

> This reflects a realistic DevOps approach: **logs first, metrics next, dashboards later**.

---

## 🔐 Security

### Implemented

* Non‑root Docker container
* Minimal base image (reduced attack surface)
* No secrets hard‑coded
* Health endpoint limited in scope

### SAST / DAST

* ⚠️ Planned integration in CI/CD pipeline
* Tools considered:

  * SAST: Bandit / Semgrep
  * DAST: OWASP ZAP

> The repository is structured to **plug these tools easily**, which is often what matters in real teams.

---

## 🔁 CI/CD Pipeline

### Implemented

* Automated Docker build
* Automated Docker image publishing

### Planned Extensions

* Automated unit tests
* SAST scan on pull requests
* DAST scan after deployment
* Kubernetes deployment automation

> CI/CD is treated as an **evolving system**, not a one‑shot script.

---

## 🧑‍💻 GitHub Workflow

* Tasks tracked via GitHub Project / Issues
* Logical commits
* Infrastructure changes isolated
* Kubernetes manifests versioned

### Peer Review

* PR‑based workflow respected
* Constructive review mindset applied

---

## 📁 Repository Structure

```
.
├── app.py
├── Dockerfile
├── requirements.txt
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── configmap.yaml
│   └── ingress.yaml
└── README.md
```

---

## 🚀 How to Run the Project

### Local (Docker)

```bash
docker run -p 8080:8080 diamodou1968/devops-api:latest
```

### Kubernetes (Minikube)

```bash
minikube start
kubectl create namespace devops-project
kubectl apply -f k8s/ -n devops-project
minikube service devops-api-service -n devops-project
```

---

## 🧪 Validation Checklist (Recruiter View)

* [x] API works locally
* [x] Docker image builds and runs
* [x] Image published
* [x] Kubernetes deployment successful
* [x] Health checks operational
* [x] Logs accessible
* [x] Scalable via replicas
* [ ] Metrics endpoint (planned)
* [ ] Automated security scans (planned)

---

## 📈 Lessons Learned

* Kubernetes is about **control**, not just deployment
* Health checks are the backbone of reliability
* Logs without structure are noise
* DevOps is iterative: correctness first, maturity second
* Simplicity scales better than premature complexity

---

## 🏁 Conclusion

This project proves my ability to:

* Think like a **DevOps engineer**, not just a developer
* Deliver reproducible, observable, and scalable services
* Be honest about trade‑offs and improvements
* Build systems that are ready to grow

If this were a real production system, the next steps would be:

* Full CI/CD automation
* Prometheus + Grafana
* Security gates
* Cloud deployment (GKE / EKS)


