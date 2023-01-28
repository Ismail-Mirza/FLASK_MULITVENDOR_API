from flask_restx import Resource, Namespace
from src.auth.authentication.permission_required import permission_required
from src.helpers import remove_space
from flask import request,jsonify
from azure.storage.blob import BlobServiceClient, ContainerClient
from os import environ
from werkzeug.datastructures import FileStorage

from flask_restx import reqparse
from src.helpers.paginate import paginate_resource
from src.helpers.responses import success_response
from src.product.helper.schema import ProductSchema
from src.product.models import Product


AZURE_CONNECTION_STRING = environ.get("CONNECTION_STRING")

api = Namespace('products', description='product related operations')
upload_parser = api.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)

@api.route('upload/')
class UploadFile(Resource):
    """ Uploads file to Azure Blob Storage """
    @api.expect(upload_parser)
    def post(self):
        args = upload_parser.parse_args()
        f = args['file']
        # f = request.files["file"]

        try:
            service_client = BlobServiceClient.from_connection_string(
                AZURE_CONNECTION_STRING)
            container_client = service_client.get_container_client(
                "flaskcontainer")
            blob_client = container_client.get_blob_client(f.filename)
            blob_client.upload_blob(f)

            return jsonify(success=True)
        except:
            return jsonify(success=False)

@api.route("")
class ProductView(Resource):
    """Resource class for product endpoint"""
    def get(self):
        """ Endpoint to get all products """

        products_schema = ProductSchema(many=True)
        data, meta = paginate_resource(Product, products_schema)

        success_response['message'] = 'Products successfully fetched'
        success_response['data'] = {
            'products': data,
            'meta': meta
        }

        return success_response, 200
    def post(self):
        pass
    def delete(self):
        pass
    def patch(self):
        pass
    def put(self):
        pass
    
