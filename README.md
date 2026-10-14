# cicd-demo

Flask web app with an automated CI/CD pipeline (GitHub Actions -> Docker Hub -> AWS EC2).

## Pipeline
1. **test** - installs dependencies and runs pytest on every push / pull request
2. **package** - builds a Docker image and pushes it to Docker Hub (tags: `latest` and commit SHA)
3. **deploy** - SSHs into the EC2 server, pulls the image, restarts the container, runs a health check

## Endpoints
- `/` - home page
- `/health` - health check (`{"status":"ok"}`)
- `/add/<a>/<b>` - returns the sum

## Run locally
```
pip install -r requirements.txt
pytest -v
python app.py
```

## Required GitHub secrets
`DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN`, `EC2_HOST`, `EC2_USER`, `EC2_SSH_KEY`
