import fastapi
from fastapi.responses import HTMLResponse
import uvicorn


app = fastapi.FastAPI()

@app.get('/')
def home():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <a href='/home'>To home </a>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200) 

@app.get('/home')
def home():
    return 'You in home'

uvicorn.run(app,   port=1234)