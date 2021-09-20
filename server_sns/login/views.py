from rest_framework.views import APIView
from rest_framework.response import Response
from .models import loginUser
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class RegistUser(APIView):
    #APIView에 있는 post() method
    def post(self, request):
        # client로 부터 받은 id와 pw를 저장
        user_id = request.data.get('user_id')
        user_pw = request.data.get('user_pw')
        user_pw_encryted = make_password(user_pw)

        # if user_id가 특수문자인지. 숫자인지. 한글인지.

        user = loginUser.objects.filter(user_id = user_id).first()
        if user is not None:
            return Response(dict(msg="동일한 아이디가 있습니다."))

        loginUser.objects.create(user_id = user_id, user_pw = user_pw_encryted)


        #Response는 dictionary 형태이다.
        data = dict(
            user_id = user_id,
            user_pw = user_pw_encryted
        )

        return Response(data)


class AppLogin(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        user_pw = request.data.get('user_pw')

        user = loginUser.objects.filter(user_id = user_id).first()

        if user is None:
            return JsonResponse({'code': '0001', 'msg': '로그인 실패, 아이디 틀림'}, status=200)
            # return JsonResponse(dict(msg="해당 사용자가 없습니다."))

        if check_password(user_pw, user.user_pw):
            return JsonResponse({'code': '0000', 'msg': '로그인 성공'}, status=200)
            # return Response(dict(msg="로그인 성공"))
        else:
            return JsonResponse({'code': '0002', 'msg': '로그인 실패, 비밀번호 틀림'}, status=200)
            # return JsonResponse(dict(msg="로그인 실패, 비밀번호 틀림"))


