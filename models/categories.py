import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Categories(db.Model):
    __tablename__ = "Categories"

    category_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category_name = db.Column(db.String(), unique=True, nullable=False)


    def __init__(self, category_name):
        self.category_name = category_name

    
    def get_new_category():
        return Categories("")
    
    
class CategoriesSchema(ma.Schema):
    class Meta:
        fields = ["category_id", "category_name"]

category_schema = CategoriesSchema()
categories_schema = CategoriesSchema(many=True)