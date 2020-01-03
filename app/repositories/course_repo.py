from app.models.course import CategoryORM, CourseORM


class CategoryRepo:
    def __init__(self, entity):
        self.entity = entity

    def convert_to_entity(self, data_orm):
        return self.entity.create(**data_orm.__dict__)

    def convert_queryset_to_list_of_entity(self, queryset):
        data = []
        for data_orm in queryset:
            data.append(self.convert_to_entity(data_orm))

        return data

    def get_by_id(self, id):
        try:
            data_orm = CategoryORM.objects.get(id=id)
            return self.convert_to_entity(data_orm)
        except CategoryORM.DoesNotExist:
            raise Exception

    def get_all(self):
        queryset = CategoryORM.objects.all()
        return self.convert_queryset_to_list_of_entity(queryset)

    def create(self, data):
        data_orm = CategoryORM.objects.create(**data.__dict__)
        return self.convert_to_entity(data_orm)

    def update(self, data):
        queryset = CategoryORM.objects.filter(pk=data.id)
        queryset.update(**data.__dict__)
        return self.convert_to_entity(queryset.first())

    def delete(self, id):
        CategoryORM.objects.filter(id=id).delete()
        return True


class CourseRepo:
    def __init__(self, entity):
        self.entity = entity

    def convert_to_entity(self, data_orm):
        return self.entity.create(**data_orm.__dict__)

    def convert_queryset_to_list_of_entity(self, queryset):
        data = []
        for data_orm in queryset:
            data.append(self.convert_to_entity(data_orm))
        return data

    def get_data_by_id(self, id):
        instance = CourseORM.objects.get(id=id)
        return self.convert_to_entity(instance)

    def create(self, data):
        instance = CourseORM.objects.create(**data.__dict__)
        return self.convert_to_entity(instance)

    def update(self, data):
        instance = CourseORM.objects.update(**data.__dict__)
        return self.convert_to_entity(instance)

    def delete(self, id):
        CourseORM.objects.filter(id=id).delete()
        return True
