# 🐳 Containerization Lab

A collection of Docker containerization examples demonstrating various Python and Shell scripts running inside Docker containers.

---

## 📋 Prerequisites

- Docker installed and running on your system
- Basic knowledge of Docker commands

---

## 📁 Program List

| Program | Description | Type |
|---------|-------------|------|
| Program-1 | Hello World | Python |
| Program-2 | Calculator (Basic Arithmetic) | Python |
| Program-3 | CPU Delay Simulation | Python |
| Program-4 | Factorial Calculator | Python |
| Program-5 | Environment Variables Display | Python |
| Program-6 | Ping Host Connectivity | Python |
| Program-7 | Prime Number Checker | Python |
| Program-8 | Shell Script Demo | Bash |
| Program-9 | Temperature Converter | Python |

---

## 🚀 Commands to Build and Run Each Program

### Programs

```bash
# Navigate to Programs directory
cd ProgramNames

# Build the Docker image
docker build -t PythonFileName .

# Run the container
docker run PythonFileName
```

### Program-7: Prime Number Checker
Checks if a given number is prime or not

```bash
# Navigate to Program-7 directory
cd Program-7

# Build the Docker image
docker build -t prime-app .

# Run the container (interactive mode required for user input)
docker run -it prime-app
```

### Build All Images
```bash
# From the root Containerization Lab directory
docker build -t hello-world-app ./Program-1
docker build -t calci-app ./Program-2
docker build -t cpu-delay-app ./Program-3
docker build -t fact-app ./Program-4
docker build -t env-app ./Program-5
docker build -t ping-app ./Program-6
docker build -t prime-app ./Program-7
docker build -t shell-app ./Program-8
docker build -t temp-app ./Program-9
```

### Run Non-Interactive Programs
```bash
docker run hello-world-app
docker run cpu-delay-app
docker run env-app
docker run ping-app
docker run shell-app
```

### Run Interactive Programs
```bash
docker run -it calci-app
docker run -it fact-app
docker run -it prime-app
docker run -it temp-app
```

## 🧹 Cleanup Commands

```bash
# List all containers
docker ps -a

# Remove a specific container
docker rm <container_id>

# Remove all stopped containers
docker container prune

# List all images
docker images

# Remove a specific image
docker rmi <image_name>

# Remove all unused images
docker image prune -a

# Remove all (containers, images, networks, cache)
docker system prune -a
```

---

## 📝 Useful Docker Commands

| Command | Description |
|---------|-------------|
| `docker build -t <name> .` | Build an image with a tag |
| `docker run <image>` | Run a container from an image |
| `docker run -it <image>` | Run container in interactive mode |
| `docker run -d <image>` | Run container in detached mode |
| `docker run -e VAR=value <image>` | Run with environment variable |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker images` | List all images |
| `docker logs <container>` | View container logs |
| `docker exec -it <container> bash` | Access container shell |
| `docker stop <container>` | Stop a running container |
| `docker rm <container>` | Remove a container |
| `docker rmi <image>` | Remove an image |

---

## 📌 Notes

- Programs that require user input (2, 4, 7, 9) must be run with `-it` flag for interactive mode
- Program-3 (CPU Delay) runs for approximately 30 seconds
- Program-6 (Ping) requires network connectivity from the container
- Program-5 demonstrates passing environment variables to containers

---

## 👨‍💻 Author

Containerization Lab - Docker Learning Examples
