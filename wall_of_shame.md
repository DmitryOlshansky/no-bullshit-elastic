#Wall of Shame

## Products that awfully fail the full-text search test


### Apple

*Apple Music* as of  _2018-06-26_  

Almst all attempts to do even slightly fuzzy search fail which scares the shit out of me. They did FaceID but...

 Bllions of dollars, and 1000's of great engineers, and yet *crapy shit* instead of sensible *full-text search*. 
 
 My favorite "Cold lay" - finds "lay me down" -> some other track that is not even "prefix correct" for my query!
 On the other hand Yandex music would first finds some "Cold ..." band which is fine actually.

 ### Pocket. Former "Read it later" as of _2018

 Does only plain stupid prefix search. Not even substring!!!

 It's called `strncmp` using `strlen` of smallest of 2 strings, i.e. even in low-level C it's trivial.
 It's not even a search but sadly input box is advertised as such.