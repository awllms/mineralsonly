from django.test import TestCase
from django.urls import reverse

from .models import Mineral

# Create your tests here.
class MineralModelTests(TestCase):
    """Test for Mineral model."""

    def setUp(self):
        """Set up method to use for model test."""
        self.mineral = Mineral.objects.create(
            name='Test Mineral',
            image_filename='testfilename.jpg',
            image_caption='test caption',
            category='test category',
            formula='test formula',
            strunz_classification='test strunz_classification',
            color='test color',
            crystal_system='test crystal system',
            unit_cell='test unit cell',
            crystal_symmetry='test crystal symmetry',
            cleavage='test cleavage',
            mohs_scale_hardness='test mohs scale hardness',
            luster='test luster',
            streak='test streak',
            diaphaneity='test diaphaneity',
            optical_properties='test optical properties',
            refractive_index='test refractive index',
            crystal_habit='test crystal habit',
            specific_gravity='test spacific gravity',
            group='test group')

    def test_mineral_creation(self):
        """Model that tests a Mineral objects creations."""
        self.assertIn(self.mineral, Mineral.objects.all())


class MineralViewsTests(TestCase):
    """Test for Mineral views."""

    def setUp(self):
        """Set up method to use for model test."""
        self.mineral = Mineral.objects.create(
            name='Test Mineral',
            image_filename='testfilename.jpg',
            image_caption='test caption',
            category='test category',
            formula='test formula',
            strunz_classification='test strunz_classification',
            color='test color',
            crystal_system='test crystal system',
            unit_cell='test unit cell',
            crystal_symmetry='test crystal symmetry',
            cleavage='test cleavage',
            mohs_scale_hardness='test mohs scale hardness',
            luster='test luster',
            streak='test streak',
            diaphaneity='test diaphaneity',
            optical_properties='test optical properties',
            refractive_index='test refractive index',
            crystal_habit='test crystal habit',
            specific_gravity='test spacific gravity',
            group='test group')

        self.mineral2 = Mineral.objects.create(
            name='Test Mineral2',
            image_filename='testfilename2.jpg',
            image_caption='test caption2',
            category='test category2',
            formula='test formula2',
            strunz_classification='test strunz_classification2',
            color='test color2',
            crystal_system='test crystal system2',
            unit_cell='test unit cell2',
            crystal_symmetry='test crystal symmetry2',
            cleavage='test cleavage2',
            mohs_scale_hardness='test mohs scale hardness2',
            luster='test luster2',
            streak='test streak2',
            diaphaneity='test diaphaneity2',
            optical_properties='test optical properties2',
            refractive_index='test refractive index2',
            crystal_habit='test crystal habit2',
            specific_gravity='test spacific gravity2',
            group='test group2')

    def test_mineral_list_view(self):
        """Testing Mineral home view."""
        resp = self.client.get(reverse('minerals:home'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_detail_view(self):
        """Testing Mineral detail view."""
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk':self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')
        self.assertContains(resp, self.mineral.name)
