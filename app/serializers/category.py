

class CategorySerializer:

    @staticmethod
    def serialize_entity(category_entity):
        return {
            "id": category_entity.id,
            "name": category_entity.name
        }

    @staticmethod
    def serialize_many(queryset):
        data = []
        for instance in queryset:
            data.append(
                CategorySerializer.serialize_entity(instance)
            )
        return data
