# Engineering Manager - Professional Leadership Plugin

🚀 **Comprehensive engineering management toolkit** for technical leaders. Build high-performing teams, guide technical strategy, develop talent, and drive organizational excellence.

## Overview

Transform your engineering leadership with expert guidance, professional templates, and strategic frameworks. This Claude Code plugin provides:

- **5 Specialized Agents** - Expert guidance on people, strategy, hiring, culture, and growth
- **5 Invokable Skills** - Hands-on tools for team dynamics, technical decisions, hiring, performance, and culture
- **4 Slash Commands** - Management toolkit, expert guidance, team assessment, and strategic planning
- **100+ Templates & Frameworks** - Ready-to-use for management activities
- **500+ Best Practices** - From top engineering leaders and industry research

## Quick Start

### Installation

```bash
# In Claude Code, add this plugin:
/plugin-add ./custom-plugin-engineering-manager
```

### First Commands

1. **Get Management Tools**
   ```
   /manage
   ```
   Access templates, frameworks, and best practices

2. **Get Expert Guidance**
   ```
   /guide [challenge]
   ```
   Get advice on specific management situations

3. **Assess Your Team**
   ```
   /assess-team
   ```
   Evaluate team health and get recommendations

4. **Plan Strategy**
   ```
   /strategies [period]
   ```
   Create technical and organizational strategies

## Features

### 5 Specialized Agents

Each agent is an expert in engineering management:

1. **👥 Team Leadership & People Management**
   - Building high-performing teams
   - 1-on-1 meetings and mentoring
   - Delegation and empowerment
   - Conflict resolution
   - Psychological safety

2. **🏗️ Technical Strategy & Architecture**
   - Technical decision-making
   - Architecture selection
   - Technology roadmaps
   - Technical debt management
   - System design guidance

3. **📊 Hiring, Performance & Metrics**
   - Recruitment and hiring
   - Performance management
   - Goal-setting and OKRs
   - Data-driven decisions
   - Metrics and analytics

4. **🌱 Culture, Communication & Engagement**
   - Team culture building
   - Psychological safety creation
   - Communication strategies
   - Team engagement
   - Inclusion and belonging

5. **📈 Career Growth & Development**
   - Career path development
   - Individual development plans
   - Succession planning
   - Skill development
   - High-potential talent building

### 4 Slash Commands

- **`/manage`** - Access management tools, templates, and frameworks
- **`/guide`** - Get expert advice on specific management challenges
- **`/assess-team`** - Evaluate team health and get recommendations
- **`/strategies`** - Plan technical and organizational strategies

### 5 Invokable Skills

Each skill provides hands-on management tools:

1. **team-dynamics** - Team leadership, delegation, mentoring, communication
2. **technical-decision-making** - Architecture decisions, tech choices, roadmaps
3. **hiring-recruitment** - Recruiting, interviewing, hiring processes
4. **performance-management** - Reviews, goals, OKRs, metrics, feedback
5. **culture-engagement** - Culture building, safety, communication, engagement

## Plugin Structure

```
custom-plugin-engineering-manager/
├── .claude-plugin/
│   └── plugin.json                # Plugin manifest
│
├── agents/                         # 5 Specialized agents
│   ├── 01-team-leadership-agent.md
│   ├── 02-technical-strategy-agent.md
│   ├── 03-hiring-performance-agent.md
│   ├── 04-culture-engagement-agent.md
│   └── 05-growth-development-agent.md
│
├── commands/                       # 4 Slash commands
│   ├── manage.md
│   ├── guide.md
│   ├── assess-team.md
│   └── strategies.md
│
├── skills/                         # 5 Invokable skills
│   ├── team-dynamics/SKILL.md
│   ├── technical-decision-making/SKILL.md
│   ├── hiring-recruitment/SKILL.md
│   ├── performance-management/SKILL.md
│   └── culture-engagement/SKILL.md
│
├── hooks/
│   └── hooks.json                # Automation hooks
│
├── README.md
└── LICENSE
```

## Management Areas Covered

### People & Team Management
- Building and developing teams
- 1-on-1 meetings and mentoring
- Delegation and empowerment
- Conflict resolution
- Leadership development
- Psychological safety
- Team dynamics

