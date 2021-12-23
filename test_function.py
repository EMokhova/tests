import unittest
from functions import get_doc_owner_name, get_doc_shelf, check_document_existance, delete_doc, add_new_doc
from unittest.mock import patch


class TestFunctionsUnittest(unittest.TestCase):

    def setUp(self):
        print('метод SetUp')

    def testDown(self):
        print('метод TestDown')

    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name("11-2"), "Геннадий Покемонов")

    def test_get_doc_shelf(self):
        self.assertEqual(get_doc_shelf("2207 876234"), '1')

    def test_check_document_existance(self):
        self.assertEqual(check_document_existance("11-2"), True)

    def test_add_new_doc(self):
        self.assertEqual(add_new_doc("34767", "passport", "Ivan Ivanov", "2"), "2")

    def test_delete_doc(self):
        self.assertEqual(delete_doc("10006"), ("10006", True))
