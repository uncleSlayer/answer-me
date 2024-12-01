from app import app
import uvicorn

from app.configs.env import env_config

if __name__ == "__main__":
    uvicorn.run('app:app', host="0.0.0.0", port=8000, reload=(True if env_config.DEVELOPMENT_ENV == "DEV" else False))
