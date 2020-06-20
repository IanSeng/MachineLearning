# General Set up 
## Conda envirnment
- To create conda requirenment 
```
conda list -e > requirenments.txt
```

- To create an env with requirements
```
conda create --prefix ./env --file requirements.txt
```

- To create conda env file in yml 
```
conda env export --prefix env/ > environment.yml
```

- To create an environment (abc) from environment.yml
```
conda env create --file environment.yml --name abc
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

- To deactivate conda env 
```
conda deactivate
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
 - Open jupyter notebook
 ```
 jupyter notebook
 ```

 - To close jupyter
 ```
 control + c 
 ```

