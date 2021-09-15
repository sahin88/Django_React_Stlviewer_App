
from rest_framework.response import Response
from rest_framework import status
from .models import FileModel
from .serializers import  FileSerializer
from rest_framework.decorators import api_view 
from stl import mesh
import os
import numpy as np
from .utils import MeshSolve


def get_mesh(fileUrl):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(BASE_DIR,fileUrl.strip("/"))
    return mesh.Mesh.from_file(full_path)

def delete_file(id):
    res={}
    try:
        file=FileModel.objects.get(id=id)
        file.delete()
        res['response']=True
        return res
    except  Exception as error:
        res['response']=False
        res['message']=error
        return res





@api_view(['GET', 'POST'])
def file_list(request):
    if request.method == 'POST':

        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            mesh=get_mesh(serializer.data['file'])
         
            meshObject=MeshSolve(mesh)
            res=meshObject.solve()
            delete_response=delete_file(serializer.data['id'])




            if delete_response['response']==True:
                pass
            else:
               
                content = {'error':str(delete_response['message'])}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)


           
           

            return Response(res, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



        
        
