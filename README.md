# Workflow Tracker Backend

Django Ninja backend API for the Mini Application Workflow Tracker.

## Tech Stack

- Django
- Django Ninja
- SQLite
- Render Deployment

---

# Features

- Create application drafts
- Update draft applications
- Submit applications
- Start review workflow
- Reviewer decisions
- Workflow validation rules
- REST API endpoints

---

# Workflow States

Draft → Submitted → Under Review → Approved / Rejected

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/HOSEWELL/workflow-tracker-backend.git
```

## 2. Navigate Into Project

```bash
cd workflow-tracker-backend
```

## 3. Create Virtual Environment

```bash
python -m venv venv
```

## 4. Activate Virtual Environment

### Linux / Mac

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# Start Development Server

```bash
python manage.py runserver
```

Backend runs on:

```txt
http://127.0.0.1:8000
```

---

# API Documentation

Django Ninja Swagger Docs:

```txt
http://127.0.0.1:8000/api/docs
```

---

# API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /api/applications | List applications |
| POST | /api/applications | Create draft |
| GET | /api/applications/{id} | Application details |
| PUT | /api/applications/{id} | Update draft |
| POST | /api/applications/{id}/submit | Submit application |
| POST | /api/applications/{id}/start-review | Start review |
| POST | /api/applications/{id}/decision | Reviewer decision |

---

# Workflow Rules

- Only Draft applications can be edited
- Only Draft applications can be submitted
- Only Submitted applications can move to Under Review
- Only Under Review applications can receive decisions
- Approved and Rejected applications are locked
- Rejected decisions require reviewer comments

---

# Assumptions

- SQLite was used for simplicity
- Authentication was not implemented due to assignment scope
- Single reviewer workflow assumed

---

# Improvements With More Time

- Authentication and authorization
- Role-based permissions
- Email notifications
- Pagination
- Search and filtering
- Docker support
- Unit and integration tests
- CI/CD pipelines
- PostgreSQL production database

---

# Deployment

Backend deployed on Render.

---

# Developed By

Hosewell Karanja
