from unittest.case import TestCase

from django.urls import reverse 
from django.test import TestCase , Client

from rest_framework import status

from mentorship_project.tasks.models import Task
from mentorship_project.tasks.views import is_status_changeable


class TestIsStatusChangeable(TestCase):
    def test_draft_to_active(self):
        self.assertTrue(is_status_changeable("Draft","Active"))

    def test_draft_to_done(self):
        self.assertFalse(is_status_changeable("Draft","Done"))
    
    def test_draft_to_archived(self):
        self.assertTrue(is_status_changeable("Draft","Archived"))
        
    def test_active_to_draft(self):
        self.assertFalse(is_status_changeable("Active","Draft"))

    def test_active_to_done(self):
        self.assertTrue(is_status_changeable("Active","Done"))

    def test_active_to_archived(self):
        self.assertTrue(is_status_changeable("Active","Archived"))
                            
    def test_done_to_draft(self):
        self.assertFalse(is_status_changeable("Done","Draft"))

    def test_done_to_active(self):
        self.assertTrue(is_status_changeable("Done","Active"))           
    
    def test_done_to_archived(self):
        self.assertTrue(is_status_changeable("Done","Archived"))

    def test_archived_to_draft(self):
        self.assertFalse(is_status_changeable("Archived","Draft"))

    def test_archived_to_active(self):
        self.assertFalse(is_status_changeable("Archived","Active"))  

    def test_archived_to_draft(self):
        self.assertFalse(is_status_changeable("Archived","Done"))
            

          
class TestViews(TestCase):
    def form_tasks_url(self):
            return reverse("list_create_task")
       
    #Test Get all tasks
    def test_get_all_tasks(self):
        client= Client()
        response = client.get(self.form_tasks_url())
        self.assertEquals(response.status_code, 200) 

    #Test Post task to the database
    def test_post_tasks_view(self):
        client = Client()
        response = client.post(
            self.form_tasks_url(),
            {
                "status":"Draft",
                "title":"task",
            },
            format ="json"
        )
        self.assertEquals(response.status_code, 201)  
        self.assertEquals(response.data["title"], "task")
        

class TestListCreateAPIView(TestCase):
    def form_tasks_pk_url(self, pk):
        return reverse("get_update_delete_task", kwargs={"pk": pk})    
    
    #Get a specific task with pk
    def test_get_task(self):
        client = Client()
        created_task = Task.objects.create(title="test title", status="Done")
        response = client.get(self.form_tasks_pk_url(created_task.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['status'], 'Done')

    #Update a task
    def test_put_task(self):
        client = Client()
        created_task = Task.objects.create(title="test title", status="Draft")
        response = client.patch(
            self.form_tasks_pk_url(created_task.id),
            {"status":"Active"},
            content_type = 'application/json'
        )
        self.assertEquals(response.status_code, 200) 
        self.assertEquals(response.data['status'], 'Active')
        created_task.refresh_from_db()
        assert created_task.status == "Active"   

    #Delete a specific task with pk
    def test_delete_task(self):
        created_task = Task.objects.create(title="test title", status="Done")
        tasks_count_before_request = Task.objects.count()
        assert tasks_count_before_request == 1
        response = self.client.delete(self.form_tasks_pk_url(created_task.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        tasks_count_after_request = Task.objects.count()
        assert tasks_count_after_request == 0
    

       


