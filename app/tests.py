from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product, Order, Cart, CartItem, Address, OrderReview
from decimal import Decimal

# Create your tests here.

class ProductModelTest(TestCase):
    def setUp(self):
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

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.brand, "Test Brand")
        self.assertEqual(self.product.price, Decimal('99.99'))
        self.assertEqual(self.product.stock, 10)

    def test_product_str(self):
        self.assertEqual(str(self.product), "Test Product")

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.order = Order.objects.create(
            user=self.user,
            address="Test Address",
            addressNro="123",
            status="Pending",
            total_amount=Decimal('199.98')
        )

    def test_order_creation(self):
        self.assertEqual(self.order.user, self.user)
        self.assertEqual(self.order.status, "Pending")
        self.assertEqual(self.order.total_amount, Decimal('199.98'))

    def test_order_str(self):
        self.assertEqual(str(self.order), f'Order {self.order.id} by testuser')

class CartModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.cart = Cart.objects.create(user=self.user)
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
        self.cart_item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
            quantity=2,
            price=Decimal('99.99')
        )

    def test_cart_creation(self):
        self.assertEqual(self.cart.user, self.user)
        self.assertEqual(self.cart.get_total_price(), Decimal('199.98'))

    def test_cart_item_creation(self):
        self.assertEqual(self.cart_item.quantity, 2)
        self.assertEqual(self.cart_item.get_total_price(), Decimal('199.98'))

class AddressModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.address = Address.objects.create(
            user=self.user,
            street="Test Street",
            number="123",
            city="Test City",
            region="Test Region",
            postal_code="12345"
        )

    def test_address_creation(self):
        self.assertEqual(self.address.user, self.user)
        self.assertEqual(self.address.street, "Test Street")
        self.assertEqual(self.address.city, "Test City")

    def test_address_str(self):
        self.assertEqual(str(self.address), "Test Street 123, Test City")

class OrderReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.order = Order.objects.create(
            user=self.user,
            total_amount=Decimal('99.99')
        )
        self.review = OrderReview.objects.create(
            order=self.order,
            user=self.user,
            rating=5,
            comment="Great service!"
        )

    def test_review_creation(self):
        self.assertEqual(self.review.order, self.order)
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comment, "Great service!")

    def test_review_str(self):
        self.assertEqual(str(self.review), f"Review for Order {self.order.id} by testuser")
