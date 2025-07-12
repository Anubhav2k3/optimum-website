@@ .. @@
 from flask import Flask
 from flask_sqlalchemy import SQLAlchemy
 from flask_login import LoginManager
 from sqlalchemy.orm import DeclarativeBase
 from werkzeug.middleware.proxy_fix import ProxyFix
 import logging
+import json

 # Configure logging
 logging.basicConfig(level=logging.DEBUG)

@@ .. @@
 with app.app_context():
     import models  # noqa: F401
     import routes  # noqa: F401
     db.create_all()
     logging.info("Database tables created")
+    
+    # Add custom Jinja2 filter for JSON parsing
+    @app.template_filter('from_json')
+    def from_json_filter(value):
+        if value:
+            try:
+                return json.loads(value)
+            except (json.JSONDecodeError, TypeError):
+                return []
+        return []