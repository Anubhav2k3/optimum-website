# Optimum Value Website

A professional Flask-based corporate website for Optimum Value, a Salesforce consulting company with a comprehensive content management system.

## 🚀 Quick Start

### 1. Setup Database
```bash
python setup_database.py
```

### 2. Run the Application
```bash
python main.py
```

### 3. Access Admin Panel
1. Open http://localhost:5000
2. Hover over the navbar to reveal the admin button
3. Login with: `admin` / `admin123`
4. **Important:** Change the default password after first login!

## 📁 Project Structure

```
optimum_value_website/
├── app.py                 # Main Flask application
├── main.py               # Application entry point
├── models.py             # Database models
├── routes.py             # URL routes and handlers
├── create_admin.py       # Admin user and sample data creation
├── setup_database.py     # Quick database setup script
├── optimum_value.db      # SQLite database (created after setup)
├── templates/            # Jinja2 templates
│   ├── admin/           # Admin panel templates
│   └── *.html           # Public website templates
└── static/              # CSS, JS, and images
    ├── css/style.css    # Custom styling
    ├── js/main.js       # Frontend JavaScript
    └── images/          # Website images
```

## 🎯 Features

### Public Website
- **Responsive Design:** Professional purple-themed layout
- **Service Pages:** Dynamic service listings with detail pages
- **Industry Solutions:** Industry-specific content and case studies
- **Blog System:** Published blog posts with featured content
- **Case Studies:** Client success stories and testimonials
- **Contact Forms:** Lead capture and inquiry handling

### Admin Dashboard
- **Content Management:** Create, edit, delete blogs and case studies
- **Service Management:** Manage service offerings and descriptions
- **Industry Management:** Configure industry-specific content
- **User Authentication:** Secure admin access with login system
- **Publishing Controls:** Draft/published status and featured content
- **Rich Forms:** Auto-slug generation, validation, and helpful tips

## 🗄️ Database

Uses SQLite for simplicity - no external database setup required!

### Models
- **Admin:** User accounts for admin access
- **BlogPost:** Blog articles with publishing controls
- **CaseStudy:** Client success stories
- **Service:** Service offerings with features/benefits
- **Industry:** Industry-specific solutions

## 🔧 Configuration

### Environment Variables (Optional)
- `DATABASE_URL`: Custom database URL (defaults to SQLite)
- `SESSION_SECRET`: Session secret key (has secure default)

### Default Admin Account
- **Username:** admin
- **Password:** admin123
- **⚠️ Change this password immediately after first login!**

## 📝 Content Management

### Creating Blog Posts
1. Go to Admin → Blog Posts → New Blog Post
2. Fill in title (slug auto-generates)
3. Add excerpt and full content
4. Set featured image URL
5. Choose draft or published status
6. Mark as featured for homepage display

### Creating Case Studies
1. Go to Admin → Case Studies → New Case Study
2. Enter client and project details
3. Describe challenge, solution, and results
4. Select industry category
5. Publish when ready

### Managing Services & Industries
- Services and Industries come pre-populated with sample data
- Edit existing items or create new ones
- Control display order and active status
- Add features, benefits, challenges, and solutions

## 🎨 Customization

### Styling
- Edit `static/css/style.css` for design changes
- CSS variables in `:root` for easy color theming
- Bootstrap 5.3.0 for responsive components

### Content
- Modify templates in `templates/` directory
- Update company information in footer
- Customize hero sections and messaging

## 🔒 Security

- Flask-Login for session management
- Password hashing with Werkzeug
- CSRF protection on forms
- Admin-only content management
- Secure session configuration

## 📱 Responsive Design

- Mobile-first approach
- Flexible navigation with collapsible menu
- Optimized for all screen sizes
- Touch-friendly admin interface

## 🚀 Deployment

For production deployment:
1. Set `DATABASE_URL` environment variable for production database
2. Set `SESSION_SECRET` to a secure random value
3. Disable debug mode
4. Use a WSGI server like Gunicorn
5. Serve static files with nginx or similar

## 📞 Support

For questions or issues with this website system, refer to the code comments and admin interface tips, or modify the templates and routes as needed for your specific requirements.