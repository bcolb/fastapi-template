# fastapi-template

Everyone needs a starting point. Here is a very simple one for FastAPI.

## Usage

First, open up a terminal and clone the repository.

```
git git@github.com:bcolb/fastapi-template.git
```

Next, navigate into the freshly cloned repo.

```
cd fastapi-template
```

### Running locally with a virtual environment

Run the following commands to create a local virtual environment, source it, and install the requirements.

```
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

Now, start the app using uvicorn.

```
uvicorn app.main:app --reload 
```

The uvicorn server will start up and you'll see log info starting to print to stdout in the terminal, akin to this.

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Next check to see that you can access the site locally by navigating in a browser to 
- http://localhost:8000/

You should see the following message:

```
{"message":"hello"}
```

Likewise, the following url will serve up docs related to the defined API.
- http://localhost:8000/docs


Alternatively, use curl to get the web page.

```
curl http://localhost:8000/
```

### Running From VS Code

With the addition of the the .vscode/launch.json file you can run the app using Run & Debug in VS Code.

### Running From Docker

This repo has been setup to use docker-compose to manage the docker container. With the following command docker-compose will build the image, create and start the container.

```
docker compose up -d
```

Using the -d flag will run docker in daemon mode meaning you retain access to your terminal window. To stop the docker container(s) and application run:

```
docker compose down
```

Confirm that your FastAPI API endpoint is available by using curl or navigating to the following URL in your browser http://localhost:8008/


## Testing

Pytest tests are located in the 'tests' directory. To run them, make sure the virtual environment is sourced and then enter:

```
pytest
```
