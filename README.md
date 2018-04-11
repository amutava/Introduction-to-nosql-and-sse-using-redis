# Introduction-to-nosql-and-sse-using-redis

This is a simple issues application that is implemented using python flask, and Redis database. In my quest to learn NoSQL databases I decided to build.

**Installation**
* Clone the repo.
* Install requirements using the command. `pip install -r requirements.txt`
* Run the application using the command. `python issues.py`
* On different terminal run the redis server. `redis-server`

**Why NoSql and why do they matter?**

I'm not trying to prove anything but I think it's key to know why we prefer certain technologies to others. When you here NoSQL then be ready for SQL. Relational databases vs non-Relational databases. Got it now?


**Case study**

Redis works on the concept of key-value pair. It provides the ability to store a  value inside a key. This data can be retrieved if you know the exact key used to store it. It follows the client-server architecture.

**Some features that make Redis outstanding** 

 **Speed** : It stores it's data in the primary memory(RAM). This makes it extremely fast. <br/>

 **Data Structures** : It supports a various data structures which include: Lists, strings, hashes, sets, sorted sets 
 <br/>

 **Atomic Operations** : Redis operations working on the different Data Types are atomic, so it is safe to set or increase a key, add and remove elements from a set, increase a counter.
 <br/>

 **Supported by various Languages** : It is supported by various languages.<br/>

 **Sharding** : It is very easy to distribute the dataset across multiple Redis instances, like other key-value store.

**Redis vs RDBMS** 
| Redis | RDBMS |

| -------- | ------------- | 

| Redis stores everything in primary memory. | RDBMS stores everything in secondary memory.  | 

|  In Redis, Read and Write operations are extremely fast because of storing data in primary memory. | In RDBMS, Read and Write operations are slow because of storing data in secondary memory. |

| Primary memory is in lesser in size and much expensive than secondary so, Redis cannot store large files or binary data. | Secondary memory is in abundant in size and cheap than primary memory so, RDBMS can easily deal with these type of files. | 

| Redis is used only to store those small textual information which needs to be accessed, modified and inserted at a very fast rate.If you try to write bulk data more than the available memory then you will receive errors. | RDBMS can hold large data which has less frequently usage and not required to be very fast. | 

**Redis vs Other Key-Value Stores**
* Redis is a different evolution path in the key-value databases where values can contain more complex data types, with atomic operations defined on those data types.
* Redis data types are closely related to fundamental data structures and are exposed to the programmer as such, without additional abstraction layers.
* Redis is an in-memory but persistent on disk database, so it represents a different trade off where very high write and read speed is achieved with the limitation of data sets that can't be larger than memory.
* Another advantage of in memory databases is that the memory representation of complex data structures is much simpler to manipulate compared to the same data structure on disk, so Redis can do a lot, with little internal complexity.
* At the same time the two on-disk storage formats (RDB and AOF) don't need to be suitable for random access, so they are compact and always generated in an append-only fashion.


