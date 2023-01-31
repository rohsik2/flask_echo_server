# flask_echo_server
프론트엔드에서 json 형태의 데이터가 올바르게 넘어가고 있는지 확인하기 위한 서버입니다.

# how to use

```
pip3 install -r requirements.txt
python3 ./echo.py
```

이후 아무 경로로 아무 method를 호출해서 보내시면 됩니다.
# request Example
```
POST /aa HTTP/1.1

{
    "this" : "is json"
}

```


# response Example
```
{
    "body": "{\n    \"this\" :\"is json\"\n}",
    "method": "POST",
    "path": "aa",
    "request": {
        "this": "is json"
    }
}

```