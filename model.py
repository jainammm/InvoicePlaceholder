from pydantic import BaseModel

class ModelOutput(BaseModel):
    
    model_output: list


class Text:
    class_name: str
    test: str
    bounding_box: any
    confidence: float
