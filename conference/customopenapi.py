from drf_yasg.generators import OpenAPISchemaGenerator


class CustomOpenAPISchemaGenerator(OpenAPISchemaGenerator):
  def get_schema(self, request=None, public=False):
    """Generate a :class:`.Swagger` object with custom tags"""

    swagger = super().get_schema(request, public)
    swagger.tags = [
        {
            "name": "author",
            "description": "Набор методов для работы с данными о авторах тезисов"
        },
        {
            "name": "section-number",
            "description": "Набор методов для работы с данными о секциях"
        },
        {
            "name": "thesis",
            "description": "Набор методов для работы с данными о тезисах"
        },
        {
            "name": "scientific-director",
            "description": "Набор методов для работы с данными о научных руководителях"
        },



    ]

    return swagger