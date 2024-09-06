from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Note

class NoteTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.note = Note.objects.create(title="Sample Title", body="Sample Body")
    
    def test_create_note(self):
        response = self.client.post('/api/notes/', {'title': 'New Note', 'body': 'This is a test note.'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_fetch_note_by_id(self):
        response = self.client.get(f'/api/notes/{self.note.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_query_notes_by_title(self):
        response = self.client.get('/api/notes/', {'title': 'Sample'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_note(self):
        response = self.client.put(f'/api/notes/{self.note.id}/', {'title': 'Updated Title', 'body': 'Updated Body'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
