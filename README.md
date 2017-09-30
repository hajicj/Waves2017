# Waves2017
Making the Twitter birds sing...

```
# start the word2vec-api service:
# - Go to the word2vec-api directory,
# - Run:

python path/to/word2vec-api.py --model path/to/model/glove.twitter.27B.200d.header.txt --port 9001

# start NLP-Backend

FLASK_APP=nlp/server.py flask run

```


```bash
curl -H "Content-Type: application/json" -X POST -d '{"text":"My thoughts are with all those observing Yom Kippur, the holiest day of the Jewish year.","lang":"en"}' http://127.0.0.1:5000/api/analysis
```

# start the pipes

```
$ cd trumpet.pipes
$ node server.js
```

# watch the final output

http://localhost/path/to/waves2017/trumpet.output/