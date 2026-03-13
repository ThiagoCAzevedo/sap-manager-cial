from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Any, Dict


@dataclass
class SAPSession:
    session_id: str
    user: str
    system: str
    transaction: Optional[str] = None
    is_active: bool = False
    properties: Dict[str, Any] = field(default_factory=dict)
    created_at: Optional[datetime] = None
    last_activity: Optional[datetime] = None

    def to_dict(self) -> dict:
        return {
            "session_id": self.session_id,
            "user": self.user,
            "system": self.system,
            "transaction": self.transaction,
            "is_active": self.is_active,
            "properties": self.properties,
            "created_at": self.created_at,
            "last_activity": self.last_activity,
        }

    def update_activity(self) -> None:
        self.last_activity = datetime.now()


@dataclass
class SAPTransaction:
    transaction_code: str
    session_id: str
    status: str = "pending"
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    result: Optional[Dict[str, Any]] = None
    error_message: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "transaction_code": self.transaction_code,
            "session_id": self.session_id,
            "status": self.status,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "result": self.result,
            "error_message": self.error_message,
        }

    def is_completed(self) -> bool:
        return self.status in ["completed", "failed"]

    def duration(self) -> Optional[float]:
        if self.start_time and self.end_time:
            delta = self.end_time - self.start_time
            return delta.total_seconds()
        return None


@dataclass
class SAPAuthenticator:
    username: str
    password: str
    system_id: str
    client: str
    language: str = "EN"
    properties: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "system_id": self.system_id,
            "client": self.client,
            "language": self.language,
            "properties": self.properties,
        }