### Technical Leadership
- Architecture decisions
- Technology selection
- Technical roadmaps
- Technical debt management
- System design
- Technical excellence
- Scaling strategies

### Hiring & Talent
- Recruitment process
- Interview techniques
- Candidate assessment
- Onboarding
- Talent planning
- Succession planning
- Retention strategies

### Performance Management
- Goal-setting and OKRs
- Performance reviews
- Feedback and coaching
- Metrics and analytics
- Career development
- Promotions
- Recognition

### Culture & Engagement
- Team culture building
- Psychological safety
- Communication
- Engagement strategies
- Inclusion and diversity
- Retention
- Team rituals

## Usage Examples

### Example 1: New Engineering Manager

```
You: "I just became an engineering manager. Where do I start?"

/manage team-leadership
→ Get 1-on-1 meeting template
→ Get delegation framework
→ Get mentoring guidance

/guide new-manager
→ Get foundational leadership advice
→ Get first 90-day plan
```

### Example 2: Team Performance Issues

```
You: "My team's morale is low and people seem disengaged"

/assess-team engagement
→ Get detailed engagement evaluation
→ Identify specific problems
→ Get prioritized recommendations

/guide engagement
→ Get evidence-based improvement strategies
→ Get action plan

/manage culture
→ Access team engagement templates
→ Get recognition program template
```

### Example 3: Hiring Challenges

```
You: "I need to hire 2 engineers but my interview process is weak"

/manage hiring
→ Get job description template
→ Get interview plan template
→ Get candidate scorecard

/guide interviewing
→ Get structured interview techniques
→ Get assessment best practices
```

### Example 4: Technical Strategy

```
You: "Should we refactor our monolith or switch to microservices?"

/guide architecture-decision
→ Get decision-making framework
→ Get trade-off analysis
→ Get recommendations

/strategies technical
→ Create technical roadmap
→ Plan migration path
```

## Plugin Specifications

- **Total Agents**: 5
- **Total Commands**: 4
- **Total Skills**: 5
- **Management Templates**: 100+
- **Best Practices**: 500+
- **Frameworks**: 50+

## Key Resources

### Templates
- 1-on-1 meeting template
- Performance review template
- OKR planning template
- Job description template
- Interview plan template
- Career development plan
- Team strategy template
- Technical roadmap template
- And 100+ more...

### Frameworks
- Leadership frameworks
- Decision-making frameworks
- Team development models
- Performance management process
- Hiring process framework
- Career ladder design
- Tech selection framework
- And 50+ more...

### Tools & Guides
- Team assessment rubrics
- Engagement survey templates
- Culture evaluation tools
- Technical debt tracking
- Metrics dashboards
- Hiring scorecards
- And comprehensive guides for each topic...

## How It Works

### 4 Main Commands

1. **`/manage`** → Access all templates and frameworks
2. **`/guide`** → Get expert advice on challenges
3. **`/assess-team`** → Evaluate team health
4. **`/strategies`** → Plan technical and organizational roadmaps

### 5 Expert Agents

Behind each command are specialized agents:
- **Team Leadership Agent** 👥 - People management
- **Technical Strategy Agent** 🏗️ - Technical decisions
- **Hiring & Performance Agent** 📊 - Talent and metrics
- **Culture & Engagement Agent** 🌱 - Culture and communication
- **Growth & Development Agent** 📈 - Career development

### 5 Invokable Skills

Hands-on tools for specific tasks:
- Team dynamics and leadership
- Technical decision-making
- Hiring and recruitment
- Performance management
- Culture and engagement

## Version

- **Plugin Version**: 1.0.0
- **Format**: Claude Code Plugin Format (Official)
- **Compatibility**: Claude Code 1.0+
- **Last Updated**: November 18, 2024

## License

MIT License - See LICENSE file for details

---

**Transform Your Engineering Leadership!** 🚀

```
/manage       → Access templates and frameworks
/guide        → Get expert guidance
/assess-team  → Evaluate team health
/strategies   → Plan your strategy
```

**Start with:** `/manage` or `/guide [challenge]`

Good luck managing your team! 👥✨