from pydantic import BaseModel

class FileResponse(BaseModel):
    message: str
    report: str
