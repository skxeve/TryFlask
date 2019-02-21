# GAE 2nd generation

python3.7が動くのでテストも兼ねて

## `__name__` について

どうも`__main__`ではない模様

どういうロジックで動いているのかは謎だが、普通のモジュールのように扱われる模様


## ログについて

flask標準のロガーで問題なくGAE上のログに残せる


## flake8

文法チェッカー的なもの。動作上は必要ない。

```
$ flake8 main.py
```

## キューの作成

`queue.yml`を使う方法と、`gcloud beta`コマンドで作成する方法があるらしい

`gcloud beta`コマンドで作成するとこんな感じになる

```
$ gcloud beta tasks queues create-app-engine-queue queue-name
WARNING: You are managing queues with gcloud, do not use queue.yaml or queue.xml in the future. More details at: https://cloud.google.com/cloud-tasks/docs/queue-yaml.
Created queue [queue-name].
```

続けてキューの対象サービス指定、これしないとdefaultに行っちゃう

```
$ gcloud beta tasks queues update-app-engine-queue queue-name --routing-override=service:flaskpy
WARNING: You are managing queues with gcloud, do not use queue.yaml or queue.xml in the future. More details at: https://cloud.google.com/cloud-tasks/docs/queue-yaml.
Updated queue [queue-name].
```
