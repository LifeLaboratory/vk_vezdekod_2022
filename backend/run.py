import keyboard
from requests import get
from json import loads
from time import sleep

__author__ = 'Чусовитин А.Р.'


class ImagesUserInterface:
    def __init__(self):
        self.url = 'http://79.141.74.176:13455'
        self.is_admin = False
        self.current_image = None
        self.next_image = None
        self.prev_image = None
        self.limit = 10
        self.offset = 0

    def get_list_memes(self):
        offset = 0
        while True:
            memes = loads(get(f'{self.url}/list/{self.limit}/{offset}').text)
            for mem in memes.get('Мемы'):
                print(f'''\nМем ID({mem.get('id_image')}) от автора "{mem.get('author')} собрал {mem.get('likes')} лайков. Мем можно посмотреть по ссылке:\n {mem.get('link')}"''')
            print(self.is_admin)
            action = input('''
Показать следующие мемы?
1. Следующие
2. Открыть мем
3. Выйти
''') if not self.is_admin else input('''
Показать следующие мемы?
1. Следующие
2. Открыть мем
3. Повысить приоритет мема
4. Выйти
''')
            if action == '1':
                offset += self.limit
            if action == '2':
                self.get_memes()
            if action == '3':
                if self.is_admin:
                    self.set_priority()
                else:
                    break
            if action == '4':
                break

    def get_memes(self):
        id_image = input('''
Какой мем хочешь открыть?
Введи ID:''')

        while True:
            memes = loads(get(f'{self.url}/get/{id_image}').text)
            next_image = None
            prev_image = None
            ord = None
            for mem in memes:
                print(
                    f'''\nМем ID({mem.get('id_image')}) от автора "{mem.get('author')} собрал {mem.get('likes')} лайков. Мем можно посмотреть по ссылке:\n {mem.get('link')}"''')
                next_image = mem.get('next_image')
                prev_image = mem.get('prev_image')
                ord = mem.get('ord')
            action = '5'
            if self.is_admin:
                if prev_image:
                    action = input(f'''
Показать следующий мемы?
1. Поставить LIKE!
2. Следующий
3. Предыдущий
4. {'Понизить' if ord else 'Повысить'} приоритет
5. Выйти
''')
                else:
                    action = input(f'''
Показать следующий мемы?
1. Поставить LIKE!
2. Следующий
3. {'Понизить' if ord else 'Повысить'} приоритет
4. Выйти
''')
            else:
                if prev_image:
                    action = input(f'''
Показать следующий мемы?
1. Поставить LIKE!
2. Следующий
3. Предыдущий
4. Выйти
''')
                else:
                    action = input('''
Показать следующий мемы?
1. Поставить LIKE!
2. Следующий
3. Выйти
''')
            if action == '1':
                self.set_like(id_image)
            if action == '2':
                id_image = next_image
            if action == '3':
                if prev_image:
                    id_image = prev_image
                else:
                    if self.is_admin:
                        self.put_priority(id_image)
                    else:
                        break
            if action == '4':
                if self.is_admin and prev_image:
                    self.put_priority(id_image)
                else:
                    break
            if action == '5':
                break

    def get_statistic(self):
        if not self.is_admin:
            return
        while True:
            statistic = loads(get(f'{self.url}/statistic').text)
            print('\n\nТоп по Like:')
            for mem in statistic.get('images'):
                print(f'''\nМем ID({mem.get('id_image')}) от автора "{mem.get('author')} собрал {mem.get('likes')} лайков. Мем можно посмотреть по ссылке:\n {mem.get('link')}"''')
            print('Последние события:')
            for mem in statistic.get('history'):
                print(mem.get("История"))
            print('Для выхода нажми q')
            keyboard.start_recording()
            sleep(1)
            events = keyboard.stop_recording()
            if [key.name for key in events if key.name == 'q']:
                break

    def put_priority(self, id_image):
        if not self.is_admin:
            return
        loads(get(f'{self.url}/priority/{id_image}').text)
        print('Ждем много like!')

    def set_priority(self):
        if not self.is_admin:
            return
        while True:
            id_image = input('''
    Какой мем хочешь вывести в топ?
    Введи ID:''')
            if id_image.isdigit():
                self.put_priority(id_image)
                break
            else:
                print("Вы не правильно выбираете, попробуйте еще раз")

    def set_like(self, id_image):
        loads(get(f'{self.url}/like/{id_image}').text)
        print('Like поставлен!')

    def admin_panel(self):
        if not self.is_admin:
            return
        choise_action = {
            '1': self.get_list_memes,
            '2': self.get_memes,
            '3': self.get_statistic,
            '4': self.set_priority,
            '5': self.choise_user_mode
        }
        action = input(f"""
Вы авторизованы как администратор
Что будем делать?
1. Посмотреть все мемы
2. Посмотреть конкретный мем
3. Посмотреть статистику и историю
4. Сменить приоритет мема
5. Сменить пользователя
6. Выйти
""")
        if action in choise_action:
            choise_action.get(action)()
        else:
            if action == '6':
                raise
            print("Вы не правильно выбираете, попробуйте еще раз")

    def user_panel(self):
        choise_action = {
            '1': self.get_list_memes,
            '2': self.get_memes,
            '3': self.choise_user_mode
        }
        action = input(f"""
Вы авторизованы как пользователь
Что будем делать?
1. Посмотреть все мемы
2. Посмотреть конкретный мем
3. Сменить пользователя
4. Выйти
""")
        if action in choise_action:
            choise_action.get(action)()
        else:
            if action == '4':
                raise
            print("Вы не правильно выбираете, попробуйте еще раз")

    def choise_user_mode(self):
        is_admin = input("""
Кто будет смотреть мемы?
1. Администратор
2. Пользователь
""")
        self.is_admin = True if is_admin == '1' else False

    def main(self):
        self.choise_user_mode()
        while True:
            try:
                self.admin_panel() if self.is_admin else self.user_panel()
            except:
                break


ImagesUserInterface().main()
