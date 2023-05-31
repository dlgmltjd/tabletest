from django.test import TestCase
from tabletest.models import Department, Person


class ModelTestCase(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name='Department 1')

    def test_department_model(self):
        department = Department.objects.get(name='Department 1')
        self.assertEqual(department.name, 'Department 1')

    def test_person_model(self):
        person = Person.objects.create(first_name='John', last_name='Doe', department=self.department)
        self.assertEqual(person.first_name, 'John')
        self.assertEqual(person.last_name, 'Doe')
        self.assertEqual(person.department, self.department)
