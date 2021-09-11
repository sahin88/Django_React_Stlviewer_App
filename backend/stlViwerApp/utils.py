from mpl_toolkits import mplot3d
from matplotlib import pyplot
import base64
import io
from matplotlib.pyplot import figure
from stl import mesh
import os
import numpy as np

class MeshSolve:
    def __init__(self,mesh,*args,**kwargs):
        self.mesh=mesh
        self.result={}

    def getBoundingBox(self,mesh):
        minx = mesh.x.min()
        maxx = mesh.x.max()
        miny = mesh.y.min()
        maxy = mesh.y.max()
        minz = mesh.z.min()
        maxz = mesh.z.max()
        width = maxx - minx
        height = maxy - miny
        length = maxz - minz
        return width,height,length

    def describeVector(self,p2, p1):
        return p2-p1


    def findMeshArea(self,p1, p2,p3):
        v1 = self.describeVector(p2,p1)
        v2 = self.describeVector(p3,p1)
        v3=np.cross(v2, v1)
        res=np.linalg.norm(v3)
        return res/2


    def getSurfaceArea(self,mesh):
        total_area=0
        number_of_mesh=len(mesh.points)
        for i in range(number_of_mesh):
            total_area+= self.findMeshArea(mesh.v0[i],mesh.v1[i],mesh.v2[i])
        return total_area

    def getImagesBytes(self,mesh):
        figure = pyplot.figure(figsize=[5, 5])
        axes = mplot3d.Axes3D(figure, auto_add_to_figure=False)
        axes.add_collection3d(mplot3d.art3d.Poly3DCollection(mesh.vectors))
        figure.add_axes(axes)
        scale = mesh.points.flatten()
        axes.auto_scale_xyz(scale, scale, scale)
        buffer = io.BytesIO()
        pyplot.savefig(buffer)
        graph = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()
        return graph

    def getVolume(self,mesh):
        volume, cog, inertia = self.mesh.get_mass_properties()
        return volume

    def solve(self):

        self.result['total_area']=self.getSurfaceArea(self.mesh)
        self.result['graph']=self.getImagesBytes(self.mesh)
        self.result['width'],self.result['height'], self.result['length']=self.getBoundingBox(self.mesh)
        self.result['volume']=self.getVolume(self.mesh)
        return self.result

    
