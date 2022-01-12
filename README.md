# 以財換柴，錢拿出來

## 動機發想
* 我們回家有時候都會把零錢隨意地放在桌上，十分凌亂，所以我們想請療癒的柴柴幫我們收集零錢，讓零錢集中在一個地方，當然也有抖內箱的功能~看到可愛的柴柴誰不會想投個錢看看他呢?

* 既然是抖內箱，就想看看是哪位金主貢獻了無用的(寶貴的)錢錢~可愛的柴柴會一一記錄下來，但不會感謝你。柴柴只會拿錢，不會做事。

## 器材
* Raspberry Pi
* pi camera
* 馬達
* 導線
* 杜邦線
* 繼電器
* 調速器 
* 觸摸感應開關

## 功能
* 存錢
* 拍照

## pi 3  安裝套件

### telegram bot
```python = 
sudo pip install telepot
```
## 準備
Telegram bot

* 加 `BotFather`為好友
* `/newbot`建立機器人
* 幫機器人&user取名
<img src = "https://i.imgur.com/jlsATOI.jpg" width = "300px">

* `/token`查看token 

## 遇到的困難
* 網路環境不佳導致pi camera無法成功拍照、照片無法成功傳到Telegram bot

* 用程式控制電流輸出，不能使用樹梅派3.3V還有5V的接腳，而GPIO的接腳又不及3.3V與5V的接腳電流大，導致電流不足以驅動調速器和馬達

* 馬達因為焊接問題燒掉

* 電流腳位輸出電壓不穩

## 工作分配
* 謝沐恩 : pi camera&接腳連接

* 林庭君 : 開關、馬達&接腳連接

* 張淯婷 : 盒子組裝

* 嚴彥婷 : telegram bot、README