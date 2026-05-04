import argparse
import sys

from app.infrastructure.adapters.repositories.sqlite_book_repository import SQLiteBookRepository
from app.application.use_cases.create_book import CreateBook
from app.application.use_cases.get_all_books import GetAllBooks
from app.application.use_cases.delete_book import DeleteBook


def manage_books():
    parser = argparse.ArgumentParser(description="Gestor de Libros CLI")
    subparsers = parser.add_subparsers(
        dest="command", help="Comandos disponibles")

    # Repositorio y Casos de Uso (Inyección de dependencias)
    repo = SQLiteBookRepository()

    # --- COMANDO: LISTAR ---
    subparsers.add_parser("list", help="Listar todos los libros")

    # --- COMANDO: AGREGAR ---
    add_parser = subparsers.add_parser("add", help="Agregar un nuevo libro")
    add_parser.add_argument("--title", required=True, help="Título del libro")
    add_parser.add_argument("--author", required=True, help="Autor del libro")
    add_parser.add_argument("--pages", type=int,
                            default=0, help="Número de páginas")
    add_parser.add_argument("--desc", default="", help="Descripción")
    add_parser.add_argument(
        "--rating", type=int, choices=range(1, 6), default=5, help="Calificación (1-5)")

    # --- COMANDO: ELIMINAR ---
    del_parser = subparsers.add_parser(
        "delete", help="Eliminar un libro por ID")
    del_parser.add_argument(
        "--id", type=int, required=True, help="ID del libro a borrar")

    args = parser.parse_args()

    # Lógica de ejecución según el comando
    if args.command == "list":
        use_case = GetAllBooks(repo)
        books = use_case.execute()
        print(f"\n{'ID':<5} | {'TÍTULO':<30} | {'AUTOR':<20} | {'⭐'}")
        print("-" * 70)
        for b in books:
            print(
                f"{b.id:<5} | {b.title[:30]:<30} | {b.author[:20]:<20} | {b.rating}")

    elif args.command == "add":
        use_case = CreateBook(repo)
        book = use_case.execute(args.title, args.author,
                                args.pages, args.desc, args.rating)
        print(f"✅ Libro agregado exitosamente con ID: {book.id}")

    elif args.command == "delete":
        use_case = DeleteBook(repo)
        if use_case.execute(args.id):
            print(f"🗑️ Libro con ID {args.id} eliminado.")
        else:
            print(f"❌ No se encontró el libro con ID {args.id}.")

    else:
        parser.print_help()


if __name__ == "__main__":
    manage_books()
