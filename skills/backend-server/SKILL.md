---
name: backend-server
description: Master backend and server-side development. Learn database design, API development, server architecture, authentication, and deployment. Use when building server applications, APIs, or distributed systems.
---

# Backend & Server Development Skill

## Quick Start

Backend development focuses on server logic, databases, and APIs. It powers the functionality behind user-facing applications.

### Simple Node.js Express Server

```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.json({ message: 'Hello, World!' });
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
```

### Simple Python Flask Server

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return {'message': 'Hello, World!'}

if __name__ == '__main__':
    app.run(debug=True, port=3000)
```

### REST API Design

```javascript
// GET - Retrieve
GET /api/users

// POST - Create
POST /api/users
{ "name": "John", "email": "john@example.com" }

// PUT - Update
PUT /api/users/1
{ "name": "Jane" }

// DELETE - Remove
DELETE /api/users/1
```

## Technologies

### Programming Languages
- **Node.js/JavaScript**: Async-first, event-driven
- **Python**: Simple syntax, great libraries
- **Java**: Enterprise-grade, strong typing
- **Go**: Fast, concurrent, cloud-native
- **Rust**: Memory-safe, high performance

### Web Frameworks
- **Express.js** (Node.js): Minimal, flexible
- **Flask/Django** (Python): Simple to full-featured
- **Spring Boot** (Java): Enterprise framework
- **Gin** (Go): Fast and lightweight
- **FastAPI** (Python): Modern, async-first

### Databases
- **SQL**: PostgreSQL, MySQL, MariaDB
- **NoSQL**: MongoDB, Redis, DynamoDB
- **Graph**: Neo4j, ArangoDB
- **Time-series**: InfluxDB, Prometheus
- **Full-text Search**: Elasticsearch

### API Design

**REST (Representational State Transfer)**
- Resource-oriented design
- HTTP methods (GET, POST, PUT, DELETE)
- Status codes (200, 201, 400, 404, 500)
- Versioning strategies
- Pagination and filtering

**GraphQL**
- Query language for APIs
- Single endpoint
- Client-specified data requirements
- Real-time subscriptions

### Authentication & Security
- **OAuth 2.0**: Delegated authentication
- **JWT**: Stateless authentication tokens
- **Sessions**: Server-side session management
- **API Keys**: Simple token-based auth
- **Encryption**: TLS/SSL, data encryption at rest
- **Rate Limiting**: Prevent abuse

### Architecture Patterns
- **Monolithic**: Single application
- **Microservices**: Small, independent services
- **Serverless**: Event-driven functions (Lambda, Cloud Functions)
- **Event-Driven**: Message queues and event streaming

### Message Queues & Async
- **RabbitMQ**: Message broker
- **Apache Kafka**: Event streaming
- **Redis**: In-memory data structure
- **Job Queues**: Celery, Bull, Hangfire

### Monitoring & Logging
- **Logging**: Winston, Bunyan, Logback
- **APM**: New Relic, Datadog, Elastic APM
- **Health Checks**: Readiness and liveness probes
- **Metrics**: Prometheus, StatsD

## Learning Resources

- **REST API Design Best Practices**: https://restfulapi.net/
- **GraphQL**: https://graphql.org/
- **Database Design**: https://www.postgresql.org/docs/
- **Node.js**: https://nodejs.org/docs/
- **Python Web Development**: https://docs.python-guide.org/

## When to Use This Skill

- Building REST or GraphQL APIs
- Database design and optimization
- Authentication and authorization
- Server architecture and scalability
- Asynchronous processing
- Error handling and logging
- API documentation
