#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name_with_space(self):
        testcase = " Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_one_name_with_space_end(self):
        testcase = "Voltaire "
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_one_name_with_space_both(self):
        testcase = " Voltaire "
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name_with_space_middle(self):
        testcase = "Vol taire"
        expected = "Vol taire"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name_with_space_middle_end(self):
        testcase = "Vol taire "
        expected = "Vol taire"
        self.assertEqual(rearrange_name(testcase), expected)  
    
    def test_one_name_with_space_middle_start(self):
        testcase = " Vol taire"
        expected = "Vol taire"
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_one_name_with_space_middle_both(self):
        testcase = " Vol taire "
        expected = "Vol taire"
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_one_name_with_space_middle_both_end(self):
        testcase = " Vol taire  "
        expected = "Vol taire"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name_with_space_middle_both_start(self):    
        testcase = "  Vol taire "
        expected = "Vol taire"
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_one_name_with_space_middle_both_start_end(self):
        testcase = "  Vol taire  "
        expected = "Vol taire"
        self.assertEqual(rearrange_name(testcase), expected)
    


# Run the tests
unittest.main()
