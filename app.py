import responder
from marshmallow import Schema, fields


description = "This is a sample server for a pet store."

api = responder.API(
        title="web service",
        version="1.0",
        openapi="3.0.2",
        description=description,
        )


@api.schema("Pet")
class PetSchema(Schema):
    name = fields.Str()


@api.route("/")
def route(req, resp):
    """A cute furry animal endpoint
    ---
    get:
        description: Get a random pet
        responses:
            200:
                description: A pet to be returned
                content:
                    application/json:
                        schema:
                            $ref: '#/components/schemas/Pet'
    """
    resp.media = PetSchema().dump({"name": "little orange"})


if __name__ == '__main__':
    api.run()
    # curl http://127.0.0.1:5042/schema.yml -> swagger
    # curl http://127.0.0.1:5042/ -> {"name": "little orange"}
