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
    NEW = 'new'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'
    CANCELLED = 'cancelled'


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

#init orders list and id generator
sales_orders: list[SaleOrder] =[]
next_order_id = create_order_id()

def create_order(title: str,
                 amount: float,
                 email:str,
                 status: OrderStatus = OrderStatus.NEW,
                 due: Optional[datetime] = None,
                 closed_at: Optional[datetime] = None,
                 tags: Optional[set[str]] = None,
                 created_at: Optional[datetime] = None
                 ):
    """Создание нового заказа"""
    if tags is None:
        tags = set()

    if created_at is None:
        created_at = datetime.now()    

    new_order: SaleOrder = { 
        "id":   next_order_id(),
        "title" : title.strip(),
        "amount": amount if amount > 0 else 0,
        "email": email.strip(),
        "status": status,
        "tags":   tags,
        "created_at": created_at,
        "due": due,
        "closed_at": closed_at
    }

    sales_orders.append(new_order)

def list_orders():
    """Печать  заказа на продажу"""
    delim: str = " | "
    headers: list[str] = list(SaleOrder.__annotations__.keys())
    def fmt_row_str(order: SaleOrder) -> list[str] :   
        row: list[str] = [
            f"{order['id']}",
            order['title'],
            f"{order['amount']:.2f}",
            order['email'],
            order['status'],
            f"{', '.join(order['tags']) if order['tags'] else '-'}",
            f"{order['created_at'].strftime('%Y-%m-%d %H:%M:%S')}",
            f"{order['due'].strftime('%Y-%m-%d %H:%M:%S') if order['due'] else '-'}",
            f"{order['closed_at'].strftime("%Y-%m-%d %H:%M:%S")if order['closed_at'] else '-'}"           
        ]
        return row
    
    rows= list(map(fmt_row_str, sales_orders))
    
    col_lens = [len(h) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            col_lens[i] = max(col_lens[i], len(val))
    
    table_len: int = sum(col_lens) + len(delim)* len(col_lens)
    underline: str = f"\n{'-'*table_len}"
    
    def fmt_row_out(row: list[str]): 
        return delim.join(f"{val:<{col_lens[i]}}" for i, val in enumerate(row)) + underline

    print(f"{'\n'*2}Список заказов ({len(rows)}):" + underline)
    print(fmt_row_out(headers))
    print("\n".join(map(fmt_row_out, rows)))
   

def edit_order(id_: int, fields_opdated : SaleOrder) -> bool:
    """Редактирование  заказа на продажу"""
    ret: bool = False
    orders_found: list[SaleOrder] = list(filter(lambda o: o["id"] == id_, sales_orders))
    if len(orders_found) > 0:
        order = orders_found[0]
        ret = True
        for key in fields_opdated:
            if key in order and key not in EXCLUDE_KEY_UPDATE:
                order[key] = fields_opdated[key]
    return ret
    

def remove_order(id_: int) -> bool:
    """Удаление  заказа на продажу"""
    for index, order in enumerate(sales_orders):
        if order.get("id") == id_:
            del sales_orders[index]
            return True
    return False
    




