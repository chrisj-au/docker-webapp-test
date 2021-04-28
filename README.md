
# Description

Test webapp for deploying to ECS using CodeDeploy (Using external IaC).

# Dependancies

- External IaC for ECS, CodeDeploy etc
- /status endpoint
- /api/service-test prefix on all routes

# Usage

`docker build -t webapp-test:v1 .`

`docker run -it --rm --name webapp-test webapp-test:v1`
