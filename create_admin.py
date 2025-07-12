@@ .. @@
 if __name__ == '__main__':
     print("Setting up admin system...")
+    print("Using SQLite database: optimum_value.db")
     create_admin_user()
     create_sample_services()
     create_sample_industries()
     print("Setup complete!")
+    print("\nTo access admin panel:")
+    print("1. Run the application: python main.py")
+    print("2. Go to: http://localhost:5000")
+    print("3. Hover over navbar and click admin button")
+    print("4. Login with: admin / admin123")
+    print("5. IMPORTANT: Change the default password after first login!")