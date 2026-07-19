## Knowledge Questions

### Databases

SQL vs NoSQL — when would you choose one over the other?
What is database indexing, and why does it speed up reads but slow down writes?
What's the difference between horizontal and vertical scaling?
What is sharding? What are common sharding strategies (range-based, hash-based)?
What is database replication? Master-slave vs master-master?
What are ACID properties?
What is the CAP theorem, and can you give a real example of a system choosing CP vs AP?
What is eventual consistency vs strong consistency?
What's a database transaction, and what problems (dirty reads, phantom reads) can occur without proper isolation?

### Caching

What is caching, and where can you cache at different layers (client, CDN, app, DB)?
What are common cache eviction policies (LRU, LFU, FIFO)?
What's the difference between write-through, write-back, and write-around caching?
What is cache invalidation, and why is it "one of the two hard things in computer science"?
What is a CDN, and how does it improve latency?

### Messaging & async processing

What's the difference between a message queue and a pub/sub system?
Kafka vs RabbitMQ — what's the general difference in design philosophy?
What is idempotency, and why does it matter for retries?
At-most-once vs at-least-once vs exactly-once delivery — what's the difference?

### Scalability & reliability

What's the difference between horizontal and vertical scaling? (very common)
What is a single point of failure, and how do you eliminate one?
What's the difference between availability and reliability?
How do you calculate "nines" of availability (99.9% vs 99.99%)?
What is a rate limiter, and what algorithms exist (token bucket, leaky bucket, sliding window)?
What is backpressure?
What is a circuit breaker pattern, and why is it used?
What's the difference between synchronous and asynchronous communication between services?

### Architecture concepts

Monolith vs microservices — trade-offs?
What is an API gateway, and what problems does it solve?
What is service discovery?
What's the difference between orchestration and choreography in microservices?
What is idempotency in API design?
How do you handle versioning in an API?

### Estimation / fundamentals

How much storage does X take (they'll give you a scenario)?
What's the difference between latency and throughput?
What is consistent hashing, and why is it used instead of simple modulo hashing?
3 benefits of cloud vs on-prem and vice versa



## Classic "design X" questions

### Social/content platforms

Design Twitter/X (feed generation, fan-out)
Design Instagram (media storage, feed, follow graph)
Design TikTok/YouTube (video upload, transcoding, streaming)
Design a news feed system

### Messaging & real-time

Design WhatsApp/a chat application (message delivery, online status, group chat)
Design a notification system
Design a live comments/chat feature for streaming

### Storage & infrastructure

Design a URL shortener (bit.ly) — often the "hello world" of system design
Design a distributed key-value store
Design a distributed cache (like Redis)
Design a rate limiter
Design a distributed file storage system (like Dropbox/Google Drive)
Design a distributed job scheduler / task queue

### Search & discovery

Design a search autocomplete/typeahead system
Design a web crawler
Design a search engine (simplified)

### Location & logistics

Design Uber/Lyft (ride matching, location tracking)
Design Google Maps / a ride-sharing ETA system
Design a food delivery system (DoorDash)

### Commerce & booking

Design an e-commerce checkout/inventory system
Design a ticket booking system (Ticketmaster) — handles high contention
Design a hotel/flight booking system (like Airbnb)

### Other frequent ones

Design a payment system
Design a leaderboard
Design a parking lot system (more OOP-flavored)
Design an ad click aggregation/analytics system
Design a video conferencing system (Zoom)