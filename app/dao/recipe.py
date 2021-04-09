from datetime import datetime
from app.db import db
from app.db.models import File, Recipe, RecipeFile


def all_recipes():
    recipes = Recipe.query.all()

    return recipes


def create_recipe(name, recipe_date, chef_id, ingredients, preparations, adicional_information):
    recipe = Recipe(name=name,
                    date=recipe_date,
                    chef_id=chef_id, 
                    ingredients=ingredients,
                    preparations=preparations,
                    adicional_information=adicional_information)
    db.session.add(recipe)
    db.session.commit()
    
    return recipe.id


def create_recipe_file(recipe_id, file_id):
    recipe_file = RecipeFile(recipe_id=recipe_id, file_id=file_id)
    db.session.add(recipe_file)
    db.session.commit()


def remove_recipe_file(recipe_id, file_id):
    query = RecipeFile.query.filter(RecipeFile.recipe_id == recipe_id).\
        filter(RecipeFile.file_id==file_id)

    recipe = query.all()
    
    db.session.delete(recipe[0])
    db.session.commit()


def find_recipe(recipe_id):
    recipe = Recipe.query.filter_by(id=recipe_id).first()
    
    return recipe


def list_recipes_chef(id):
    list_recipes_chef = Recipe.query.filter_by(chef_id=id).all()
    
    return list_recipes_chef


def update_recipe(recipe_id, name, date, chef_id, ingredients, preparations, adicional_information):
    recipe = Recipe.query.get(recipe_id)

    if date != recipe.date or name != recipe.name or chef_id != recipe.chef_id or ingredients != recipe.ingredients or preparations != recipe.preparations or adicional_information != recipe.adicional_information:
        recipe.name = name
        recipe.date = date
        recipe.chef_id = chef_id
        recipe.ingredients = ingredients
        recipe.preparations = preparations
        recipe.adicional_information = adicional_information
        recipe.modified_at = datetime.utcnow()
        db.session.add(recipe)
        db.session.commit()   
    
    return 


def find_recipe_file(recipe_id):
    recipe_file = RecipeFile.query.filter_by(recipe_id=recipe_id).all()

    return recipe_file


def delete_recipe(recipe):
    db.session.delete(recipe)
    db.session.commit()
    
    return


def filter_recipe(data_filter):
    search = '%{}%'.format(data_filter)
    
    recipes = Recipe.query.filter(
        Recipe.name.like(search)
    ).all()

    return recipes