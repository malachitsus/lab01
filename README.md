# Toolkit

> Консольный набор утилит: **калькулятор** и **конвертер единиц измерения**.

---

## Установка

Откройте терминал в корне проекта (`.../lab01`) и выполните:

```bash
pip install -e .
```

---

## Использование

### Калькулятор

Вычисляет математическое выражение. Поддерживает `+`, `-`, `*`, `/`, `%`, скобки, унарные `+`/`-`.

```bash
python -m toolkit calc "2 + 2"
# 4.0

python -m toolkit calc "(1 + 1) * 2"
# 4.0

python -m toolkit calc "3 + 4 * (2 - 1)"
# 7.0
```

### Конвертер единиц

Конвертирует значение из одной единицы в другую.

| Группа | Единицы |
|---|---|
| **Длина** | `mm`, `cm`, `m`, `km` |
| **Масса** | `g`, `kg` |
| **Температура** | `c`, `f`, `k` |

```bash
python -m toolkit convert 5 --from km --to m
# 5000.0

python -m toolkit convert 100 --from c --to f
# 212.0

python -m toolkit convert 2 --from kg --to g
# 2000.0
```

### Справка

```bash
python -m toolkit --help
```

---

## Тесты

```bash
python -m pytest
```

---

## Проверка стиля

```bash
python -m ruff check .
```
---

## Структура

```
lab01/
├── src/
│   └── toolkit/
│       ├── __init__.py
│       ├── __main__.py      
│       ├── calculator.py    
│       └── converter.py     
├── tests/                   
├── pyproject.toml
└── README.md
```

---

## Требования

- Python ≥ 3.12