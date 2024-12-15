# 📚 Library Management API - README

## Project Overview

This project is a RESTful API designed for managing a library's collection of books. It includes functionality for adding, updating, searching, listing, and deleting books. The API is built using **Flask**, and its endpoints are documented with **Swagger**. Additionally, the project is Dockerized 🐳 for easy deployment, and GitHub Actions are used for continuous integration and deployment (CI/CD) to **Azure** ☁️.

## Features

1. **Add a new book** 📖
2. **List all books** 📚
3. **Search for books** by author, year, or genre 🔍
4. **Delete a book** by ISBN 🗑️
5. **Update book details** by ISBN ✏️

## Branch Strategy 🧑‍💻

This project uses the following GitHub branch strategy:

1. **main branch** - Stable branch containing production-ready code ✅
2. **backend branch** - Contains development of backend functionality 🔧
3. **deploy branch** - Contains the code that will be deployed to Azure 🚀

## GitHub Actions Workflows ⚙️

We use three GitHub Actions workflows for testing, building, and deploying the application:

1. **Pre-Merge Workflow** - Runs tests and lint checks on pull requests targeting the main branch 🔄
2. **Component Build Workflow** - Runs when changes are pushed to the backend branch to test and build backend components ⚡
3. **Deployment Workflow** - Runs when changes are pushed to the deploy branch to automatically deploy the application to Azure 🌐

## Steps to Set Up 🛠️

### 1. Clone the Repository 💻

First, clone the repository to your local machine:
```bash
git clone https://github.com/AlHasSaN0ALi/Assignment_1_SWE.git
cd Assignment_1_SWE
```

### 2. Set Up a Virtual Environment 🌱

Create and activate a virtual environment for Python:
```bash
python -m venv .venv
# Activate the virtual environment (Windows)
.\venv\Scripts\Activate.ps1
# Activate the virtual environment (macOS/Linux)
source .venv/bin/activate
```

### 3. Install Dependencies 📦

Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```

### 4. Running the Application Locally 🖥️

To run the Flask API locally, use the following command:
```bash
flask run
```
Access the API at [http://127.0.0.1:5000](http://127.0.0.1:5000).

### 5. Dockerizing the Application 🐋

To containerize the application using Docker, follow these steps:

#### 5.1. Create the Dockerfile 🔧

Create a `Dockerfile` in the project root directory:
```Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app when the container launches
CMD ["flask", "run"]
```

#### 5.2. Build the Docker Image ⚙️

Build the Docker image using the following command:
```bash
docker build -t library-management-api .
```

#### 5.3. Run the Docker Container 🚢

Run the application inside a container:
```bash
docker run -p 5000:5000 library-management-api
```

### 6. Set Up Azure Deployment ☁️

#### 6.1. Create an Azure App Service 🏢

1. Log into the [Azure Portal](https://portal.azure.com/).
2. Create a new **App Service** for Python 🐍.
3. Choose the **Python 3.x** runtime.
4. Configure the **Resource Group**, **App Name**, and **Region**.
5. Click **Create** to deploy the App Service.

#### 6.2. Set Up Azure Secrets in GitHub 🔐

1. Create an Azure Service Principal 🛡️:
```bash
az ad sp create-for-rbac --name "github-actions-service-principal" --role contributor --scopes /subscriptions/<your-subscription-id>/resourceGroups/<your-resource-group> --sdk-auth
```
2. Add the following secrets to your GitHub repository 🧩:
   - **AZURE_SUBSCRIPTION_ID**
   - **AZURE_CREDENTIALS** (service principal JSON)

#### 6.3. Push Changes to Deploy Branch 🔄

Push code to the `deploy` branch to trigger deployment 🔥:
```bash
git checkout deploy
git push origin deploy
```

### 7. GitHub Actions Workflows 🔄

#### 7.1. Pre-Merge Workflow ⚙️

This workflow runs on pull requests targeting the **main branch**. It checks for code quality by running **linting** and **tests** before merging.

Example `.github/workflows/pre-merge.yml`:
```yaml
name: Pre-Merge Workflow

on:
  pull_request:
    branches:
      - main

jobs:
  lint_and_test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      - name: Lint Python code
        run: |
          pip install flake8
          flake8 .
      - name: Run tests
        run: |
          pytest
```

#### 7.2. Component Build Workflow ⚙️

This workflow runs on **push events** to the `backend` branch, testing and building backend components.

Example `.github/workflows/component-build.yml`:
```yaml
name: Component Build Workflow

on:
  push:
    branches:
      - backend

jobs:
  build_backend:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      - name: Run backend tests
        run: |
          pytest tests/backend
```

#### 7.3. Deployment Workflow 🚀

This workflow runs on **push events** to the `deploy` branch and deploys the app to **Azure**.

Example `.github/workflows/deployment.yml`:
```yaml
name: Deployment Workflow

on:
  push:
    branches:
      - deploy

jobs:
  deploy_to_azure:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      - name: Set up Azure CLI
        uses: Azure/azure-cli-action@v1
        with:
          azure-subscription: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
          azure-credentials: ${{ secrets.AZURE_CREDENTIALS }}
      - name: Deploy to Azure
        run: |
          az webapp up --name <YOUR_AZURE_APP_NAME> --resource-group <YOUR_RESOURCE_GROUP> --plan <YOUR_APP_SERVICE_PLAN>

```



```markdown
## Commands Used 💻

1. **Create Virtual Environment** 🌱
```bash
python -m venv .venv
```

2. **Activate Virtual Environment** (Windows) 🪟
```bash
.\\venv\\Scripts\\Activate.ps1
```

3. **Install Dependencies** 📦
```bash
pip install -r requirements.txt
```

4. **Create Git Branches** 🧑‍💻
```bash
git checkout -b backend
git checkout -b deploy
```

5. **Push to GitHub** ⬆️
```bash
git push origin backend
git push origin deploy
```

6. **Create Dockerfile** 🐋
- Write the Dockerfile in the root directory of your project.

7. **Build Docker Image** 🏗️
```bash
docker build -t library-management-api .
```

8. **Run Docker Container** 🚢
```bash
docker run -p 5000:5000 library-management-api
```

9. **Azure Service Principal Creation** 🔑
```bash
az ad sp create-for-rbac --name "github-actions-service-principal" --role contributor --scopes /subscriptions/<your-subscription-id>/resourceGroups/<your-resource-group> --sdk-auth
```

10. **Create Azure App Service** ☁️
- Follow the instructions on the Azure portal to create an App Service for Python, choose the desired **Resource Group**, **App Name**, and **Region**.

11. **Push Code to Deploy Branch** 🚀
```bash
git checkout deploy
git push origin deploy
```

---

### Deployment Verification 🔍

- After pushing the code to the `deploy` branch, the GitHub Action will trigger the **deployment workflow**.
- Visit the **Azure Portal**, and check if your **App Service** is live with the Flask API.
- Access the deployed application using the provided URL.

---

### Conclusion 🎉

With this project, you now have a fully **Dockerized** 🐋, **CI/CD-enabled** ⚙️ **Library Management API** 📚 that automates the entire development, build, and deployment cycle. Through **GitHub Actions** and **Azure**, we’ve automated the process to ensure faster, more reliable updates to the live environment. By following the steps in this **README**, you can easily manage, test, and deploy your library management API to the cloud!

```





