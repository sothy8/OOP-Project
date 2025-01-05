from django.urls import path
from product import views

#create path that urls in project will noticed
urlpatterns = [
    path(route="", view=views.index,name="index"),   # 'index' function in view(app)
    path(route="about/", view=views.about,name="about"),  #'route' : address to access your function"about"
    path(route="read/", view=views.read,name="read"),
    path(route="create/", view=views.create,name="create") , #connect create with urls
    path(route="update/<int:product_id>", view=views.update,name="update"),  #connect update with urls
                        #it mean: when we click on update in row 1(id) , it will read the whole row1 and allowed us to update
    path(route="delete/<int:product_id>", view=views.delete,name="delete") #it similars to update
]
