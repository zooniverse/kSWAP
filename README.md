# kSWAP
General implementation of SWAP for Zooniverse projects.

## Requirements

Currently only tested with python 3.8.

Package requirements:

```python
sqlite3
matplotlib
```
## Testing

Running:

```
$ python run.py
```

will run tests of offline and a simulation of online SWAP.  It will also produce a plot showing a comparison of an example user score based on the offline and online versions.

## Notes
The example config files allow for some customisation.  They are currently implemented for the [Supernova Hunters](https://www.zooniverse.org/projects/dwright04/supernova-hunters) citizen science project, where volunteers are asked a binary question with a Yes or No response.
