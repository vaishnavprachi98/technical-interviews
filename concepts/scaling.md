# Scalability

By Scaling horizontally, you are spinning up more _instances_ of the same application. (Vertical Scaling is when you add more resources to the server).
It is more cost efficient in the long run, as you don't necessarily need the resources all the time.

Cloud is good for scalability from a business/developer point of view as it has the property of being elastic where you can grab more machines (scale out horizontally) when under heavy load and reduce under low load making it more computationally efficient for the cloud provider and thus cheaper for the business.

Things to keep in mind to scale
- keep code base clean (enforce conventions)
- data layer (pick a good database such as datastore, also keep in mind sharding the database later on )
- load balance

> **Datastore** Google Cloud Datastore is a NoSQL document database built for automatic scaling, high performance, and ease of application development. Cloud Datastore features include: Atomic transactions. Cloud Datastore can execute a set of operations where either all succeed, or none occur.

> **Sharding** A database shard is a horizontal partition of data in a database or search engine. Each individual partition is referred to as a shard or database shard. Each shard is held on a separate database server instance, to spread load. Separates very large databases the into smaller, faster, more easily managed parts called data shards. The word shard means a small part of a whole.

If you think of a SQL database with name as the primary key, you could shard it by putting the first A-M names into one database and then the rest N-Z names in another. Here you would be partitioning the database horizontally keeping all columns for each row.
It also needs to be able to figure out what shard to look for what data fast, in this basic example you can just check what letter the name starts with.

> **Load balancer** A load balancer acts as the “traffic cop” sitting in front of your servers and routing client requests across all servers capable of fulfilling those requests in a manner that maximizes speed and capacity utilization and ensures that no one server is overworked, which could degrade performance.

## REST and Scalability

Sticking to REST makes it easier to scale as following REST means you don't store session state. Storing session state is really bad for scaling horizontally as it means the specific instance of your application knows some information about the client's session. If you spin up another instance that won't know that state of the client session and so you have created a bottle neck.

I think in general following REST and using microservices also helps scale because it enforces a convention and allows you to swap services in and out.

Resources:
- [Scalling web applications](https://www.quora.com/Whats-the-best-way-to-learn-how-to-scale-web-applications)

## How does Facebook scale?

- loose coupled architecture that can scale well horizontally
- move fast
- small incremental changes

> application architecture has very few choke points and by adding more servers, they can handle more users. Such an architecture would scale well in any language.

Sources:
- https://www.facebook.com/notes/facebook-engineering/scaling-facebook-to-500-million-users-and-beyond/409881258919/
- https://www.quora.com/How-does-Facebook-scale-their-application-in-PHP