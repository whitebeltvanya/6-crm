"""Точка входа"""
import time

from  orders import SaleOrder, create_order, edit_order, list_orders, remove_order


# Точка входа
def main():
    """Временная заглушка"""
    pass
    # while True:
    #     try:
    #         raw = input("Введите команду:").strip().lower()
    #         parts = raw.split()
    #         cmd, args = parts[0], parts[1:]
    #         match cmd:
    #             case "help":
    #                 pass
    #             case "exit":
    #                 break
    #             case _ :
    #                 raise cmd_valid.CrmCmdError("Ошибка в команде")
    #     except ValueError as e:
    #         print(f"Завершение работы. Ошибка: {e}")
    #         break


if __name__ == '__main__':
    #Тест create, edit, delete:
   
    # Тест create
    create_order("aaa", 123.00,"ddddg@fff.tt")
    time.sleep(2)
    create_order("bbb",0.50,"rrrr@gggg.uu")
    time.sleep(2)
    create_order("eee",2,"bybyby@www.du")
    list_orders()

    # Тест edit
    id_find: int = 2
    order_fields_edit: SaleOrder = {}
    order_fields_edit["amount"] = 123.45
    order_fields_edit["title"] = "ddd"
    if edit_order(id_find, order_fields_edit):
        list_orders()
    else:
        print(f"id: {id_find} not found")


    # Тест remove
    remove_order(id_find)
    list_orders()