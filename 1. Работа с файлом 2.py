from typing import TextIO


class File:
    def __init__(self, file_name: str, mode_operation: str) -> None:
        self.file_name = file_name
        self.mode_operation = mode_operation
        self.file = None

    def __enter__(self) -> TextIO:
        try:
            self.file = open(self.file_name, self.mode_operation, encoding="utf-8")
            return self.file

        except FileNotFoundError:
            self.file = open(self.file_name, "w", encoding="utf-8")
            print("Файл не существует, создаю новый...\n"
                  "Файл открыт в режиме записи")
            return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        if exc_type is FileNotFoundError or exc_type is FileExistsError:
            return True


with File("example.txt", "r") as file:
    file.write("Всем привет!")
