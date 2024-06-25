## Char vs Varchar vs Text

1. Implemented a POC for understanding the storage difference in terms of bytes between different string column

![ ](image.png)



## Differences

1. Char(n) -> Fix length storage
2. Varchar(n) -> Upto n length storage
3. Text -> For larger strings and for this datatype we cannot have foreign check


### How long text stored on disk ?

1. For smaller string , it is stored inline
2. For larger string , it is stored on separate pages
3. Same things applied for varchar of length of varchar is large

Lookup for larger string column is slow because of multiple  read of pages from disk
