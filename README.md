# TranslateNameTelegramBot

## Инструкция для запуска бота через docker
Скачайте проект (все файлы).
В папке проекта откройте терминал и выполните следующие команды:
```
$ sudo docker build .
$ sudo docker images
$ sudo docker run -d -p 80:80 image id 
# image id - id образа, который создался
```
Для того, чтобы остановить бота, выполните команды:
```
$ sudo docker ps
$ sudo docker stop CONTAINER ID
# CONTAINER ID - id  контейнера созданного образа
```
