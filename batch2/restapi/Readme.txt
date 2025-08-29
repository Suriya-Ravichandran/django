create django project

"django-admin startproject myproject ."

create django app

"python manage.py startapp"


To deploy a **Django REST API** using **Docker**, with:

* **Ubuntu base image**
* **MySQL** as the database
* **phpMyAdmin** accessible on port **5000**
* **Django REST API** accessible on port **80**

Here's a **step-by-step guide** to set it up using **Docker Compose**, which simplifies multi-container setups.

---

## ✅ Step-by-Step Deployment

### 📁 Project Structure

```
myproject/
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── (your Django project files)
├── docker-compose.yml
```

---

## 1. ✅ Django Backend Dockerfile

**`backend/Dockerfile`**:

```Dockerfile
FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    libmysqlclient-dev \
    build-essential \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy Django project files
COPY . /app

# Install Python dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Run migrations and start server (overridden in docker-compose for manage.py tasks)
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:80"]
```

---

## 2. ✅ Requirements File

**`backend/requirements.txt`** (simplified):

```
Django>=3.2
djangorestframework
mysqlclient
gunicorn
```

---

## 3. ✅ Docker Compose File

**`docker-compose.yml`**:

```yaml
version: "3.8"

services:
  web:
    build: ./backend
    container_name: django_app
    ports:
      - "80:80"
    depends_on:
      - db
    environment:
      - DB_NAME=mydb
      - DB_USER=root
      - DB_PASSWORD=rootpassword
      - DB_HOST=db

  db:
    image: mysql:8.0
    container_name: mysql_db
    restart: always
    environment:
      MYSQL_DATABASE: mydb
      MYSQL_ROOT_PASSWORD: rootpassword
    volumes:
      - db_data:/var/lib/mysql

  phpmyadmin:
    image: phpmyadmin/phpmyadmin
    container_name: my_phpmyadmin
    restart: always
    ports:
      - "5000:80"
    environment:
      PMA_HOST: db
      PMA_USER: root
      PMA_PASSWORD: rootpassword

volumes:
  db_data:
```

---

## 4. ✅ Configure Django for MySQL

In your Django `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'root',
        'PASSWORD': 'rootpassword',
        'HOST': 'db',
        'PORT': '3306',
    }
}
```

---

## 5. ✅ Build and Run Containers

From the root of your project (`myproject/`):

```bash
docker-compose build
docker-compose up -d
```

---

## 6. ✅ Run Migrations and Create Superuser

Run these commands inside the Django container:

```bash
docker-compose exec web python3 manage.py migrate
docker-compose exec web python3 manage.py createsuperuser
```

---

## 7. ✅ Access Your Services

* Django REST API: [http://localhost](http://localhost)
* phpMyAdmin: [http://localhost:5000](http://localhost:5000)

---

## ✅ Optional Tips

* Replace `"myproject.wsgi:application"` with your actual WSGI module if named differently.
* You can use environment variables or `.env` files for secure secrets.
* For production, consider using **nginx** in front of Django.

---

Let me know if you want this as a downloadable zip or with a sample Django project preconfigured.
