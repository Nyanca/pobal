from .views import view_cart, add_to_cart, edit_cart
from pobalStudio.models import Ticket
from .contexts import cart_contents

class TestCartViews(TestCase):
    def test_cart_template_renders_correctly(self):
        page = self.client.get('/cart/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart.html')
    
    