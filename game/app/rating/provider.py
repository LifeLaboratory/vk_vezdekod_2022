import base.provider as bp

__author__ = 'Чусовитин А.Р.'


class Provider(bp.Provider):
    def __init__(self):
        super().__init__()
        self.table_name = 'rating'
        self.field = ['login, password, name', 'email']

    def get_top_users(self):
        self.query = f'''
  with get_users as(
      select
        distinct id_user
      from game
  )
  select
    coalesce(g.point, 0) as point
    , g.health as health
    , g.money as money
    , g.round as round
    , g.time_close as time_close
    , u.id_user as id_user
    , u.login as user_name
    , u.pic as user_pic
    , p.name as person_name 
    , p.description as person_descr
    , p.pic as person_pic
  from get_users gu
  join users u on (gu.id_user = u.id_user)
  join lateral (
      select
        health
        , coalesce(point, 0) as point
        , money
        , id_person
        , time_close
        , round
      from game g
      where g.id_user = u.id_user
      order by g.point desc
      limit 1
  ) g on True
  join person p on (g.id_person = p.id_person)
  order by coalesce(g.point, 0) desc
'''
        return self.execute()
