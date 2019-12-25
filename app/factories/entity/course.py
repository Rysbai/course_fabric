from app.entities.course import Category, Course


class CategoryEntity:
    @staticmethod
    def create(id, name):
        Category(
            id=id,
            name=name
        )


class CourseEntity:
    @staticmethod
    def create(id, category, name):
        Course(
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
