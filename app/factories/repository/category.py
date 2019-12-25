from app.repositories.course_repo import CategoryRepo
from app.factories.entity.course import CategoryEntityFactory


class CategoryRepoFactory:
    @staticmethod
    def create():
        return CategoryRepo(
            entity=CategoryEntityFactory.create()
        )
