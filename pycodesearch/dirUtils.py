import pandas as pd
import os

class DirUtils:
    def __init__(self):
        pass

    def list_paths(self,folder_path):
        file_paths = []
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                file_paths.append(os.path.join(root, filename))
        return file_paths

    def from_list(self,input_list):
        try:
            seg_paths = []
            for path in input_list:
                seg_paths.append(self.list_paths(path))
            return seg_paths
        except:
            raise('!Input list is missing')

    def from_file(self,input_file):
        try:
            df = pd.read_csv(input_file)
            folder_path = df['FOLDER_PATH']
            return self.from_list(folder_path)
        except:
            raise('!Input File not found, check the path')

    def get_paths_with_words(self):
        pass