import json
import re

FILE_NAME = "D:/python_text/sample.txt"
RESULT_FILE = "D:/python_text/result.json"


# 统计文本文件
def analyze_file():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            text = file.read()

    except FileNotFoundError:
        print("文件不存在，请检查文件名！")
        return

    # 统计行数
    lines = text.splitlines()
    #splitlines()是按照换行符，把字符串拆分成多行，返回一个列表
    line_count = len(lines)

    # 统计字符数
    char_count = len(text)

    # 提取单词，统一转换成小写
    words = re.findall(r"[a-zA-Z0-9]+", text.lower())
    #re.findall() 在一段文本中查找所有符合正则表达式要求的内容，并返回一个列表
    #r"[a-zA-Z0-9]+"提取由英文字母或数字组成的连续内容
    # 统计单词出现次数
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    # 按出现次数从高到低排序
    top_words = sorted(
        word_count.items(),
        key=lambda item: item[1],
        reverse=True
    )[:5]

    # 整理统计结果
    result = {
        "总行数": line_count,
        "总字符数": char_count,
        "总单词数": len(words),
        "出现次数最多的5个单词": top_words
    }

    # 显示统计结果
    print("\n====== 文本统计结果 ======")
    print(f"总行数：{line_count}")
    print(f"总字符数：{char_count}")
    print(f"总单词数：{len(words)}")

    print("\n出现次数最多的5个单词:")

    for word, count in top_words:
        print(f"{word}:{count}次")

    # 保存为 JSON
    try:
        with open(RESULT_FILE, "w", encoding="utf-8") as file:
            json.dump(result, file, ensure_ascii=False, indent=4)

        print(f"\n统计结果已保存到 {RESULT_FILE}")

    except OSError:
        print("统计结果保存失败！")


if __name__ == "__main__":
    analyze_file()