"""
Test cases for Dimension and Dimensioned object behaviour.
"""
from unittest import SkipTest
from holoviews.core import Dimensioned, Dimension
from holoviews.element.comparison import ComparisonTestCase

import numpy as np
try:
    import pandas as pd
except:
    pd = None


class DimensionTest(ComparisonTestCase):

    def setUp(self):
        self.values1 = [0,1,2,3,4,5,6]
        self.values2 = ['a','b','c','d']

        self.duplicates1 = [0,1,0,2,3,4,3,2,5,5,6]
        self.duplicates2 = ['a','b','b','a','c','a','c','d','d']

    def test_dimension_values_list1(self):
        dim = Dimension('test', values=self.values1)
        self.assertEqual(dim.values, self.values1)

    def test_dimension_values_list2(self):
        dim = Dimension('test', values=self.values2)
        self.assertEqual(dim.values, self.values2)

    def test_dimension_values_list_duplicates1(self):
        dim = Dimension('test', values=self.duplicates1)
        self.assertEqual(dim.values, self.values1)

    def test_dimension_values_list_duplicates2(self):
        dim = Dimension('test', values=self.duplicates2)
        self.assertEqual(dim.values, self.values2)

    def test_dimension_values_array1(self):
        dim = Dimension('test', values=np.array(self.values1))
        self.assertEqual(dim.values, self.values1)

    def test_dimension_values_array2(self):
        dim = Dimension('test', values=np.array(self.values2))
        self.assertEqual(dim.values, self.values2)

    def test_dimension_values_array_duplicates1(self):
        dim = Dimension('test', values=np.array(self.duplicates1))
        self.assertEqual(dim.values, self.values1)

    def test_dimension_values_array_duplicates2(self):
        dim = Dimension('test', values=np.array(self.duplicates2))
        self.assertEqual(dim.values, self.values2)

    def test_dimension_values_series1(self):
        if pd is None:
            raise SkipTest("Pandas not available")
        df = pd.DataFrame({'col':self.values1})
        dim = Dimension('test', values=df['col'])
        self.assertEqual(dim.values, self.values1)

    def test_dimension_values_series2(self):
        if pd is None:
            raise SkipTest("Pandas not available")
        df = pd.DataFrame({'col':self.values2})
        dim = Dimension('test', values=df['col'])
        self.assertEqual(dim.values, self.values2)


    def test_dimension_values_series_duplicates1(self):
        if pd is None:
            raise SkipTest("Pandas not available")
        df = pd.DataFrame({'col':self.duplicates1})
        dim = Dimension('test', values=df['col'])
        self.assertEqual(dim.values, self.values1)


    def test_dimension_values_series_duplicates2(self):
        if pd is None:
            raise SkipTest("Pandas not available")
        df = pd.DataFrame({'col':self.duplicates2})
        dim = Dimension('test', values=df['col'])
        self.assertEqual(dim.values, self.values2)


class DimensionedTest(ComparisonTestCase):

    def test_dimensioned_init(self):
        Dimensioned('An example of arbitrary data')

    def test_dimensioned_constant_label(self):
        label = 'label'
        view = Dimensioned('An example of arbitrary data', label=label)
        self.assertEqual(view.label, label)
        try:
            view.label = 'another label'
            raise AssertionError("Label should be a constant parameter.")
        except TypeError: pass

    def test_dimensionsed_redim_string(self):
        dimensioned = Dimensioned('Arbitrary Data', kdims=['x'])
        redimensioned = dimensioned.clone(kdims=['Test'])
        self.assertEqual(redimensioned, dimensioned.redim(x='Test'))

    def test_dimensionsed_redim_dimension(self):
        dimensioned = Dimensioned('Arbitrary Data', kdims=['x'])
        redimensioned = dimensioned.clone(kdims=['Test'])
        self.assertEqual(redimensioned, dimensioned.redim(x=Dimension('Test')))

    def test_dimensionsed_redim_dict(self):
        dimensioned = Dimensioned('Arbitrary Data', kdims=['x'])
        redimensioned = dimensioned.clone(kdims=['Test'])
        self.assertEqual(redimensioned, dimensioned.redim(x={'name': 'Test'}))

    def test_dimensionsed_redim_dict_range(self):
        redimensioned = Dimensioned('Arbitrary Data', kdims=['x']).redim(x={'range': (0, 10)})
        self.assertEqual(redimensioned.kdims[0].range, (0, 10))
