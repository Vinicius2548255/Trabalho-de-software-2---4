import unittest
from unittest.mock import MagicMock

# Teste da classe Render2D
class TestRender2D(unittest.TestCase):
    def test_render_circle(self):
        renderer = Render2D()
        renderer.render_circle = MagicMock()
        renderer.render_circle(5)
        renderer.render_circle.assert_called_with(5)

    def test_render_square(self):
        renderer = Render2D()
        renderer.render_square = MagicMock()
        renderer.render_square(10)
        renderer.render_square.assert_called_with(10)

# Teste da classe Render3D
class TestRender3D(unittest.TestCase):
    def test_render_circle(self):
        renderer = Render3D()
        renderer.render_circle = MagicMock()
        renderer.render_circle(5)
        renderer.render_circle.assert_called_with(5)

    def test_render_square(self):
        renderer = Render3D()
        renderer.render_square = MagicMock()
        renderer.render_square(10)
        renderer.render_square.assert_called_with(10)

# Teste das classes de Shape
class TestShape(unittest.TestCase):
    def test_circle_draw(self):
        renderer = MagicMock()
        circle = Circle(renderer, 5)
        circle.draw()
        renderer.render_circle.assert_called_with(5)

    def test_square_draw(self):
        renderer = MagicMock()
        square = Square(renderer, 10)
        square.draw()
        renderer.render_square.assert_called_with(10)

if __name__ == "__main__":
    unittest.main()
