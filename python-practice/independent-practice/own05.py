import json

with open(
    r"D:\code_work\python-practice\independent-practice\students.json", encoding="utf-8"
) as f:
    students = json.load(f)


def group_stats(students):
    stats = {}
    for line in students:
        cls = line["cls"]
        score = line["score"]
        if cls in stats:
            stats[cls]["count"] += 1
            stats[cls]["total"] += score
            stats[cls]["max"] = max(stats[cls]["max"], score)
            stats[cls]["min"] = min(stats[cls]["min"], score)
        else:
            stats[cls] = {"count": 1, "max": score, "min": score, "total": score}
    for cls in stats:
        stats[cls]["avg"] = stats[cls]["total"] / stats[cls]["count"]
    return stats


def main():
    stats = group_stats(students)
    for cls, info in sorted(stats.items(), key=lambda x: x[1]["avg"], reverse=True):
        print(f"{cls} {info['count']}人 最大 {info['max']} 最小 {info['min']} 总分 {info['total']} 平均分 {info['avg']}")
    with open("own05_summary.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
