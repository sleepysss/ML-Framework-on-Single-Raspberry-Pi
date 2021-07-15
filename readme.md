兩個端點Device1和Device2 \
#Device1是負責蒐集圖片並傳給Device2和使用Device2傳回的model來做預測 \
#Device2則是負責訓練模型和把訓練好的模型提供給Device1

1.client_for_catIMG.py:Device1執行。把cat圖片給Device1 會每隔n分鐘送一輪 \
2.client_for_dogIMG.py:Device1執行。把dog圖片給Device1 會每隔n分鐘送一輪 \
3.server_for_catIMG.py:Device2執行。把Device1提供的cat圖片存起來 \
4.server_for_dogIMG.py:Device2執行。把Device1提供的dog圖片存起來 \
5.ML.py:Device2執行。訓練並儲存模型 \
6.send_model_back_server.py:Device1執行。取得Device2訓練好的模型 \
7.send_model_back_client.py:Device2執行。把模型提供給Device1 \
8.test_image_class.py:Device1執行。預測圖片的類別為貓或狗

dataset:https://drive.google.com/drive/folders/1m2X9OZiUGhK5khiDteMPDkz2pRpbrnp2?usp=sharing
