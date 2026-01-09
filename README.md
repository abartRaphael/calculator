# calculator

Projet exemple pour le TD1 Devops.

## Run calculator

### Sum

Example : 
```bash
python src/main.py -op sum -val1 1 -val2 2
```

### Max

Exemple : 
```bash
python src/main.py -op max -val1 3 -val2 5
```


### Product
Example
```bash
python src/main.py -op prod -val1 1 -val2 2
```

## Installation des dépendances

```bash
pip install -r requirements.txt
```

## Exécution des tests
```bash
python -m coverage run -m unittest tests/test_calculator.py
```
