
from django.urls import reverse, resolve
from django.core.files.uploadedfile import SimpleUploadedFile
import numpy as np
from rest_framework import status
from django.test import SimpleTestCase, TestCase
from .models import FileModel
from .views import file_exract
import os
from stl import mesh
from .serializers import  FileSerializer



class TestUrls(SimpleTestCase):
    def test_file_url(self):
        url = reverse('get_post')
        self.assertEqual(resolve(url).func, file_exract)
        
class TestViews(TestCase):
    file_extension_error='File extention is not supported'
    file_contents_error='Uploaded file is defect'
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    content_type='multipart/form-data; boundary=----WebKitFormBoundaryyrV7KO0BoCBuDbTL'
    url = reverse('get_post')

    def create_simple_upload_file(self, absolute_path):
        full_path=os.path.join(self.base_dir,absolute_path)
        willbe_uploaded_file=SimpleUploadedFile(name=absolute_path, content=open(full_path, 'rb').read(), content_type=self.content_type)
        response=self.client.post(self.url, {'file':willbe_uploaded_file })
        return response

    
    def test_mesh_function_with_file_its_ciontent_is_list(self): 
        absolute_path='testfiles/test_array.stl'
        response=self.create_simple_upload_file(absolute_path)
  
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_file_check_file_extension(self):
        absolute_path='testfiles/file.txt'
        response=self.create_simple_upload_file(absolute_path)
        self.assertEqual(response.data['detail'], self.file_extension_error)
    
    def test_file_check_mesh(self):
        absolute_path='testfiles/file.stl'
        response=self.create_simple_upload_file(absolute_path)
        self.assertEqual(response.data['detail'], self.file_contents_error)

    def test_file_check_mesh_status(self):
        absolute_path='testfiles/file.stl'
        response=self.create_simple_upload_file(absolute_path)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_file_check_file_name_double_dot(self):
        absolute_path='testfiles/test.txt.stl'
        response=self.create_simple_upload_file(absolute_path)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_file_check_file_created_deleted(self):
        absolute_path='testfiles/octova.stl'
        response=self.create_simple_upload_file(absolute_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestModel(TestCase):

    def setUp(self):
        self.myfile=FileModel.objects.create(file='trail.stl')
    def test_model_create(self):
        self.assertEqual(self.myfile.file.name,'trail.stl')
    
     
class TestSerilaizer(TestCase):

    def setUp(self):

        self.serializer_data = {
            'file': 'trial.stl',
            'id': 55
        }

        self.file = FileModel.objects.create(file='trail.stl')
        self.serializer = FileSerializer(instance=self.file)


    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(['file', 'id']))


