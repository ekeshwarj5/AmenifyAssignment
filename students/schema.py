import graphene
from graphene_django.types import DjangoObjectType
from .models import Student

class StudentType(DjangoObjectType):
    class Meta:
        model = Student

class Query(graphene.ObjectType):
    students = graphene.List(StudentType)

    def resolve_students(self, info):
        return Student.objects.all()

class CreateStudent(graphene.Mutation):
    student = graphene.Field(StudentType)

    class Arguments:
        name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        age = graphene.Int(required=True)

    def mutate(self, info, name, last_name, age):
        student = Student(name=name, last_name=last_name, age=age)
        student.save()
        return CreateStudent(student=student)

class UpdateStudent(graphene.Mutation):
    student = graphene.Field(StudentType)

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        last_name = graphene.String()
        age = graphene.Int()

    def mutate(self, info, id, name=None, last_name=None, age=None):
        student = Student.objects.get(pk=id)
        if name is not None:
            student.name = name
        if last_name is not None:
            student.last_name = last_name
        if age is not None:
            student.age = age
        student.save()
        return UpdateStudent(student=student)

class DeleteStudent(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        student = Student.objects.get(pk=id)
        student.delete()
        return DeleteStudent(success=True)

class Mutation(graphene.ObjectType):
    create_student = CreateStudent.Field()
    update_student = UpdateStudent.Field()
    delete_student = DeleteStudent.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
