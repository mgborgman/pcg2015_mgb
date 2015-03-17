# MVC: A GENERIC ARCHITECTURE FOR MAKING APPS THAT DISPLAY DATA

# MODEL: A LIST OF OBJECTS. TYPICALLY FROM A DATABASE
class Model(object):
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields
        self.objects = {}

    def create(self, item):
        self.objects.append(item)


# VIEW: A TEMPLATE FOR A PAGE OR PAGE FRAGMENT
class View(object):
    def __init__(self, template, model):
        self.template = template
        self.model = model

    def render(self):
        output = ""
        for item in self.model.objects:
            item_template = self.template
            for field in self.model.fields:
                if item.has_key(field):
                    item_template = item_template.replace("{{" + field + "}}", item[field])
            output += item_template
        return output


# CONTROLLER: Routes messages
class Controller(object):
    def __init__(self):
        self.routes = {}

    def route(self, path):
        return self.routes[path].render()


# CONTAINS THE SINGLE CONTROLLER AND ALL MODEL AND VIEW INSTANCES
class Application():
    def __init__(self):
        self.models = {}
        self.views = {}
        self.controller = Controller()

# CREATE AN APPLICATION INSTANCE
app = Application()

# define models (
app.models["user"] = Model("user", ["name", "score", "age"])
app.models["game"] = Model("game", ["game_name", "description"])
app.models["stock"] = Model("product", ["id", "name", "price"])
app.models["directory"] = Model("directory", ["name", "suite"])

# load model objects form database tables
app.models["user"].objects = [
    {"name": "Bob", "score": "9", "age": "25"},
    {"name": "Carol", "score": "11", "age": "21"},
    {"name": "Ted", "score": "15", "age": "32"},
    {"name": "Alice", "score": "13", "age": "23"}]

app.models["stock"].objects = [
    {"id": "111", "name": "Laptop", "price": "799.99"},
    {"id": "222", "name": "TV", "price": "1299.99"},
    {"id": "333", "name": "Tablet", "price": "399.99"},
    {"id": "444", "name": "Printer", "price": "99.99"}]

app.models["directory"].objects = [
    {"name": "Matt Borgman", "suite": "111"},
    {"name": "Ashley Althuisius", "suite": "222"},
    {"name": "Kevin Auchenbach", "suite": "333"},
    {"name": "Andrew Fiorentino", "suite": "444"},
]

template = '\nHello <em>{{name}}</em>, your age is <strong>{{age}}</strong>and you score is {{score}}.<br>\n'
template_results = '\nHello <em>{{name}}</em>, your rank is <strong>{{score}}</strong>.<br>\n'
template_store = '\nThe {{name}} you are looking at is ${{price}}, you can also find it online with id# {{id}}\n'
template_directory =
view = View(template, app.models["user"])
view_results = View(template_results, app.models["user"])
view_store = View(template_store, app.models["stock"])
view_directory = View(template_directory, app.models["directory"])
app.controller.routes = {
    "/scores/": view,
    "/results/": view_results,
    "/store/": view_store,
    "/directory/": view_directory
}

# request_path = "/scores/"
# print(app.controller.route(request_path))
# request_path = "/results/"
# print(app.controller.route(request_path))
# request_path = "/store/"
# print(app.controller.route(request_path))
# print(app.models["stock"].name)
request_path = "/directory/"
print(app.controller.route(request_path))