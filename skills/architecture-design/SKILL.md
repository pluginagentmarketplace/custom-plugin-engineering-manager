---
name: architecture-design
description: Master system architecture, API design, and design patterns. Learn distributed systems, scalability, and software design principles. Use when architecting systems or designing APIs.
---

# Architecture & System Design Skill

## Quick Start

System architecture is the high-level design of how a system is structured and components interact.

### Simple Monolithic Architecture

```
User Interface (Frontend)
        |
    API Gateway
        |
    Service Layer
        |
    Data Access Layer
        |
    Database
```

### Microservices Architecture

```
User Interface
    |
    +-- API Gateway
        |
        +-- User Service
        +-- Product Service
        +-- Order Service
        +-- Payment Service
        |
    Database (per service)
```

### REST API Design

```
Resource-oriented design:
- GET /api/users          (list users)
- GET /api/users/:id      (get specific user)
- POST /api/users         (create user)
- PUT /api/users/:id      (update user)
- DELETE /api/users/:id   (delete user)
```

### Design Patterns - Observer Pattern

```python
class Subject:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def notify(self, event):
        for observer in self._observers:
            observer.update(event)

class Observer:
    def update(self, event):
        print(f"Received event: {event}")
```

## Technologies & Concepts

### Architectural Patterns
- **Monolithic**: Single, unified application
- **Microservices**: Small, independent services
- **Serverless**: Event-driven functions
- **Event-Driven**: Message-based communication
- **CQRS**: Separate read and write models
- **API-Gateway**: Single entry point

### Scalability Techniques
- **Horizontal Scaling**: Add more servers
- **Vertical Scaling**: Increase server capacity
- **Load Balancing**: Distribute traffic
- **Caching**: Reduce database load
- **Database Sharding**: Distribute data
- **Read Replicas**: Multiple read databases

### Design Patterns

**Creational Patterns:**
- Singleton: One instance of a class
- Factory: Create objects without specifying classes
- Builder: Construct complex objects step-by-step
- Abstract Factory: Create families of objects

**Structural Patterns:**
- Adapter: Make incompatible interfaces work together
- Decorator: Add behavior to objects dynamically
- Facade: Provide simplified interface
- Proxy: Substitute for another object

**Behavioral Patterns:**
- Observer: Notify multiple objects of state changes
- Strategy: Encapsulate algorithms
- Command: Encapsulate requests as objects
- State: Change behavior based on state
- Factory Method: Create objects in subclasses

### SOLID Principles
- **S**ingle Responsibility: One reason to change
- **O**pen/Closed: Open for extension, closed for modification
- **L**iskov Substitution: Subtypes must be substitutable
- **I**nterface Segregation: Client-specific interfaces
- **D**ependency Inversion: Depend on abstractions

### API Design

**REST Principles:**
- Resource-oriented (nouns, not verbs)
- Stateless
- Client-server separation
- Cacheable responses
- Uniform interface

**GraphQL:**
- Query language
- Single endpoint
- Client-specified data needs
- Real-time subscriptions
- Strong typing

**API Versioning:**
- URL versioning: /api/v1/resource
- Header versioning: Accept: application/vnd.api+v1
- Content negotiation

### Distributed Systems

**CAP Theorem:**
- Consistency: All replicas have the same data
- Availability: System is always available
- Partition Tolerance: System works despite network partitions

**Concepts:**
- Service Discovery
- Load Balancing
- Circuit Breakers
- Retry Logic
- Distributed Tracing
- Message Queues

### Database Design

**Normalization:**
- 1NF: No repeating groups
- 2NF: Partial dependencies removed
- 3NF: Transitive dependencies removed
- BCNF: Boyce-Codd Normal Form

**NoSQL:**
- Document: MongoDB, CouchDB
- Key-Value: Redis, DynamoDB
- Column-Family: Cassandra, HBase
- Graph: Neo4j, ArangoDB

### Code Quality & Design

**Principles:**
- DRY (Don't Repeat Yourself)
- KISS (Keep It Simple, Stupid)
- YAGNI (You Aren't Gonna Need It)
- Clean Code: Readable, maintainable code

**Code Review:**
- Functionality: Does it work?
- Design: Is it well-designed?
- Testing: Are there adequate tests?
- Security: Are there vulnerabilities?
- Performance: Could it be faster?

## Learning Resources

- **System Design Primer**: https://github.com/donnemartin/system-design-primer
- **Refactoring**: https://refactoring.guru/
- **Design Patterns**: https://www.patterns.dev/
- **SOLID Principles**: https://stackify.com/solid-design-principles/
- **API Design**: https://restfulapi.net/

## When to Use This Skill

- Designing system architecture
- Designing and documenting APIs
- Improving code quality
- Implementing design patterns
- Optimizing performance
- Planning scalability
- Making architectural decisions
- Code review and mentoring
