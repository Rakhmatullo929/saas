# 🔧 SmartDocs Troubleshooting Guide

## 🚨 Common Issues and Solutions

### 1. **Dependency Installation Errors**

#### Problem: `cryptography==41.0.8` installation fails
```
ERROR: No matching distribution found for cryptography==41.0.8
```

**✅ Solution:**
- Use `requirements-basic.txt` instead of `requirements.txt` for initial setup
- Run: `pip install -r backend/requirements-basic.txt`

#### Problem: Python version compatibility
```
ERROR: Requires-Python >=3.11
```

**✅ Solution:**
- Ensure you're using Python 3.10 or higher
- Check version: `python --version`
- Update if needed or use pyenv/conda

### 2. **Database Connection Issues**

#### Problem: PostgreSQL connection failed
```
django.db.utils.OperationalError: could not translate host name "db"
```

**✅ Solution:**
- Use local settings: `--settings=config.settings_local`
- This uses SQLite instead of PostgreSQL for local development
- Or run with Docker: `docker-compose up`

### 3. **Import Errors**

#### Problem: Cannot import Celery app
```
ImportError: cannot import name 'app' from 'config.celery'
```

**✅ Solution:**
- Install celery: `pip install celery`
- Ensure `backend/config/celery.py` exists and has proper content
- Use the startup script: `./start_dev.sh`

### 4. **Server Won't Start**

#### Problem: Server not responding
```
curl: (7) Failed to connect to localhost port 8000
```

**✅ Solution:**
1. Check if server is actually running
2. Use correct settings: `python manage.py runserver --settings=config.settings_local`
3. Check for error messages in terminal
4. Try different port: `python manage.py runserver 127.0.0.1:8001`

### 5. **Permission Errors**

#### Problem: Script not executable
```
bash: ./start_dev.sh: Permission denied
```

**✅ Solution:**
```bash
chmod +x start_dev.sh
./start_dev.sh
```

## 📋 Quick Commands Reference

### Local Development (SQLite)
```bash
# Quick start
./start_dev.sh

# Manual commands
cd backend
python manage.py migrate --settings=config.settings_local
python manage.py runserver --settings=config.settings_local
```

### Docker Development (PostgreSQL)
```bash
# Full stack
docker-compose up --build

# Backend only
docker-compose up db redis backend
```

### Common Django Commands
```bash
# Check system
python manage.py check --settings=config.settings_local

# Create migrations
python manage.py makemigrations --settings=config.settings_local

# Django shell
python manage.py shell --settings=config.settings_local

# Create superuser
python manage.py createsuperuser --settings=config.settings_local
```

## 🔍 Debug Information

### Check Installation
```bash
python --version          # Should be 3.10+
pip list | grep Django    # Should show Django 4.2.8
pip list | grep celery    # Should show celery 5.3.4
```

### Check Database
```bash
# With local settings (SQLite)
python manage.py dbshell --settings=config.settings_local

# List migrations
python manage.py showmigrations --settings=config.settings_local
```

### Check API Endpoints
```bash
# Health check
curl http://127.0.0.1:8000/api/v1/core/health/

# API documentation
open http://127.0.0.1:8000/api/docs/
```

## 📞 Need Help?

1. **Check logs**: Look for error messages in terminal
2. **Verify setup**: Ensure all steps in README were followed
3. **Clean start**: Delete `backend/db.sqlite3` and run migrations again
4. **Virtual environment**: Make sure you're in activated venv

## 🔄 Reset Everything

If nothing works, here's how to start fresh:

```bash
# Remove database
rm -f backend/db.sqlite3

# Remove Python cache
find . -name "__pycache__" -type d -exec rm -rf {} +

# Reinstall dependencies
cd backend
pip install -r requirements-basic.txt

# Run fresh migrations
python manage.py migrate --settings=config.settings_local

# Start development
python manage.py runserver --settings=config.settings_local
``` 