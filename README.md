# ✨ToyPythonML✨
## Compatibility
make sure you installed api/requirements.txt
## Run project
```sh
git clone https://github.com/dinhvandai63/ToyPythonML.git
cd ToyPythonML/api
python3 api.py
```
> now Running on http://127.0.0.1:5000
## Function

-  /EM/predict
-  /SVM/LinearSVC/predict
-  /ML/:algorithm_name
```
    #algorithm_name is
    - GradientBoostingClassifier
    - AdaBoostClassifier
    - GradientBoostingRegressor
```
#### example
```sh
curl --location --request POST 'http://localhost:5000/EM/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "train":  [["x","x","labeled"],["x","x","labeled"],["x","x","labeled"]],
    "test": [["x","x","label"],["x","x","label"],["x","x","label"]]
}'
```
if test Set data is unlabel, you need to add label is nil
>return
```sh
{
    "score": 0,
    "status": "success",
    "yPredict": []
}
```