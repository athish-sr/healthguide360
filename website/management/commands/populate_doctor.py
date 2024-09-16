from website.models import Doctor, Department
from django.core.management.base import BaseCommand
from faker import Faker

class Command(BaseCommand):
    help = 'Add 100 doctors to the database'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create departments if they don't exist
        departments = ['Cardiology', 'Neurology', 'Orthopedics', 'Pediatrics', 'Oncology']
        for dept_name in departments:
            Department.objects.get_or_create(name=dept_name)

        # Fetch all departments
        all_departments = Department.objects.all()

        # Add 100 doctors
        for _ in range(100):
            doctor_name = fake.name()
            department = fake.random_element(elements=all_departments)
            Doctor.objects.create(name=doctor_name, department=department)

        self.stdout.write(self.style.SUCCESS('Successfully added 100 doctors'))