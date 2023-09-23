from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()
from sqlalchemy.schema import CheckConstraint

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable = False)
    @validates("name")
    def validate_name(self,key,value):
        if value == "":
            raise ValueError("failed name")
        return value


    phone_number = db.Column(db.String, CheckConstraint("LENGTH(phone_number) = 10),"))
    @validates("phone_number")
    def validate_phone_number(self,key,value):
        if len(value) != 10:
            raise ValueError("invalid phoen number")
        return value
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    
    @validates("title")
    def validate_title(self,key,value):
        if value == "":
            raise ValueError("you need title")
        else:
            value not in("Won't Believe","Secret","Top","Guess")
            raise ValueError("agian invalid input")
    
    
    def second_validator(self,key,value):
        if value not in("Won't Believe","Secret","Top","Guess"):
            raise ValueError("again invalid title input")
        return value
            
    content = db.Column(db.String)  
    @validates("content")
    def validate_content(self,key,value):
        if len(value) <250:
            raise ValueError("invalid content")
        return value
    summary = db.Column(db.String)
    category = db.Column(db.String)
    @validates("category")
    def validate_category(self,key,value):
        if value not in ("Fiction", "Non-Fiction"):
            raise ValueError("invalid category selection")
        return value
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    @validates("summary")
    def validate_summery(self,key,value):
        if len(value) >= 250:
            raise ValueError("invalid summery input")
        return value
   
    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
