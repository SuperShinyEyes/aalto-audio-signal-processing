# Aalto Audio Signal Processing

## Dependency
- Anaconda or [Miniconda](https://conda.io/en/latest/miniconda.html)
```
# On macOS,
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh

# Run the installer
bash Miniconda3-latest-MacOSX-x86_64.sh
```

## Installation
```
make init

# Validate your installation
python -c 'import asp; print("asp installation ok.")'
```

## How to validate Homework
```
. activate asp
jupyter notebook

# Navigate to `homework/` and open relevant homework
```
To run an entire notebook, click "Run All"

![run_all_cells](images/run_all_cells.png)


## Miscellaneous
<img src="images/Warped_FIR_Filter.png",width=560,height=560>


## References
- http://www.musicdsp.org/files/Audio-EQ-Cookbook.txt
