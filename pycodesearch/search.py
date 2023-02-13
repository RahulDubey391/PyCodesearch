import re

class Search:
    def __init__(self,path_list,word_list):
        self.path_list = path_list
        self.word_list = word_list

    def search_from_list(self):
        results = []
        for path in self.path_list:
            for word in self.word_list:
                results.append(self.search_code(word,path))
        return results

    def search_code(self,query, path):
        results = []
        with open(path, encoding="utf8") as f:
            code = f.read()
            lines = code.split("\n")
            for i, line in enumerate(lines):
                match = re.search(query, line)
                if match:
                    results.append((path, query,i, match.start(), match.end()))
        return sorted(results, key=lambda x: x[1])
