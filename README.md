# Запуск проекта

1. ### Склонируйте проект

   >git clone 

2. ### Создайте виртуальное окружение и активируйте

     >python -m venv venv

     >🪟 Windows:

     >cd venv/Scripts/activate

     >🐧linux and 🍏 OS X:

      >source venv/bin/activate
   
4. ### Установите зависимости

      >pip install -r requirements.txt

5. ### Создайте и заполните .env

      >cp .env.template .env

6. ### Запустите проект

      >sh run.sh

# Запуск с помощью Docker

### Установите Docker: https://www.docker.com/get-started/

### Соберите и запустите контейнер:

  >docker-compose up --build
