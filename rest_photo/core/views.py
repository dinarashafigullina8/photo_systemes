from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Photo
from django.core.files.storage import FileSystemStorage
from rest_framework.parsers import FileUploadParser
from core.serializers import PhotoSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django_filters import rest_framework as filters


class PhotoAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        token = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
        user = User.objects.filter(auth_token=token).values('id')
        lst = Photo.objects.filter(user_id=user[0]['id']).values('photo')
        lst_res = []
        for l in lst:
            name = l['photo'].split('/')[-1].split('.')[0]
            lst_res.append(name)
        return Response({'photos':lst_res})

    def post(self, request):
        request_dict = request.data.dict()
        print(request_dict)
        request_dict['people'] = request_dict['people'].lower()
        serializer = PhotoSerializer(data=request_dict, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'photo': serializer.data})


class FileUploadView(APIView):
    parser_classes = [FileUploadParser]


    def put(self, request, format=None):
        file_obj = request.data['file']
        fs = FileSystemStorage()
        filename = fs.save('images/' + file_obj.name, file_obj)
        uploaded_file_url = fs.url(filename)

        return Response({'url': uploaded_file_url})


class PhotoFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Photo
        fields = ['date', 'location', 'people']


class PhotoListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        token = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
        user = User.objects.filter(auth_token=token).values('id')
        lst = Photo.objects.filter(user_id=user[0]['id']).values()
        print(lst)
        return Response({'photos':list(lst)})

class AutocomplitView(APIView):
    def get(self, request):
        print(request)
        name = request.GET.get("name")
        print(name)
        people = Photo.objects.filter(people__icontains=name).values('people')
        print(people)
        return Response({'people':list(people)})