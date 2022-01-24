from flask import Flask
from flask_restful import Api, Resource
import json
app = Flask(__name__)
api = Api(app)

class Home(Resource) : 
    def get(self):
        home = open("home.json", "r")
        jsonHome = json.load(home)
        return {"home": jsonHome}
       

class Menu(Resource) : 
    def get(self):
        menu = open("menu.json", "r")
        jsonMenu = json.load(menu)
        return {"menu": jsonMenu}

class Blog(Resource) : 
    def get(self):
        blog = open("blog.json", "r")
        jsonBlog = json.load(blog)
        return {"blog": jsonBlog}

api.add_resource(Home, '/home/')
api.add_resource(Menu, '/menu/')
api.add_resource(Blog, '/blog/')

if __name__ == '__main__':
    app.run()
