from app.views.category import CategoryListCreateView, CategoryRetrieveUpdateDeleteView
from app.factories.interactor.category import (
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
            get_all_interactor_factory=GetAllCategoryInteractorFactory,
            create_interactor_factory=CreateCategoryInteractorFactory
        )


class CategoryRetrieveUpdateDeleteViewFactory:
    @staticmethod
    def create():
        return CategoryRetrieveUpdateDeleteView(
            retrieve_interactor_factory=RetrieveCategoryInteractorFactory,
            update_interactor_factory=UpdateCategoryInteractorFactory,
            delete_interactor_factory=DeleteCategoryInteractorFactory
        )
