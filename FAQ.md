## No bullshit ElasticSearch

### Why no bullshit? What do you mean - no bullshit?

Because I'm tired to fucking damned ungodly ugly queuer(!) fuck(!!) of lectures that either *assume you can't youself download stuff from internet* and *run it*, then *try 5 toy examples* and *feel good*.

Or, for instance, as a second option - *post tons of mostly relevant* theoretical *stuff*,
and *once you are intimidated*, *tired* or *confused* *sell you something*: a service, a subscription, more lectures (and shitty, really "placebo" stuff at best), and finally *sell you a product* that you'll *spend next few years getting rid off*.

So my approach - no bullshit, no SMS or payment involed, no shame and no useless crap (for once!).

Jokingly but still almost on spot, it looks like this:

```
[English]

- Oh, it's simple to use may thetra-SQL-but-not-quite uber DB you just
and take an example from: demos/for-the-deaf-dumb-blind/simple.go

Aaaand thne the classic moment:

- Use, the source, Luke!

And then damned silence, not even a single sensible shit follows after that.
Like in one TV show, I just want to say: "Yo, Beatch!" in customary "Pinkman" voice.
```

Real facts, real data, real examples and and near-full improvisation in delivery. I want to do stuff that you (the audience) want with say ElasticSearch but maybe beyond. Later I may try a "No bullshit" style with something else. There are two problems, first - I must know that new stuff *very well*. Second it *must be useful to at least 7+ more people* among us.

### Search is not only full-text 

Even more to the point: 
almost anything else is 10x of code/value/etc
full-text search is the last or at least a minor 
machinery detail in the process of Google/Yandex/etc. level search.

But lexical-only, effectively almost only token based stuff that
what ElasticSearch and Solar and Sphinx are. Of all three - ElasticSearch.

### Search is not magic but may feel like magic if you know your tool well

To say it again, a 100500-th time probably. Search is not magic.
Search is not magic. Magic is magick ;)

More to the point - so-called full-text search is nothing but:

An inverted index - a datastructure or rather an appraoch to build an index "in reverse", from content to ids of documents, that are usualy the keys in say RDBMS.


### Goals of this workshop series?
 
1. I want to shame bad stuff and make at least half of you "experts" on full-text search. As if there is somthing special about it to begin with, really. It is SIMPLE, Google search is complex, but sensible full-text search is not.

2. More exploration, moar exploitation(!) and above of all it *must be fun*.

3. Real data - log filles. I think we can also get a bunch of MP3s (~10k is more then enough) and start searching over that with playback if you'd like... Make your own Yandex Music / Apple Music in 1.5h :)

4. I want more real examples, real fedback and real you. Show that you can think and have imagination for use cases of full-text search. I'm challenging you.

5. I'd like to stay simple and we'll have only as much code as we absolutely need. And sorry, no Scala or Monads. I don't need that ugly shit to show you the power of ElasticSearch. Particularly because I want us to be equal, including devops and other non-Scala people.

6. Again to *deliver a god damn point* - *ElasticSearch is a server, and no(!) Java and transport client is not(!) really faster*. Yes, I know it's *binary*, but no - it is not any faster in practice and awkward bitch to deal with. Again - there is nothing of value in using only Java/JVM language with ElasticSearch. Even fucking shellscript with curl can use it very well.

7. Make sure I say at least once, that *scripts in ElasticSearch are good but it's like transactions* - *you don't need them, untill you actually do*.

