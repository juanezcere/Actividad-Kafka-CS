import unittest
from unittest.mock import MagicMock
from app.application.use_cases.create_book import CreateBook
from app.domain.models.book import BookModel
from app.domain.ports.book_repository import BookRepository


class TestCreateBook(unittest.TestCase):
    def test_should_create_a_book_successfully(self):
        # 1. ARRANGE (Preparar)
        # Creamos un mock del puerto (no necesitamos la base de datos real)
        mock_repo = MagicMock(spec=BookRepository)

        # Simulamos que al guardar, el repositorio devuelve el libro con un ID (1)
        expected_book = BookModel(id=1, title="Test", author="Author",
                                  pages=100, description="Desc", rating=5)
        mock_repo.save.return_value = expected_book

        use_case = CreateBook(mock_repo)

        # 2. ACT (Actuar)
        result = use_case.execute(
            title="Test",
            author="Author",
            pages=100,
            description="Desc",
            rating=5
        )

        # 3. ASSERT (Afirmar/Verificar)
        # Verificamos que el resultado sea el esperado
        self.assertEqual(result.title, "Test")
        self.assertEqual(result.id, 1)

        # Verificamos que se llamó al método save del repositorio exactamente una vez
        mock_repo.save.assert_called_once()

        print("✅ Test de creación de libro pasado con éxito.")


if __name__ == "__main__":
    unittest.main()
