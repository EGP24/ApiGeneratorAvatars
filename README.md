# Описание переменных окружения
- EE_POSTGRES_USERNAME, EE_POSTGRES_PASSWORD - имя пользователя и пароль postgresql
- EE_POSTGRES_DB - название postgeres базы данных
- EE_REDIS_URL - ссылка для подключения к redis
- EE_REDIS_PASSWORD - пароль redis
- EE_SECRET_KEY - секретный ключ дл хэширования паролей 
- EE_ACCESS_TOKEN_EXPIRE_MINUTES - время существования токена авторизации (в минутах)
- EE_ALGORITHM - алгоритм хэширования

# Запуск приложения
1. Настроить переменные виртуального окружения
2. Выполнить слудующие команды из корня проекта
```
   docker-compose -f docker-compose.yaml biuld
   docker-compose -f docker-compose.yaml up
```

# Описание API
### POST /registration 
Регистрирует пользователя по username и password.
Возвращает JWT Token авторизации
### POST /login
Авторизация пользователя по username и password.
Возвращает JWT Token авторизации
### GET /avatar
Получение аватарки пользователя по JWT токену.
Возвращает аватарку в байтах
### GET /docs
Более подробная документация
