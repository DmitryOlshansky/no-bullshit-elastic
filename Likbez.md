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

And then damned silence, not even a single sensible shit follows after that. Ever.
Like in one TV show, I just want to say: "Yo, Beatch!" in customary "Pinkman" voice.

[Russian, heavily altered but the same idea]

- Юзай сорцес, Люк! Я - твой отец!

Пиздец, все, добавить нечего - зановес!

...

Народ безмолствует.

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
