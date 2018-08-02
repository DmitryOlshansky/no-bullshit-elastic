## Terms of Insertorella competition

Minimual contest honesty agreement is required to participate:

I hereby declare that my results as submitted are correct and I *did wait for refresh to complete* in my solution.
Timings should be reproducible on the same hardware using same software.

For the constest we use `uploader` term for an application(s) that does upload of documents 
and `ES` for ElasticSearch (ES).

### Rules

Pick whatever tools you have mastered, except that:
- only single machine is used for uploaded and ES
- CPU is listed in Passmark and it's score is correctly presented in summary
- you may use any JVM options but if you modified your `config` directory it must be part of submission
- submission is a PR to add a folder there + add a line in this file

A submission should have a simple run.sh that *at least* does some things - create index with mappings, call uploaded and measures time of insert, and time of refresh, validates number of documents in index via `localhost:9200/_cat/indices`. BAT files from Windows is also fine, no run.sh/run.bat is shameful.

Dataset is sadly logs from MVNO QA and are not to be shared or uploaded anywhere.
I'll post the files to Slack. It will be 4 of about 1Gb files, one per host for total of roughly 4Gb.
Hint: you need at least 10Gb of total RAM to hit anywhere close to highscores.

Anything in range 16+ Gb is considered fair, it will be interesting to see if you could cheat by using more RAM.
Hint: pagecache is a thing on Linux and Windows, so once you have read all of these files, they stay in RAM...

Since my CPU (i7-6700) is so close to 10000 Passmark points, I'll use it as our unit.

Pro Tips:
 - take a look at who is using how much of CPU, your `uploader` should be at least 50:50 with elasticsearch to be fast, less is better
 - try using more or less memory both for your app and for elastic, more or less threads etc.
 - I/O is more of a problem with "big" dataset still run at least a once before gonig for results to ensure page cache is hot

We compute score as estimate of # of events per second normalized by CPU passmark score.
My machine has 10010 score so I'm using it as a unit:

```python
# for small logs
score = 231500 / ( 10000 / pass_mark_score * elapsed)
# for big logs
score = ??? / ( 10000 / pass_mark_score * elapsed)
```

### Sprint (small logs)


| Name     | Author           | Score | Elapsed  | CPU rating | Language | OS version         | Elastic version | JVM for ES           | 
|----------|------------------|-------|----------|------------|----------|--------------------|-----------------|----------------------|
| baseline | Dmitry Olshansky | 1258  | 3:04.01  |  10010     | Python3  | Ubuntu 4.15.0-29   | 6.3.2           |  Oracle 10.0.1       |




### Marathon (big logs)


| Name     | Author           | Score | Elapsed  | CPU rating | Language | OS version         | Elastic version | JVM for ES           | 
|----------|------------------|-------|----------|------------|----------|--------------------|-----------------|----------------------|
| baseline | Dmitry Olshansky | ???   | ???      |  10010     | Python3  | Ubuntu 4.15.0-29   | 6.3.2           |  Oracle 10.0.1       |

