# kSWAP
General implementation of SWAP for Zooniverse projects.  This implementation extends SWAP (for binary tasks) to k-classes (kSWAP).

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

will run tests of offline and a simulation of online SWAP and kSWAP.  It will also produce a plot showing a comparison of an example user score based on the offline and online versions.

## Notes
The example config files allow for some customisation.  They are currently implemented for the [Supernova Hunters](https://www.zooniverse.org/projects/dwright04/supernova-hunters) citizen science project, where volunteers are asked a binary question with a yes or no response.
![alt text](https://github.com/dr-darryl-wright/kSWAP/blob/master/swap_example_volunteer_history.png =250x)

The kSWAP tests use artificially generated data where simulated volunteers annotations '0', '1' or '2'.  The ```generate_kswap_demo_data.py``` script allows the competence of these simulated volunteers to be altered.
![alt text](https://github.com/dr-darryl-wright/kSWAP/blob/master/kswap_example_volunteer_history.png =250x)
