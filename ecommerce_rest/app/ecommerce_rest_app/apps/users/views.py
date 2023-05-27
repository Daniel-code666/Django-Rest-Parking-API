from datetime import datetime
from django.contrib.sessions.models import Session
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from apps.users.api.serializers import *
from rest_framework.views import APIView


class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )

        if login_serializer.is_valid():
            user = login_serializer._validated_data["user"]

            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)

                if created:
                    return Response(
                        {
                            "token": token.key,
                            "user": user_serializer.data,
                            "msg": "Login successfull",
                        },
                        status=status.HTTP_201_CREATED,
                    )
                else:
                    all_sessions = Session.objects.filter(
                        expire_date__gte=datetime.now()
                    )

                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get("_auth_user_id")):
                                session.delete()

                    token.delete()
                    token = Token.objects.create(user=user)
                    return Response(
                        {
                            "token": token.key,
                            "user": user_serializer.data,
                            "msg": "Login successfull",
                        },
                        status=status.HTTP_201_CREATED,
                    )
            return Response({"msg": "error"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(
            {"msg": "error", "errors": login_serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class Logout(APIView):
    def post(self, request):
        try:
            token = request.GET.get("token")
            token = Token.objects.filter(key=token).first()

            if token:
                user = token.user

                all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                if all_sessions:
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get("_auth_user_id")):
                            session.delete()
                token.delete()

                session_message = "Sesiones eliminadas"
                token_message = "Token eliminado"
                return Response(
                    {"tkn_msg": token_message, "ses_msg": session_message},
                    status=status.HTTP_200_OK,
                )

            return Response(
                {"errors": "no hay usuarios con esas credenciales"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except:
            return Response(
                {"errors": "no hay token"}, status=status.HTTP_404_NOT_FOUND
            )
