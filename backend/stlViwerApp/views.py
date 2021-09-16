

from rest_framework.response import Response
from rest_framework import status
from .models import FileModel
from .serializers import  FileSerializer
from rest_framework.decorators import api_view 
from stl import mesh
import os
import numpy as np
from .utils import MeshSolve
from rest_framework.exceptions import NotFound
from django.core.exceptions import ValidationError
from rest_framework.exceptions import NotFound,APIException,ParseError


def validate_extension_function(name:str):
    """ Function, which check  file extentions
    Parameters
    ----------
    name : str
        the name of file
    Returns
    -------
    Boolean
        if file extention is allowed return True
    """
    accepted_extensions=['.stl']
    file_extension = os.path.splitext(name)[1].lower()
    if file_extension not in accepted_extensions:
        raise ParseError('File extention is not supported', code=400)
        
    return True

def get_mesh(fileUrl:str):
    """ Get file content.
    Parameters
    ----------
    fileUrl : str
        The relative path of the uploaded file.
    Returns
    -------
    Mesh
        Mesh is a network that is formed of cells and points.
    """
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(BASE_DIR,fileUrl.strip("/"))
    response=None

    try: 
        return mesh.Mesh.from_file(full_path)
    except Exception as my:
        raise NotFound('The file is not existing or too large, maximum  number of triangles of 100000000 ')
        


def delete_file(id:int):
    """ After data extraction delete the object
    Parameters
    ----------
    id : int
        The id of uploaded file
    Returns
    -------
    Boolean
        if the file is found and deleted, return true; otherweise false.
        
    """
    try:
        file=FileModel.objects.get(id=id)
        file.delete()
      
        return True
    except:
        raise NotFound('The file  not found')



@api_view(['POST'])
def file_exract(request):
    if request.method == 'POST':
        #Check the validity of  file
        validate_extension_function(request.FILES['file'].name)
  
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            mesh=get_mesh(serializer.data['file'])
            if not mesh:
                message={'detail':'Uploaded file is defect'}
                return  Response(message, status=status.HTTP_400_BAD_REQUEST)
    
            
            meshObject=MeshSolve(mesh)
            res=meshObject.solve()
           
            delete_response=delete_file(serializer.data['id'])
            if not delete_response:
                message = {'detail':str(delete_response['status'])}
                return Response(message, status=status.HTTP_404_NOT_FOUND)

            return Response(res, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

