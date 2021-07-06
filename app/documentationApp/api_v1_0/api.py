from flask import  Blueprint
from flask_restful import Api

from .users.resources import UserListResource, UserResource
from .docManifest.resources import ManifestListResource, ManifestResource

docapp_v1_0_bp = Blueprint('docapp_v1_0_bp', __name__)

api = Api(docapp_v1_0_bp)

#Endpoints Usuarios
api.add_resource(UserListResource, '/api/v1.0/users/', endpoint='user_list_resource')
api.add_resource(UserResource, '/api/v1.0/users/<int:user_id>', endpoint='user_resource')


#Endpoints Manifest
api.add_resource(ManifestListResource, '/api/v1.0/manifest/', endpoint='manifest_list_resource')
api.add_resource(ManifestResource, '/api/v1.0/manifest/<int:manifest_id>', endpoint='manifest_resource')