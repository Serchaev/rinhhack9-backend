import asyncio
from datetime import datetime

from app.database import Transaction
from app.database.registries.transaction_registry import TransactionRegistry


class ModelSubscriber:
    def __init__(self, transaction_registry: TransactionRegistry):
        self.transaction_registry = transaction_registry

    async def subscribe(self, data):
        data["record_id"] = data["id"]
        data["datetime"] = datetime.strptime(data["datetime"], "%Y-%m-%d %H:%M:%S")
        data["expiration_date"] = datetime.strptime(data["expiration_date"], "%Y-%m-%d")
        data.pop("id", None)

        await self.transaction_registry.create(**data)
        await asyncio.sleep(1)
