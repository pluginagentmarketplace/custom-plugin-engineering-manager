---
name: cloud-devops
description: Master cloud platforms and DevOps infrastructure. Learn containerization, orchestration, infrastructure as code, and CI/CD. Use when managing cloud deployments, infrastructure, or automated pipelines.
---

# Cloud & DevOps Infrastructure Skill

## Quick Start

DevOps combines development and operations to automate infrastructure and deployment processes.

### Docker Basic Example

```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000
CMD ["node", "index.js"]
```

### Docker Compose Example

```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production

  db:
    image: postgres:15
    environment:
      - POSTGRES_PASSWORD=secret
```

### Kubernetes Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: app
        image: my-app:latest
        ports:
        - containerPort: 3000
```

### Terraform Infrastructure

```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "web-server"
  }
}
```

## Technologies

### Container Technologies
- **Docker**: Image format, registries, networking
- **Podman**: Daemonless container alternative
- **Docker Compose**: Multi-container orchestration

### Container Orchestration
- **Kubernetes**: Production orchestration
  - Pods, Deployments, Services
  - ConfigMaps and Secrets
  - Ingress and networking
  - StatefulSets and DaemonSets
  - Helm for package management

- **Docker Swarm**: Simpler orchestration
- **AWS ECS**: Managed container service
- **Google Cloud Run**: Serverless containers

### Infrastructure as Code
- **Terraform**: Cloud-agnostic IaC
- **CloudFormation**: AWS-specific
- **Ansible**: Configuration management
- **Puppet**: Infrastructure automation
- **Bicep**: Azure IaC

### Cloud Platforms
- **AWS**
  - Compute: EC2, Lambda, ECS, EKS
  - Storage: S3, EBS, EFS
  - Databases: RDS, DynamoDB
  - Networking: VPC, Route 53, CloudFront
  - Management: CloudWatch, IAM

- **Azure**
  - Compute: VMs, App Service, AKS
  - Storage: Blob Storage, Managed Disks
  - Databases: Azure SQL, Cosmos DB
  - Networking: Virtual Networks, Application Gateway

- **GCP**
  - Compute: Compute Engine, Cloud Run, GKE
  - Storage: Cloud Storage, Persistent Disk
  - Databases: Cloud SQL, Firestore, BigQuery

### CI/CD Pipelines
- **GitHub Actions**: GitHub-native CI/CD
- **GitLab CI**: GitLab-integrated CI/CD
- **Jenkins**: Self-hosted automation
- **CircleCI**: Cloud-based CI/CD
- **ArgoCD**: GitOps for Kubernetes

### Monitoring & Logging
- **Prometheus**: Metrics collection
- **Grafana**: Metrics visualization
- **ELK Stack**: Elasticsearch, Logstash, Kibana
- **CloudWatch**: AWS monitoring
- **Stackdriver**: GCP monitoring
- **Azure Monitor**: Azure monitoring

### Linux & Shell
- **Linux Distribution**: Ubuntu, CentOS, Alpine
- **Shell Scripting**: bash, zsh
- **Package Managers**: apt, yum, pacman
- **User Management**: Users, groups, permissions
- **Services**: systemd, init scripts

## Learning Resources

- **Kubernetes**: https://kubernetes.io/docs/
- **Docker**: https://docs.docker.com/
- **Terraform**: https://www.terraform.io/docs/
- **AWS**: https://docs.aws.amazon.com/
- **Linux**: https://linux.die.net/

## When to Use This Skill

- Containerizing applications
- Setting up CI/CD pipelines
- Infrastructure provisioning
- Kubernetes deployment and management
- Cloud platform usage (AWS, Azure, GCP)
- Monitoring and logging setup
- Scaling and high availability
- Cost optimization
