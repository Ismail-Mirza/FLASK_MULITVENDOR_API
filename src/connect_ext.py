from .extension import db,bcrypt,jwt,migrate
from .admin.routes import admin
from .admin.register_model import register_model



def connect_ext(app)->None:
    db.init_app(app)
    bcrypt.init_app(app)
    admin.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app,db)
 
    register_model(admin)
    
    
