from django.test import SimpleTestCase,TestCase


class SimpleTestCase(SimpleTestCase):

    def test_main_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class TrainingModelTestCase(TestCase):
    def setUp(self):
        self.training = Training.objects.create(
    date_of_publication='2023-04-22',
    slug='test-slug',
    category='test-category',
    training_title='Test Training',
    summary_training='Test Summary',
    full_training='Test Full Training',
    links_training='http://www.example.com',
    video_training='video/test.mp4',
    graphic_illustrations='illustrations/test.png'
)