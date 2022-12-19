# middleware-rest-api
Middleware Assignment - Rest API

## Steps to Run

1.	Open your command prompt and change the location to where your python file is present.
2.	Run the following command in the command prompt to run your Fast API application.

    uvicorn rest_api:app --port 80

3.	Open your browser and open the below URL to test the get call:

    URL: http://127.0.0.1:80/getGreetings
    
4.	Open postman and do a post call on the following URL with the body mentioned below.

    URL: http://127.0.0.1:80/postData

    Body: (Type: json)
    {
        "name": "chetali",
        "id": "2020HS70007",
        "description": "this is middleware assignment - rest api's post call"
    }


