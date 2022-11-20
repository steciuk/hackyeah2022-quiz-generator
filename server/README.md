# templates

## Setup

### Windows

```
py -3 -m venv .venv
```

```
.venv\scripts\activate
```

```
python -m pip install -r requirements.txt
```

### macOS/Linux

```
python3 -m venv .venv
```

```
source .venv/bin/activate
```

```
python3 -m pip install -r requirements.txt
```

## Installing new packages

With activated virtual environment run:

### Windows

```
python -m pip install -U <package_name>
```

Before commit run:

```
python -m pip freeze > requirements.txt
```

### macOS/Linux

```
python3 -m pip install -U <package_name>
```

Before commit run:

```
python3 -m pip freeze > requirements.txt
```

## Running tests

### Windows

```
python -m pytest
```

### macOS/Linux

```
python3 -m pytest
```

## Start FastAPI server

### macOS

```
python3 -m uvicorn server:app --reload
```

