from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

fake_db = [
    {
        "id": 0,
        "username": "Nam",
    },
    {
        "id": 1,
        "username": "Lan",
    },
]

origins = [
    "http://14.225.207.9",
    "http://14.225.207.9:1991",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    try:
        file_path = f"/home/test_server/upload_data/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        print("File server saved successfully!")
    except Exception as e:
        return {"message": e.args}

    return {
        "filename": file.filename,
        "content_type": file.content_type,
    }

@app.get("/get_user")
def get_user(user_id: int):
    return fake_db[user_id]


@app.post("/post_user")
def post_user(username: str):
    new_user = {"id": len(fake_db), "username": username}
    fake_db.append(new_user)
    return new_user


@app.put("/update_user")
def update_user(user_id: int, username: str):
    fake_db[user_id]["username"] = username
    return fake_db[user_id]


@app.delete("/delete_user")
def delete_user(user_id: int):
    del fake_db[user_id]
    return {"message": "User deleted successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="14.225.207.9", port=1991)