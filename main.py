from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.openapi.docs import get_swagger_ui_html
from app.endpoints import router as endpoints_router

app = FastAPI()

# Include API routes
app.include_router(endpoints_router, prefix="/api")

# Swagger UI setup
@app.get("/", response_class=HTMLResponse)
async def get_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/api/openapi.json", title="Payment Gateway API")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
