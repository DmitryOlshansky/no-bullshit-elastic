#Wall of Shame

## Products that awfully fail the full-text search test


### Apple

*Apple Music* as of  _2018-06-26_  

Almst all attempts to do even slightly fuzzy search fail which scares the shit out of me. They did FaceID but...

 Bllions of dollars, and 1000's of great engineers, and yet *crapy shit* instead of sensible *full-text search*. 
 
 My favorite "Cold lay" - finds "lay me down" -> some other track that is not even "prefix correct" for my query!
 On the other hand Yandex music would first finds some "Cold ..." band which is fine actually.

 ### Pocket (former "Read it later")

 Does only stupid prefix search, it's called `strncmp` on `strlen` of your query, i.e. even in low-level C it's trivial.
 It's not event a search sadly but advertised as such.