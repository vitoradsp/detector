from rest_framework import viewsets
from rest_framework.response import Response
from aapi.models import Recebedor
from aapi.serializers import RecebedorSerializer
from PIL import Image
import numpy as np
import cv2
from io import BytesIO
from urllib.request import urlopen
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class RecebedorViewSet(viewsets.ModelViewSet):
    queryset = Recebedor.objects.all()
    serializer_class = RecebedorSerializer

    def create(self, request):
        if request.method == 'POST':
            user = request.user
            imgp = Image.open(request.FILES['img'])
            '''logo_path = urlopen('https://lh3.googleusercontent.com/pw/AJFCJaXOEgt3camMAEgkBalkOLOQa8DYPFYyrXTdB6hJ5rKX_LJN93Y97cpa0VlQEEFf5W2aHoESwBnqqCshypIVMR6diUjli8aR14SN-nDj_Y9GJWxgJ7vupAuCkGTk7h1k57apztADi1ZMDJXHsMvxKVeaMIferQShckiCd2b9TzR_44vwYeHGEjOcYV88FQ7SPGeInP6y_My7PXrDKVS4XQeBU2gI_am0iDclF7AfZhADFZQsjcxRMhss6Q3dgUgTRQZxHsxBOmAhsD5jIp8NeP7ZPs6Y3hQfpS_CqOY4fIsWAc-0OoNARBmWRnY6BvWUHc9pArUZ-M-Z5WokIZmAuRpKXbmhsW0f2tr5kjdeEoSjEBbSdJApltL-CiqPx2wjw5JH5SDEFtIG4CV9p4w_MDMV-61EiMHeI33mJDYuFinLWiKNJk_wt702AzrT1wzT5Z_9H-UykTa5FJJ5m_zIaFPE8HqGyQ76mxX1RyyTR64OAnUUA39igGVEdfO9c3bmJtqyD47WSImpejXqsZYE4NLZYHtFz9Zz0AV_q4JYKfpAblJou7Awox_XA3cvIV66cKQV2CRcI7ZpGOOruCkFO6fkSWxBtOGe8bkxrYtrh5f4HJXXd7Pm89yDFtihJLbqTfu__joR6yonxVs7Y-4og-jQ3AKiF5Ty8ynViAOpWYQdsNjiyKyJpx-YiDiYofuHM2tDOAdAmfBMVl4DcnqYZA31x0XA_DLQRfeCxtPcVCwVP9tQjBIGvhFHICEQtEq1Nxh53mJO1ZGsTiivkG5VaAZD8wcDdXnGhwHeAJdF9skr5nJLu_X5nRyeFZRC4vD_Xy5NEX_NQxXWYkTB_iUpvZ9r8-Nojcq8Wp-LLgT9xul_ls1FaKw-tqn7fXtt9UC8FrmMI8dbKSHhq4XNs7hSYizNX4-MkkbqCpGRMH6dNLwFLOg1powNThuQQi1T7UYc3X3qEEKEYxXtquJdogJIsy0QZT0aXoLCA0W0qmkjqIFCizgtJa8eq59hdmILM07vSorQauRKb5TW6BO2i3nmY_e8e1CwZg3fhv5kJEUqCsGGPoQuS4L_3jQiORHvcpNNJHXkZliC2zgk8g1xZr3XtIFl_oF_DdCm9_zh9m4YCjDtKbvpDQ3bSxM8LO5uON_Nc_QPfnxTDAcDZg=w176-h34-s-no?authuser=0')'''
            logo_path = urlopen('https://i.imgur.com/wzTpTHg.png')
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
