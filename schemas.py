from pydantic import BaseModel

class OperadoraResponse(BaseModel):
    cnpj: str
    razao_social: str
    uf: str
