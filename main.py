from fastapi.responses import HTMLResponse #インポート
from typing import Optional
from fastapi import FastAPI

import random  # randomライブラリを追加

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]
    
    return {"result" : omikuji_list[random.randrange(10)]}

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
            <h2>This is a pen!</h2>
            <h2>Oh! Is this a pen!?</h2>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/greeting")
async def give_name(name):
    return {"response": f"サーバです。{name}と言うのですね！これからよろしくお願いします。"}  # f文字列というPythonの機能を使っている