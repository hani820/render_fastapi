from fastapi.responses import HTMLResponse #インポート

### コードいろいろ... ###

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