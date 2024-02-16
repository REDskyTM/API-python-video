import requests

url = 'http://localhost:5000/add_quote'  # Замените на ваш реальный URL

# Отправляем POST-запрос с новой цитатой
data = {'quote': 'Новая цитата для добавления'}
response = requests.post(url, json=data)

# Проверяем статус код ответа
if response.status_code == 201:
    print('Цитата успешно добавлена')
else:
    print('Ошибка при добавлении цитаты')
