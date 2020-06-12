from django.test import TestCase
from .models import Student, Notes

# Create your tests here.


class StudentTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james = Student(
            first_name='James', last_name='Muriuki', email='james@moringaschool.com')

    # Testing  instance

    def test_instance(self):
        self.assertTrue(isinstance(self.james, Student))
# Testing Save Method

    def test_save_method(self):
        self.james.save_student()
        students = Student.objects.all()
        self.assertTrue(len(students) > 0)


class NotesTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james = Student(
            first_name='James', last_name='Muriuki', email='james@moringaschool.com')
        self.james.save_student()

        # Creating a new tag and saving it
        # self.new_tag = tags(name = 'testing')
        # self.new_tag.save()

        self.new_notes = Notes(
            title='Test Notes', post='This is a random test Post', student=self.james)
        self.new_notes.save()

        self.new_notes.add(self)

    def tearDown(self):
        Student.objects.all().delete()
        Notes.objects.all().delete()


def test_get_courses_today(self):
    today_courses = Notes.todays_courses()
    self.assertTrue(len(today_courses) > 0)


@classmethod
def days_courses(cls,date):
        courses = cls.objects.filter(pub_date__date = date)
        return courses
