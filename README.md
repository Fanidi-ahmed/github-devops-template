# GitHub DevOps Template

[![CI](https://github.com/Fanidi-ahmed/github-devops-template/actions/workflows/ci.yml/badge.svg)](https://github.com/Fanidi-ahmed/github-devops-template/actions/workflows/ci.yml)

A reusable FastAPI project template with testing, linting, Docker support, and GitHub Actions CI.

---

## Overview

This repository is a clean starting point for future:
- FastAPI backends
- internal Python tools
- DevOps automation services
- Dockerized microservices
- SaaS API foundations

It includes:
- FastAPI application
- healthcheck endpoint
- example business logic
- pytest tests
- ruff linting
- Docker build
- GitHub Actions CI pipeline

---

## Project Structure

```bash
github-devops-template/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── .dockerignore
├── .gitignore
├── Dockerfile
├── pyproject.toml
├── README.md
└── requirements.txt
Requirements
Python 3.11
Docker
Git
GitHub account
Local Setup

Clone the repository:

git clone https://github.com/Fanidi-ahmed/github-devops-template.git
cd github-devops-template

Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt
Run the API Locally

Start the FastAPI server:

uvicorn app.main:app --host 0.0.0.0 --port 8001
Available Endpoints
Root endpoint
curl http://127.0.0.1:8001/

Expected response:

{"message":"Hello from FastAPI","project":"github-devops-template","status":"ok"}
Health check
curl http://127.0.0.1:8001/health

Expected response:

{"status":"healthy"}
Add two numbers
curl "http://127.0.0.1:8001/add?a=2&b=3"

Expected response:

{"result":5}
Run the Tests
pytest
Run Lint Checks
ruff check .

To auto-fix simple issues:

ruff check . --fix
Run with Docker

Build the image:

docker build -t github-devops-template:local .

Run the container:

docker run --rm -p 8000:8000 github-devops-template:local

Test the containerized API:

curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/health
curl "http://127.0.0.1:8000/add?a=10&b=7"
CI Pipeline

The GitHub Actions workflow is defined in:

.github/workflows/ci.yml

It runs automatically on push and pull request to main or master.

Current CI stages:

checkout repository
install Python 3.11
install dependencies
run ruff lint checks
run pytest
build Docker image
Why This Template Matters

This project provides a reusable foundation for building professional repositories with:

clean structure
automated quality checks
container support
GitHub-based validation
a presentable public portfolio
Next Improvements

Possible next steps:

add Makefile
add pre-commit hooks
publish Docker image to GitHub Container Registry
add environment variable support
add Terraform validation workflow
create a second reusable template for Terraform projects

Author: Ahmed Fanidi
