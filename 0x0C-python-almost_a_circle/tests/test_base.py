#!/usr/bin/python3
"""Test document for base file."""

from unittest import TestCase
from models.base import Base


class TestBase(TestCase):
    """Tests the base class."""

    def test_base(self):
        """Test suite for the base instance"""

        a_base = Base()
        self.assertEqual(a_base.id, 1)

        b_base = Base()
        self.assertEqual(b_base.id, 2)

        c_base = Base()
        self.assertEqual(c_base.id, 3)

        d_base = Base(15)
        self.assertEqual(d_base.id, 15)
