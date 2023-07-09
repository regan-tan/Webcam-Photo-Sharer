class FileSharer:

    def __init__(self, file_path, api_key="abc"):
        self.filepath = file_path
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url