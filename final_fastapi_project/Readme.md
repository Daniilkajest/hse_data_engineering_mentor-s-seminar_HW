ФИнальное дз - проекты на Fastapi

## Запуск
Для запуска требуются Docker и Docker Compose (или ручной билд).

### Сборка
docker build -t todo-service:latest todo_app/
docker build -t shorturl-service:latest shorturl_app/

### Запуск
docker run -d -p 8000:80 -v todo_data:/app/data todo-service:latest
docker run -d -p 8001:80 -v shorturl_data:/app/data shorturl-service:latest
