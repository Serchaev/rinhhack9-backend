from typing import Any

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.database import Transaction
from app.helpers.db import BaseDbRegistry, SessionManager


class TransactionRegistry:

    def __init__(self, session_manager: SessionManager):
        """
        Базовый класс взаимодействия с моделями бд
        :param session_manager:         Менеджер сессий
        """
        self.async_session_factory: async_sessionmaker = session_manager.async_session_factory

    async def create(self, **kwargs) -> dict[str, Any]:
        async with self.async_session_factory() as session:
            stmt = insert(Transaction).values(**kwargs)
            await session.execute(stmt)
            await session.commit()
        return kwargs
