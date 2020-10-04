from django.test import TestCase

# Create your tests here.
from .models import Category, Product, Chapter

class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="Romance-Fantasy", friendly_name="Romance Fantasy")
        Category.objects.create(name="Comic-Picture", friendly_name="Comic Picture")

    def test_category_has_friendly_name(self):
        """category has name are correctly identified"""
        rf = Category.objects.get(name="Romance-Fantasy")
        cp = Category.objects.get(name="Comic-Picture")
        self.assertEqual(rf.friendly_name, 'Romance Fantasy')
        self.assertEqual(cp.friendly_name, 'Comic Picture')

class ProductTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(name="Romance-Fantasy", friendly_name="Romance Fantasy")
        Product.objects.create(category=category, isbn="1234", sku="987", name="The Lost Sword", description="good", \
                               author="Ann", price=12,rating= 4.5, image_url="https//ss", image="date/img", \
                               format="Paper", currency="usd")

    def test_product_has_friendly_name(self):
        """product has name are correctly identified"""
        book = Product.objects.get(sku="987")
        self.assertEqual(book.name, 'The Lost Sword')
        self.assertEqual(book.description, 'good')
        self.assertEqual(book.price, 12)



class ChapterTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(name="Romance-Fantasy", friendly_name="Romance Fantasy")
        book = Product.objects.create(category=category, isbn="1234", sku="987", name="The Lost Sword", description="good", \
                                      author="Ann", price=12,rating= 4.5, image_url="https//ss", image="date/img", \
                                      format="Paper", currency="usd")
        Chapter.objects.create(book=book, chapter="Chapter X", name="The meeting", price=0.5, author="Ann", translator="Lily", \
                               sku="987C22", context="A longgggggggggggggggggggggggggggggggggggggggggggggggggggggggg word", modalcode="DFSS")


    def test_category_has_friendly_name(self):
        """category has name are correctly identified"""
        chapter = Chapter.objects.get(sku="987C22")
        self.assertEqual(chapter.chapter, 'Chapter X')
        self.assertEqual(chapter.name, 'The meeting')
        self.assertEqual(chapter.price, 0.5)
        self.assertEqual(chapter.context, 'A longgggggggggggggggggggggggggggggggggggggggggggggggggggggggg word')




