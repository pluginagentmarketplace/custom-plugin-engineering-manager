# Developer Roadmap Learning System - Claude Code Plugin

🚀 **Ultra-comprehensive learning system for 69 developer roles** with 7 specialized agents, interactive roadmaps, and skill-based learning paths.

## Overview

Transform your career with structured learning paths based on the legendary [roadmap.sh](https://roadmap.sh) collection. This Claude Code plugin provides:

- **69 Developer Roles** - Complete career paths across all specializations
- **7 Specialized Agents** - Expert guidance for different career tracks
- **7 Invokable Skills** - Hands-on learning for each category
- **4 Slash Commands** - Easy navigation and interaction
- **1000+ Learning Resources** - Books, courses, projects, documentation
- **500+ Hands-on Projects** - From beginner to expert level

## Quick Start

### Installation

```bash
# In Claude Code, add this plugin to your project:
# Option 1: Load from directory
/plugin-add ./developer-roadmap-plugin

# Option 2: Add to marketplace (coming soon)
/plugin-add marketplace://developer-roadmap-plugin
```

### First Steps

1. **Explore Available Roles**
   ```
   /browse-role
   ```

2. **Start Your Learning Journey**
   ```
   /learn
   ```

3. **Assess Your Knowledge**
   ```
   /assess
   ```

4. **View Detailed Roadmap**
   ```
   /roadmap [role-name]
   ```

## Features

### 7 Specialized Agents

Each agent is an expert in its domain:

1. **🎨 Frontend & Web Development**
   - 12 roles including React, Vue, Angular specialists
   - Web performance, testing, UX design

2. **🖥️ Backend & Server Development**
   - 15+ roles across Python, Java, Go, Node.js, PHP, Rust
   - APIs, databases, microservices

3. **☁️ Cloud & DevOps Infrastructure**
   - 10+ roles from Docker to Kubernetes to AWS
   - CI/CD, infrastructure as code, monitoring

4. **🤖 Data & AI Engineering**
   - 10+ roles for data engineers, ML engineers, AI specialists
   - LLM development, prompt engineering

5. **🏗️ Architecture & System Design**
   - 8+ roles for architects and senior designers
   - System design, API design, design patterns

6. **📚 Languages & Computer Science**
   - 25+ roles for programming languages
   - Data structures, algorithms, CS fundamentals

7. **🎯 Specialized Professional Roles**
   - 15+ unique roles: product managers, DevRel, technical writers
   - iOS, Android, game development

### 4 Slash Commands

- **`/learn`** - Choose a role and start your personalized learning journey
- **`/browse-role`** - Explore all 69 available roles and search by keyword
- **`/assess`** - Evaluate your knowledge and get recommendations
- **`/roadmap [role]`** - View detailed learning path for any role

### 7 Invokable Skills

Each skill provides hands-on learning for its category:

1. **frontend-web** - HTML, CSS, JavaScript, React, Vue, Angular
2. **backend-server** - Python, Java, Node.js, Go, databases, APIs
3. **cloud-devops** - Docker, Kubernetes, Terraform, AWS, CI/CD
4. **data-ai** - Data engineering, ML, AI, LLMs, prompt engineering
5. **architecture-design** - System design, API design, design patterns
6. **languages-fundamentals** - Programming languages, CS theory, Git
7. **specialized-roles** - Product management, DevRel, UX, mobile, games

## Plugin Structure

```
developer-roadmap-plugin/
├── .claude-plugin/
│   └── plugin.json                # Plugin manifest
│
├── agents/                         # 7 Specialized agents
│   ├── 01-frontend-web-agent.md
│   ├── 02-backend-server-agent.md
│   ├── 03-cloud-devops-agent.md
│   ├── 04-data-ai-agent.md
│   ├── 05-architecture-design-agent.md
│   ├── 06-languages-fundamentals-agent.md
│   └── 07-specialized-roles-agent.md
│
├── commands/                       # 4 Slash commands
│   ├── learn.md
│   ├── browse-role.md
│   ├── assess.md
│   └── roadmap.md
│
├── skills/                         # 7 Invokable skills
│   ├── frontend-web/SKILL.md
│   ├── backend-server/SKILL.md
│   ├── cloud-devops/SKILL.md
│   ├── data-ai/SKILL.md
│   ├── architecture-design/SKILL.md
│   ├── languages-fundamentals/SKILL.md
│   └── specialized-roles/SKILL.md
│
├── hooks/
│   └── hooks.json                # Automation hooks
│
├── config/
│   ├── agent-registry.json       # Agent mappings
│   └── role-database.json        # 69 roles database
│
├── README.md
└── LICENSE
```

## 69 Available Roles

### Frontend & Web Development (12)
Frontend, Frontend (Beginner), React, Vue, Angular, Next.js, HTML, CSS, JavaScript, UX Design, Web Performance, Testing

### Backend & Server Development (15+)
Backend, Backend (Beginner), Full-Stack, Python, JavaScript/Node.js, TypeScript, Java, Go, Rust, PHP, Kotlin, C++, Spring Boot, ASP.NET Core, Laravel

### Cloud & DevOps Infrastructure (10+)
DevOps, AWS, Kubernetes, Docker, Terraform, Linux, Cloudflare, SRE

### Data & AI Engineering (10+)
Data Engineer, Data Analyst, BI Analyst, DBA, Machine Learning Engineer, AI Engineer, AI Data Scientist, AI Agents, MLOps, Prompt Engineer

### Architecture & System Design (8+)
Software Architect, System Design, API Design, Design Patterns, Code Review, UX Design, Design System

### Languages & Fundamentals (25+)
Python, JavaScript, TypeScript, Java, Go, Rust, PHP, Kotlin, C++, HTML, CSS, SQL, Git, Shell/Bash, Cyber Security, Data Structures & Algorithms, Blockchain, Computer Science

### Specialized Professional Roles (15+)
Product Manager, Engineering Manager, DevRel, Technical Writer, iOS, Android, React Native, Flutter, Game Developer, Server-Side Game Developer

## Usage Examples

### Example 1: Career Switcher

```
User: "I want to become a backend developer"

/learn
→ Select: Backend & Server Development
→ Choose: Backend Developer (Beginner)
→ Get: 6-month personalized learning plan
```

### Example 2: Specialist Deepening

```
User: "I'm a frontend developer, how do I learn React?"

/browse-role react
→ See React specialist path details

/roadmap react --detailed
→ Get 6-month React mastery plan
```

### Example 3: Learning Assessment

```
User: "How good are my skills?"

/assess
→ Interactive assessment across all areas
```

## Plugin Specifications

- **Total Agents**: 7
- **Total Commands**: 4
- **Total Skills**: 7
- **Total Roles**: 69
- **Estimated Total Learning Hours**: 1000+
- **Projects**: 500+
- **Resources**: 1000+

## Version

- **Plugin Version**: 1.0.0
- **Format**: Claude Code Plugin Format (Official)
- **Compatibility**: Claude Code 1.0+
- **Last Updated**: November 18, 2024

## License

MIT License - See LICENSE file for details

---

**Ready to Transform Your Tech Career?** 🚀

```
/learn        → Start your learning journey
/browse-role  → Explore all available roles
/assess       → Evaluate your knowledge
/roadmap      → View detailed learning paths
```

Happy learning! 📚✨