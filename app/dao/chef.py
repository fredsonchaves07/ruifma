from datetime import datetime
from app.db import db
from app.db.models import File, Chef

def all_chef():
    sql = db.select([
        db.text(
            """
               c."ID" as id , 
               f."NAME" as avatar, 
               c."NAME" as name 
               FROM "FCHEF" c

               INNER JOIN "FFILES" f
               ON f."ID" = c."FILEID" 
            """
        )
    ])

    return db.engine.execute(sql).fetchall()

def create_chef(name, file_id, ):
    chef = Chef(name=name, file_id=file_id)
    db.session.add(chef)
    db.session.commit()
    
    return chef.id

def find_chef(chef_id):
    chef = Chef.query.filter_by(id=chef_id).first()
    
    return chef

def update_chef(chef_id, chef_name):
    chef = Chef.query.get(chef_id)

    if chef_name != chef.name:
        chef.name = chef_name
        chef.modified_at = datetime.utcnow()
        db.session.add(chef)
        db.session.commit()   
    
    return 

def delete_chef(chef):
    db.session.delete(chef)
    db.session.commit()
    
    return
