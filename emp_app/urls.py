from . import views
from django.urls import path

urlpatterns = [
    path("",views.index, name="Index"),
    path("all_emp",views.all_emp, name="all_emp"),
    path("add_emp",views.add_emp, name="add_emp"),
    path("remove_emp",views.remove_emp, name="remove_emp"),
    path("remove_emp/<int:id>",views.remove_emp, name="Remove Employee With ID!"),
    path("filter_emp",views.filter_emp, name="filter_emp"),

]
