import subprocess
import os
import dotenv

# Load the .env file to update the SECRET_KEY
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

# Generate a new Django SECRET_KEY and update it in the .env file
from django.core.management.utils import get_random_secret_key
scrt = get_random_secret_key()
dotenv.set_key('.env', 'SECRET_KEY', scrt)

# Build and start the Docker containers in detached mode
subprocess.run("docker-compose up --build -d", shell=True)

# Check if the containers started successfully
command = "docker ps"
result = subprocess.run(command, shell=True, capture_output=True, text=True)

# Look for both the web service and the database container in the output
search_string = "socialnet-web"
another_string = "postgres:16"

# Check if both containers are running
if search_string in result.stdout and another_string in result.stdout:
    print("Build Success")
else:
    print("Build Failed. Please check the logs for more information.")

# Function to retrieve the container ID of the 'socialnet-web' service
def pid():
    if os.name == "nt":
        # Windows systems
        pid = subprocess.run("docker ps -aqf name=socialnet-web", shell=True, capture_output=True, text=True)
    elif os.name == "posix":
        # Unix-like systems (Linux, macOS)
        pid = subprocess.run("docker ps -aqf name=socialnet-web", shell=True, capture_output=True, text=True)
    else:
        print("OS not supported, Contact the developer for more information.")
        return ""
    return pid.stdout.strip()

# Get the container ID and confirm the web service is running
cid = pid()
print("web service running with container id =", cid)

# Print the Python version used in the container
ver = subprocess.run(f'docker exec {cid} python --version', shell=True, capture_output=True, text=True)
print(ver.stdout.strip())

# Run Django management commands inside the web container
subprocess.run(f'docker exec {cid} python manage.py makemigrations', shell=True)
subprocess.run(f'docker exec {cid} python manage.py migrate', shell=True)

# Create a superuser with no interactive input (credentials must be preset in the code or env)
subprocess.run(f'docker exec {cid} python manage.py createsuperuser --noinput', shell=True)
