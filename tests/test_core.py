import os
import pandas as pd
from eda_cli.viz import generate_report

def test_generate_report_creates_file(tmp_path):
    # Создаём пример DataFrame
    df = pd.DataFrame({
        "A": [1, 2, 3, 4, 5],
        "B": [5, 4, 3, 2, 1]
    })

    # Указываем путь для сохранения графика
    output_file = tmp_path / "report.png"

    # Функция не должна выдавать ошибок
    generate_report(df, output_path=str(output_file))

    # Проверяем, что файл создан
    assert output_file.exists()
