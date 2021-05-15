# ToyPythonML

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

### /EM/predict
### /SVM/LinearSVC/predict

#### example
```sh
curl --location --request GET 'http://localhost:5000/EM/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "train":  [["x","x","label"],["x","x","label"],["x","x","label"]],
    "test": [["x","x","label"],["x","x","label"],["x","x","label"]]
}'
```
>return
```sh
{
    "score": 0,
    "status": "success",
    "yPredict": []
}
```