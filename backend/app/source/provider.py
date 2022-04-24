import base.provider as bp


class Provider(bp.Provider):
    def __init__(self):
        super().__init__()
        self.table_name = 'memes'
        self.field = []

    def create_images_data(self, image_info):
        self.query = f'''
  insert into images (id_image, link, author, likes, ord, time_stamp) 
    values(
    {image_info.get('id_photo')},
    '{image_info.get('link')}',
    '{image_info.get('author')}',
    {image_info.get('like')},
    {image_info.get('ord')},
    '{image_info.get('time_stamp')}'::timestamp 
    )
        '''
        return self.execute()

    def get_all_images(self, limit, offset):
        self.query = '''
  select ord
  from images
  where ord = 1
        '''
        self.query = f'''
  select 
    id_image, 
    link, 
    author, 
    likes
  from images
  order by ord desc, time_stamp::date desc, likes {'' if self.execute() else 'desc'}
  limit {limit} offset {offset}
        '''
        return self.execute()

    def get_image(self, id_image):
        self.query = '''
  select ord
  from images
  where ord = 1
'''
        if id_image:
            where = f'where id_image = {id_image}'
        self.query = f'''
with list_images as (
  select 
    id_image, 
    link, 
    author, 
    likes,
    ord,
    LEAD(id_image,1) OVER (
      ORDER BY ord desc, likes desc
    ) next_image,
    LEAD(id_image,-1) OVER (
      ORDER BY ord desc, likes desc
    ) prev_image
  from images
  order by ord desc, {'likes, time_stamp::date desc ' if self.execute() else 'time_stamp::date desc, likes desc'} 
)

select *
from list_images
{where if where else ''}
limit 1
        '''
        return self.execute()

    def get_history(self, limit):
        self.query = f'''
with history_list as (
  select  id_history, 
    'Изображение ' || h.id_image::text || ' автора ' || author::text
      || ' получило лайк!!! Сейчас у мема ' || likes::text || ' лайков' as "История"
  from history h
  left join images im using(id_image)
  order by id_history
  limit 1000
)
select *
from (
  select distinct on("История") id_history, "История"
  from history_list
) n
order by id_history desc, "История"
limit {limit}
        '''
        return self.execute()

    def set_likes(self, id_image):
        self.query = f'''
  update images
  set likes = likes + 1
  where id_image = {id_image}
        '''
        self.execute()
        self.set_history(id_image)
        return self.get_image(id_image)

    def set_priority(self, id_image):
        self.query = f'''
  update images
  set ord = case when ord = 0 then 1 else 0 end
  where id_image = {id_image}
        '''
        self.execute()
        return self.get_image(id_image)

    def get_count_in_table(self):
        self.query = f'''
   select count(1) as count_image
   from images
        '''
        return self.execute()

    def set_history(self, id_image):
        self.query = f'''
  insert into history(id_image, time_stamp) values({id_image}, now()) 
        '''
        return self.execute()

    def get_top_likes(self, limit):
        self.query = '''
  select ord
  from images
  where ord = 1
        '''
        self.query = f'''
  select 
    id_image, 
    link, 
    author, 
    likes
  from images
  order by likes desc
  limit {limit}
        '''
        return self.execute()