from django.test import TestCase
from myTelegramUser.models import TelegramUser
from task.models import Task

class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create the user in the same class to ensure it exists
        cls.user1 = TelegramUser.objects.create(
            username="user1", 
            first_name="John", 
            last_name="Doe", 
            full_name="John Doe", 
            telegram_id="123456789", 
            language_code="en", 
            currency="ADA"
        )
        cls.task = Task.objects.create(task="Test Task", quantity=5, url="http://example.com")
        cls.task.user.add(cls.user1)
        
    def test_task_creation(self):
        task = Task.objects.get(id=self.task.id)
        self.assertEqual(task.task, "Test Task")
        self.assertEqual(task.quantity, 5)
        self.assertEqual(task.url, "http://example.com")
        
    def test_task_users_relationship(self):
        task = Task.objects.get(id=self.task.id)
        self.assertIn(self.user1, task.user.all())
        self.assertEqual(task.user.count(), 1)

    def test_task_string_representation(self):
        task = Task.objects.get(user=self.user1)
        # Assuming 'completed' is a boolean field on the Task model, added for completion
        # You would need to update the model to include 'completed' or adjust this test accordingly.
        task.completed = True  
        expected_string = f"Task {task.id} {task.completed}"
        self.assertEqual(str(task), expected_string)