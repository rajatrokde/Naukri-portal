# Production Ready DevOps Full Stack Project

Includes:
- Frontend (Nginx static)
- Backend (Flask API)
- Dockerized services
- Kubernetes deployment
- Terraform AWS infra
- GitHub Actions CI/CD
- Monitoring placeholders

Structure:
frontend/
backend/
docker/
k8s/
terraform/
.github/workflows/

Deploy Flow:
1. Build docker images
2. Push to registry
3. Terraform infra
4. Deploy K8s