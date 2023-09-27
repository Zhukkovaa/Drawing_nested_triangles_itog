import unittest
from unittest.mock import Mock, patch
import tkinter as tk
from DrawingTriangle.main import DrawingTriangle

class TestDeleteLastTriangle(unittest.TestCase):
    @patch('DrawingTriangle.main.tk.Tk')
    def setUp(self, mock_tk):

        self.root = mock_tk()
        self.canvas = Mock()
        self.error_label = Mock()

        self.app = DrawingTriangle(self.root)
        self.app.canvas = self.canvas
        self.app.error_label = self.error_label

    def test_delete_last_triangle_with_triangles(self):

        triangle_mock = Mock()
        self.app.triangles = [triangle_mock]


        self.canvas.coords.return_value = [0, 0, 1, 0, 0.5, 0.866]

        self.app.delete_last_triangle()

        self.assertEqual(len(self.app.triangles), 0)
        self.error_label.config.assert_called_once_with(text="")
        self.canvas.delete.assert_called_once_with(triangle_mock)
    def test_delete_last_triangle_without_triangles(self):

        self.app.triangles = []

        self.app.delete_last_triangle()
        self.assertEqual(self.app.h, None)
        self.error_label.config.assert_not_called()
        self.canvas.coords.assert_not_called()

    def test_delete_last_triangle_with_invalid_triangle(self):

        triangle_mock = Mock()
        self.app.triangles = [triangle_mock]

        self.canvas.coords.return_value = [0, 0, 0, 0, 0, 0]

        self.app.delete_last_triangle()

        self.assertEqual(len(self.app.triangles), 0)
        self.error_label.config.assert_called_once_with(text="")
        self.canvas.delete.assert_called_once_with(triangle_mock)
    def test_delete_last_triangle_with_invalid_triangle(self):

        triangle_mock = Mock()
        self.app.triangles = [triangle_mock]

        self.canvas.coords.return_value = [0, 0, 0, 0, 0, 0]

        self.app.delete_last_triangle()

        self.assertEqual(len(self.app.triangles), 0)
        self.error_label.config.assert_not_called()
        self.canvas.delete.assert_called_once_with(triangle_mock)

if __name__ == "__main__":
    unittest.main()
