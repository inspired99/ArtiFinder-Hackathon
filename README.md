# [ArtiFinder](https://cathackers.xyz/)

**ArtiFinder** - это веб-сервис для помощи в управлении музейными коллекциями. Используя возможности компьютерного зрения, он быстро идентифицирует дубликаты изображений среди обширного каталога музейных предметов, обеспечивая целостность и стандартизацию данных. Благодаря автоматическому созданию описаний он упрощает процесс добавления новых записей, открывая путь к более эффективной и точной музейной каталогизации.

https://cathackers.xyz/

# Описание

Веб-сервис **ArtiFinder** был разработан в рамках кейса "Поиск музейных предметов" на хакатоне Цифровой прорыв.
**ArtiFinder** обладает следующей функциональностью:

* Просмотр каталога изображений
* Поиск дубликатов в каталоге
* Генерация описания по изображению
* Поиск с фильтрацией по категориям
* Поиск с фильтрацией по описанию

# Развертывание сервиса

Клонируйте репозиторий в директорию на вашем сервере

```bash
git clone https://github.com/VadimShabashov/ArtiFinder.git
```

## Развертывание веб-интерфейса

### Шаг 1: Установка Nginx

[Установите Nginx](https://www.nginx.com/resources/wiki/start/topics/tutorials/install/) на ваш сервер. Для Debian/Ubuntu это можно сделать с помощью команды:

```bash
sudo apt update
sudo apt install nginx
```

### Шаг 2: Конфигурация Nginx

1. Удалите содержимое кталага конфигураций Nginx.  

```bash
sudo rm -r /etc/nginx/*
```

2. Переместите наш кталаг конфигураций Nginx в ```/etc/nginx/```

```bash
sudo mv /path/to/ArtiFinder/web_client/.nginx/* /etc/nginx/
```

3. В конфигурационном файле ```/etc/nginx/sites-available/default``` замените ```example.com``` на ваш доменный или IP адрес.

```bash
sudo nano /etc/nginx/sites-available/default
```

4. Также можно настроить SSL сертификат по этой [инструкции](https://certbot.eff.org).

5. Добавьте ссылку на сближенный сайт в папку `/var/www`.
```bash
sudo ln -s /path/to/ArtiFinder/web_client/dist/spa /var/www/spa
```
Не забудьте дать доступ пользователю `www-data` к папке `/path/to/ArtiFinder/web_client/dist/spa`. Например, так: 

```bash
gpasswd -a www-data username
```
 
6. Добавьте ссылку на папку с изображениями сайт в папку `/var/www`.

```bash
sudo ln -s /path/to/images /var/www/imgs
```

## Развертывание серверной части

1. Перейдите в каталог `/path/to/ArtiFinder/`
```bash
cd /path/to/ArtiFinder/
```
2. Установите зависимости из файла `requirements.txt`, выполнив следующую команду:
```bash
pip install -r requirements.txt
```
3. Запустите сервер, выполнив команду:
```bash
python3 main.py
```
4. Убедитесь, что сервер работает корректно и отвечает на запросы. Откройте веб-браузер. Введите адрес `http://localhost:8000/api/docs`

# ML модели

* Для классификации изображений используется предобученный визуальный трансформер Swin - `swin_tiny_patch4_window7_224`. Для повышения точности модель была дообучена на тренировочных изображениях с применением аугментаций. Веса модели доступны по [ссылке](https://drive.google.com/file/d/1nm1xIbH08QyWKBAJsmDHK-9m8LWYCXkJ/view?usp=sharing).

* Для извлечения эмбеддингов и поиска с помощью FAISS по векторам используется предобученная мультимодальная модель от OpenAI CLIP - `openai/clip-vit-base-patch32`.

* Для генерации текста по изображению для описания используется img2text модель на основе LLM и энкодера для изображений LLaVA - `llava-v1.5-13b`. 


# Сборка веб-интерфейса

1. Перейдите в папку `/path/to/ArtiFinder/web_client/`
```bash
cd /path/to/ArtiFinder/web_client/
```
2. Сборка веб-интерфейса

```bash
npm install
npm run build
```

3. Теперь ваш веб-интерфейс успешно собран с помощью npm и готов к развертыванию.

# Команда
1. Евсеев Елисей - ML, CV
2. Шабашов Вадим - ML, Pipeline
3. Галоев Илькин - Backend
4. Сайфуллин Дмитрий - Backend
5. Иванцов Илья - Frontend


