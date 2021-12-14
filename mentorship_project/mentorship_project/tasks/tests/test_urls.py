from mentorship_project.tasks.views import list_create_task, get_update_delete_task
from django.urls import reverse , resolve
from django.test import TestCase 

class TestApiUrl(TestCase):
    def test_task_url_is_resolved(self):
        url = reverse('list_create_task')
        self.assertEquals(resolve(url).func, list_create_task)

    def test_task_pk_url_is_resolved(self):
        url = reverse('get_update_delete_task', args=[1])
        self.assertEquals(resolve(url).func, get_update_delete_task)
