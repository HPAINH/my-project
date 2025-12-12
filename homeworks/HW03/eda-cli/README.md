СОДЕРЖИМОЕ README.md
# EDA-CLI

## Команды

### 1) Overview  


uv run eda-cli overview data/example.csv


### 2) Report  


uv run eda-cli report data/example.csv --out-dir reports --max-hist-columns 5 --top-k-categories 10


## Новые параметры
- `--max-hist-columns` — ограничение на число гистограмм  
- `--top-k-categories` — top-K категорий  
- `--title` — заголовок отчёта  
- `--min-missing-share` — порог пропусков  