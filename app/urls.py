from django.urls import path
from app.view_wrapper import ViewWrapper
from app.factories.view.category import (
    CategoryListCreateViewFactory,
    CategoryRetrieveUpdateDeleteViewFactory
)

urlpatterns = [
    path('courses', ViewWrapper.as_view(view_factory=CategoryListCreateViewFactory)),
    path('courses/<int:pk>',  ViewWrapper.as_view(view_factory=CategoryRetrieveUpdateDeleteViewFactory)),
    path('categories',  ViewWrapper.as_view(view_factory=CategoryListCreateViewFactory)),
    path('categories/<int:pk>',  ViewWrapper.as_view(view_factory=CategoryListCreateViewFactory))
]
