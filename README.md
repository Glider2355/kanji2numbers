# kanjinumbers

## エンドポイント
### トップページ 
https://kanji2numbers.herokuapp.com/
### number2kanji(アラビア数字→漢数字)
https://kanji2numbers.herokuapp.com/v1/number2kanji/{変換元のアラビア数字}
### kanji2number(漢数字→アラビア数字)
https://kanji2numbers.herokuapp.com/v1/kanji2number/{変換元の漢数字}

## 注意点
- herokuは30分間アクセスがないとスリープモードに入るため、初回のアクセスは時間がかかります。  
- kanji2numberにてエラーが起きた際は漢数字を以下のURLからエンコードしてください。  
https://tech-unlimited.com/urlencode.html

## HTTPステータスコード
200: 正常  
204: 変換できない入力
