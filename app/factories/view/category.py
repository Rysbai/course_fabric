from app.views.category import CategoryListCreateView, CategoryRetrieveUpdateDeleteView
from app.factories.interactor import (
    GetAllCategoryInteractorFactory,
    CreateCategoryInteractorFactory,
    RetrieveCategoryInteractorFactory,
    UpdateCategoryInteractorFactory,
    DeleteCategoryInteractorFactory
)


class CategoryListCreateViewFactory:
    @staticmethod
    def create():
        return CategoryListCreateView(
            get_all_interactor_factory=GetAllCategoryInteractorFactory.create(),
            create_interactor_factory=CreateCategoryInteractorFactory.create()
        )


class CategoryRetrieveUpdateDeleteViewFactory:
    @staticmethod
    def create():
        return CategoryRetrieveUpdateDeleteView(
            retrieve_interactor_factory=RetrieveCategoryInteractorFactory.create(),
            update_interactor_factory=UpdateCategoryInteractorFactory.create(),
            delete_interactor_factory=DeleteCategoryInteractorFactory.create()
        )
