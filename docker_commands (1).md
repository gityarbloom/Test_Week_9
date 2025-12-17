# Docker Commands

Fill in the Docker commands you used to complete the test.

## Volume

### Create the volume

```bash
docker volume create fastapi-db
```

### Seed the volume (via Docker Desktop)

```bash

```

## Server 1

### Build the image

```bash
docker build -t shopping-server1:v1 .
```
"""(הנתיב המלא הוא: ly_Tests/Test_Week_9/week9_docker/server1$ docker build -t shopp
ing-server1:v1 .
== יצירה מתוך הספרייה הנדרשת)"""

### Run the container

```bash
docker run -p 8000:8000 --mount source=fastapi-db,target=/app/db shopping-server1:v1
```

## Server 2

### Build the image

```bash
docker build -t shopping-server2:v1 .
"""מתוך תיקיית Server2"""
### Run the container

```bash
docker run -p 8080:8000 --mount source=fastapi-db,target=/app/db shopping-server2:v1
```
