from fastapi import FastAPI
import uvicorn
# יצירת מופע של האפליקציה
app = FastAPI()
a = {'david':5,'nachmen':7}
# מסלול בסיסי שמחזיר מחרוזת
# @app.get("/")
# async def result():
#     return {"message": "hello world"}
@app.get("/")
async def json():
    return a['david']


# הרצה מקומית של האפליקציה
if __name__ == "__main__":
    uvicorn.run("servers:app", host="127.0.0.1", port=8000)
