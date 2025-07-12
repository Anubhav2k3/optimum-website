@@ .. @@
 @app.route('/admin/services/<int:id>/edit', methods=['GET', 'POST'])
 @login_required
 def admin_service_edit(id):
     """Edit service."""
     service = Service.query.get_or_404(id)
     
     if request.method == 'POST':
         service.title = request.form.get('title')
         service.slug = request.form.get('slug')
         service.short_description = request.form.get('short_description')
         service.full_description = request.form.get('full_description')
         features = request.form.getlist('features')
         benefits = request.form.getlist('benefits')
         service.features = json.dumps([f for f in features if f.strip()])
         service.benefits = json.dumps([b for b in benefits if b.strip()])
         service.image_url = request.form.get('image_url')
         service.icon_class = request.form.get('icon_class')
         service.is_active = bool(request.form.get('is_active'))
         service.order_index = int(request.form.get('order_index', 0))
         
         try:
             db.session.commit()
             flash('Service updated successfully!', 'success')
             return redirect(url_for('admin_services'))
         except Exception as e:
             db.session.rollback()
             flash('Error updating service. Please try again.', 'error')
     
     return render_template('admin/service_form.html', service=service)

+@app.route('/admin/services/<int:id>/delete', methods=['POST'])
+@login_required
+def admin_service_delete(id):
+    """Delete service."""
+    service = Service.query.get_or_404(id)
+    
+    try:
+        db.session.delete(service)
+        db.session.commit()
+        flash('Service deleted successfully!', 'success')
+    except Exception as e:
+        db.session.rollback()
+        flash('Error deleting service. Please try again.', 'error')
+    
+    return redirect(url_for('admin_services'))

+@app.route('/admin/services/<int:id>/edit', methods=['GET', 'POST'])
+@login_required
+def admin_service_edit(id):
+    """Edit service."""
+    service = Service.query.get_or_404(id)
+    
+    if request.method == 'POST':
+        service.title = request.form.get('title')
+        service.slug = request.form.get('slug')
+        service.short_description = request.form.get('short_description')
+        service.full_description = request.form.get('full_description')
+        features = request.form.getlist('features')
+        benefits = request.form.getlist('benefits')
+        service.features = json.dumps([f for f in features if f.strip()])
+        service.benefits = json.dumps([b for b in benefits if b.strip()])
+        service.image_url = request.form.get('image_url')
+        service.icon_class = request.form.get('icon_class')
+        service.is_active = bool(request.form.get('is_active'))
+        service.order_index = int(request.form.get('order_index', 0))
+        
+        try:
+            db.session.commit()
+            flash('Service updated successfully!', 'success')
+            return redirect(url_for('admin_services'))
+        except Exception as e:
+            db.session.rollback()
+            flash('Error updating service. Please try again.', 'error')
+    
+    return render_template('admin/service_form.html', service=service)

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
             challenges=json.dumps([c for c in challenges if c.strip()]),
             solutions=json.dumps([s for s in solutions if s.strip()]),
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

+@app.route('/admin/industries/<int:id>/edit', methods=['GET', 'POST'])
+@login_required
+def admin_industry_edit(id):
+    """Edit industry."""
+    industry = Industry.query.get_or_404(id)
+    
+    if request.method == 'POST':
+        industry.title = request.form.get('title')
+        industry.slug = request.form.get('slug')
+        industry.short_description = request.form.get('short_description')
+        industry.full_description = request.form.get('full_description')
+        challenges = request.form.getlist('challenges')
+        solutions = request.form.getlist('solutions')
+        industry.challenges = json.dumps([c for c in challenges if c.strip()])
+        industry.solutions = json.dumps([s for s in solutions if s.strip()])
+        industry.image_url = request.form.get('image_url')
+        industry.icon_class = request.form.get('icon_class')
+        industry.is_active = bool(request.form.get('is_active'))
+        industry.order_index = int(request.form.get('order_index', 0))
+        
+        try:
+            db.session.commit()
+            flash('Industry updated successfully!', 'success')
+            return redirect(url_for('admin_industries'))
+        except Exception as e:
+            db.session.rollback()
+            flash('Error updating industry. Please try again.', 'error')
+    
+    return render_template('admin/industry_form.html', industry=industry)

+@app.route('/admin/industries/<int:id>/delete', methods=['POST'])
+@login_required
+def admin_industry_delete(id):
+    """Delete industry."""
+    industry = Industry.query.get_or_404(id)
+    
+    try:
+        db.session.delete(industry)
+        db.session.commit()
+        flash('Industry deleted successfully!', 'success')
+    except Exception as e:
+        db.session.rollback()
+        flash('Error deleting industry. Please try again.', 'error')
+    
+    return redirect(url_for('admin_industries'))