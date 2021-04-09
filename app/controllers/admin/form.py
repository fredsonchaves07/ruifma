from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, FileField, MultipleFileField, SelectField, TextAreaField, FieldList, FormField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField

class RegistrationChef(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    avatar = FileField('avatar')

    
class RegistrationRecipe(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    chef = SelectField('chef', choices=[("", "Selecione um chef")], validators=[DataRequired()])
    date = DateField('date', format='%Y-%m-%d')
    ingredients = FieldList(StringField('ingredients[]', validators=[DataRequired()]))
    preparations = TextAreaField('adicional_information')
    adicional_information = TextAreaField('adicional_information')
    recipe_img = MultipleFileField('recipe_img')
    