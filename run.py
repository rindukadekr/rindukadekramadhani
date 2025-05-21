import os
from app import create_app, db
from app.models import Registrasi

app = create_app()

UPLOAD_FOLDER = 'c:/Users/user/Documents/ppdb sederhana/uploads'

# Ensure the uploads directory is created before the application starts
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Hanya create_all, jangan drop_all

        # Create the admin user
        if not Registrasi.query.filter_by(username='admin').first():
            admin_user = Registrasi(username='admin', is_admin=True)  # Set is_admin=True
            admin_user.set_password('admin123')  # Set a default password
            db.session.add(admin_user)
            db.session.commit()

    app.run(debug=True)