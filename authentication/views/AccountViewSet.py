from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from authentication.models import UserProfile
from authentication.serializers.UserProfileSerializer import UserProfileSerializer
from authentication.serializers.UserSerializer import UserSerializer


class AccountViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)

    lookup_field = 'id'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    user_profile_serializer_class = UserProfileSerializer

    def list(self, request, *args, **kwargs):

        user = request.user

        if user.username == 'webadmin':
            all_users = User.objects.all()
            all_user_data = list()

            for user in all_users:
                user_data = self.serializer_class(user).data

                user_profile = UserProfile.objects.get(user=self.request.user)
                user_profile_data = self.user_profile_serializer_class(user_profile).data
                user_data.update(user_profile_data)
                all_user_data.append(user_data)
            return Response(all_user_data)

        user_data = self.serializer_class(user).data
        user_profile = UserProfile.objects.get(user=self.request.user)
        user_profile_data = self.user_profile_serializer_class(user_profile).data
        user_data.update(user_profile_data)

        return Response(user_data)

    def retrieve(self, request, *args, **kwargs):
        user_id = kwargs.get(self.lookup_field)
        user = User.objects.get(id=user_id)

        user_data = self.serializer_class(user).data
        user_profile = UserProfile.objects.get(user=self.request.user)
        user_profile_data = self.user_profile_serializer_class(user_profile).data

        user_data.update(user_profile_data)

        return Response(user_data)

    def create(self, request, *args, **kwargs):
        data = request.data

        print data
        if data:
            created_data = self.create_or_update_profile(data, None)
            return Response(created_data, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        data = request.data
        if data:
            user_id = kwargs.get(self.lookup_field)
            updated_data = self.create_or_update_profile(data, user_id)
            return Response(updated_data, status=status.HTTP_200_OK)
        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)

    def create_or_update_profile(self, data, user_id):

        print data, "============="
        if not user_id:

            email = data.get('email', None)
            password = data.get('password', None)
            user = User.objects.create_user(email=email, username=email, password=password)

        else:
            user = User.objects.get(id=user_id)
            email = user.email

        first_name = data.get('first_name', None)
        last_name = data.get('last_name', None)

        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # create user profile

        address_one = data.get('address_one', None)
        address_two = data.get('address_two', None)
        street = data.get('street', None)
        landmark = data.get('landmark', None)
        district = data.get('district', None)
        city = data.get('city', None)
        state = data.get('state', None)
        pincode = data.get('pincode', None)
        phonenumber = data.get('phonenumber', None)
        phonenumber_two = data.get('phonenumber_two', None)
        company = data.get('company', None)

        user_profile, created = UserProfile.objects.get_or_create(user=user)

        user_profile.address_one = address_one
        user_profile.address_two = address_two
        user_profile.street = street
        user_profile.landmark = landmark
        user_profile.district = district
        user_profile.city = city
        user_profile.state = state
        user_profile.pincode = pincode
        user_profile.phonenumber = phonenumber
        user_profile.phonenumber_two = phonenumber_two
        user_profile.company = company

        user_profile.save()
        return data
