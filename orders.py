"""БИЗНЕС ЛОГИКА"""
from typing import TypedDict, Optional
from enum import StrEnum
from datetime import datetime

EXCLUDE_KEY_UPDATE ={"id"}

def create_order_id(start_id:int = 0):
    """Номер заказа на продажу"""
    order_id = start_id
    def new_id():
        nonlocal order_id
        order_id += 1
        return order_id
    return new_id


class OrderStatus(StrEnum):
    """Статусы заказа на продажу"""
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
    due: Optional[datetime]
    closed_at: Optional[datetime]


def create_order(id_:   int,
                 title: str,
                 amount: float,
                 email:str,
                 status: OrderStatus = OrderStatus.NEW,
                 due: Optional[datetime] = None,
                 closed_at: Optional[datetime] = None,
                 tags: Optional[set[str]] = None,
                 created_at: datetime = datetime.now()
                 ) -> SaleOrder:
    """Создание нового заказа"""
    if tags is None:
        tags = set()

    new_order: SaleOrder = { 
        "id": id_,
        "title" : title,
        "amount": amount,
        "email": email,
        "status": status,
        "tags":   tags,
        "created_at": created_at,
        "due": due,
        "closed_at": closed_at
    }

    return new_order

def list_orders(orders : list[SaleOrder]):
    """Печать  заказа на продажу"""
    def format_order(o: SaleOrder) -> str :
        formatted: str = (
                f"{o['id']:<4} | {o['title']:<10} | " 
                f"{o['amount']:<7.2f} | {o['email']:<15} | {o['status']:<10} | "
                f"{', '.join(o['tags']):<15} | "
                f"{o['created_at'].strftime("%Y-%m-%d %H:%M:%S"):<18} | "
                f"{o['due'].strftime("%Y-%m-%d %H:%M:%S") if o['due'] else "":<18} | "
                f"{o['closed_at'].strftime("%Y-%m-%d %H:%M:%S")if o['closed_at'] else "":<18} | "
        )
        return formatted
    
    print("\n".join(map(format_order, orders)))

def edit_order(order: SaleOrder, order_fields : SaleOrder) -> SaleOrder:
    """Редактирование  заказа на продажу"""
    for key in order_fields:
        if key in order and key not in EXCLUDE_KEY_UPDATE:
            order[key] = order_fields[key]
    return order
    

def remove_order(id_: int, orders: list[SaleOrder]) -> bool:
    """Удаление  заказа на продажу"""
    for index, order in enumerate(orders):
        if order.get("id") == id_:
            del orders[index]
            return True
    return False
    




