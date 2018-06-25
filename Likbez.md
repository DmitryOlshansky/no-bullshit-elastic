## No bullshit ElasticSearch

Why no bullshit?

Because I'm tired to FUCK(!) of lectures that either assume you can't youself
download stuff from internet and run it, then try 5 toy examples and feel good.

Or, for instance, as a second option - post tons of mostly relevant theoretical stuff,
and once you are intimidated and confused sell you something: a service, a subscription,
more lectures (and shitty, really "placebo" stuff at best), and finally sell you a product
that you'll spend next few years getting rid off.

So my approach - no bullshit, no shame and no useless crap.

Real facts, real data, real examples and and near-full improvisation in delivery. I want to do stuff that you (the audience) want with ElasticSearch (for now ES, later - anything good goes).

### Search is not only full-text 

Even more to the point: 
almost anything else is 10x of code/value/etc
full-text search is the last or at least a minor 
machinery detail in the process of Google/Yandex/etc. level search.

But lexical-only, effectively almost only token based stuff that
what ElasticSearch and Solar and Sphinx are. Of all three - ElasticSearch,

### Search is not magic but may feel like magic if you know your tool well

To say it again, a 100500-th time probably. Search is not magic.
Search is not magic. Magic is magick ;)

More to the point - so-called full-text search is nothing but:

1. An inverted index - a datastructure or rather an appraoch to build an index "in reverse", from content to ids of documents, that are usualy the keys in say RDBMS.

2. 