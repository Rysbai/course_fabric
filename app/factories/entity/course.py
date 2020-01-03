from app.entities.course import Category, Course


class CategoryEntity:
    @staticmethod
    def create(name, id=None, *args, **kwargs):
        return Category(
            id=id,
            name=name
        )


class CourseEntity:
    @staticmethod
    def create(category, name, id=None, *args, **kwargs):
        return Course(
            id=id,
            category=category,
            name=name
        )


class CourseEntityFactory:
    @staticmethod
    def create():
        return CourseEntity


class CategoryEntityFactory:
    @staticmethod
    def create():
        return CategoryEntity
