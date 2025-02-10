<h1>Calender Application</h1>

<h2>Requirements</h2>
<ul>
    <li>
        Podman <br/>
        <i>`https://podman.io/docs/installation`</i>
    </li>
    <li>
        Datagrip <br/>
        <i>`https://www.jetbrains.com/datagrip/`</i>
    </li>
    <li>Python <br />
        `https://www.python.org/downloads/`
    </li>
</ul>

<h2>How to run the application</h2>
<ol>
    <li>Run `podman compose up -d`</li>
    <li>Go into the python container using `podman exec -it python bash` </li>
    <li>After going into python container run `pip install -r requirements.txt` and `python3 server.py`</li>
    <li>Open browser and go to `localhost:8080` to run the application</li>
</ol>

<b>
    Note: To develop instead of going to `localhost:8080` for app, go to terminal and change directory to frontend using 
    `cd frontend` and run `npm run dev`. Keep in mind to have the python server running.
</b>