# cat-feeder
Motorized cat food dispenser with optional camera module

### Install
Must be run on a Raspberry Pi, from project root:
```bash
sudo python3 -m pip install .
```

### Run
Feeds the cats by dispensing 2 units of food:
```bash
feed-cats --units 2
```

### Run Tests
```bash
python3 -m unittest discover . "*_test.py"
```
