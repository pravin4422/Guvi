# Backend Operation Guide

## 🎯 Quick Start (Easiest Way)

### Method 1: Using Startup Script (Recommended)
```bash
# Navigate to backend folder
cd backend

# Double-click or run:
start_backend.bat
```

This script will:
- ✅ Check if MySQL is running
- ✅ Check if MongoDB is running  
- ✅ Check if Redis is running
- ✅ Start Flask backend on http://localhost:5000

---

## 📋 Manual Operation

### Step-by-Step Manual Start:

#### 1. Start MySQL
- Open XAMPP Control Panel
- Click "Start" next to MySQL
- Wait for green status

#### 2. Verify MongoDB & Redis (Auto-start as Windows services)
```bash
# Check MongoDB
sc query MongoDB

# Check Redis
sc query Redis

# If not running, start them:
net start MongoDB
net start Redis
```

#### 3. Start Flask Backend
```bash
cd backend
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

---

## 🔍 Check Service Status

### Method 1: Using Check Script
```bash
cd backend
check_services.bat
```

### Method 2: Manual Check
```bash
# Check all ports
netstat -an | findstr "3306 27017 6379 5000"
```

Expected output:
```
TCP    127.0.0.1:3306    LISTENING   <- MySQL
TCP    127.0.0.1:27017   LISTENING   <- MongoDB
TCP    0.0.0.0:6379      LISTENING   <- Redis
TCP    127.0.0.1:5000    LISTENING   <- Flask Backend
```

---

## 🛑 Stop Backend

### Method 1: Using Stop Script
```bash
cd backend
stop_backend.bat
```

### Method 2: Manual Stop
- Press `Ctrl + C` in the terminal where Flask is running

### Stop All Services:
```bash
# Stop MySQL: Use XAMPP Control Panel

# Stop MongoDB
net stop MongoDB

# Stop Redis
net stop Redis
```

---

## 🔧 Backend Configuration

### Database Connections

**MySQL Configuration** (`db.py`):
```python
host='localhost'
user='root'
password=''          # Change if you set a password
database='secureauth'
port=3306
```

**MongoDB Configuration** (`mongo_client.py`):
```python
MongoClient('mongodb://localhost:27017/')
database='secureauth'
collection='profiles'
```

**Redis Configuration** (`redis_client.py`):
```python
host='localhost'
port=6379
session_timeout=3600  # 1 hour
```

---

## 🐛 Troubleshooting

### Problem: "Can't connect to MySQL"
**Solution:**
1. Open XAMPP Control Panel
2. Start MySQL
3. Check port 3306: `netstat -an | findstr "3306"`

### Problem: "Can't connect to MongoDB"
**Solution:**
```bash
# Start MongoDB service
net start MongoDB

# Or check if it's running
sc query MongoDB
```

### Problem: "Can't connect to Redis"
**Solution:**
```bash
# Start Redis service
net start Redis

# Or check if it's running
sc query Redis
```

### Problem: "Port 5000 already in use"
**Solution:**
```bash
# Find process using port 5000
netstat -ano | findstr "5000"

# Kill the process (replace PID with actual number)
taskkill /F /PID <PID>
```

### Problem: "Module not found"
**Solution:**
```bash
cd backend
pip install -r requirements.txt
```

---

## 📊 Backend API Testing

### Test with Browser:
1. Start backend: `start_backend.bat`
2. Open browser: http://localhost:5000
3. You should see Flask running

### Test with curl:
```bash
# Test registration
curl -X POST http://localhost:5000/api/register ^
  -H "Content-Type: application/json" ^
  -d "{\"name\":\"Test User\",\"email\":\"test@example.com\",\"password\":\"password123\"}"

# Test login
curl -X POST http://localhost:5000/api/login ^
  -H "Content-Type: application/json" ^
  -d "{\"email\":\"test@example.com\",\"password\":\"password123\"}"
```

---

## 📁 Backend File Structure

```
backend/
├── app.py              # Main Flask application (START HERE)
├── db.py               # MySQL operations
├── redis_client.py     # Redis session management
├── mongo_client.py     # MongoDB profile operations
├── routes/
│   ├── auth.py        # /api/register, /api/login
│   └── profile.py     # /api/profile (GET, PUT)
├── requirements.txt    # Python dependencies
├── setup_db.py        # Database initialization
├── start_backend.bat  # Quick start script
├── check_services.bat # Service status checker
└── stop_backend.bat   # Stop backend script
```

---

## 🔄 Daily Workflow

### Starting Work:
1. Open XAMPP Control Panel → Start MySQL
2. Run `start_backend.bat`
3. Open `frontend/register.html` in browser

### During Development:
- Backend auto-reloads on code changes (Flask debug mode)
- Check logs in terminal for errors
- Use `check_services.bat` to verify services

### Ending Work:
1. Press `Ctrl + C` to stop Flask
2. Stop MySQL from XAMPP (optional)
3. MongoDB & Redis can keep running (they're services)

---

## 🎓 Understanding Backend Flow

### 1. Registration Flow:
```
Frontend (register.js) 
  → POST /api/register 
  → routes/auth.py 
  → db.py (MySQL with prepared statement)
  → bcrypt hash password
  → Store in MySQL
  → Return success
```

### 2. Login Flow:
```
Frontend (login.js)
  → POST /api/login
  → routes/auth.py
  → db.py (verify credentials)
  → bcrypt compare password
  → redis_client.py (create session)
  → Return token
  → Frontend stores in localStorage
```

### 3. Profile Flow:
```
Frontend (profile.js)
  → GET /api/profile (with token header)
  → routes/profile.py
  → redis_client.py (validate token)
  → mongo_client.py (get profile)
  → Return profile data
```

### 4. Update Profile Flow:
```
Frontend (profile.js)
  → PUT /api/profile (with token + data)
  → routes/profile.py
  → redis_client.py (validate token)
  → mongo_client.py (update profile)
  → Return success
```

---

## ✅ Backend Checklist

Before running frontend, ensure:
- [ ] MySQL running (port 3306)
- [ ] MongoDB running (port 27017)
- [ ] Redis running (port 6379)
- [ ] Flask backend running (port 5000)
- [ ] Database 'secureauth' created
- [ ] Table 'users' exists

Run `check_services.bat` to verify all!

---

## 🚀 You're Ready!

Now you know how to:
- ✅ Start the backend
- ✅ Check service status
- ✅ Stop the backend
- ✅ Troubleshoot issues
- ✅ Understand the flow

**Next Step:** Run `start_backend.bat` and test your application!
