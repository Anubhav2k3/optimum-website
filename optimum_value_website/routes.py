import json
from flask import render_template, request, redirect, url_for, flash, jsonify, abort
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from app import app, db
from models import Admin, BlogPost, CaseStudy, Service, Industry

# Main public routes
@app.route('/')
def index():
    """Main landing page with dynamic content."""
    # Get published content for display
    featured_blogs = BlogPost.query.filter_by(published=True, featured=True).limit(3).all()
    featured_case_studies = CaseStudy.query.filter_by(published=True, featured=True).limit(3).all()
    active_services = Service.query.filter_by(is_active=True).order_by(Service.order_index).all()
    active_industries = Industry.query.filter_by(is_active=True).order_by(Industry.order_index).all()
    
    return render_template('index.html', 
                         featured_blogs=featured_blogs,
                         featured_case_studies=featured_case_studies,
                         services=active_services,
                         industries=active_industries)

# Service pages
@app.route('/services/<slug>')
def service_detail(slug):
    """Individual service page."""
    service = Service.query.filter_by(slug=slug, is_active=True).first_or_404()
    
    # Parse JSON fields
    features = json.loads(service.features) if service.features else []
    benefits = json.loads(service.benefits) if service.benefits else []
    
    return render_template('service_detail.html', 
                         service=service, 
                         features=features, 
                         benefits=benefits)

@app.route('/services')
def services_list():
    """All services listing page."""
    services = Service.query.filter_by(is_active=True).order_by(Service.order_index).all()
    return render_template('services_list.html', services=services)

# Industry pages
@app.route('/industries/<slug>')
def industry_detail(slug):
    """Individual industry page."""
    industry = Industry.query.filter_by(slug=slug, is_active=True).first_or_404()
    
    # Parse JSON fields
    challenges = json.loads(industry.challenges) if industry.challenges else []
    solutions = json.loads(industry.solutions) if industry.solutions else []
    
    # Get related case studies
    related_case_studies = CaseStudy.query.filter_by(
        industry=industry.title, published=True
    ).limit(3).all()
    
    return render_template('industry_detail.html', 
                         industry=industry, 
                         challenges=challenges, 
                         solutions=solutions,
                         related_case_studies=related_case_studies)

@app.route('/industries')
def industries_list():
    """All industries listing page."""
    industries = Industry.query.filter_by(is_active=True).order_by(Industry.order_index).all()
    return render_template('industries_list.html', industries=industries)

# Blog and case study routes
@app.route('/blog')
def blog():
    """Blog listing page."""
    page = request.args.get('page', 1, type=int)
    posts = BlogPost.query.filter_by(published=True).order_by(
        BlogPost.created_at.desc()
    ).paginate(
        page=page, per_page=9, error_out=False
    )
    return render_template('blog.html', posts=posts)

@app.route('/blog/<slug>')
def blog_post(slug):
    """Individual blog post."""
    post = BlogPost.query.filter_by(slug=slug, published=True).first_or_404()
    return render_template('blog_post.html', post=post)

@app.route('/case-studies')
def case_studies():
    """Case studies listing page."""
    studies = CaseStudy.query.filter_by(published=True).order_by(
        CaseStudy.created_at.desc()
    ).all()
    return render_template('case_studies.html', studies=studies)

@app.route('/case-studies/<slug>')
def case_study(slug):
    """Individual case study."""
    study = CaseStudy.query.filter_by(slug=slug, published=True).first_or_404()
    return render_template('case_study.html', study=study)

# Contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact form handler."""
    if request.method == 'POST':
        # Handle contact form submission
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # For now, just flash a success message
        flash('Thank you for your message! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

# Admin authentication routes
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    """Admin login page."""
    if current_user.is_authenticated:
        return redirect(url_for('admin_dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        admin = Admin.query.filter_by(username=username).first()
        
        if admin and admin.check_password(password) and admin.is_active:
            login_user(admin)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('admin/login.html')

@app.route('/admin/logout')
@login_required
def admin_logout():
    """Admin logout."""
    logout_user()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('index'))

# Admin dashboard and management routes
@app.route('/admin')
@login_required
def admin_dashboard():
    """Admin dashboard."""
    blog_count = BlogPost.query.count()
    case_study_count = CaseStudy.query.count()
    service_count = Service.query.count()
    industry_count = Industry.query.count()
    
    recent_blogs = BlogPost.query.order_by(BlogPost.created_at.desc()).limit(5).all()
    recent_cases = CaseStudy.query.order_by(CaseStudy.created_at.desc()).limit(5).all()
    
    return render_template('admin/dashboard.html',
                         blog_count=blog_count,
                         case_study_count=case_study_count,
                         service_count=service_count,
                         industry_count=industry_count,
                         recent_blogs=recent_blogs,
                         recent_cases=recent_cases)

# Blog management routes
@app.route('/admin/blogs')
@login_required
def admin_blogs():
    """Admin blog management."""
    blogs = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    return render_template('admin/blogs.html', blogs=blogs)

@app.route('/admin/blogs/new', methods=['GET', 'POST'])
@login_required
def admin_blog_new():
    """Create new blog post."""
    if request.method == 'POST':
        title = request.form.get('title')
        slug = request.form.get('slug')
        excerpt = request.form.get('excerpt')
        content = request.form.get('content')
        image_url = request.form.get('image_url')
        published = bool(request.form.get('published'))
        featured = bool(request.form.get('featured'))
        
        blog = BlogPost(
            title=title,
            slug=slug,
            excerpt=excerpt,
            content=content,
            image_url=image_url,
            author_id=current_user.id,
            published=published,
            featured=featured
        )
        
        try:
            db.session.add(blog)
            db.session.commit()
            flash('Blog post created successfully!', 'success')
            return redirect(url_for('admin_blogs'))
        except Exception as e:
            db.session.rollback()
            flash('Error creating blog post. Please try again.', 'error')
    
    return render_template('admin/blog_form.html', blog=None)

@app.route('/admin/blogs/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def admin_blog_edit(id):
    """Edit blog post."""
    blog = BlogPost.query.get_or_404(id)
    
    if request.method == 'POST':
        blog.title = request.form.get('title')
        blog.slug = request.form.get('slug')
        blog.excerpt = request.form.get('excerpt')
        blog.content = request.form.get('content')
        blog.image_url = request.form.get('image_url')
        blog.published = bool(request.form.get('published'))
        blog.featured = bool(request.form.get('featured'))
        
        try:
            db.session.commit()
            flash('Blog post updated successfully!', 'success')
            return redirect(url_for('admin_blogs'))
        except Exception as e:
            db.session.rollback()
            flash('Error updating blog post. Please try again.', 'error')
    
    return render_template('admin/blog_form.html', blog=blog)

@app.route('/admin/blogs/<int:id>/delete', methods=['POST'])
@login_required
def admin_blog_delete(id):
    """Delete blog post."""
    blog = BlogPost.query.get_or_404(id)
    
    try:
        db.session.delete(blog)
        db.session.commit()
        flash('Blog post deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error deleting blog post. Please try again.', 'error')
    
    return redirect(url_for('admin_blogs'))

# Case study management routes
@app.route('/admin/case-studies')
@login_required
def admin_case_studies():
    """Admin case study management."""
    case_studies = CaseStudy.query.order_by(CaseStudy.created_at.desc()).all()
    return render_template('admin/case_studies.html', case_studies=case_studies)

@app.route('/admin/case-studies/new', methods=['GET', 'POST'])
@login_required
def admin_case_study_new():
    """Create new case study."""
    if request.method == 'POST':
        title = request.form.get('title')
        slug = request.form.get('slug')
        client_name = request.form.get('client_name')
        industry = request.form.get('industry')
        challenge = request.form.get('challenge')
        solution = request.form.get('solution')
        results = request.form.get('results')
        image_url = request.form.get('image_url')
        published = bool(request.form.get('published'))
        featured = bool(request.form.get('featured'))
        
        case_study = CaseStudy(
            title=title,
            slug=slug,
            client_name=client_name,
            industry=industry,
            challenge=challenge,
            solution=solution,
            results=results,
            image_url=image_url,
            author_id=current_user.id,
            published=published,
            featured=featured
        )
        
        try:
            db.session.add(case_study)
            db.session.commit()
            flash('Case study created successfully!', 'success')
            return redirect(url_for('admin_case_studies'))
        except Exception as e:
            db.session.rollback()
            flash('Error creating case study. Please try again.', 'error')
    
    return render_template('admin/case_study_form.html', case_study=None)

@app.route('/admin/case-studies/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def admin_case_study_edit(id):
    """Edit case study."""
    case_study = CaseStudy.query.get_or_404(id)
    
    if request.method == 'POST':
        case_study.title = request.form.get('title')
        case_study.slug = request.form.get('slug')
        case_study.client_name = request.form.get('client_name')
        case_study.industry = request.form.get('industry')
        case_study.challenge = request.form.get('challenge')
        case_study.solution = request.form.get('solution')
        case_study.results = request.form.get('results')
        case_study.image_url = request.form.get('image_url')
        case_study.published = bool(request.form.get('published'))
        case_study.featured = bool(request.form.get('featured'))
        
        try:
            db.session.commit()
            flash('Case study updated successfully!', 'success')
            return redirect(url_for('admin_case_studies'))
        except Exception as e:
            db.session.rollback()
            flash('Error updating case study. Please try again.', 'error')
    
    return render_template('admin/case_study_form.html', case_study=case_study)

@app.route('/admin/case-studies/<int:id>/delete', methods=['POST'])
@login_required
def admin_case_study_delete(id):
    """Delete case study."""
    case_study = CaseStudy.query.get_or_404(id)
    
    try:
        db.session.delete(case_study)
        db.session.commit()
        flash('Case study deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error deleting case study. Please try again.', 'error')
    
    return redirect(url_for('admin_case_studies'))

# Services management routes
@app.route('/admin/services')
@login_required
def admin_services():
    """Admin services management."""
    services = Service.query.order_by(Service.order_index).all()
    return render_template('admin/services.html', services=services)

@app.route('/admin/services/new', methods=['GET', 'POST'])
@login_required
def admin_service_new():
    """Create new service."""
    if request.method == 'POST':
        title = request.form.get('title')
        slug = request.form.get('slug')
        short_description = request.form.get('short_description')
        full_description = request.form.get('full_description')
        features = request.form.getlist('features')
        benefits = request.form.getlist('benefits')
        image_url = request.form.get('image_url')
        icon_class = request.form.get('icon_class')
        is_active = bool(request.form.get('is_active'))
        order_index = int(request.form.get('order_index', 0))
        
        service = Service(
            title=title,
            slug=slug,
            short_description=short_description,
            full_description=full_description,
            features=json.dumps(features),
            benefits=json.dumps(benefits),
            image_url=image_url,
            icon_class=icon_class,
            is_active=is_active,
            order_index=order_index
        )
        
        try:
            db.session.add(service)
            db.session.commit()
            flash('Service created successfully!', 'success')
            return redirect(url_for('admin_services'))
        except Exception as e:
            db.session.rollback()
            flash('Error creating service. Please try again.', 'error')
    
    return render_template('admin/service_form.html', service=None)

# Industries management routes
@app.route('/admin/industries')
@login_required
def admin_industries():
    """Admin industries management."""
    industries = Industry.query.order_by(Industry.order_index).all()
    return render_template('admin/industries.html', industries=industries)

@app.route('/admin/industries/new', methods=['GET', 'POST'])
@login_required
def admin_industry_new():
    """Create new industry."""
    if request.method == 'POST':
        title = request.form.get('title')
        slug = request.form.get('slug')
        short_description = request.form.get('short_description')
        full_description = request.form.get('full_description')
        challenges = request.form.getlist('challenges')
        solutions = request.form.getlist('solutions')
        image_url = request.form.get('image_url')
        icon_class = request.form.get('icon_class')
        is_active = bool(request.form.get('is_active'))
        order_index = int(request.form.get('order_index', 0))
        
        industry = Industry(
            title=title,
            slug=slug,
            short_description=short_description,
            full_description=full_description,
            challenges=json.dumps(challenges),
            solutions=json.dumps(solutions),
            image_url=image_url,
            icon_class=icon_class,
            is_active=is_active,
            order_index=order_index
        )
        
        try:
            db.session.add(industry)
            db.session.commit()
            flash('Industry created successfully!', 'success')
            return redirect(url_for('admin_industries'))
        except Exception as e:
            db.session.rollback()
            flash('Error creating industry. Please try again.', 'error')
    
    return render_template('admin/industry_form.html', industry=None)