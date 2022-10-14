from rest_framework import generics, status
from rest_framework.response import Response

from apps.teachers.models import Teacher

from apps.students.models import Assignment
from .serializers import TeacherAssignmentSerializer


class AssignmentsView(generics.ListCreateAPIView):
    serializer_class = TeacherAssignmentSerializer

    def get(self, request, *args, **kwargs):
        teacher = Teacher.objects.get(user=request.user)

        #adding teacher key in request data with its value
        request.data['teacher'] = teacher.id
        assignments = Assignment.objects.filter(teacher__user=request.user)

        return Response(
            data=self.serializer_class(assignments, many=True).data,
            status=status.HTTP_200_OK
        )

    def patch(self, request, *args, **kwargs):

        # if content is present in payload then return 400 error because teacher only give grade
        # they can't change assignment content
        if 'content' in request.data:
            return Response(
                data={'error': 'Teacher cannot change the content of the assignment'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            teacher = Teacher.objects.get(user=request.user)
            assignment = Assignment.objects.get(
                pk=request.data['id'], teacher=teacher.id)

            # if state of assignment is DRAFT then don't give access to teacher to grade, it can only give grade to submitted one
            if assignment.state == 'DRAFT':
                return Response(
                    data={'error': 'SUBMITTED assignments can only be graded'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # if state of assignment is GRADED then don't give access to teacher to give grade again
            if assignment.state == 'GRADED':
                return Response(
                    data={'error': 'GRADED assignments cannot be graded again'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        except Assignment.DoesNotExist:
            return Response(
                data={'error': 'Assignment does not exist/permission denied'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.serializer_class(
            assignment, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            # important step
            # after grade is assigned mark it as GRADED and save it
            assignment.state = 'GRADED'
            assignment.save(update_fields=["state"])
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
