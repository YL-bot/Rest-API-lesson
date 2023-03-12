from requests import get, post, delete, put
import datetime

print('Тесты начались')


#post некор из за сущ адр
print(post('http://127.0.0.1:8080/api/v2/users',
           json={"id": 123123123123123123, "address": 'module_1', "age": 20, "email": 'mark@gmail.com', "modified_date": None,
                 "name": 'mark', "position": 'test', "surname": 'test', 'speciality': 'test',
                 'password_hash': 'dakdf2:sha336:260000$yilawWgMGYQPegQ4$6c1c4ed775ee52c71fa8bd89be8f8a53e28b1ce69edcae316b267f493647961f'}).json())

#post кор 
print(post('http://127.0.0.1:8080/api/v2/users',
           json={"id": 23374141291213213231232, "address": 'module_1', "age": 20, "email": 'marasdsdasdadasdasdasdadk@gmail.ru', "modified_date": None,
                 "name": 'mark', "position": 'test', "surname": 'test', 'speciality': 'test',
                 'password_hash': 'dakdf2:sha336:260000$yilawWgMGYQPegQ4$6c1c4ed775ee52c71fa8bd89be8f8a53e28b1ce69edcae316b267f493647961f'}).json())


#post некор из за отсутствия данных
print(post('http://127.0.0.1:8080/api/v2/users',
           json={"id": 323223131312321, "address": 'module_1'}).json())


#post некор из за id 
print(post('http://127.0.0.1:8080/api/v2/users',
           json={"id": 1, "address": 'module_1', "age": 20, "email": 'mark@gmaiadasdl.ru', "modified_date": None,
                 "name": 'mark', "position": 'test', "surname": 'test', 'speciality': 'test',
                 'password_hash': 'dakdf2:sha336:260000$yilawWgMGYQPegQ4$6c1c4ed775ee52c71fa8bd89be8f8a53e28b1ce69edcae316b267f493647961f'}).json())

#check
print(get('http://127.0.0.1:8080/api/v2/users').json())

#datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#put кор (почта)
time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(put('http://127.0.0.1:8080/api/v2/users/234237',
           json={"address": 'module_1', "age": 20, "email": 'WDADSAASDSDADmarasdsdadk@gmail.ru', "modified_date": None,
                 "name": 'mark', "position": 'test', "surname": 'test', 'speciality': 'test',
                 'password_hash': 'dakdf2:sha336:260000$yilawWgMGYQPegQ4$6c1c4ed775ee52c71fa8bd89be8f8a53e28b1ce69edcae316b267f493647961f'}).json())

#put некор из за id
print(put('http://127.0.0.1:8080/api/v2/users/1',
           json={"id": 23374141291213213, "address": 'module_1', "age": 20, "email": 'marasdsdadk@gmail.ru', "modified_date": None,
                 "name": 'mark', "position": 'test', "surname": 'test', 'speciality': 'test',
                 'password_hash': 'dakdf2:sha336:260000$yilawWgMGYQPegQ4$6c1c4ed775ee52c71fa8bd89be8f8a53e28b1ce69edcae316b267f493647961f'}).json())

#mark@gmail.com
#put некор из за почты
print(put('http://127.0.0.1:8080/api/v2/users/4',
           json={"address": 'module_1', "age": 20, "email": 'mark@gmail.com', "modified_date": None,
                 "name": 'mark', "position": 'test', "surname": 'test', 'speciality': 'test',
                 'password_hash': 'dakdf2:sha336:260000$yilawWgMGYQPegQ4$6c1c4ed775ee52c71fa8bd89be8f8a53e28b1ce69edcae316b267f493647961f'}).json())


#put некор из за отсутств данных
print(put('http://127.0.0.1:8080/api/v2/users/23',
           json={"address": 'module_1', "age": 20, "email": 'mark@gmail.com', "modified_date": None}).json())



#норм удал
print(delete('http://127.0.0.1:8080/api/v2/users/1').json())


#нет id такого
print(delete('http://127.0.0.1:8080/api/v2/users/213123123312455632343123124').json())