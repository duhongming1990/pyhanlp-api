# 0 安装依赖
```
pip install -r requirements.txt
```

# 1 基础组件

## 1.1 fastapi

- [ASGI wiki](https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface)
- [fastapi官网](https://fastapi.tiangolo.com/)
- [uvicorn官网](https://www.uvicorn.org/)

### Requirements

    Python 3.10

### Installation

```bash
pip install fastapi
pip install uvicorn
```

### Run it

```bash
uvicorn main:app --host 0.0.0.0 --port 8080
```

### Interactive API docs

- [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs)
- [http://127.0.0.1:8080/redoc](http://127.0.0.1:8080/redoc)




# 2 基础服务

## 2.1 jieba(废弃)

https://github.com/fxsjy/jieba
