#!/usr/bin/env python3
import unittest
from db import SQLiteDatabase


db = SQLiteDatabase()

print(db.get_all())

#def sweet_test():
#    results = db.get_all()
#    assert results == [(1, 'Steve'), (2, 'Amanda')], "Something is not right"
#    return 'Results OK'


#if __name__ == '__main__':
#    print(sweet_test())

class TestAllResults(unittest.TestCase):

    def test_get_all(self):
        results = db.get_all()
        self.assertEqual(results, [(1, 'Steve'),(2, 'Amanda')], "Something is not right")


if __name__ == '__main__':
    unittest.main()
