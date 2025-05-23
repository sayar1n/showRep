## Предварительные требования
- Установленный Docker
- Установленный Docker Compose
- Node.js 18+ (для локальной разработки)

## Запуск через Docker

### Сборка и запуск

```bash
docker-compose up --build
```
### Запуск в фоновом режиме

```bash
docker-compose up -d --build
```

### Остановка контейнера

```bash
docker-compose down
```
## Разработка

Frontend будет доступен по адресу: http://localhost:3000

### Структура Docker файлов

- `Dockerfile` - основной файл для сборки образа
- `docker-compose.yaml` - конфигурация для запуска контейнера
- `.dockerignore` - файлы, исключаемые из сборки

### Перезапуск контейнера

```bash
docker-compose restart
```
### Остановка и удаление контейнера

```bash
docker-compose down
```
### Остановка и удаление контейнера вместе с volumes

```bash
docker-compose down -v
```
### Просмотр запущенных контейнеров

```bash
docker ps
```
