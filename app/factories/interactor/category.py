from app.interactors.category import (
GetAllCategoryInteractor,
CreateCategoryInteractor,
RetrieveCategoryInteractor,
UpdateCategoryInteractor,
DeleteCategoryInteractor
)
from app.factories.repository.category import CategoryRepoFactory


class GetAllCategoryInteractorFactory:
    @staticmethod
    def create():
        return GetAllCategoryInteractor(
            category_repo=CategoryRepoFactory.create()
        )


class CreateCategoryInteractorFactory:
    @staticmethod
    def create():
        return CreateCategoryInteractor(
            category_repo=CategoryRepoFactory.create()
        )


class RetrieveCategoryInteractorFactory:
    @staticmethod
    def create():
        return RetrieveCategoryInteractor(
            category_repo=CategoryRepoFactory.create()
        )


class UpdateCategoryInteractorFactory:
    @staticmethod
    def create():
        return UpdateCategoryInteractor(
            category_repo=CategoryRepoFactory.create()
        )


class DeleteCategoryInteractorFactory:
    @staticmethod
    def create():
        return DeleteCategoryInteractor(
            category_repo=CategoryRepoFactory.create()
        )
