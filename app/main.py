from fastapi import FastAPI, security ,requests, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Depends
from app.routers import auth, categories, products, suppliers, users
from app.dbs import get_db
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI(title="Inventory Management System")

origins = 'http://localhost:8000'

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Include Routers


#app.include_router(auth.router)
#app.include_router(products.router,dependencies=[Depends(auth.verify_token)])
app.include_router(auth.router)
app.include_router(products.router)
app.include_router(categories.router)
app.include_router(suppliers.router)
app.include_router(users.router)
# Static Files
app.mount("/static", StaticFiles(directory="app/static"), name="static")
# Templates
templates = Jinja2Templates(directory="app/templates")
# React Frontend
app.mount("/react", StaticFiles(directory="react", html=True), name="react")
@app.get("/")
def read_root(request: requests.Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})
@app.get("/react-app")
def read_react_app(request: requests.Request):
    return templates.TemplateResponse("react_index.html", {"request": request})
# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
