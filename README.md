# No bullshit ElasticSearch and ELK

## Preparations

First if you are on Linux it's ideal as I'll use Ubuntu myself.
Windows is "mostly" fine. MacOS can be as easy as Linux but it's your call I never used ElasticSearch there.

Dependencies and quick checks. The full list of downloads  is:
- [Python 3](https://www.python.org/downloads/) - download from website if you are on Windows
- Java, use packages on Linux, homebrew on MacOS and install from Oracle on Windows
- [ElasticSearch](https://www.elastic.co/downloads/) use ZIP for Windows, tar.gz for Linux/MacOS. Use any version you'd like in 6.x line.
- curl or other HTTP client - GUI, console or browser extensions
- code editor as we don't need IDE, notepad might work but something better is preferable.


## Quick preflight checks

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


# This should show quite chatty log that shows good info, really good debugging aid. 
elasticsearch-6.3.0/bin/elasticsearch


# Elasticsearch log will shows the following cool stuff and more:
# state of cluster as it comes up, plugins, system settings 
# and warnings that should be all adressed before going
# to production, usually. 
#
# Keep it running! Open new window or tab as needed but keep this one.
#
# We will look in these logs for debugging later if needed.
# Quite probably, yes and more then once! ;)
#


# Alternative is to use sysyemd if you'd like to run it as a service
# but at least 1-2G (the more the better up to ~16Gb) would be needed to run it. 
# .deb package should install it like that. Then:
systemctl start elasticsearch # it may use other service name, I did not try .deb package

# In any case - test local ElasticSearch with curl or wget or httpie or Postman ...
# (you can also use dev box hostname instead if failed to install locally)
curl localhost:9200
```

For recent Ubuntu this "spell" should work well:

```bash
sudo apt install openjdk-8-jdk-headless python3 python3-pip python3-dev
pip install --user requests # to not pollute system's libs unless you have it already
```

## Advanced stuff to try

 For those on old laptops or maybe on big iron: you can tune the size of heap and other JVM option in a file config/jvm.options (shocking, I know). In fact I suggest also to remove all -XX:CMSSomeCMSStuff and -XX:Pretouch. The latter is super important in producation but if you disable it you will get JVM to commit more memory as needed not upfront. Of course in production, you'd rather do everything upfront and "pretouched", that is wired to RAM and in fact ElasticSearch will also try to _lock_ it in RAM if it has enough permissions.

*I highly recommend everybody to _find a way_ to get ElasticSearch _permissions and ulimits_ to lock all of JVM Heap in RAM, you won't believe the kind of shit that may happen on a big machine with 128Gb of RAM that _still has swap space enabled_ and, of course, ElasticSearch that has 64Gb  is quite easily choosen to swap out to disk. Why the fuck no? WE only have 58Gb to spare - swap that sucker out. And before you ask - no, it wasn't funny, not a single bit of fun.*

Bonus points: I will actually do all of that stuff using GraalVM to run ElasticSearch instead of "canonical" HotSpot + OpenJDK build from Oracle (it's just that or pretyy close this days).

For the brave, running on GraalVM, Linux:

```bash
# Linux-only and x86_64 like GraalVM itself (for now but might stay like that until 2019-2020)

# First - kill all of CMS collector options and switches, GraalVM only sports G1 GC
#
# Here is a simple Unix command-line spell version of that:
sed -i -r 's/-XX:.*CMS.*//g'

# Secondly you may tweak options in config/jvm.options yourself
# I highly recommend to comment-out this one: -XX:+AlwaysPreTouch
# Since that would rezerve 1G (or more as you choosen) upfront and
# it may not use it but you'd loose that RAM right off the gate.

# Lastly start it with your copy of GraalVM:
JAVA_HOME=~/graalvm-ce-1.0.0-rc2 bin/elasticsearch

```

If you have RAM, then start multiple ElasticSearch servers on same host, they do auto-join, so you can also test what happens when say 1 out of 3 crashes. They will auto-pick ports 9201, 9202..

```bash
# Nothing special, I just copy original directory to a new place with all permission intact
cp -rp elasticsearch-6.3.0 elasticsearch-node-1
# do the above as many times as you can/like ...
# and then - clear data directory in each of them before(!) starting
# data directory is is empty on fresh download but gets initialized on first start,
# watch out for this(!) or waste time looking at funny logs, and even then they got better lately

# command is untested but should work with or without minor tweaks
# where N is a number of your copies named in the above notation of elasticsearch-node-[0-9]
#
for n in 1 2 ... N ; do elasticsearch-node-$n/bin/elasticsearch > node-$n.log 2>&1 & ; done
# it should start a bunch of elasticsearch nodes each writing stdout logs to a separate file
```

And with that setup stuff is *mostly* covered let's go over to [FAQ](FAQ.md), learn the minimum theory. And then (finally!) [dive into *no bullshit* practice](ch1.md)!
