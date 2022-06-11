#DO NOT EXECUTE THIS FILE#

#// Build and Deploy Cloud Run Containers

GOOGLE_CLOUD_PROJECT=glossy-chimera-350206

gcloud builds submit --tag gcr.io/acoustic-env-352906/cloudsql:1.0.0 .
gcloud builds submit --tag gcr.io/acoustic-env-352906/mlclassifier:1.0.0 .

# setup cloud sql connector 
# setup vpc connector

gcloud run deploy --image=gcr.io/acoustic-env-352906/cloudsql:1.0.0 \
--platform managed \
--max-instances=1 \
--allow-unauthenticated 

gcloud run deploy --image=gcr.io/acoustic-env-352906/mlclassifier:1.0.0 \
--platform managed \
--max-instances=1 \
--allow-unauthenticated \
--memory=8Gi \
--cpu=2

#// Setup Pub Sub and Cloud Function with pub/sub trigger
gcloud pubsub topics create eyeam-loguser-topic

# function name = eyeam-loguser

#create service account and it's private key

#// Setup API Gateway
gcloud api-gateway apis create eyeam-api
gcloud api-gateway api-configs create eyeam-api-conf --api=eyeam-api --openapi-spec=api.yaml --backend-auth-service-account=eyeam-sa@acoustic-env-352906.iam.gserviceaccount.com
gcloud api-gateway gateways create eyeam-api-gw --api=eyeam-api --api-config=eyeam-api-conf --location=asia-southeast2	


gcloud api-gateway apis create eyeam-api

gcloud api-gateway api-configs create eyeam-api-conf \
--api=eyeam-api \
--openapi-spec=./api.yaml \
--backend-auth-service-account=cc-api-sa@glossy-chimera-350206.iam.gserviceaccount.com

