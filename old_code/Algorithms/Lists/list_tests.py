import unittest
from old_code.Algorithms.Lists.linked_list import LinkedList
from old_code.Algorithms.Lists.linked_list import Node


class TestLinkedList(unittest.TestCase):

    def test_push_new_node(self):
        cls = LinkedList()
        cls.push(1)
        self.assertIsNotNone(cls.head)

    def test_push_new_node_data(self):
        cls = LinkedList()
        cls.push(1)
        self.assertEqual(cls.head.data, Node(1).data)

    def test_insert_after_prev_node_is_none(self):
        pass

    def test_insert_after_prev_node(self):
        pass

    def test_append_to_list(self):
        pass
