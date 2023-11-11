
contact_dict = {}

def com_hello():
    return 'How can I help you?'

def com_add(string_list):
    if string_list[1] in contact_dict:
        return 'Користувач з таким іменем вже існує'
    contact_dict[string_list[1]] = string_list[2]
    return 'mission add completed'

def com_change(string_list):
    if string_list[1] in contact_dict:
        contact_dict[string_list[1]] = string_list[2]
        return 'mission change completed'
    else:
        return 'Користувача з таким іменем не знайдено'

def com_phone(string_list):
    return contact_dict[string_list[1]]

def com_show():
    return contact_dict

def com_exit():
    return 

simple_command_dict = {
    'hello': com_hello,
    'show all': com_show,
    'good bye': com_exit,
    'close': com_exit,
    'exit': com_exit
}

command_dict = {
    'add': com_add,
    'change': com_change,
    'phone': com_phone,
}

def simple_command_handler(string):
    return simple_command_dict[string]

def command_handler(string_list):
    return command_dict[string_list[0].lower()]

def decor_error(func):
    def inner(*arks, **kwarks):
        try:
            result = func(*arks, **kwarks)
            return result
        except KeyError:
            return "Вкажіть ім'я"
        except IndexError:
            return "Вкажіть ім'я та номер"
        except ValueError:
            return 'Прикольно, я її викликати не зміг'
    return inner

@decor_error
def parser_func(string = None):
    if string.lower() in simple_command_dict:
        result = simple_command_handler(string.lower())
        return result()
    string_list = string.split()
    if string_list[0].lower() in command_dict:
        result = command_handler(string_list)
        return result(string_list)
    return 'Я вас не зрозумів'

def main():
    while True:
        string = input('Очікую ... ')
        result = parser_func(string)
        if result == None:
            print('Good bye!')
            break
        else:
            print(result)

if __name__ == '__main__':
    main()
    
        


