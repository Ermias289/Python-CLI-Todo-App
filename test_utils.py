import unittest
from utils import load_tasks
import tempfile
import os
import json

class TestLoadTasks(unittest.TestCase):

    def test_file_not_found(self):
        result = load_tasks("non_existent.json")
        self.assertEqual(result, {}, "Should return empty dict for missing file")

    def test_empty_file(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            path = temp.name
        try:
            self.assertEqual(load_tasks(path), {}, "Should return empty dict for empty file")
        finally:
            os.remove(path)

    def test_invalid_json(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp:
            temp.write("{ invalid json }")
            path = temp.name
        try:
            self.assertEqual(load_tasks(path), {}, "Should return empty dict for invalid JSON")
        finally:
            os.remove(path)

    def test_valid_json_not_dict(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp:
            json.dump(["task1", "task2"], temp)
            path = temp.name
        try:
            self.assertEqual(load_tasks(path), {}, "Should return empty dict for JSON list, not dict")
        finally:
            os.remove(path)

    def test_valid_json_dict(self):
        sample_dict = {"task_id": 1, "task_title": "Test Task"}
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp:
            json.dump(sample_dict, temp)
            path = temp.name
        try:
            self.assertEqual(load_tasks(path), sample_dict, "Should return actual dict from valid JSON")
        finally:
            os.remove(path)

if __name__ == '__main__':
    unittest.main()
