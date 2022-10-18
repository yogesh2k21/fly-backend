from apps.students.models import Assignment
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Teacher
from .serializers import TeacherAssignmentSerializer


class TeachersView(generics.ListCreateAPIView):
    serializer_class = TeacherAssignmentSerializer

    def get(self, request, *args, **kwargs):
        try:
            # checking if it is a real teacher or not
            teacher = Teacher.objects.get(user=request.user)

        except Teacher.DoesNotExist:
            return Response(data={'error': 'Teacher does not exist/permission denied'}, status=status.HTTP_400_BAD_REQUEST)
        assignments = Assignment.objects.filter(teacher__user=request.user)

        return Response(data=self.serializer_class(assignments, many=True).data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        try:
            # checking if it is a real teacher or not
            teacher = Teacher.objects.get(user=request.user)

        except Teacher.DoesNotExist:
            return Response(data={'error': 'Teacher does not exist/permission denied'}, status=status.HTTP_400_BAD_REQUEST)

        request.data['teacher'] = teacher.id

        try:
            #checking object exists or not
            assignment = Assignment.objects.get(pk=request.data['id'])

        except Assignment.DoesNotExist:
            return Response(data={'error': 'Assignment does not exist/permission denied'}, status=status.HTTP_400_BAD_REQUEST)

        # passing teacher ID to serializer valid()
        serializer = self.serializer_class(assignment, data=request.data, context={'teacher_id': teacher.id}, partial=True)

        if serializer.is_valid():
            # Now change state to GRADED
            serializer.validated_data['state'] = 'GRADED'
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)

        #if not valid return with errors
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
