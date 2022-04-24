from rating.provider import Provider

__author__ = 'Чусовитин А.Р.'


class Processor:
    def __init__(self):
        self.provider = Provider()

    def get_top_users(self, user_id):
        users_ratings = self.provider.get_top_users()
        ratings = []
        my_user_pos = None
        for k in range(len(users_ratings)):
            users_ratings[k]['id'] = k+1
            if k < 20:
                ratings.append(users_ratings[k])
        if user_id is None:
            return ratings
        for now_id in range(len(users_ratings)):
            if users_ratings[now_id].get('id_user') == user_id and now_id > 19:
                my_user_pos = now_id + 1
                break
        if my_user_pos is None:
            return ratings
        for new_id in range(my_user_pos - 5, my_user_pos):
            if new_id > 19:
                users_ratings[new_id]['id'] = new_id + 1
                ratings.append(users_ratings[new_id])
        return ratings
