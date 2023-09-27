import unittest
from unittest.mock import Mock, patch
import tkinter as tk
import math
from DrawingTriangle.main import DrawingTriangle

class TestDrawTriangle(unittest.TestCase):

    @patch('DrawingTriangle.main.tk.Tk')
    def setUp(self, mock_tk):

        self.root = mock_tk()
        self.app = DrawingTriangle(self.root)
        self.app.canvas = Mock()
        self.app.h_entry = Mock()
        self.app.error_label = Mock()
        self.app.h_increment = 10

    def tearDown(self):
        self.root.destroy()

    def test_draw_triangle_with_valid_h(self):

        self.app.h = 500
        self.app.h_entry.get.return_value = "10"

        self.app.can_draw_triangle = Mock(return_value=True)

        self.app.draw_triangle()

        self.app.h_entry.delete.assert_called_once_with(0, tk.END)
        self.app.h_entry.config.assert_called_once_with(state=tk.DISABLED)
        self.app.canvas.create_polygon.assert_called_once()
        self.assertEqual(len(self.app.triangles), 1)
    def test_draw_triangle_with_invalid_h(self):

        self.app.h = 10
        self.app.h_entry.get.return_value = "10"

        self.app.can_draw_triangle = Mock(return_value=False)

        self.app.draw_triangle()

        self.app.h_entry.delete.assert_called_once_with(0, tk.END)
        self.app.h_entry.config.assert_called_once_with(state=tk.DISABLED)
        self.app.canvas.create_polygon.assert_not_called()
        self.app.error_label.config.assert_called_once_with(text="Вы не можете нарисовать треугольник меньшего размера!")

    def test_compute_triangle_coordinates(self):

        self.app.h = 500
        self.app.h_entry.get.return_value = "10"


        expected_x1 = self.app.width_canvas / 2
        expected_y1 = (self.app.height_canvas / 2) - (self.app.h / 2)
        expected_x2 = expected_x1 - (2 * self.app.h / math.sqrt(3)) / 2
        expected_y2 = (self.app.height_canvas / 2) + (self.app.h / 2) - (self.app.h / 5)
        expected_x3 = expected_x1 + (2 * self.app.h / math.sqrt(3)) / 2
        expected_y3 = (self.app.height_canvas / 2) + (self.app.h / 2) - (self.app.h / 5)

        self.app.draw_triangle()


        self.app.canvas.create_polygon.assert_called_once_with(
            expected_x1, expected_y1,
            expected_x2, expected_y2,
            expected_x3, expected_y3,
            fill="", outline="black"
        )

if __name__ == "__main__":
    unittest.main()
