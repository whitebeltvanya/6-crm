"""Точка входа"""
import orders


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
    sales_orders: list[orders.SaleOrder] = [] # список заказов на продажу
    next_order_id = orders.create_order_id() #новый номер заказа

    # Тест create
    new_sale_order: orders.SaleOrder = orders.create_order(
                                        next_order_id(),
                                        "aaa",
                                        123.00,
                                        "dddd@fff.tt"
                                         )

    new_sale_order_2: orders.SaleOrder = orders.create_order(
                                            next_order_id(),
                                            "bbb",
                                            0.50,
                                            "rrrr@gggg.uu"
                                             )
    
    sales_orders.append(new_sale_order)
    sales_orders.append(new_sale_order_2)
    orders.list_orders(sales_orders)
    print("---"*20)

    # Тест edit
    id_find: int = 2
    orders_find = list(filter(lambda o: o["id"] == id_find, sales_orders))
    if orders_find[0]:
            order_found = orders_find[0]
            order_fields_edit: orders.SaleOrder = {}
            order_fields_edit["amount"] = 123.45
            order_fields_edit["title"] = "ddd"
            orders.edit_order(order_found, order_fields_edit)
            orders.list_orders(sales_orders)
            print("---"*20)

    # Тест remove
    orders.remove_order(new_sale_order_2["id"], sales_orders)
    orders.list_orders(sales_orders)