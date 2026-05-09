# SmartHome Pro

Home Service & Task Management System built with Django and TiDB Cloud.

## Production Setup (TiDB Cloud + Render)

This project is configured for seamless deployment on **Render** using **TiDB Cloud** as the database.

### 1. Database Setup
1. Create a cluster on [TiDB Cloud](https://tidbcloud.com/).
2. Retrieve your connection details: **Host**, **Port**, **User**, and **Password**.
3. The database name is configured as `sys` by default.

### 2. Environment Variables
Create a `.env` file in the root directory (or set them in Render dashboard):
```env
DEBUG=False
SECRET_KEY=your_secret_key
DB_HOST=your_tidb_host
DB_PORT=4000
DB_NAME=sys
DB_USER=your_tidb_user.root
DB_PASSWORD=your_tidb_password
SSL_CA=/etc/ssl/cert.pem
ALLOWED_HOSTS=.onrender.com
```

### 3. Local Development
```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run migrations
python manage.py migrate

# 4. Run development server
python manage.py runserver
```

### 4. Deployment
The project includes a `render.yaml` for "Infrastructure as Code" deployment.
1. Connect your repo to Render.
2. Render will use `render.yaml` to provision the web service.
3. Database migrations and static file collection will run automatically during the build phase.

## Health Monitoring
A health check endpoint is available at `/health/` to monitor application and database status.

