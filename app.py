from app import create_app
from app.models import db
from config import DevelopmentConfig

# app = create_app(config="config.DevelopmentConfig")
app = create_app(config=DevelopmentConfig)  

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)


