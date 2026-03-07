# SocialNet

SocialNet is a Django-based social networking platform where users can find and connect with friends. Currently this platform can be used to:

    * Create a new account
    * Log in to an existing account
    * Find and connect with other users

## Installation

To get started with SocialNet, follow these steps:

1. **Clone the repository**

    ```bash
   git clone https://github.com/Shaunaksb/socialnet
   cd socialnet
   ```

2. **Set up a virtual environment**

   It's recommended to use a virtual environment for Python projects. You can set one up by running:

    ```bash
    python -m venv venv
   
    source venv/bin/activate  
    ```
   
   On Windows use 
   
    ```bash
   venv\Scripts\activate
    ```

3. **Install dependencies**

   Install all the required packages using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**

   Copy the `template_env.txt` to a new file named `.env` and adjust the variables to your needs.

   ```bash
   cp template_env.txt .env
   ```

## Docker

SocialNet is built with docker in mind, and it is recommended to run the application in a containerized environment. To get started with Docker, follow these steps:

1. **Run install.py**

   ```bash
   python install.py
   ```

   This script takes care of all the critical tasks required to run the application in a docker-container such as:

        * Generating a new secret key
        * Building the docker image
        * Running the docker container
        * Applying Migrations
        * Creating a superuser

   The application will be accessible at `http://localhost:8000/`.

For more detailed instructions and additional information, please refer to the project documentation in the shared postman collection.

[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://app.getpostman.com/run-collection/26845651-f928a294-379d-428b-a3de-cbe36eda0208?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D26845651-f928a294-379d-428b-a3de-cbe36eda0208%26entityType%3Dcollection%26workspaceId%3D7cd78b67-f7cb-47d8-8134-2d4fe74e316c#?env%5BSocialnet%5D=W3sia2V5IjoiYWNjZXNzIiwidmFsdWUiOiI8PiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJzZWNyZXQiLCJzZXNzaW9uVmFsdWUiOiI8PiIsInNlc3Npb25JbmRleCI6MH0seyJrZXkiOiJyZWZyZXNoX3Rva2VuIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoic2VjcmV0Iiwic2Vzc2lvblZhbHVlIjoiIiwic2Vzc2lvbkluZGV4IjoxfV0=)

