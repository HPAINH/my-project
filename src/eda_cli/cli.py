import pandas as pd
from .viz import generate_report

def main():
    import sys
    if len(sys.argv) < 3:
        print("Использование: python -m eda_cli overview <путь к CSV>")
        sys.exit(1)

    command = sys.argv[1]
    file_path = sys.argv[2]

    if command == "overview":
        df = pd.read_csv(file_path)
        generate_report(df)
    else:
        print(f"Неизвестная команда: {command}")
        sys.exit(1)

