### Reddit User Activity Parser
## Описание
Данный проект - это парсер, который собирает статистику по пользователям на конкретном сабреддите на платформе Reddit. Он выводит два списка пользователей:

* Топ-10 пользователей по количеству созданных постов.
* Топ-10 пользователей по количеству оставленных комментариев.
## Начало работы
Чтобы начать использовать этот проект, выполните следующие шаги:
* Клонируйте репозиторий (git clone https://github.com/MagerOK/Reddit_Parser.git)
* Установите библиотеку PRAW (pip install praw)
* Зайти на https://www.reddit.com/prefs/apps и создать там приложение-скрипт.
* В корневой папке проекта создайте файл config.py и добавьте в него следующий код:
  reddit_config = {
    'client_id': 'Ваш_Client_ID',
    'client_secret': 'Ваш_Client_Secret',
    'user_agent': 'Ваш_User_Agent',
    'username': 'Ваше_имя_пользователя_Reddit',
    'password': 'Ваш_пароль_Reddit',
}
* Заполните поля своими данными от аккаунта Reddit, которые вы получите при регистрации вашего приложения на Reddit.
* Запустите приложение с помощью команды python app.py 
