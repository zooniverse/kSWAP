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

The SWAP test will result in the plot below. The plot shows the tracked performance history of an example volunteer, comparing the offline and online versions of the algorithm.

<img src="https://github.com/dr-darryl-wright/kSWAP/blob/master/swap_example_volunteer_history.png" width="500">

The kSWAP tests use artificially generated data where simulated volunteers provide annotations in {'0', '1', '2'}.  The ```generate_kswap_demo_data.py``` script allows the competence of these simulated volunteers to be altered.

Similar to the plot above, the kSWAP test (if using the provided generated simulated annotations) will result in the plot below.  This plot compares an example simulated volunteers performance history for both the offline and online versions.  Since these are simulations with a hard-coded competence, the expected user score is plotted as the dashed black line.

<img src="https://github.com/dr-darryl-wright/kSWAP/blob/master/kswap_example_volunteer_history.png" width="500">
