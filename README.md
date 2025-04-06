# Kronos

## Project Overview
A full-stack calendar scheduling web application with support for creating, updating, deleting, and viewing events. Built using Flask for the backend and Vue for the frontend, containerized with Podman for seamless cross-platform development.

---

## Requirements
**Works on all operating systems as long as all dependencies are installed**

- **[Podman](https://podman.io/docs/installation)**
- **[Podman Compose](https://github.com/containers/podman-compose)**
- **[Python](https://www.python.org/downloads/)**
- **[DataGrip (Optional)](https://www.jetbrains.com/datagrip/)** – for viewing/managing the database

---

## Environment Variables

Create a `.env` file in the root directory with the following:

```env
MYSQL_DATABASE=YOUR-DATABASE
MYSQL_USER=YOUR-DATABASE-USER
MYSQL_PASSWORD=YOUR-DATABASE-PASSWORD
MYSQL_ROOT_PASSWORD=YOUR-DATABASE-ROOT-PASSWORD

ENVIRONMENT=development
```

Create a `.env` file in the backend directory with the following:
```env
DB_CONNECTION=YOUR-DATABASE
DB_NAME=YOUR-DATABASE-NAME
DB_USER=YOUR-DATABASE-USER
DB_PASSWORD=YOUR-DATABASE-PASSWORD
DB_HOST=YOUR-DATABASE-HOST
DB_PORT=YOUR-DATABASE-PORT
```
---

## Project Structure

```
calendar/
├── backend/               # Python backend
├── frontend/              # Vue.js frontend
├── .env                   # Environment variables
├── docker-compose.yml     # Container configuration
├── Dockerfile             # Python container image
└── README.md
```

---

## How to Run the Application

Before running the application, make sure that Podman and Podman Compose are installed and configured correctly.

> ⚠️ If you get the error `podman-compose not found in %PATH`, install the `podman-compose` binary.

> 🐳 If using Docker instead, replace all `podman` commands with `docker`.

### 1. Build and Run Containers

```bash
podman compose build --no-cache
podman compose up -d
```

### 2. Enter the Python Container

```bash
podman exec -it python bash
```

### 3. Install Backend Dependencies & Start Server

```bash
pip install -r requirements.txt
python3 server.py
```

### 4. Open in Browser

```
http://localhost:8080
```

---

### For Frontend Development

To run the frontend separately in development mode:

```bash
cd frontend
npm run dev
```

> Make sure the Python server is already running before starting the frontend.

---

## Bug Reports

1. Go to [Issues](https://github.com/aaronchristian99/calender/issues)
2. Click `New Issue`
3. Use a clear and concise title (e.g., `"Adding event crashes program"`)
4. In the description, include:
    - Steps to reproduce the bug
    - Any additional context or logs that help identify the problem

---