from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI(
    title='AirBnB',
    description='WIP',
    docs_url='/docs'
)

app.mount('/static', StaticFiles(directory='api/static'), name='static')
templates = Jinja2Templates(directory='api/templates')


@app.get("/", tags=['Homepage'])
async def homepage(request: Request):
    return templates.TemplateResponse('homepage.html', context={'request': request})


@app.get("/", tags=['Homepage'])
async def homepage(request: Request):
    return templates.TemplateResponse('homepage.html', context={'request': request})

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
if __name__ == "__main__":
    uvicorn.run(app)
