# 🚀 OtakuVault Platform Engineering

> **Building, operating, and scaling a cloud-native anime merchandise e-commerce platform on Microsoft Azure using Site Reliability Engineering (SRE) principles.**

---

## 📖 Project Overview

OtakuVault is a hands-on platform engineering project designed to simulate how a modern engineering team builds and operates a production-grade e-commerce application.

Instead of creating isolated Azure resources or following simple Kubernetes tutorials, this project focuses on solving real business problems while implementing industry-standard engineering practices.

The platform is built using **Microsoft Azure**, **Azure Kubernetes Service (AKS)**, **Docker**, **FastAPI**, and **GitHub Actions**, with a strong emphasis on reliability, observability, scalability, and automation.

This repository documents every architectural decision, deployment, incident, and operational improvement throughout the journey.

---

# 🎯 Mission

Build an enterprise-ready cloud platform capable of hosting a modern anime merchandise e-commerce application while learning:

* Azure Infrastructure
* Azure Kubernetes Service (AKS)
* Site Reliability Engineering (SRE)
* Kubernetes
* Docker & Containerization
* CI/CD
* Monitoring & Observability
* Incident Response
* Production Operations
* Cloud Architecture

---

# 🏗️ Project Vision

The goal is to build a production-like platform that hosts an anime merchandise store where customers can:

* Create an account
* Browse products
* Search merchandise
* Add products to cart
* Place orders
* Track order history

While the application provides the business functionality, the primary focus of this project is designing and operating the underlying cloud platform.

---

# 🛠️ Technology Stack

## Cloud Platform

* Microsoft Azure
* Azure Kubernetes Service (AKS)
* Azure Container Registry (ACR)
* Azure Monitor
* Log Analytics Workspace
* Virtual Networks
* Microsoft Entra ID
* Azure Key Vault *(planned)*

## Backend

* Python
* FastAPI

## Frontend *(planned)*

* React

## Containerization

* Docker

## CI/CD *(planned)*

* GitHub Actions

## Messaging *(planned)*

* RabbitMQ

## Database *(planned)*

* MongoDB

## Caching *(planned)*

* Redis

## AI Features *(future roadmap)*

* Azure AI Foundry
* Azure OpenAI
* Product Recommendation Engine

---

# 🏛️ High-Level Architecture

```text
Internet
    │
Azure Front Door (Future)
    │
NGINX Ingress
    │
──────────────────────────────
Azure Kubernetes Service (AKS)
──────────────────────────────

Frontend

│

├── Catalog Service
├── User Service
├── Cart Service
├── Order Service
├── Payment Service

──────────────────────────────

Azure Container Registry

Azure Monitor

Log Analytics Workspace

GitHub Actions

Azure Key Vault (Future)
```

---

# 📂 Repository Structure

```text
otakuvault-platform/

├── backend/
│   └── catalog-service/
│
├── infrastructure/
│
├── kubernetes/
│
├── monitoring/
│
├── runbooks/
│
├── incidents/
│
├── docs/
│
└── .github/
```

---

# 🚀 Sprint Roadmap

## Sprint 1 – Azure Foundation

* [x] Create Azure Subscription
* [x] Create Resource Group
* [x] Create Log Analytics Workspace
* [ ] Create Azure Container Registry
* [ ] Create Virtual Network
* [ ] Deploy AKS Cluster

---

## Sprint 2 – Application Foundation

* [ ] Build Catalog Service (FastAPI)
* [ ] Dockerize Application
* [ ] Push Image to Azure Container Registry
* [ ] Deploy to AKS

---

## Sprint 3 – Kubernetes Fundamentals

* [ ] Pods
* [ ] Deployments
* [ ] Services
* [ ] Namespaces
* [ ] ConfigMaps
* [ ] Secrets

---

## Sprint 4 – Production Operations

* [ ] Monitoring
* [ ] Logging
* [ ] Alerts
* [ ] Dashboards

---

## Sprint 5 – Reliability Engineering

* [ ] Autoscaling
* [ ] Health Probes
* [ ] Rolling Updates
* [ ] Self-Healing
* [ ] Incident Simulations

---

## Sprint 6 – CI/CD

* [ ] GitHub Actions
* [ ] Automated Build
* [ ] Automated Deployment
* [ ] Image Versioning

---

# 🎓 Learning Philosophy

This repository is intentionally built differently from a traditional tutorial.

Every Azure service is introduced by answering five questions:

1. What business problem does it solve?
2. Why is it needed?
3. Where does it fit in the architecture?
4. How does Kubernetes interact with it?
5. What happens if it fails?

The objective is to understand **why** each technology exists instead of memorizing commands.

---

# 📚 Engineering Documentation

Throughout the project, the following documentation will be maintained:

* Architecture Decision Records (ADR)
* Infrastructure Documentation
* Deployment Guides
* Runbooks
* Incident Reports
* Root Cause Analysis (RCA)
* Postmortems

---

# 🎯 Project Goals

By the completion of this project, the platform will include:

* Production-style Azure architecture
* Kubernetes-based microservices
* Infrastructure documentation
* CI/CD pipelines
* Monitoring dashboards
* Incident response playbooks
* Security best practices
* AI-powered product recommendations
* A portfolio-quality engineering project suitable for interviews

---

# 👨‍💻 Author

**Sedjwick Drego**

Platform Engineering • Azure • Kubernetes • Site Reliability Engineering

---

> **"Don't memorize cloud services. Understand the engineering problems they solve."**
