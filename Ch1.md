### First steps

With routine shit safely out of the way let's start playing with it on some basic stuff,
the kind you'll see on elastic.co en masse. 

Let's imagine imaginery (pun intended) collections of music (MP3s?) and the like, of course, only meta-data is stored. A document in ElasticSearch is defined as JSON `document` or `object` but typically `document` even if it has 1 or 2 `fields`. Fields are more or less what they are in JSON, except when they are not we'll get to that later. 

See a simple example for an MP3 track. *Real MP3 file meta-data ahead, you have been warned:*

```json
{
    ""
}
```

You can easily get it via, say `ffmpeg` tool on Linux, using `fprobe` cmd-line app.
A few more examples and you can make sensible search for Apple Music. 

*By the way Apply Music has clinically stupid search to put it plainly, I'd personally strangle the guys who made it and ashamed Apple on the whole world. And it keeps working like that forever, I swear as of today June 2018 it's a pile of garabage. If they keep it going, Yandex Music / Spotify / etc. will kill it by the next decade, mark my words - they mayeasily die around 2022-2023.*


# First, I **cking want to see real meta-data on MP3s let's not brainwash people

```

*Typically - yeees, but you won't believe what kind of shit people dump in there as base64 or even worse eg as URL-encodede base64 of PNG, I kid you not.*

Here and later dumb ass facts from real life, if you see *text like that*, use your brain(!) and/or keep these things (tales) in mind as a warning for future reference.


