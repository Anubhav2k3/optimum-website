#!/usr/bin/env python3
"""
Script to create a default admin user and sample data.
Run this script once to set up the admin system.
"""

import json
from app import app, db
from models import Admin, Service, Industry, BlogPost, CaseStudy

def create_admin_user():
    """Create a default admin user."""
    with app.app_context():
        # Check if admin already exists
        existing_admin = Admin.query.filter_by(username='admin').first()
        if existing_admin:
            print("Admin user already exists!")
            return
        
        # Create new admin
        admin = Admin(
            username='admin',
            email='admin@optimumvalue.com'
        )
        admin.set_password('admin123')  # Change this password!
        
        db.session.add(admin)
        db.session.commit()
        print("Default admin user created!")
        print("Username: admin")
        print("Password: admin123")
        print("IMPORTANT: Change this password after first login!")

def create_sample_services():
    """Create sample services."""
    with app.app_context():
        services_data = [
            {
                'title': 'Salesforce Implementation',
                'slug': 'salesforce-implementation',
                'short_description': 'Complete Salesforce setup and configuration for your business needs.',
                'full_description': 'Our expert team provides comprehensive Salesforce implementation services, from initial planning and configuration to data migration and user training. We ensure your Salesforce instance is optimized for your specific business processes and goals.',
                'features': ['Custom Configuration', 'Data Migration', 'User Training', 'Integration Setup'],
                'benefits': ['Faster Time to Value', 'Reduced Implementation Risks', 'Expert Guidance', 'Best Practices'],
                'icon_class': 'fas fa-rocket',
                'order_index': 1
            },
            {
                'title': 'Salesforce Consulting',
                'slug': 'salesforce-consulting',
                'short_description': 'Strategic guidance to maximize your Salesforce investment.',
                'full_description': 'Our certified consultants work with you to develop strategic roadmaps, optimize existing implementations, and ensure your Salesforce platform evolves with your business needs.',
                'features': ['Strategic Planning', 'Business Analysis', 'Process Optimization', 'ROI Assessment'],
                'benefits': ['Strategic Alignment', 'Process Efficiency', 'Cost Optimization', 'Competitive Advantage'],
                'icon_class': 'fas fa-lightbulb',
                'order_index': 2
            },
            {
                'title': 'Custom Development',
                'slug': 'custom-development',
                'short_description': 'Tailored Salesforce solutions built for your unique requirements.',
                'full_description': 'From custom objects and workflows to complex integrations and Lightning components, we develop solutions that extend Salesforce capabilities to meet your specific business needs.',
                'features': ['Apex Development', 'Lightning Components', 'Custom Objects', 'Workflow Automation'],
                'benefits': ['Tailored Solutions', 'Enhanced Functionality', 'Seamless Integration', 'Scalable Architecture'],
                'icon_class': 'fas fa-code',
                'order_index': 3
            },
            {
                'title': 'Integration Services',
                'slug': 'integration-services',
                'short_description': 'Connect Salesforce with your existing systems and applications.',
                'full_description': 'We design and implement robust integration solutions that connect Salesforce with your ERP, marketing automation, financial systems, and other business-critical applications.',
                'features': ['API Integration', 'Data Synchronization', 'Real-time Updates', 'Error Handling'],
                'benefits': ['Data Consistency', 'Process Automation', 'Reduced Manual Work', 'Real-time Insights'],
                'icon_class': 'fas fa-plug',
                'order_index': 4
            },
            {
                'title': 'Support & Maintenance',
                'slug': 'support-maintenance',
                'short_description': 'Ongoing support to keep your Salesforce running smoothly.',
                'full_description': 'Our support team provides ongoing maintenance, troubleshooting, and optimization services to ensure your Salesforce platform continues to deliver value as your business grows.',
                'features': ['24/7 Support', 'Regular Health Checks', 'Performance Optimization', 'Security Updates'],
                'benefits': ['System Reliability', 'Performance Optimization', 'Security Assurance', 'Peace of Mind'],
                'icon_class': 'fas fa-tools',
                'order_index': 5
            },
            {
                'title': 'Training & Adoption',
                'slug': 'training-adoption',
                'short_description': 'Comprehensive training programs to maximize user adoption.',
                'full_description': 'We provide tailored training programs, change management support, and adoption strategies to ensure your team gets the most out of your Salesforce investment.',
                'features': ['User Training', 'Admin Training', 'Change Management', 'Adoption Strategies'],
                'benefits': ['Higher User Adoption', 'Increased Productivity', 'Better ROI', 'Reduced Support Tickets'],
                'icon_class': 'fas fa-graduation-cap',
                'order_index': 6
            }
        ]
        
        for service_data in services_data:
            existing = Service.query.filter_by(slug=service_data['slug']).first()
            if not existing:
                service = Service(
                    title=service_data['title'],
                    slug=service_data['slug'],
                    short_description=service_data['short_description'],
                    full_description=service_data['full_description'],
                    features=json.dumps(service_data['features']),
                    benefits=json.dumps(service_data['benefits']),
                    icon_class=service_data['icon_class'],
                    order_index=service_data['order_index'],
                    is_active=True
                )
                db.session.add(service)
        
        db.session.commit()
        print(f"Created {len(services_data)} sample services!")

