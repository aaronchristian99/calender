# Calendar Application

## Requirements
**Works on all operating systems as long as all dependecies are installed**
- **Podman**  
  [Installation Guide](https://podman.io/docs/installation)

- **Podman Compose**  
  [Installation Guide](https://github.com/containers/podman-compose)

- **DataGrip**  
  [Download DataGrip](https://www.jetbrains.com/datagrip/)

- **Python**  
  [Download Python](https://www.python.org/downloads/)

## How to Run the Application
Before running the application make sure that Podman and Podman Compose are installed and configured correctly.

**_If you get this error `podman-compose not found in %PATH` please install `podman-compose` binary library._**

**_If using Docker replace all commands with 'docker' instead of 'podman'_**
1. Run:
   ```
   podman compose build --no-cache
   podman compose up -d
    ```
   
2. Enter the Python container:
    ```
   podman exec -it python bash
   ```
   
3. Inside the container, install dependencies and start the server:
    ```
    pip install -r requirements.txt
    python3 server.py
   ```
   
4. Open your browser and go to:
    ```
   http://localhost:8080
   ```
   
**Note:**
To develop frontend separately:
- Instead of opening `localhost:8080`, open a terminal
- Navigate to frontend directory:
``` 
cd frontend
```
- Run the development server:
```
npm run dev
```
**Make sure python server is running before the frontend.**

**If running on windows platform, ensure script.sh has line endings with 'LF' than 'CRLF'. You can manually convert it 
by using Intellij, visual code, notepad++ or any IDE**

## Bug Reports
- Go to [Issues](https://github.com/aaronchristian99/calender/issues)
- Click 'New Issue'
- The title should sufficiently summarize the bug
  - eg. "Adding event crashes program"
- The description should include
  - A descriptive guide to reproduce the bug
  - Any extra details to narrow the source of the bug
