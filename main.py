from webbrowser import get
from fastapi import FastAPI  #PYTHON LIBRARIES NEED TO INSTELL FASTAPI AND UVICORN TO RUN THE CODE 

app = FastAPI() #it is the instance of the FastAPI
@app.get("/posts") #@app.get("/")  #decorator which provides magic to the function and allow the user to access the specific path
def display_user(): #function which will be called user access path #imp note inthe development env we pass uvicorn main:app --reload
      return{"data": "GOOD NIGHTY NIGHTY!!"}
     # python dictonary#fast#moving forward in the development environment

@app.get("/")
def get_posts():
    return {"Name": "Hello, It's 11:00: PM!!"}