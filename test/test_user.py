from requests import get, post, delete, put


print('Тесты начались')


print(post('http://127.0.0.1:8080/api/users',
           json={"id": 234234, "address": 'module_1', "age": 20, "email": 'mark@gami;.com', "modified_date": None,
                 "name": 'mark', "position": 'test', "surname": 'test', 'speciality': 'test',
                 'password_hash': 'dakdf2:sha336:260000$yilawWgMGYQPegQ4$6c1c4ed775ee52c71fa8bd89be8f8a53e28b1ce69edcae316b267f493647961f'}).json())