import unittest
from tkinter import Tk
from unittest.mock import patch
from src.GUI.GUI_login import App

class TestVerifyCorrectCredentials(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.root = self.app.root

    def tearDown(self):
        self.root.destroy()

    @patch.object(App, 'destroy_root')
    def test_verify_correct_credentials(self, mock_destroy_root):
        # Configura las entradas de usuario y contraseña
        self.app.user.insert(0, "root")
        self.app.password.insert(0, "12345")

        # Llama a la función verify
        self.app.verify()

        # Verifica que la ventana principal (root) se haya destruido
        mock_destroy_root.assert_called_once()

if __name__ == '__main__':
    unittest.main()
