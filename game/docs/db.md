# Структура базы данных

### users
```sql
  'id_user': str,
  'login': str,
  'password': str,
  'pic': str # Ссылка на картинку
```

### game
```sql
  'id_game': int,
  'id_user': int,
  'id_question': int,
  'time_open': timestamp,
  'time_close': timestamp,
  'round': int, # Номер раунда игры
  'health': float,   # Здоровье
  'point': int, # количество очков
  'money': int, # количество денег
  'id_person': int 
```


### question
```sql
  'id_question': int,
  'description': text,
  'pic': text, # Ссылка на картинку
  'answer': {
  '0':
    {
      'text': text,
      'health': float,   # Здоровье
      'point': int, # количество очков
      'money': int, # количество денег
      'id_event': int # 
    },
  },
  'tags': text[]
```


### person
```sql
  'id_person': int,
  'name': str,
  'description': str, # описание персонажа
  'health': float,
  'money': int,
  'point': int,
  'pic': str # ссылка на картинку
```


### session
```sql
  'id_user': int,
  'id_session': text
```


### event
```sql
  'id_event': int,
  'description': text,
  'health': float,
  'money': int, # Количество денег
  'point': int, # Количество очков
  'tags': text[],
  'round': int  # через сколько рауднов стрельнет
```

### event_to_game 

```sql
  'id_event': int,
  'id_game': int,
  'round': int
```