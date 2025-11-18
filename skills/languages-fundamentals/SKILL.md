---
name: languages-fundamentals
description: Master programming languages and computer science fundamentals. Learn data structures, algorithms, mathematics, and version control. Use when learning new languages or reinforcing CS concepts.
---

# Languages & Computer Science Fundamentals Skill

## Quick Start

Programming languages are the tools to express algorithms and solve problems. Understanding fundamentals helps you learn any language.

### Python Basics

```python
# Variables and data types
name = "John"
age = 30
height = 5.9

# Lists and loops
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num * 2)

# Functions
def greet(name):
    return f"Hello, {name}!"

# Classes (OOP)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}"
```

### JavaScript Basics

```javascript
// Variables
const name = "John";
let age = 30;

// Arrays
const numbers = [1, 2, 3, 4, 5];
numbers.forEach(num => console.log(num * 2));

// Functions
const greet = (name) => `Hello, ${name}!`;

// Objects (similar to classes)
const person = {
    name: "John",
    age: 30,
    greet() {
        return `Hi, I'm ${this.name}`;
    }
};

// Async/Await
async function fetchData() {
    const response = await fetch('/api/data');
    return response.json();
}
```

### Git Basics

```bash
# Initialize repository
git init

# Add changes
git add .

# Commit
git commit -m "Initial commit"

# Create branch
git branch feature-branch
git checkout feature-branch

# Merge back
git checkout main
git merge feature-branch

# Push to remote
git push origin main
```

## Technologies & Concepts

### Programming Languages

**Python:**
- Simple, readable syntax
- Great for data science and web development
- Libraries: NumPy, Pandas, Django, Flask
- Paradigms: OOP, functional, procedural

**JavaScript:**
- Web browser language
- Node.js for server-side
- Asynchronous and event-driven
- Frameworks: React, Vue, Angular

**Java:**
- Enterprise standard
- Strong typing and OOP
- JVM platform
- Frameworks: Spring, Hibernate

**Go:**
- Concurrent and efficient
- Built for cloud and systems
- Simple syntax
- Excellent networking libraries

**Rust:**
- Memory-safe without garbage collection
- High performance
- Ownership and borrowing system
- Growing ecosystem

### Computer Science Fundamentals

**Data Structures:**
- Arrays: Fixed-size, indexed collections
- Linked Lists: Nodes with pointers
- Stacks: LIFO (Last In, First Out)
- Queues: FIFO (First In, First Out)
- Trees: Hierarchical structures
- Graphs: Connected nodes
- Hash Tables: Key-value storage

**Algorithms:**
- Sorting: Bubble, Quick, Merge, Heap
- Searching: Linear, Binary
- Graph Algorithms: BFS, DFS, Dijkstra
- Dynamic Programming: Optimization problems
- Greedy Algorithms: Local optimization

**Complexity Analysis:**
- Big O Notation
- Time Complexity: How runtime grows
- Space Complexity: How memory grows
- Optimizing algorithms

### Mathematics for Programming

**Discrete Mathematics:**
- Set Theory: Collections and operations
- Logic: Boolean algebra, truth tables
- Combinatorics: Counting and permutations
- Graph Theory: Nodes, edges, paths

**Linear Algebra:**
- Vectors: Direction and magnitude
- Matrices: 2D data structures
- Matrix Operations: Multiplication, inversion
- Eigenvalues and Eigenvectors

**Calculus (for ML/AI):**
- Derivatives: Rate of change
- Gradients: Direction of steepest ascent
- Optimization: Finding minimums/maximums

**Probability & Statistics:**
- Distributions: Normal, Poisson, Binomial
- Hypothesis Testing: Validating assumptions
- Regression: Predicting values
- Correlation: Measuring relationships

### Version Control (Git)

**Basic Concepts:**
- Repository: Project storage
- Commit: Save state
- Branch: Parallel development
- Merge: Combine branches
- Conflict Resolution: Fixing merge conflicts

**Workflows:**
- Git Flow: Multiple branches per feature
- GitHub Flow: Simple branch-based workflow
- Trunk-Based: Frequent integration

**GitHub/GitLab:**
- Pull Requests: Code review mechanism
- Issues: Bug tracking
- Actions: CI/CD automation
- Collaboration: Teams and permissions

### Security Fundamentals

**Cryptography:**
- Symmetric: Same key for encryption/decryption
- Asymmetric: Public/private key pairs
- Hashing: One-way functions
- Digital Signatures: Verify authenticity

**Web Security:**
- SQL Injection: Database attacks
- Cross-Site Scripting (XSS): JavaScript attacks
- Cross-Site Request Forgery (CSRF): Unauthorized actions
- Input Validation: Sanitize user input
- Output Encoding: Escape special characters

## Learning Resources

- **Python**: https://docs.python.org/3/
- **JavaScript**: https://developer.mozilla.org/en-US/docs/Web/JavaScript/
- **Data Structures & Algorithms**: https://www.geeksforgeeks.org/data-structures/
- **Git**: https://git-scm.com/doc
- **GitHub**: https://docs.github.com/

## When to Use This Skill

- Learning a new programming language
- Understanding algorithms and complexity
- Implementing data structures
- Version control and collaboration
- Optimizing code performance
- Understanding CS theory
- Security and cryptography basics
- Choosing the right language for a task
