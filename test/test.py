from requests import get, post, delete, put

print('Тесты начались')

#Получение всех работа
print(get('http://127.0.0.1:8080/api/jobs').json())


#Корректное получение одной работы
print(get('http://127.0.0.1:8080/api/jobs/1').json())


#Ошибочный запрос на получение одной работы — неверный id
print(get('http://127.0.0.1:8080/api/jobs/2342342423424234').json())


#Ошибочный запрос на получение одной работы — строка
print(get('http://127.0.0.1:8080/api/jobs/lmao').json())


#для проверки выполнения
print(get('http://127.0.0.1:8080/api/jobs').json())


#корректный POST-запрос
print(post('http://127.0.0.1:8080/api/jobs',
           json={"id": 67, "team_leader": 1, "title": "test", "work_size": 24, "collaborators": '1, 2',
                 "start_date": None, "end_date": None, "is_finished": True}).json())


#для проверки выполнения
print(get('http://127.0.0.1:8080/api/jobs').json())


#дубликат предыдущего ( id такой уже есть )
print(post('http://127.0.0.1:8080/api/jobs',
           json={"id": 67, "team_leader": 1, "title": "test", "work_size": 24, "collaborators": '1, 2',
                 "start_date": None, "end_date": None, "is_finished": True}).json())


#wrong POST-запрос ( тим лида нет )
print(post('http://127.0.0.1:8080/api/jobs',
           json={"id": 21, "team_leader": 12323, "title": "test", "work_size": 24, "collaborators": '1, 2',
                 "start_date": None, "end_date": None, "is_finished": True}).json())

#нехватка данных
print(post('http://127.0.0.1:8080/api/jobs',
           json={"id": 20, "team_leader": 1, "title": "test"}).json())


#верный POST-запрос, но без указания id
print(post('http://127.0.0.1:8080/api/jobs',
           json={"team_leader": 1, "title": "test", "work_size": 24, "collaborators": '1, 2',
                 "start_date": None, "end_date": None, "is_finished": True}).json())


#для проверки выполнения
print(get('http://127.0.0.1:8080/api/jobs').json())


#верное удаление
print(delete('http://127.0.0.1:8080/api/jobs/1').json())


#для проверки выполнения
print(get('http://127.0.0.1:8080/api/jobs').json())


#wrong удаление, так как нет такого id
print(delete('http://127.0.0.1:8080/api/jobs/1232332').json())


#wrong удаление, так как нет такого id
print(delete('http://127.0.0.1:8080/api/jobs/101232323').json())


#для проверки выполнения
print(get('http://127.0.0.1:8080/api/jobs').json())


#корректный PUT-запрос
print(put('http://127.0.0.1:8080/api/jobs/55',
           json={"team_leader": 2, "title": "test", "work_size": 24, "collaborators": '1, 2',
                 "start_date": None, "end_date": None, "is_finished": True}).json())


#для проверки выполнения (изменился тим лид)
print(get('http://127.0.0.1:8080/api/jobs').json())


#wrong PUT-запрос, так как нет такого тим лида
print(put('http://127.0.0.1:8080/api/jobs/55',
           json={"team_leader": 123323, "title": "test", "work_size": 24, "collaborators": '1, 2',
                 "start_date": None, "end_date": None, "is_finished": True}).json())


#wrong PUT-запрос, так как нет такого id
print(put('http://127.0.0.1:8080/api/jobs/342423424',
           json={"team_leader": 123323, "title": "test", "work_size": 24, "collaborators": '1, 2',
                 "start_date": None, "end_date": None, "is_finished": True}).json())


#wrong PUT-запрос, так как нет некоторых данных
print(put('http://127.0.0.1:8080/api/jobs/55',
           json={"team_leader": 1, "title": "test"}).json())


#для проверки выполнения
print(get('http://127.0.0.1:8080/api/jobs').json())

print('Тесты завершены')