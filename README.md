# ML-Framework-on-Single-Raspberry-Pi
 @step1 for client.py &server.py
client寄圖片給server(執行兩次,一次寄dog的,一次寄cat的),server接收圖片並把它存起來

註:
(1)cat:https://drive.google.com/drive/folders/1Sj3q_s2AlOPyY9t-p7vG_qdUjAOkHGrM?usp=sharing
	 dog:https://drive.google.com/drive/folders/1Luk8R1_fH9Q3-YDtMVn-6G6dfDxbBS7g?usp=sharing
	 各有200張
(2)執行完請自行關掉server,因為它會卡在accept()中出不去
(3)請自行更改程式中讀取圖片位置,ip address和port num
	
 @step2 for ML.py
執行ML的py,dataset為剛剛存的圖片,model採用VGG16的遷移式學習(準確率還不夠完善)

註:
(1)請自行更改程式中讀取圖片位置
