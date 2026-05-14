from typing import Literal

RouteType = Literal["llm", "vision", "ocr_rag", "agent"]

def detect_route(message: str) -> RouteType:
    lower = message.lower()
    if any(word in lower for word in ["pdf", "документ", "скан", "ocr"]):
        return "ocr_rag"
    if any(word in lower for word in ["изображение", "картинка", "скрин"]):
        return "vision"
    if any(word in lower for word in ["код", "agent", "автоматизируй"]):
        return "agent"
    return "llm"
