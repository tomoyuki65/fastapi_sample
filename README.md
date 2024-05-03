# FastAPIによるAPIのサンプル  
FastAPIによるAPI開発のサンプルです。  
  
## 機能一覧  
・ユーザー作成（POST /user）  
・ユーザー1件取得（GET /user/{uid}）  
・ユーザー更新（PUT /user/{uid}）  
・ユーザー論理削除（DELETE /user/{uid}）  
・ユーザーを論理削除データ含めて全件取得（GET /users）  
  
## 使用技術  
Python "3.12.3"  
FastAPI "0.110.2"  
sqlalchemy "2.0.29"  
Docker  
docker-compose  
MySQL "8.0.36"  
  
## 参考記事  
[・【FastAPI入門】Dockerで環境構築してPythonのAPIを開発する方法まとめ](https://tomoyuki65.com/how-to-use-fastapi)  