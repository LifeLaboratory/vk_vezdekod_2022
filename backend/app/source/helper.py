__author__ = 'Чусовитин А.Р.'

import vk_api
from source.provider import Provider
from datetime import datetime


def main():
    count_table = Provider().get_count_in_table()
    if count_table[0].get('count_image') > 1000:
        return
    print('Заливка мемов')
    vk_session = vk_api.VkApi(token='TOKEN')

    vk = vk_session.get_api()
    for owner, album in ((-197700721, 283939598), (-29842742, 170372519)):
        photos = vk.photos.get(owner_id=owner, album_id=album, extended=1, count=1000)  # Группа с 1127 записями
        for ur in photos.get('items'):
            user = vk.users.get(user_ids=ur.get('user_id'))[0]
            img_info = {
                'author': f'{user.get("first_name")} {user.get("last_name")}',
                'link': ur.get('sizes')[-1].get('url'),
                'like': ur.get('likes').get('count'),
                'ord': 0,
                'id_photo': ur.get('id'),
                'time_stamp': datetime.fromtimestamp(ur.get('date')).strftime('%Y-%m-%d %H:%M:%S')
            }
            Provider().create_images_data(img_info)

    print('Заливка мемов закончена')


if __name__ == '__main__':
    main()
