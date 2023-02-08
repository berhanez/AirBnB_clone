#!/usr/bin/python3
"""Defines unittests for models/file_storage.py.
Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittest for testin FileStorage class."""
    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(1)

    def test_FileStorage_file_path_is_private_attribute(self):
        with self.assertRaises(AttributeError):
            fs = FileStorage()
            print(fs.__file_name)
            
    def testFileStorage_objects_is_private_attribute(self):
        with self.assertRaises(AttributeError):
            fs = FileStorage()
            print(fs.__objects)

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)

class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing all method of the FileStorage class."""

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
	
        except IOError:
            pass
    def test_all(self):
        """test all"""
        self.assertEqual(type(storage.all()), dict)

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(1)

    def test_new(self):
        bm = BaseModel(id="123")
        models.storage.new(bm)
        self.assertIn("BaseModel.123", models.storage.all().keys())
        self.assertIn(bm, storage.all().values())

    def test_new_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(1)

    def test_save(self):
        bm = BaseModel(name="Holberton")
        models.storage.new(bm)
        bm.save()
        save_text = ""
        with open("file.json") as f:
            save_text = f.read()
        bm = BaseModel(name="Poppy")
        models.storage.new(bm)
        bm.save()
        with open("file.json") as f:
            self.assertNotEqual(save_text, f.read())

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(1)

    def test_reload(self):
        bm = BaseModel(id="98", name="Mission")
        with open("file.json", "w") as f:
            json.dump({"BaseModel.98": bm.to_dict()}, f)
        models.storage.reload()
        self.assertIn("BaseModel.98", models.storage.all().keys())

    def test_reload_no_file(self):
        objs = models.storage.all()
        try:
            os.remove("file.json")
        except:
            pass
        models.storage.reload()
        self.assertEqual(objs, models.storage.all())

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(1)

if __name__ == "__main__":
    unittest.main()
