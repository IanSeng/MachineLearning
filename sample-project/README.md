# General Set up 
## Conda requirement
- To create conda requirenment 
```
conda list -e > requirenments.txt
```
- To create an env with reuirements
```
conda create --prefix ./env --file requirements.txt
```

## Set up Conda 
- To activate conda 
```
conda activate
```

- Setting up conda environment 
```
conda create --prefix ./env pandas numpy matplotlib scikit-learn
```

- To activate a specific env
```
conda activate ../path/to/env
```
 
 - To list all conda env 
 ```
 conda env list
 ```

 - To install a package 
 ```
 conda install jupyter
 ```

 ## Set up jupyter notebook
 - open jupyter notebook
 ```
 jupyter notebook
 ```