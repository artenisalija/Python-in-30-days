from fastapi import FastAPI
from mangum import Mangum
from routes.route import router


app = FastAPI()
handler = Mangum(app)

app.include_router(router)