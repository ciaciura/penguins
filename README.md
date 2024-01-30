# penguins

## Runing the project

1. Create conda envirement

```
conda env create -f environment.yml
```

2. Activte the envirement

```
conda activate penguins-env
```

3. Run the project

```
kedro run -p preprocessing
kedro run -p modeling
uvicorn main:app
```

4. Running model visualisation

```
kedro viz run
```

5. Running experiment results

```
mlflow ui
```


## PyCharm Setup

[Setup link](https://docs.kedro.org/en/stable/development/set_up_pycharm.html)

