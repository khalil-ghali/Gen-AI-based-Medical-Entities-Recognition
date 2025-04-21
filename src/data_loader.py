class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_conversation(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            conversation = file.read()
        return conversation