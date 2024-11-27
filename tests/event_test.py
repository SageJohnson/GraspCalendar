import unittest
import coverage
from app.__init__ import app, db
from app.models import Event
from flask_testing import TestCase
import datetime

class AddEvent(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_event_valid_input(self):
        with self.client:
            response = self.client.post('/users/add_event', data={
                'title': 'Test Event',
                'start_time': '2024-05-10 12:00:00',
                'end_time': '2024-05-10 13:00:00',
                'notes': 'Test notes'
            })
            self.assertRedirects(response, '/users/week')
            events = Event.query.all()
            self.assertEqual(len(events), 1)
            self.assertEqual(events[0].title, 'Test Event')

    def test_add_event_invalid_input(self):
        with self.client:
            response = self.client.post('/users/add_event', data={
                'title': 'Test Event',
                'start_time': '2024-05-10 13:00:00',
                'end_time': '2024-05-10 12:00:00',
                'notes': 'Test notes'
            })
            self.assert200(response)
            self.assertIn(b'Invalid date range!', response.data)

class DeleteEvent(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_delete_event(self):
        test_event = Event(
            id='test_id',
            user_id='test_user_id',
            title='Test Event',
            start_time=datetime.datetime.now(),
            end_time=datetime.datetime.now() + datetime.timedelta(hours=1),
            date=datetime.datetime.now(),
            notes='Test Notes'
        )
        db.session.add(test_event)
        db.session.commit()

        response = self.app.post('/users/delete_event/test_id')

        deleted_event = Event.query.filter_by(id='test_id').first()
        self.assertIsNone(deleted_event)

        self.assertEqual(response.status_code, 302)
        self.assertIn('/users/week', response.headers['Location'])

if __name__ == '__main__':
    unittest.main()
