def show_messages(message_list):
    for message in message_list:
        print(message)

def send_messages(message_list:list[str], send_list: list[str]):
    while message_list:
        message = message_list.pop()
        send_list.append(message)


list_messages = ['Бу!', 'Не бойся меня!', 'Я твой друг.', 'Подходи ближе.']
list_send = []
print(f'изначально:')
print(f'{list_messages=}\n{list_send=}')
send_messages(list_messages[:], list_send)
print(f'итог:')
print(f'{list_messages=}\n{list_send=}')