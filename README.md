# Test task junior python developer

# Requirements for project - Python 3.9 +

## Docker installation
**to build image**  `docker build --tag python-docker .`

**to run in detached mode** `docker run -d -p 8000:5000 python-docker`


## Первая часть
Написать парсер для сайта https://shop.kz 
В разделе Смартфоны
(https://shop.kz/smartfony/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/) надо спарсить все смартфоны с их характеристиками
Данные должны быть в формате json и соответствовать примеру:
`{
"name": "Apple iPhone 11 (2020), 64Gb, Green (MHDG3)", 
"articul": "151840",
"price": "329900",
"memory-size": "64 Гб",
}`
Ниже описание каждого из ключей: name -> Название смартфона articul -> Артикул в магазине
price -> Цена смартфона на данный момент memory-size -> Объем встроенной памяти
Все данные надо сохранить в файл smartphones.json

## Вторая часть 
Написать API используя один из трех фреймворков (Flask, FastAPI)
Нужно написать эндпоинт (/smartphones) с параметром price который выведет все смартфоны с указанной ценой (данные надо взять из файла smartphones.json)
Обернуть в докер контейнер (Dockerfile, docker-compose)
Пример:
URL: localhost:8000/smartphones?price=329900 Response:

`[
{
"name": "Apple iPhone 11 (2020), 64Gb, Green (MHDG3)", 
"articul": "151840",
"price": "329900",
"memory-size": "64 Гб",
},
{
"name": "Apple iPhone 11 (2020), 64Gb, Red (MHDD3)", "articul": "152229",
"price": "329900",
"memory-size": "64 Гб",
}
]`

В качестве решения можно отправить ссылку на репозиторий или zip архив проекта
