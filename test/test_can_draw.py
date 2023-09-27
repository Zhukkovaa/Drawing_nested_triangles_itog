import unittest
from unittest.mock import Mock, patch
from DrawingTriangle.main import DrawingTriangle

class TestCanDrawTriangle(unittest.TestCase):

    @patch('DrawingTriangle.main.tk.Tk')
    def setUp(self, mock_tk):
        # Создаем мок объекты
        self.root = mock_tk()
        self.app = DrawingTriangle(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_can_draw_triangle_with_valid_h(self):
        self.app.min_size = Mock()
        self.app.min_size.return_value = 0

        h = 10
        result = self.app.can_draw_triangle(h)
        self.assertTrue(result)

    def test_can_draw_triangle_with_invalid_h(self):

        self.app.min_size = Mock()
        self.app.min_size.return_value = 0
        h = 0
        result = self.app.can_draw_triangle(h)
        self.assertFalse(result)

    def test_can_draw_triangle_with_invalid_h2(self):

        self.app.min_size = Mock()
        self.app.min_size.return_value = 0

        h = -10
        result = self.app.can_draw_triangle(h)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
