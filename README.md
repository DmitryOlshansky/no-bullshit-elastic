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

# this should print something but better at least Java 8
java -version

# I/m using Java 10/11 (preview?) version as in bleeding edge OpenJDK on Ubuntu:
# ---------------------------------------
# openjdk version "10.0.1" 2018-04-17
# OpenJDK Runtime Environment (build 10.0.1+10-Ubuntu-3ubuntu1)
# OpenJDK 64-Bit Server VM (build 10.0.1+10-Ubuntu-3ubuntu1, mixed mode)
# ---------------------------------------
# Stay on bleeding edge or die trying!


# This should show quite chatty log (), 
# Keep it running! Open new window or tab as needed but keep this one.
#
# We will look in these logs for debugging later if needed.
# Quite probably, yes and more then once! ;)
#
path-to-unpacked-elastic/bin/elasticsearch

# Alternative is to use sysyemd if you'd like to run it as a service
# but at least 1-2G (the more the better up to ~16Gb) would be needed to run it. 
# Debian package should install it like that. Then:

systemctl start elasticsearch # it may use other service name, I did not try .deb package

# In any case - test local ElasticSearch with curl or wget or httpie or Postman ...
# (you can also use dev box hostname instead if failed to install locally)
curl localhost:9200
```

Windows
```powershell
```

MacOS has python3 out of the box (I think?) or in the worst case install well-known Homebrew and install Python3 via Homebrew.
The rest should be the same.


### First steps

With routine shit out of the way let's start playing with it on some basic stuff,
the kind you'll see on elastic.co en masse. 

Some imaginery collections of music (MP3s?) and the like, of course, only meta-data is stored.
A document in ElasticSearch is defined as JSON `document` or `object` but typically `document` even if it has 1 or 2 `fields`. See example for would-be MP3 track:

```
# First, I **cking want to see real meta-data on MP3s let's not brainwash people

```

*Typically - yeees, but you won't believe what kind of shit people dump in there as base64 or even worse eg as URL-encodede base64 of PNG, I kid you not.*

Here and later dumb ass facts from real life, if you see *text like that*, use your brain! and keep these things (tales) in mind or for future reference.