def create_sample_industries():
    """Create sample industries."""
    with app.app_context():
        industries_data = [
            {
                'title': 'Financial Services',
                'slug': 'financial-services',
                'short_description': 'Comprehensive Salesforce solutions for banks, credit unions, and financial institutions.',
                'full_description': 'We help financial services organizations transform their customer experience, streamline operations, and ensure regulatory compliance through tailored Salesforce solutions.',
                'challenges': ['Regulatory Compliance', 'Customer Experience', 'Data Security', 'Digital Transformation'],
                'solutions': ['Financial Services Cloud', 'Customer 360', 'Einstein Analytics', 'Community Cloud'],
                'icon_class': 'fas fa-university',
                'order_index': 1
            },
            {
                'title': 'Healthcare',
                'slug': 'healthcare',
                'short_description': 'Patient-centered Salesforce solutions for healthcare providers and organizations.',
                'full_description': 'Our healthcare expertise helps providers improve patient engagement, streamline care coordination, and enhance operational efficiency while maintaining HIPAA compliance.',
                'challenges': ['Patient Engagement', 'Care Coordination', 'HIPAA Compliance', 'Operational Efficiency'],
                'solutions': ['Health Cloud', 'Patient Management', 'Care Coordination', 'Analytics'],
                'icon_class': 'fas fa-heartbeat',
                'order_index': 2
            },
            {
                'title': 'Manufacturing',
                'slug': 'manufacturing',
                'short_description': 'End-to-end Salesforce solutions for manufacturing companies and distributors.',
                'full_description': 'We help manufacturers optimize their sales processes, improve partner relationships, and gain visibility into their complex supply chains through Salesforce Manufacturing Cloud.',
                'challenges': ['Complex Sales Cycles', 'Partner Management', 'Supply Chain Visibility', 'Customer Service'],
                'solutions': ['Manufacturing Cloud', 'Partner Portal', 'CPQ', 'Service Cloud'],
                'icon_class': 'fas fa-industry',
                'order_index': 3
            },
            {
                'title': 'Utilities',
                'slug': 'utilities',
                'short_description': 'Specialized Salesforce solutions for utility companies and energy providers.',
                'full_description': 'Our utility expertise helps energy companies improve customer service, manage field operations, and adapt to the evolving energy landscape with modern digital solutions.',
                'challenges': ['Customer Service', 'Field Service Management', 'Regulatory Changes', 'Grid Modernization'],
                'solutions': ['Energy & Utilities Cloud', 'Field Service Lightning', 'Customer Portal', 'IoT Integration'],
                'icon_class': 'fas fa-bolt',
                'order_index': 4
            }
        ]
        
        for industry_data in industries_data:
            existing = Industry.query.filter_by(slug=industry_data['slug']).first()
            if not existing:
                industry = Industry(
                    title=industry_data['title'],
                    slug=industry_data['slug'],
                    short_description=industry_data['short_description'],
                    full_description=industry_data['full_description'],
                    challenges=json.dumps(industry_data['challenges']),
                    solutions=json.dumps(industry_data['solutions']),
                    icon_class=industry_data['icon_class'],
                    order_index=industry_data['order_index'],
                    is_active=True
                )
                db.session.add(industry)
        
        db.session.commit()
        print(f"Created {len(industries_data)} sample industries!")

if __name__ == '__main__':
    print("Setting up admin system...")
    create_admin_user()
    create_sample_services()
    create_sample_industries()
    print("Setup complete!")