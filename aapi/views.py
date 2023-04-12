from rest_framework import viewsets
from rest_framework.response import Response
from aapi.models import Recebedor
from aapi.serializers import RecebedorSerializer
from PIL import Image
import numpy as np
import cv2
from io import BytesIO
from urllib.request import urlopen

class RecebedorViewSet(viewsets.ModelViewSet):
    queryset = Recebedor.objects.all()
    serializer_class = RecebedorSerializer
    def create(self, request):
        if request.method == 'POST':
            imgp = Image.open(request.FILES['img'])
            logo_path = urlopen('https://lh3.googleusercontent.com/pw/AMWts8ANE384tAfx5LraQeLwo6kCKeXNX6vq1Yr1w4gJ1b0eosTdwe6UGJl6Ka9aijhq4ufyEWosvkKgmJsDtoriJ7isW8TzOhzet6W4fZcQwmiYEkMKBntuizF665EGQVLRRCbxLTn2io4CBCXDBAuycwIX7rbfzXJ81E_2clYE1CwfU9WKDtKKNelv10JPKUMWMJM3qy5RyDR4yOr0ZB94IUpKnOoeo0iJ4HjnulBEa1VnVORc1jhsfesSDf-F-jJ-kbaSCWjilYjC0xXj31UTxlChJxNGsCuXh1wvspKHjaUjYASx5U2kgs1wPINXaFQEIRVjjwrjZOfBsEQnZ9jOSK1FUE1zCaRjJHK-9QkU1qGTxxd6InEiNSfnC6UorYQNYiDUJlbHIYO0zzxfxhlMJPEz8sdRUuAqp3yGW8Lnjl2Ei9sqPSCq31oBYqr5eUJwQa7rQqFgE6l_9bx4e20q_ZBsszhauLl0TGBpwMgh1UmfGAwTe90WGzYmQjG7owkad_Q6q2-BHDrIQ3c8CTY4tK8N4WXJ0DJf13NdrkGWw8YESwvnCeQQq-bsNxjsTPjlITNFi-yH5axDd2frc-EeNKof7CURzrDCl3kg_rlrpm3PTYYvaFnp2EitNE8j81bITay2Tyd-JGn28bZ6-gW2CKq6TSargABV5N9i8atstRR9ZTprkK_QvFCgTjwIRlvRFKAqbImcaJ1syOJyVT6ycqOv5zQpBem1XyZsGFjo-WGaJcPUtvOfsLbh0Q2PGfJq00c7p9tZF7IBXAaEX4S7T52nCAzhjOSlbb5rYaeS_vTqIRRSO08chLQIgp8ieeg6nmNbjYeNWuJQ3mii-5OADdPpuzRs8IsDSgMXbjlGund9vADAqKe2nyGLK3pmvyTjoXTTYTpB3TonSoJG3kBCuJVWwYuS-5ot347-bEY5scmTt1Bg1W8aRlCuGUMtWW0sfZxv3wExytJAbcne2jrO50YkgS5KNxbY4bSRJZc0VbmIjyBZhLDtXmu3aAcWyHaEK2JRU_gU6iaBZmgeLnSJEcpECrcFxBLG0CUeB_hG44nBLMx0ik9Oxws1vTwPIFaIP3M_RL6JCdy43uVC1HyDpKIUdY7_bh7BsV6-V2IEJ1XdkHMD0tp_HV0jOFtrjTqZ-AhNLCKe3U0lBQ=w176-h34-s-no?authuser=0')
            logo_data = logo_path.read()
            logo_arr = np.array(bytearray(logo_data), dtype=np.uint8)
            img_bin = BytesIO()
            imgp.save(img_bin, format='PNG')
            img_data = img_bin.getvalue()
            imgf = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_GRAYSCALE)
            mainp = cv2.imdecode(logo_arr, 0)
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
