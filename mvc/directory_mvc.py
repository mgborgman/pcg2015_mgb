# MVC: A GENERIC ARCHITECTURE FOR MAKING APPS THAT DISPLAY DATA

# MODEL: A LIST OF OBJECTS. TYPICALLY FROM A DATABASE
class Model(object):
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields
        self.objects = {}

    # def create(self, item):
    #     self.objects.append(item)


# VIEW: A TEMPLATE FOR A PAGE OR PAGE FRAGMENT
class View(object):
    def __init__(self, template, model):
        self.template = template
        self.model = model

    def render(self):
        output = ""
        for letter in self.model.objects:
            #print header and letter
            output += letter + "\n"
            letter_list = self.model.objects[letter]
            for item in letter_list:
                item_template = self.template
                for field in self.model.fields:
                    if item.has_key(field):
                        item_template = item_template.replace("{{" + field + "}}", item[field])
                output += item_template + "\n"
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

app.models["directory"] = Model("directory", ["name", "suite"])

# load model objects form database tables
app.models["directory"].objects = {
    "A": [{"name": "Ashley Althuisius", "suite": "222"}, {"name": "Andrew Fiorentino", "suite": "444"}],
    "M": [{"name": "Matt Borgman", "suite": "111"}]
}

template_directory = "Name: {{name}}, Suite: {{suite}}"

view_directory = View(template_directory, app.models["directory"])
app.controller.routes = {
    "/directory/": view_directory
}




request_path = "/directory/"
print(app.controller.route(request_path))