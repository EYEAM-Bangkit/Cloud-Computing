# Get Species Classification
---
Returns Classification from ml model

URL : /classifier
Method : POST
Auth Required : YES
Permission Required : None

## Authentication
Attach firebase-access-token in Authorization Header. The token can be obtained from GET JWT Method.
`{'Authorization':'**firebase-access-token**'}`

## Body
required:
`{'user_image':'**photo-in-cloudstorage**'}`
