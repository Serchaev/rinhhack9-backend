import json
from typing import Any

from app.container import Container
from app.workers.model_subscriber import ModelSubscriber


async def model_on_message(raw_message: Any, model_subscriber: ModelSubscriber = Container.model_subscriber()):
    """
    Обязательно описываем протокол! Пример:
    Протокол:
    {
        "name": string,   # название
    }
    """
    template_object = raw_message if isinstance(raw_message, dict) else json.loads(raw_message)
    await model_subscriber.subscribe(template_object)
