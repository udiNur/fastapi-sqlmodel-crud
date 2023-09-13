from fastapi import FastAPI
from routers import machine  # Import your route modules here

app = FastAPI()

# Include your route modules here
app.include_router(machine.router)
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)