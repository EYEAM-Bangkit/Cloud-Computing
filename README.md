# EYEAM Cloud Computing Repository
A Repository for Cloud Computing part of EYEAM-Bangkit Project

- Muhammad Ilham Hanifan (C2009F0984)
- Iqbal Khariza (C2009F0920)

## Services Used
<p align="center">
  <img src="./images/services-used.png">
</p>

### Project Brief Cloud Computing

Creating serverless microservice architecture for the backend using Cloud Run, Cloud Functions, and Cloud Pub Sub. API gateway is used to route user requests to the correct service. Creating CI/CD Pipeline on Github Repository using Cloud Build Triggers on push to the main branch. Cloud SQL and Cloud Storage is used for storing important data.

## Serverless Architecture
<p align="center">
  <img src="./images/serverless_arch1.png">
</p>

We use built a serverless architecture using services listed below:
- API Gateway = Manage endpoints and provide authentication for users
- Firebase Authentication = Manage user accounts and provide token generation for authentication
- Cloud Pub Sub = Provide Communication between `mlclassifier-run` and `loguser-function` 
- Cloud Run = Hosts ML model in `mlclassifier-run` and access to cloud SQL in `cloudsql-run` as docker containers  
- Cloud Functions = Contains the code to log user actions, triggered by a topic published from `mlclassifier`
- Cloud SQL = Stores animal details and user logs
- Cloud Storage = Stores animal images, models, and .APK

## Continuous Integration & Continous Integration
<p align="center">
  <img src="./images/cicdepipeline.png">
</p> 

We create a continuous deployment workflow using Github Repo and Cloud Build. Everytime a commit is pushed to main branch Cloud Build will run the script called `cloudbuild.yaml`. This script will Build a new image from `mlclassifier-run, cloudsql-run, loguser-functions` folders, Push them to container registry, and then deploy them to Cloud Run and Cloud Functions.

We built a CI/CD pipeline using Google Cloud Platform Services listed below:
- Cloud Build = Building, Push, and deploying images from git repository using `cloudbuild.yaml` script
- Container Registry = Stores newly generated container images from cloud build
- Github Repository = Source code repository

## What's on our Cloud Console
## Cloudbuild Trigger - Substitution Variables
![CloudBuild_Trigger_Substitution_Variables.jpg](./images/CloudBuild_Trigger_Substitution_Variables.jpg)

We put secrets for our code inside CloudBuild Substitution Variables. With this we can safely host our code in this repository while keeping important variables private.

### Cloud Run 
![CloudRun_Console.jpg](./images/CloudRun_Console.jpg)
### Cloud Storage
![CloudStorage_Console.jpg](./images/CloudStorage_Console.jpg)
### Pub Sub Topics
![Pubsub_Topics.jpg](./images/Pubsub_Topics.jpg)


