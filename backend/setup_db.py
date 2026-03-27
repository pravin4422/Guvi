import mysql.connector
from mysql.connector import Error

print("=" * 50)
print("SecureAuth Database Setup")
print("=" * 50)

# Try to connect and create database
try:
    # Connect without database first
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''
    )
    
    if conn.is_connected():
        print("[OK] Connected to MySQL server")
        cursor = conn.cursor()
        
        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS secureauth")
        print("[OK] Database 'secureauth' created")
        
        # Switch to database
        cursor.execute("USE secureauth")
        
        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL
            )
        ''')
        print("[OK] Table 'users' created")
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print("\n" + "=" * 50)
        print("Setup completed successfully!")
        print("=" * 50)
        print("\nYou can now run: python app.py")
        
except Error as e:
    print(f"\n[ERROR] Error: {e}")
    print("\nMake sure MySQL server is running!")
    print("If using XAMPP: Start MySQL from XAMPP Control Panel")
    print("If standalone: Start MySQL service from Windows Services")
