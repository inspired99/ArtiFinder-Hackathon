# ArtiFinder

**ArtiFinder** - это передовой веб-сервис, призванный произвести революцию в управлении музейными коллекциями. Используя возможности компьютерного зрения, он быстро идентифицирует дубликаты изображений среди обширного каталога музейных предметов, обеспечивая целостность и стандартизацию данных. Благодаря автоматическому созданию описаний он упрощает процесс добавления новых записей, открывая путь к более эффективной и точной музейной каталогизации.

# Описание

Веб-сервис **ArtiFinder** был разработан в рамках кейса "Поиск музейных предметов" на хакатоне Цифровой прорыв.
**ArtiFinder** обладает следующим функцианалом:

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


