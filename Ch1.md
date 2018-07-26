### First steps

With routine shit safely out of the way let's start playing with it on some basic stuff,
the kind you'll see on elastic.co en masse. 

Let's imagine imaginery (pun intended) collections of music (MP3s?) and the like, of course, only meta-data is stored. A document in ElasticSearch is defined as JSON `document` or `object` but typically `document` even if it has 1 or 2 `fields`. Fields are more or less what they are in JSON, except when they are not we'll get to that later. 

We'll go with log files as an example. But first let's play with ElasticSearch by sending requests manually.

### 

```
GET http://localhost:9200/_cat/indices

###

POST http://localhost:9200/siebel/log
Content-Type: application/json

{
    "text": "\"sblproxy.proxy.package$PreventSiebelDdosException: Siebel is busy. Preventing ddos...\n \tat sblproxy.proxy.TokenizedProxyRouter$$anonfun$receive$1.applyOrElse(TokenizedProxyRouter.scala:46)\n \tat akka.actor.Actor.aroundReceive(Actor.scala:514)\n \tat akka.actor.Actor.aroundReceive$(Actor.scala:512)\n \tat sblproxy.proxy.TokenizedProxyRouter.aroundReceive(TokenizedProxyRouter.scala:19)\n \tat akka.actor.ActorCell.receiveMessage(ActorCell.scala:527)\n \tat akka.actor.ActorCell.invoke(ActorCell.scala:496)\n \tat akka.dispatch.Mailbox.processMailbox(Mailbox.scala:257)\n \tat akka.dispatch.Mailbox.run(Mailbox.scala:224)\n \tat akka.dispatch.Mailbox.exec(Mailbox.scala:234)\n \tat akka.dispatch.forkjoin.ForkJoinTask.doExec(ForkJoinTask.java:260)\n \tat akka.dispatch.forkjoin.ForkJoinPool$WorkQueue.runTask(ForkJoinPool.java:1339)\n \tat akka.dispatch.forkjoin.ForkJoinPool.runWorker(ForkJoinPool.java:1979)\n \tat akka.dispatch.forkjoin.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:107)\n 2018-05-18 14:08:59.474 [SiebelProxy-akka.actor.default-dispatcher-40] ERROR application - Request=/eaiib_enu/start.swe?SWEExtSource=SecureWebService&SWEExtCmd=Execute&UserName=ib&Password=***, Host: f5-prt-prod-sblproxy.tcsbank.ru, SOAPAction: \"document/http://siebel.com/CustomUI:GetMetaContactOptyList\", User-Agent: spray-can/1.3.3, X-Real-Ip: 10.218.7.134, Timeout-Access: <function1> failed and completedIn=1\n\""
}

###

DELETE http://localhost:9200/siebel/logs

###

GET http://localhost:9200/siebel/_search
Content-Type: application/json

{
    "query" : {
        "match" : {
            "text" : "ERROR"
        }
    }
}

###

GET http://localhost:9200/siebel
GET http://localhost:9200/_cat/indices

###

POST http://localhost:9200/siebel/log
Content-Type: application/json

{
    "text": "\"sblproxy.proxy.package$PreventSiebelDdosException: Siebel is busy. Preventing ddos...\n \tat sblproxy.proxy.TokenizedProxyRouter$$anonfun$receive$1.applyOrElse(TokenizedProxyRouter.scala:46)\n \tat akka.actor.Actor.aroundReceive(Actor.scala:514)\n \tat akka.actor.Actor.aroundReceive$(Actor.scala:512)\n \tat sblproxy.proxy.TokenizedProxyRouter.aroundReceive(TokenizedProxyRouter.scala:19)\n \tat akka.actor.ActorCell.receiveMessage(ActorCell.scala:527)\n \tat akka.actor.ActorCell.invoke(ActorCell.scala:496)\n \tat akka.dispatch.Mailbox.processMailbox(Mailbox.scala:257)\n \tat akka.dispatch.Mailbox.run(Mailbox.scala:224)\n \tat akka.dispatch.Mailbox.exec(Mailbox.scala:234)\n \tat akka.dispatch.forkjoin.ForkJoinTask.doExec(ForkJoinTask.java:260)\n \tat akka.dispatch.forkjoin.ForkJoinPool$WorkQueue.runTask(ForkJoinPool.java:1339)\n \tat akka.dispatch.forkjoin.ForkJoinPool.runWorker(ForkJoinPool.java:1979)\n \tat akka.dispatch.forkjoin.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:107)\n 2018-05-18 14:08:59.474 [SiebelProxy-akka.actor.default-dispatcher-40] ERROR application - Request=/eaiib_enu/start.swe?SWEExtSource=SecureWebService&SWEExtCmd=Execute&UserName=ib&Password=***, Host: f5-prt-prod-sblproxy.tcsbank.ru, SOAPAction: \"document/http://siebel.com/CustomUI:GetMetaContactOptyList\", User-Agent: spray-can/1.3.3, X-Real-Ip: 10.218.7.134, Timeout-Access: <function1> failed and completedIn=1\n\""
}

###

DELETE http://localhost:9200/siebel*

###

GET http://localhost:9200/siebel/_search
Content-Type: application/json

{
    "query" : {
        "match" : {
            "ts" : "2018-05-18 14:08:58.021"
        }
    }
}

###

GET http://localhost:9200/siebel

###

GET http://localhost:9200/siebel-2

###

PUT http://localhost:9200/siebel-3
Content-Type: application/json

{
    "mappings": {
        "log": {
            "properties": {
                "id": {
                    "type": "text"
                },
                "text": {
                    "type": "text"
                },
                "ts": {
                    "type": "date"
                }
            }
        }
    }
}
```

## Custom mappings

Can be defined before insertion:

```json
{
  "siebel": {
    "mappings": {
      "log": {
        "properties": {
          "id": {
            "type": "text"
          },
          "text": {
            "type": "text"
          },
          "ts": {
            "type": "text"
          }
        }
      }
    }
  }
}
```
