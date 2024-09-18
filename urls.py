from DisciplinasApp.provedor import disciplinas_ws
from DisciplinasApp.views import index,modulos
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('disciplinasws/', disciplinas_ws),
    path('web/', index),
    path('web/modulo/', modulos)
]

class DisciplinasRepo:
    def __init__(self):
        self.repo = {
            "Webservices":
                ["Conceitos de Web services",
                 "Utilizando SOAP em Java",
                 "Utilizando REST em Java"],
            "Programação Servidor com Java":
                ["Webserver Tomcat",
                 "App Server GlassFish",
                 "Servlet e JSP"],
            "JPA e JEE":
                ["Tecnologia JPA",
                 "Enterprise Java Beans",
                 "Arquitetura MVC"]                                
            }
    def getTemas(self):
        return self.repo.keys()
    def getModulosTema(self, tema):
        return self.repo[tema]
