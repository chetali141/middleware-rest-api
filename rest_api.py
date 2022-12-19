"""
Rest API - Middleware Assignment
"""

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel


def custom_openapi():
    """
    open api schema
    """
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Rest API",
        version="1.0",
        description="Middleware Assignment Rest API.",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


# class to map the input 
class StudentDetail(BaseModel):
    name: str
    id: str
    description: str | None = None


app = FastAPI()


# get call
@app.get("/getGreetings")
async def getCall():
    return "Hello! Smile, It's free :)"


# post call
@app.post("/postData")
def postCall(details: StudentDetail):
    print("Data you have given is: {}".format(details))
    return {"Student details posted successfully. ": details}


app.openapi = custom_openapi()

