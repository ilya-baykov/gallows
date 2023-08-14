class FileEditor:
    ENCODING = "UTF-8"

    @staticmethod
    def read_file(filename) -> list:
        with open(filename, "r+", encoding=FileEditor.ENCODING) as content:
            raw_content = [line.strip() for line in content.readlines() if line.strip()]
            content.seek(0)
            return raw_content

    @staticmethod
    def creating_final_file(content: list[str]):
        with open("set_words", "w+", encoding=FileEditor.ENCODING) as set_words:
            for line in content:
                set_words.write(f"{line}\n")


text_raw = FileEditor().read_file("Words_raw")
FileEditor.creating_final_file(text_raw)
