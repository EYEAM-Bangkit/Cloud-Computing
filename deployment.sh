#DO NOT EXECUTE THIS FILE#

#// Build and Deploy Cloud Run Containers

GOOGLE_CLOUD_PROJECT=glossy-chimera-350206

gcloud builds submit --tag gcr.io/glossy-chimera-350206/cloudsql:1.0.0 .
gcloud builds submit --tag gcr.io/glossy-chimera-350206/mlclassifier:1.0.0 .

# setup cloud sql connector 
# setup vpc connector

gcloud run deploy --image=gcr.io/glossy-chimera-350206/cloudsql:1.0.0 \
--platform managed \
--max-instances=1 \
--allow-unauthenticated 

gcloud run deploy --image=gcr.io/glossy-chimera-350206/mlclassifier:1.0.0 \
--platform managed \
--max-instances=1 \
--allow-unauthenticated \
--memory=8Gi

#// Setup Pub Sub and Cloud Function with pub/sub trigger
gcloud pubsub topics create eyeam-loguser-topic

# function name = eyeam-loguser

#// Setup API Gateway

#create service account and it's private key

gcloud api-gateway apis create eyeam-api

gcloud api-gateway api-configs create eyeam-api-conf \
--api=eyeam-api \
--openapi-spec=./api.yaml \
--backend-auth-service-account=cc-api-sa@glossy-chimera-350206.iam.gserviceaccount.com

