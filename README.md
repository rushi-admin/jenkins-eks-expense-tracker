# Jenkins EKS Expense Tracker (DevOps CI/CD Project)

This project demonstrates an **end-to-end DevOps CI/CD pipeline** using **Jenkins, Docker, Kubernetes (EKS), and GitHub**.
The application is a **Python Flask Expense Tracker** with a simple UI for adding and visualizing expenses (tables + charts).

---

## Project Features

* **Flask-based Expense Tracker App**

  * Add, view, and categorize expenses
  * Visualize expenses by **category (Pie chart)** and **date (Bar chart)**
* **Dockerized Application** → Container images built via Jenkins and pushed to DockerHub
* **Kubernetes (EKS) Deployment** → Application runs on AWS EKS with LoadBalancer service
* **Jenkins CI/CD Pipeline** → Fully automated from **code commit → build → deploy**

---

## Tech Stack

* **Backend**: Python (Flask)
* **Database**: SQLite
* **Frontend**: HTML, Bootstrap, Chart.js
* **DevOps Tools**: Jenkins, Docker, Kubernetes (EKS), GitHub, DockerHub
* **Cloud**: AWS (EKS, EC2 for Jenkins)

---

## Project Structure

```
expense-tracker/
 ├── app.py                # Flask application
 ├── requirements.txt      # Python dependencies
 ├── templates/            # HTML templates
 ├── static/               # CSS/JS assets
 ├── Dockerfile            # Docker build file
 ├── deployment.yaml       # Kubernetes Deployment
 ├── service.yaml          # Kubernetes Service (LoadBalancer)
 └── Jenkinsfile           # Jenkins pipeline script
```

---

## CI/CD Pipeline Flow

1. **Developer commits code** → GitHub repo
2. **Jenkins** (on EC2) triggers pipeline
3. **Build Stage** → Jenkins builds Docker image
4. **Push Stage** → Jenkins pushes image to DockerHub
5. **Deploy Stage** → Jenkins applies Kubernetes manifests on **EKS**
6. **EKS** → Runs the Expense Tracker app, accessible via LoadBalancer DNS

---

## Setup Instructions

### 1️⃣ Clone Repo

```bash
git clone https://github.com/<your-username>/jenkins-eks-expense-tracker.git
cd jenkins-eks-expense-tracker
```

### 2️⃣ Run Locally (Optional)

```bash
pip install -r requirements.txt
python app.py
```

Access at: `http://localhost:5000`

### 3️⃣ Build & Run with Docker

```bash
docker build -t expense-tracker .
docker run -p 5000:5000 expense-tracker
```

Access at: `http://localhost:5000`

### 4️⃣ Deploy to Kubernetes (EKS)

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

Access via:

```bash
kubectl get svc expense-service
```

---

## Architecture Diagram

```
   Developer → GitHub Repo → Jenkins Pipeline → DockerHub → EKS → LoadBalancer → User
<img width="457" height="639" alt="jenkins_eks_expense_tracker_architecture" src="https://github.com/user-attachments/assets/e9f0c6c7-a447-45e4-8c4a-f97a1280c330" />

```

---

## Jenkins Pipeline Stages

* **Checkout** → Pull code from GitHub
* **Build** → Build Docker image
* **Push** → Push image to DockerHub
* **Deploy** → Deploy app to EKS using `kubectl`

---

## Access

Once deployed, you can access the app via the **AWS LoadBalancer URL**:

```
http://<elb-dns-name>
```

---

## Learnings from this Project

✔ Setting up Jenkins on AWS EC2
✔ Writing Jenkins pipelines (Jenkinsfile)
✔ Building & pushing Docker images to DockerHub
✔ Deploying to AWS EKS with Kubernetes manifests
✔ Creating an **end-to-end CI/CD pipeline**

---

