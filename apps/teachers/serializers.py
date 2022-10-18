from rest_framework import serializers
from apps.students.models import Assignment


class TeacherAssignmentSerializer(serializers.ModelSerializer):
    """
    Teacher Assignment serializer
    """
    class Meta:
        model = Assignment
        fields = '__all__'

    def validate(self, attrs):

        # if state of assignment is GRADED then don't give access to teacher to give grade again
        if self.instance.state == 'GRADED' and 'grade' in attrs:
            raise serializers.ValidationError(
                'GRADED assignments cannot be graded again')

        # check if teacher has permission for the assignment id
        if self.context['teacher_id'] != self.instance.teacher.id:
            raise serializers.ValidationError(
                'Teacher cannot grade for other teacher''s assignment')

        # if assignment state is draft then teacher can't grade that assignment
        if self.instance.state == 'DRAFT' and 'grade' in attrs:
            raise serializers.ValidationError(
                'SUBMITTED assignments can only be graded')

        # if content is present in payload then return 400 error because teacher only give grade
        # they can't change assignment content
        if 'content' in attrs:
            raise serializers.ValidationError(
                'Teacher cannot change the content of the assignment')

        # teacher can't change the student assignment to other student
        if 'student' in attrs:
            raise serializers.ValidationError(
                'Teacher cannot change the student who submitted the assignment')

        if self.partial:
            return attrs
        return super().validate(attrs)
