"""БИЗНЕС ЛОГИКА"""
from typing import TypedDict
from enum import StrEnum
from datetime import datetime


def create_order():
    pass

def list_orders():
    pass

def edit_order():
    pass

def remove_order():
    pass

class OrderStatus(StrEnum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    DONE = "done"
    CANCELLED = "cancelled"


class SaleOrder (TypedDict):
    """заказ на продажу"""
    id: int
    title: str
    amount: float
    email:str
    status: OrderStatus
    tags: set[str]
    created_at: datetime
    due: datetime
    closed_at: datetime
