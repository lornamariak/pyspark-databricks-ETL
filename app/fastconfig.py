from fastapi import FastAPI

#create instance
app = FastAPI()

#route
@app.get("/")
async def root():
    return {"Building with Fast API Demo"}
