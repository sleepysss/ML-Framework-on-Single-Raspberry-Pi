兩個端點Device1和Device2
Device1是負責蒐集圖片並傳給Device2和使用Device2傳回的model來做預測
Device2則是負責訓練模型和把訓練好的模型提供給Device1

client.py:Device1執行,把圖片給server \
server.py:Device2執行,把Device1提供的圖片存起來 \
ML.py:Device2執行,訓練並儲存模型 \
send_model_back_server.py:Device1執行,取得Device2訓練好的模型 \
send_model_back_client.py:Device2執行,把模型提供給Device1 \
test_image_class.py:Device1執行,使用圖片來預測它的類別 \
