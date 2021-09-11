
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from django.core.files.uploadedfile import SimpleUploadedFile
import numpy as np
from rest_framework import status


class FileTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('', include('stlViwerApp.urls')),
    ]

    def test_create_file(self):
        """
        Ensure we can create a new call object.
        """
        m=[[ 20.,   0.,   0.,   0., -20.,   0.,   0.,   0.,   0.],
        [  0., -20.,   0.,  20.,   0.,   0.,  20., -20.,   0.],
        [ 20., -20.,  20.,   0., -20.,   0.,  20., -20.,   0.],
        [  0., -20.,   0.,  20., -20.,  20.,   0., -20.,  20.],
        [ 20.,   0.,   0.,  20., -20.,  20.,  20., -20.,   0.],
        [ 20., -20.,  20.,  20.,   0.,   0.,  20.,   0.,  20.],
        [ 20., -20.,  20.,   0.,   0.,  20.,   0., -20.,  20.],
        [  0.,   0.,  20.,  20., -20.,  20.,  20.,   0.,  20.],
        [  0.,   0.,  20.,   0., -20.,   0.,   0., -20.,  20.],
        [  0., -20.,   0.,   0.,   0.,  20.,   0.,   0.,   0.],
        [  0.,   0.,  20.,  20.,   0.,   0.,   0.,   0.,   0.],
        [ 20.,   0.,   0.,   0.,   0.,  20.,  20.,   0.,  20.]]
        m=np.array(m)

        file = SimpleUploadedFile("file.stl",m.all(), content_type='multipart/form-data')
        payload = {"file": file}
        url = reverse('get_post')
        response = self.client.post(url, payload, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)