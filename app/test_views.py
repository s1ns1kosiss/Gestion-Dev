from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from .models import Product, Order, Cart, CartItem
from decimal import Decimal

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User'
        )
        self.product = Product.objects.create(
            name="Test Product",
            brand="Test Brand",
            price=Decimal('99.99'),
            description="Test Description",
            image="https://example.com/image.jpg",
            rating=Decimal('4.5'),
            quantity=10,
            stock=10
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_product_list_view(self):
        self.client.login(username='testuser', password='testpass123')
        permission = Permission.objects.get(codename='view_product')
        self.user.user_permissions.add(permission)
        response = self.client.get(reverse('listProduct'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listProduct/index.html')
        self.assertContains(response, "Test Product")

    def test_product_detail_view(self):
        response = self.client.get(reverse('prodDetail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'productDetail/index.html')
        self.assertContains(response, "Test Product")

    def test_cart_view_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('view_cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/index.html')

    def test_cart_view_unauthenticated(self):
        response = self.client.get(reverse('view_cart'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_add_to_cart(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('add_to_cart', args=[self.product.id]), {
            'quantity': 1
        })
        self.assertEqual(response.status_code, 302)  # Redirect after adding
        cart = Cart.objects.get(user=self.user)
        self.assertEqual(cart.items.count(), 1)

    def test_checkout_view_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        cart = Cart.objects.create(user=self.user)
        CartItem.objects.create(
            cart=cart,
            product=self.product,
            quantity=1,
            price=self.product.price
        )
        response = self.client.get(reverse('customerData'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customerData/index.html')

    def test_order_history_view(self):
        self.client.login(username='testuser', password='testpass123')
        Order.objects.create(
            user=self.user,
            total_amount=Decimal('99.99'),
            status='Completed'
        )
        response = self.client.get(reverse('order_history'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/index.html')

class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User'
        )

    def test_login_view(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'pass': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful login

    def test_register_view(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'new@example.com',
            'pass': 'newpass123',
            'first_name': 'Nuevo',
            'last_name': 'Usuario'
        })
        self.assertEqual(response.status_code, 302)  # Redirige al login si es exitoso
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirect after logout 