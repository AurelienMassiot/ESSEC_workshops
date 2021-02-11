# Data visualization

### What is it ?

Data visualisation workshop which took place during February 2021. The objective was to show how to make data visualization with Python easily.

### notebooks

* **terrorism.ipynb**: explore a terrorism dataset to visualize geographical data.

### Requirements

**Python libraries**:
```bash
$ pip install plotly pandas pycountry
```
Basemap is a little bit tricky to install, you may check this forum for a solution [StackOverflow](https://stackoverflow.com/questions/42299352/installing-basemap-on-mac-python).

As Plotly is used, you may need to increase i/o in your notebook so that it does not crash, using iopub_data_rate_limit` option:
```
jupyter notebook --NotebookApp.iopub_data_rate_limit=1000000000
```

**Datasets**
* [Kaggle - Global Terrorism Database](https://www.kaggle.com/START-UMD/gtd)

