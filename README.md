## No bullshit ElasticSearch and ELK workshop

### Preparations

First if you are on Linux it's ideal as I'll use Ubuntu myself.
Windows is "mostly" fine. MacOS can be as easy as Linux but it's your call I never used ElasticSearch there.

Dependencies and quick checks. The full list of downloads  is:
- [Python 3](https://www.python.org/downloads/) - download from [website]() if you are on Windows
- Java, use packages on Linux, homebrew on MacOS and install from Oracle on Windows
- [ElasticSearch](https://www.elastic.co/downloads/) use ZIP for Windows, tar.gz for Linux/MacOS. Use any version you'd in 6.x line.
- curl or other HTTP client, GUI, console browser-based ...,  anything goes that can send HTTP requests with JSON payload as GET or POST
- sane editor as we don't need IDE, notepad might work but something better is preferable.

For web access if you can't install anything local, I'll use MVNO dev Kibana at this address:
....

### Quick preflight checks

Linux

```bash
# this should print Python 3.5.x (or later, we don't use any advanced Python)
python3 --version

# this should show quite length log, keep it running and open in some window/tab
# we will look in these logs for debugging later
path-to-unpacked-elastic/bin/elasticsearch

# test local ElasticSearch or use dev box address instead
curl localhost:9200
```

Windows
```powershell
```

MacOS has python3 out of the box (I think?) or in the worst case install well-known Homebrew and install Python3 via Homebrew.
The rest should be the same.


The



