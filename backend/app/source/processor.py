from source.provider import Provider


class Processor:
    def __init__(self):
        self.provider = Provider()

    def get_all_user(self, data):
        """
        Метод обрабатывает параметры для получения всего списка мемов и возвращает информацию о мемах
        :param data:
        :return:
        """
        limit = data.get('limit') if str(data.get('limit')).isdigit() and 0 < int(data.get('limit')) < 100 else 50
        offset = data.get('offset') if str(data.get('offset')).isdigit() and 0 < int(data.get('offset')) else 0
        return {'Мемы': self.provider.get_all_images(limit, offset), 'limit': limit, 'offset': offset}

    def get_image(self, id_image):
        """
        Метод обрабатывает параметры для получения конкретного мема и возвращает информацию о меме
        :param id_image:
        :return:
        """
        return self.provider.get_image(int(id_image))

    def set_likes(self, id_image):
        """
        Метод ставит лайк мему
        :param id_image:
        :return:
        """
        return self.provider.set_likes(int(id_image))

    def set_priority_image(self, id_image):
        """
        Метод меняет приоритет мема
        :param id_image:
        :return:
        """
        return self.provider.set_priority(int(id_image))

    def get_statistics(self):
        """
        Метод возвращает статистику по изображениям
        :return:
        """
        parts_image = self.provider.get_top_likes(5)
        parts_history = self.provider.get_history(5)
        return {
            'images': parts_image,
            'history': parts_history
        }