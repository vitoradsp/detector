from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response
from aapi.models import Recebedor
from aapi.serializers import RecebedorSerializer
from PIL import Image
import numpy as np
import cv2
from io import BytesIO
from django.middleware import csrf
from django.http import HttpResponse

class RecebedorViewSet(viewsets.ModelViewSet):
    queryset = Recebedor.objects.all()
    serializer_class = RecebedorSerializer
    def create(self, request):
        if request.method == 'POST':
            logo_path = 'media/logo.png'
            imgp = Image.open(request.FILES['img'])
            img_bin = BytesIO()
            imgp.save(img_bin, format='PNG')
            img_data = img_bin.getvalue()
            imgf = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_GRAYSCALE)
            mainp = cv2.imread(logo_path, 0)
            template2 = imgf.copy()
            w,h = mainp.shape[::-1]
            result = cv2.matchTemplate(template2, mainp, cv2.TM_CCOEFF_NORMED)
            threshold = 0.9
            location = np.where(result >= threshold)
            for pt in zip(*location[::-1]):
                loc = cv2.rectangle(template2, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
            flag = False
            if np.amax(result) > threshold:
                flag = True
                cv2.imshow('img', loc)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            if flag == True:
                return Response('Dectectado')
            else:
                return Response('Nada')
        elif request.method == 'GET':
            csrftoken = csrf.get_token(request)
            return HttpResponse(csrftoken)