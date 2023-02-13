import re
import os
import sys
import pandas as pd

def search_code(query, folder):
    results = []
    for root, dirs, files in os.walk(folder):
        for filename in files:
            filepath = os.path.join(root, filename)
            with open(filepath, encoding="utf8") as f:
                code = f.read()
                lines = code.split("\n")
                for i, line in enumerate(lines):
                    match = re.search(query, line)
                    if match:
                        results.append((filepath, query,i, match.start(), match.end()))

    return sorted(results, key=lambda x: x[1])

def main():
    if len(sys.argv) < 3:
        print("Usage: codesearch [folder_path] [list of words to search for]")
        sys.exit(1)

    folder_path = sys.argv[1]
    query = "|".join(sys.argv[2:])
    results = search_code(query, folder_path)
    
    result_list = []
    for result in results:
        filepath,word, line_number, start, end = result
        print(f"{filepath}:{line_number+1}:{start}-{end}")
        result_list.append([filepath,word,line_number+1,start,end])

    cols = ['Filepath','Word','Line Number','Start Span','End Span']
    df = pd.DataFrame(result_list,columns=cols)
    df.to_csv('OUTPUT_LIST.csv',header=True,index=False)

if __name__ =='__main__':
    main()