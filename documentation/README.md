# EYEAM-API Documentation

Developed by Ilham Hanifan and Iqbal Khariza

We use firebase auth for our auth system then apply it to our API Gateway. Before making a request to our endpoints please fetch the Bearer token first from the provided link and attach it to the Authorization header every time a request is made.

## Retrieve JWT Auth Token
Returns Authentication Token for users to access other endpoints

- URL : /https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=[FIREBASE-WEB-API-KEY]
- Method : GET
- Auth Required : No
- Parameters : `key : FIREBASE-WEB-API-KEY`
- Body : `{ "email":"EMAIL", "password":"PASSWORD", "returnSecureToken":true }`
- Response : 
```
{
    "kind": "identitytoolkit#VerifyPasswordResponse",
    "localId": "dlR..y1",
    "email": "mail@mail.com",
    "displayName": "",
    "idToken": "eyJhbG...sRfpQ",
    "registered": true,
    "refreshToken": "AIw....3gg",
    "expiresIn": "3600"
}
```
note : idToken is used as Bearer Token to access other endpoints

## Authentication Test
Returns JWT Token, only used for testing purposes.

- URL: /test
- Method : GET
- Auth Required : Yes, Bearer Token
- Parameters : `key : API-KEY`
- Body : JSON `{ "email":"EMAIL", "password":"PASSWORD", "returnSecureToken":true }`
- Response : 
```
ewogICJpc3MiOiAiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL1tQUk9KRUNULUlEXSIsCiAgImF1ZCI6ICJbUFJPSkVDVC1JRF0iLAogICJhdXRoX3RpbWUiOiAxNjU0ODI4MTQ5LAogICJ1c2VyX2lkIjogImRsUmQuLi5xa3kxIiwKICAic3ViIjogImRsUi4uLmt5MSIsCiAgImlhdCI6IDE2Li4uNDksCiAgImV4cCI6IDE2Li4uNDksCiAgImVtYWlsIjogIm1haWxAbWFpbC5jb20iLAogICJlbWFpbF92ZXJpZmllZCI6IGZhbHNlLAogICJmaXJlYmFzZSI6IHsKICAgICJpZGVudGl0aWVzIjogewogICAgICAiZW1haWwiOiBbCiAgICAgICAgIltVU0VSLUVNQUlMXSIKICAgICAgXQogICAgfSwKICAgICJzaWduX2luX3Byb3ZpZGVyIjogInBhc3N3b3JkIgogIH0KfQ
```
The Reponse is a base64 encoded string
```
{
  "iss": "https://securetoken.google.com/[PROJECT-ID]",
  "aud": "[PROJECT-ID]",
  "auth_time": 1654828149,
  "user_id": "dlRd...qky1",
  "sub": "dlR...ky1",
  "iat": 16...49,
  "exp": 16...49,
  "email": "mail@mail.com",
  "email_verified": false,
  "firebase": {
    "identities": {
      "email": [
        "mail@mail.com"
      ]
    },
    "sign_in_provider": "password"
  }
}
```

## POST Classificaiton JWT
API will identify what kind of animal is in the picture and gives back the scientific name of the animal. 
It will also logs what it identifies to the database.

- URL: /classifier
- Method : POST
- Auth Required : Yes, Bearer Token
- Parameters : None
- Body : form-data `user_image`:`[BASE64-ENCODED-IMAGE]`
- Response : JSON `{ "animalName": "Phascolarctos cinereus" }`

## GET Animal JWT
Retrieve Information abou a specific animal

- URL: /animal
- Method : GET
- Auth Required : Yes, Bearer Token
- Parameters : `name : [ANIMAL-NAME]`
- Body : None
- Response : JSON 
```
{
    "data": [
        {
            "class": "Mammalia",
            "conserv": "Livestock farming & ranching",
            "deskripsi": "Wild Boar S ... as Least Concern.",
            "family": "Suidae",
            "foto": "https://storage.googleapis.com/fotofotohewanlangka/Wild%20Boar.jpg",
            "genus": "Sus",
            "habitat": "Forest, ... Artificial/Aquatic & Marine",
            "iucn": "Least Concern",
            "kingdom": "Animalia",
            "namailmiah": "Sus scrofa",
            "namapopuler": "Wild Boar",
            "order": "Cetartiodactyla",
            "persebaran": "Afghanistan; Albania; ...  Viet Nam",
            "phylum": "Chordata",
            "populasi": "Unknown",
            "threats": "Agriculture & aquaculture"
        }
    ]
}
```

## GET Logs JWT
Retrieve user log based on the provided authorization token

- URL: /logs
- Method : GET
- Auth Required : Yes, Bearer Token
- Parameters : None
- Body : None
- Response : JSON 
```
{
    "data": [
        {
            "animal": "arctictis binturong",
            "eventid": "48....799",
            "logtime": "Thu, 09 Jun 2022 17:47:34 GMT",
            "userid": "lRd....5Yqky1"
        },
        {
            "animal": "Phascolarctos cinereus",
            "eventid": "48....572",
            "logtime": "Thu, 09 Jun 2022 18:06:30 GMT",
            "userid": "dlRd....5Yqky1"
        },
        {
            "animal": "Phascolarctos cinereus",
            "eventid": "448....520",
            "logtime": "Fri, 10 Jun 2022 09:29:26 GMT",
            "userid": "lRd....5Yqky1"
        }
    ]
}
```
