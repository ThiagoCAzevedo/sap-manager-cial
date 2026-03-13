from fastapi import APIRouter, Depends
from modules.manager.application.manager import SAPSessionManager
from modules.manager.application.client import SAP_Client
from common.http_errors import http_500
from common.logger import logger


router = APIRouter()
log = logger("manager")


def get_sap_client():
    return SAP_Client()


def get_session_manager():
    return SAPSessionManager()


def serialize_session(sess):
    if sess is None:
        return None

    try:
        return {
            "id": getattr(sess, "Id", None),
            "name": getattr(sess, "Name", None),
            "type": str(type(sess)),
            "info": {
                "active_window_id": getattr(sess.ActiveWindow, "Id", None) if getattr(sess, "ActiveWindow", None) else None,
                "number": getattr(sess, "Number", None)
            }
        }
    except Exception:
        return {"error": "Unable to serialize SAP session object"}


@router.post("/session", summary="Create a SAP session and store it")
def create_sap_session(
    client: SAP_Client = Depends(get_sap_client),
    session_manager: SAPSessionManager = Depends(get_session_manager),
):
    log.info("POST /sap-manager/session — starting SAP session creation")
    try:
        client.connect()
        log.info("SAP session successfully connected")

        session_manager.set_session(client.session)
        log.info("SAP session stored in SessionManager")

        return {"message": "SAP session created successfully!"}

    except Exception as e:
        log.error("Error creating SAP session", exc_info=True)
        raise http_500("Error creating SAP session: ", e)


@router.get("/status", summary="Get SAP session status")
def sap_status():
    log.info("GET /sap-manager/status — checking SAP session status")
    try:
        sess = SAPSessionManager.get_session()
        return {
            "session": repr(sess),
            "type": str(type(sess)),
            "has_run_transaction": hasattr(sess, "run_transaction") if sess else False
        }
    except Exception as e:
        log.error("Error getting SAP status", exc_info=True)
        raise http_500("Error getting SAP status: ", e)


@router.get("/session", summary="Get stored SAP session")
def get_sap_session(session_manager: SAPSessionManager = Depends(get_session_manager)):
    log.info("GET /sap-manager/session — retrieving stored SAP session")

    try:
        sess = session_manager.get_session()
        return {"session": serialize_session(sess)}

    except Exception as e:
        log.error("Error retrieving SAP session", exc_info=True)
        raise http_500("Error retrieving SAP session: ", e)