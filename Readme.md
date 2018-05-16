#### code quality using pre-commit hooks

__pre-commit-hooks__

> aliased python to python3

```
brew install pre-commit
```

```
sudo easy_install pip
sudo pip install pre-commit-hooks
```

Install pre commit hooks in `.pre-commit-config.yaml` to `.git/hooks/pre-commit`

```
pre-commit install
```

## Docker based run

build the docker image

```
docker build -t "opencv-project:004" .
```

run the container

```
docker run -v `pwd`:/app -it opencv-project:004
```

```
cd detect-face
python detect_faces.py
```
