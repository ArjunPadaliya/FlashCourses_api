"""
Courses REST API Class-Based Views

By:    Patrick R. McElhiney
Date:  4/10/2018

NOTE: Uncomment the commented code to enable authentication with JWT.
"""

from .serializers import InstitutionSerializer, CourseSerializer
from courses.models import Institution, Course
from rest_framework import generics
#from rest_framework import permissions

class CreateInstitutionAPIView(generics.CreateAPIView):
    """
    This API endpoint is for creating a new Institution.
    """
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class RetrieveInstitutionAPIView(generics.RetrieveAPIView):
    """
    This API endpoint is for retrieving a Institution object.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = "unique_id"
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ListInstitutionAPIView(generics.ListAPIView):
    """
    This API endpoint is for listing all Institutions associated with a Course.
    """
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DestroyInstitutionAPIView(generics.DestroyAPIView):
    """
    This API endpoint is for deleting a Institution.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = "unique_id"
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UpdateInstitutionAPIView(generics.UpdateAPIView):
    """
    This API endpoint is for updating a Institution object.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = "unique_id"
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CreateCourseAPIView(generics.CreateAPIView):
    """
    This API endpoint is for creating a new Course.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class RetrieveCourseAPIView(generics.RetrieveAPIView):
    """
    This API endpoint is for retrieving a Course object.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = "unique_id"
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ListCourseAPIView(generics.ListAPIView):
    """
    This API endpoint is for listing all Courses associated with a Deck.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DestroyCourseAPIView(generics.DestroyAPIView):
    """
    This API endpoint is for deleting a Course.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = "unique_id"
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UpdateCourseAPIView(generics.UpdateAPIView):
    """
    This API endpoint is for updating a Course object.
    """
    lookup_url_kwarg = "unique_id"
    lookup_field = "unique_id"
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
