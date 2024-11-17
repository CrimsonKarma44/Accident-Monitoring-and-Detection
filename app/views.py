from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .utils.model_runner import ModelChecker
from rest_framework.response import Response
from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from .utils.store import JsonHandler
from rest_framework import status
import datetime
from django.core.files.base import ContentFile

# Create your views here.
@method_decorator(csrf_exempt, name="dispatch")
class UploadView(APIView):
   def get(self, request):
      return HttpResponse("Welcome")
   
   def post(self, request):
      if not request.body:
         return Response({"error": "No image provided."}, status=status.HTTP_400_BAD_REQUEST)

        # Save the image
      image = request.body
 
      # print("type:", type(image))
      try:
         with open('static/img/received_image.jpg', 'wb') as f: 
            f.write(image) 
            # return Response(status=status.HTTP_200_OK)

         # checks 
         res = ModelChecker("static/img/received_image.jpg")
         if res == {}:
            print("not an event to be found!")
            raise Exception
         
         content = JsonHandler.load()
         
         res["coordinate"] = str(request.POST.get("coordinates")).lower()
         res["region"] = str(request.POST.get("region")).lower()
         res["id"] = content[-1]["id"] + 1 if len(content) != 0 else 0
         
         JsonHandler.save(res)
         
         context = {
            "message": "successfully",
            "modelRes": res,
            "status": status.HTTP_201_CREATED
         }
      except:
         context = {
            "message": "unsuccessfully",
            "status": status.HTTP_204_NO_CONTENT
         }

      return Response(context, status=status.HTTP_201_CREATED)


from typing import TypedDict


class Structure(TypedDict):
   id:int
   platenumber:str
   temperature:str
   flamestatus:bool
   type:str
   Region:str
   confidence:str
   coordinate:str
   datetime:str

@method_decorator(csrf_exempt, name="dispatch")
class RegularUploadView(APIView):
   def post(self, request):
      content = JsonHandler.load()

      # res : Structure = {}
      content[-1]["platenumber"] = request.POST.get("platenumber")
      content[-1]["temperature"] = str(request.POST.get("temperature")).lower()
      content[-1]["flamestatus"] = str(request.POST.get("flamestatus"))
      content[-1]["coordinate"] = str(request.POST.get("coordinate")).lower()
      content[-1]["datetime"] = str(datetime.datetime.now())

      JsonHandler.save2(content[-1])
      
      return Response(str(status.HTTP_201_CREATED), status=status.HTTP_201_CREATED)


@method_decorator(csrf_exempt, name="dispatch")
class RetrieveView(APIView):
   def get(self, request, pk):
      pk = int(pk)
      content = JsonHandler.load()
      if pk > len(content) or pk == 0:
         pk = len(content)
      return Response([content[-i-1] for i in range(pk)], status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name="dispatch")
class RetrieveRegionView(APIView):
   def get(self, request, pk):
      content = JsonHandler.load()
      newContent = []
      for i in content:
         if i["region"] == str(pk).lower():
            newContent.append(i)

      return Response(newContent, status=status.HTTP_200_OK)
   
