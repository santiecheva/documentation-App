from app.common.error_handling import ObjectNotFound
from flask import request
from flask_restful import  Resource

from .schemas import ManifestSchema
from .models import Manifest

manifest_schema = ManifestSchema()


class ManifestListResource(Resource):
    def get(self):
        manifests = Manifest.get_all()
        result = manifest_schema.dump(manifests, many=True)
        return result

    def post(self):
        data = request.get_json()
        user_dict = manifest_schema.load(data)
        user = Manifest(
            name=user_dict['name'],
        )
        user.save()
        response = manifest_schema.dump(user)
        return response, 201

class ManifestResource(Resource):
    def get(self, user_id):
        manifest = Manifest.get_by_id(user_id)
        if manifest is None:
            raise ObjectNotFound('No existe el usuario')
        response = manifest_schema.dump(manifest)
        return response

