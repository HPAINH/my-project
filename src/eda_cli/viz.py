import pandas as pd
import matplotlib.pyplot as plt

def generate_report(df: pd.DataFrame, output_path: str = None):
    """
    Генерация простого визуального отчёта по DataFrame.
    Выводит статистику и строит гистограммы для всех числовых столбцов.
    """
    # Статистический обзор
    print("=== Обзор данных ===")
    print(df.describe())

    # Первые 5 строк
    print("\n=== Первые 5 строк данных ===")
    print(df.head())

    # Гистограммы для всех числовых столбцов
    df.hist(figsize=(10, 8))
    plt.tight_layout()

    if output_path:
        plt.savefig(output_path)
        print(f"Графики сохранены в {output_path}")
    else:
        plt.show()
