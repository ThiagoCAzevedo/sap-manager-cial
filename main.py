from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from common.logger import logger
from api.routes import router as manager_router
import uvicorn


log = logger("main")


def create_app() -> FastAPI:
    log.info("FastAPI app initialized")

    app = FastAPI(
        title="Auto Line Feeding API",
        description="SAP manager microservice responsible for powering sap session to CIAL system",
        docs_url="/sap-docs",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(
        manager_router,
        prefix="/sap-manager",
        tags=["sap-manager"]
    )

    return app


app = create_app()


if __name__ == "__main__":
    log.info("Starting Uvicorn server with reload support")
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8002,
        reload=True
    )