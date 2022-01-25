"""
p036:实现论文查重小程序
"""

import jieba.analyse

python_article = r"./p036_python_article.txt"

flask_article = r"./p036_flask_article.txt"
java_article = r"./p036_java_article.txt"
shortvideo_article = r"./p036_shortvideo_article.txt"

def get_keywords_from_article(fname):
    with open(fname, encoding="utf-8") as fp:
        content = fp.read()
    # print(content)
    return jieba.analyse.extract_tags(content, 50)

def compute_sim(wordsa, wordsb):
    jiaoji = set(wordsa).intersection(set(wordsb))
    bingji = set(wordsa).union(set(wordsb))
    return round(len(jiaoji)/len(bingji)*100, 2)


if __name__ == '__main__':
    python_keywords = get_keywords_from_article(python_article)
    flask_keywords = get_keywords_from_article(flask_article)
    java_keywords = get_keywords_from_article(java_article)
    shortvideo_keywords = get_keywords_from_article(shortvideo_article)

    # print(python_keywords, flask_keywords, java_keywords, shortvideo_keywords)

    print("python vs python:", compute_sim(python_keywords, python_keywords))
    print("python vs flask:", compute_sim(python_keywords, flask_keywords))
    print("python vs java:", compute_sim(python_keywords, java_keywords))
    print("python vs shortvideo:", compute_sim(python_keywords, shortvideo_keywords))