# Table of Contents
1. [Intro. Motivation](#Intro)
2. [Design](#design)
    1. [Third Example](#third-example)
    2. [Security and privacy](#fourth-examplehttpwwwfourthexamplecom)
3. [Optimization]
    1. [Cache](#Cache)
4. [Aftermath](#A) 



## Intro

AutoModel was popularized by [HuggingFace Transformers]().

It fasten adaptation with new models and ML approaches. 

```python
from transfrosmers import BartModel
```

What's more it unifies interface of model call, which simplifies inference.

## Design 


Current design adapts practices from HuggingFace in simple two-agents model:
- s3Manager 
- Model

New model should implement a way of storage on s3. 

```python
class AbstractModel:
    def upload_model():
```

This design comes from fact that models differs much.

Users of registry 

### User accustomization

Learning models is now our responsibility:

'''python
from automodel import CatboostAutoModel

CatboostAutoModel.from_configs().learn(dataset='iris')
'''

Moreover, it provides serving options
```
CatboostAutoModel()
```

This might ease an year work of analyst in one-liner:

```python
CatboostAutoModel.from_configs('bayes_opts').learn(dataset='iris').serve('1234').to_dag('iris_pipeline')
```

### Cache

Uploaded models are stored in user's `~/.cache` folder.
It relaxes stress on s3

## Aftermath

Design doc was brought in hope for ease workflow of engineers and scientists. Asthereforementioned 









