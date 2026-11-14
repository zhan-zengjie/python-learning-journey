from abc import ABC, abstractmethod
import json
from data_define import Record


class FileReader(ABC):

    def __init__(self, path):
        self.path = path

    @abstractmethod
    def read_data(self):
        pass


class TextFileReader(FileReader):
    def read_data(self):
        records = []
        with open(self.path, "r", encoding="utf-8") as f:
            f.readline() 
            for line in f:
                parts = line.strip().split(",")
                records.append(Record(parts[0], parts[1], parts[2], parts[3], parts[4]))
        return records


class JsonFileReader(FileReader):
    def read_data(self):
        records = []
        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)
            for item in data:
                record = Record(
                    item["date"],
                    item["product"],
                    item["quantity"],
                    item["price"],
                    item["region"],
                )
                records.append(record)
        return records


if __name__ == "__main__":
    csv_reader = TextFileReader(r"D:\code_work\python-basics\sales_data.csv")
    json_reader = JsonFileReader(r"D:\code_work\python-basics\sales_data.json")

    csv_records = csv_reader.read_data()
    json_records = json_reader.read_data()

    print("CSV 条数:", len(csv_records))
    print("JSON 条数:", len(json_records))

    csv_total = sum(r.amount() for r in csv_records)
    json_total = sum(r.amount() for r in json_records)

    print("CSV 总额:", csv_total)
    print("JSON 总额:", json_total)
