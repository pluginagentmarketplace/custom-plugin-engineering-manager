---
name: technical-decision-making
description: Master technical decision-making, architecture choices, technology evaluation, technical roadmaps, and technical strategy for engineering teams. Use when making architectural decisions or evaluating technologies.
sasmp_version: "1.3.0"
bonded_agent: 01-team-leadership-agent
bond_type: PRIMARY_BOND
---

# Technical Decision Making Skill

## Quick Start

Effective technical decisions balance multiple factors: team capability, business goals, scalability, cost, and risk.

### Architecture Decision Record (ADR) Template

```markdown
# ADR-001: [Title]
Date: [Date]
Status: [Proposed/Accepted/Deprecated]

## Context
[Explain the issue requiring decision]
[Background and constraints]

## Options Considered
### Option A: [Description]
- Pros: ...
- Cons: ...
- Effort: ...
- Risk: ...

### Option B: [Description]
- Pros: ...
- Cons: ...
- Effort: ...
- Risk: ...

## Decision
[Chosen option and why]
[Trade-offs accepted]

## Consequences
[Positive outcomes]
[Negative outcomes]
[Future implications]
```

### Technology Evaluation Framework

```
Criteria Weight Decision
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Team expertise       30%   ★★☆
Ecosystem maturity   25%   ★★★
Community support    15%   ★★★
Performance         20%   ★★☆
Cost                10%   ★★★
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Score                ★★★

Recommendation: [Based on scores]
```

## Core Concepts

### Architecture Patterns
- **Monolithic**: Single codebase, simple for small teams
- **Microservices**: Independent services, complex but scalable
- **Serverless**: Event-driven functions, pay-per-use
- **Event-Driven**: Asynchronous communication
- **API-First**: Design APIs before implementation

### Design Principles
- Single Responsibility Principle
- Separation of Concerns
- DRY (Don't Repeat Yourself)
- KISS (Keep It Simple)
- YAGNI (You Aren't Gonna Need It)

### Technology Evaluation
1. Define requirements (must-have vs. nice-to-have)
2. List alternatives
3. Evaluate against criteria
4. Assess team capability
5. Calculate cost and effort
6. Evaluate risk
7. Document decision

### Technical Debt
- Identifies as: quick fixes, outdated code, missing tests
- Manage by: quantify impact, prioritize paydown, prevent new
- Balance: feature work vs. improvement

## Tools & Templates

### Tech Stack Review Checklist
- Is it still the right choice?
- Community still active?
- Security updates current?
- Performance adequate?
- Team expertise current?
- Migration cost if changing?

### Technical Roadmap Template
- Q1: [Theme] - [Key initiatives]
- Q2: [Theme] - [Key initiatives]
- Q3: [Theme] - [Key initiatives]
- Q4: [Theme] - [Key initiatives]

## Common Decisions

**Build vs. Buy**
- Build if: unique, core capability, cost-effective
- Buy if: commodity, expensive to build, faster time-to-market

**Monolith vs. Microservices**
- Monolith: Small teams, simple domain, high cohesion
- Microservices: Large teams, complex domain, independent scaling

**Caching Strategy**
- Client-side: Reduce requests
- Server-side: Reduce database load
- CDN: Geographic distribution

## Resources

- "Building Microservices" - Sam Newman
- "The Art of Software Architecture" - Eoin Woods
- "Designing Data-Intensive Applications" - Martin Kleppmann
- "Release It!" - Michael Nygard
- Architecture Decision Records (ADRs)

## When to Use This Skill

- Major architecture decisions
- Technology selection
- System scaling issues
- Technical debt management
- Roadmap planning
- Design reviews
- Risk assessment
- Cost optimization
