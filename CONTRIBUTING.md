# Contributing to AWS Beginners Guide

Thank you for your interest in contributing to the AWS Beginners Guide! This document provides guidelines and instructions for contributing.

## Code of Conduct

This project adheres to the Contributor Covenant [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the maintainers.

## Ways to Contribute

### 1. Report Bugs or Issues
- Use the [Bug Report](https://github.com/yourname/aws-beginners-guide/issues/new?template=bug_report.md) template
- Include as much detail as possible
- Provide links to the affected documentation
- Suggest fixes if you have them

### 2. Suggest Improvements
- Use the [Documentation Improvement](https://github.com/yourname/aws-beginners-guide/issues/new?template=documentation_improvement.md) template
- Explain what could be improved and why
- Provide references or examples

### 3. Request New Content
- Use the [Feature Request](https://github.com/yourname/aws-beginners-guide/issues/new?template=feature_request.md) template
- Describe what you'd like to see documented
- Explain the use case or problem it would solve

### 4. Submit Content or Fixes
- Fork the repository
- Create a feature branch (`git checkout -b feature/your-feature`)
- Make your changes
- Test locally (render markdown, verify links)
- Commit with clear messages (`git commit -m 'docs: add EC2 pricing information'`)
- Push to your fork
- Create a Pull Request with detailed description

### 5. Improve Existing Content
- Fix typos and grammar errors
- Clarify confusing sections
- Add missing examples
- Update outdated information
- Add better formatting or structure

### 6. Answer Questions
- Review open [Issues](https://github.com/yourname/aws-beginners-guide/issues) marked with `question` label
- Help other learners understand concepts
- Share your knowledge and experience

## Getting Started with Contributions

### Prerequisites
- GitHub account
- Git installed on your machine
- Text editor (VS Code, Sublime Text, etc.)
- Basic markdown knowledge

### Setup Steps

1. **Fork the Repository**
   ```bash
   # Click "Fork" button on GitHub
   ```

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/aws-beginners-guide.git
   cd aws-beginners-guide
   ```

3. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**
   - Edit markdown files
   - Add new files if needed
   - Follow the style guide (see below)

5. **Test Locally**
   - Verify markdown renders correctly
   - Check all links are working
   - Review formatting and grammar
   - Use a markdown preview extension in your editor

6. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "type: description of changes"
   ```

7. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create a Pull Request**
   - Go to GitHub and click "Create Pull Request"
   - Use the [PR Template](PULL_REQUEST_TEMPLATE/pull_request_template.md)
   - Describe your changes clearly
   - Reference any related issues

## Documentation Style Guide

### Markdown Formatting

**Headers:**
```markdown
# H1 - Main Title
## H2 - Section
### H3 - Subsection
#### H4 - Sub-subsection
```

**Emphasis:**
```markdown
**bold text**
*italic text*
~~strikethrough~~
```

**Lists:**
```markdown
- Bullet point
- Another point
  - Nested point
  
1. Numbered item
2. Another item
```

**Code:**
```markdown
`inline code`

\`\`\`bash
code block
\`\`\`
```

**Links:**
```markdown
[Link text](url)
[Relative link](storage/s3/README.md)
```

### Naming Conventions

- **Filenames:** Use lowercase with hyphens (e.g., `what-is-ec2.md`)
- **Directories:** Use lowercase with hyphens (e.g., `compute/ec2`)
- **Headers:** Use title case for main headers

### Content Structure

Every service documentation should include:

```markdown
# Service Name

## Overview
Brief description of the service.

## Key Concepts
- Important terms and definitions

## When to Use
- Typical use cases

## Getting Started
- First steps to use the service

## Common Patterns
- Examples and code snippets

## Best Practices
- Do's and don'ts

## Pricing
- Cost considerations

## Related Services
- Links to related services

## Resources
- Official documentation links
- Learn more resources
```

### Writing Style

1. **Be Clear and Concise**
   - Use simple language
   - Avoid unnecessary jargon
   - Explain technical terms when first introduced

2. **Be Accurate**
   - Verify information before publishing
   - Link to official AWS documentation
   - Update when AWS services change

3. **Be Helpful**
   - Include examples and code snippets
   - Provide step-by-step instructions
   - Anticipate common questions

4. **Be Consistent**
   - Use consistent terminology
   - Follow the established structure
   - Match the tone of existing content

5. **Be Inclusive**
   - Write for beginners
   - Assume minimal prior knowledge
   - Explain concepts thoroughly

### Code Examples

- Keep code examples simple and focused
- Include explanatory comments
- Never include real AWS credentials or secrets
- Use placeholder values like `<YOUR_ACCOUNT_ID>`
- Test code examples before including them

### Images and Diagrams

- Use clear, readable images
- Include alt text for accessibility
- Store images in the `images/` directory
- Reference them with relative paths
- Keep file sizes reasonable (< 1MB)

## Pull Request Guidelines

### Before Submitting

- [ ] Code follows the style guidelines
- [ ] All links have been tested
- [ ] Markdown renders correctly
- [ ] Spelling and grammar are checked
- [ ] Changes are documented in PR description
- [ ] Referenced issues are linked
- [ ] No unnecessary files are added

### During Review

- Be open to feedback
- Respond to reviewer comments
- Make requested changes promptly
- Ask questions if anything is unclear

### PR Commit Messages

Use semantic commit messages:

```
type(scope): subject

feat(s3): add bucket creation tutorial
fix(ec2): correct instance type pricing
docs(iam): clarify policy examples
style(formatting): improve markdown structure
refactor(content): reorganize database section
```

**Types:**
- `feat`: New content or feature
- `fix`: Bug fix or correction
- `docs`: Documentation updates
- `style`: Formatting or style changes
- `refactor`: Content reorganization
- `test`: Testing related changes
- `chore`: Maintenance or tooling

## Approval Process

1. **Automated Checks**
   - Link checker
   - Markdown linter
   - Spell checker
   - YAML validation

2. **Manual Review**
   - Technical accuracy
   - Clarity and readability
   - Consistency with style guide
   - Completeness of content

3. **Merging**
   - Approved by at least one maintainer
   - All checks pass
   - Branches updated if necessary

## Repository Structure

```
aws-beginners-guide/
├── README.md (Main landing page)
├── CONTRIBUTING.md (This file)
├── getting-started/
├── compute/
├── storage/
├── database/
├── networking/
├── security/
├── containers/
├── analytics/
├── machine-learning/
├── tutorials/
├── best-practices/
├── troubleshooting/
└── .github/
    ├── workflows/ (GitHub Actions)
    └── ISSUE_TEMPLATE/
```

## Common Contribution Scenarios

### Adding a New Tutorial

1. Create file in `tutorials/` with descriptive name
2. Follow the tutorial structure template
3. Include prerequisites
4. Provide step-by-step instructions
5. Add code examples where applicable
6. Include troubleshooting section
7. Link from relevant service docs and README

### Updating Existing Content

1. Check if information is still current
2. Update facts, figures, and links
3. Improve clarity if needed
4. Test any code examples
5. Maintain original structure
6. Note update date if significant

### Adding a New Service

1. Create service folder under appropriate category
2. Create README.md with overview
3. Add "what-is-[service].md" file
4. Create additional files as needed
5. Update category README to reference new service
6. Update main README if major service

### Fixing a Bug/Typo

1. Use bug report template
2. Fix the issue directly
3. Test the fix
4. Reference the original issue in your PR

## Questions or Need Help?

- **General Questions:** Use [Discussions](https://github.com/yourname/aws-beginners-guide/discussions)
- **Issues:** Create an [Issue](https://github.com/yourname/aws-beginners-guide/issues)
- **Direct Contact:** Email maintainers (see CONTRIBUTORS.md)

## Attribution

Your contributions will be recognized:
- Your name will be added to [CONTRIBUTORS.md](CONTRIBUTORS.md)
- You'll be credited in commit messages
- Listed in release notes for significant contributions

## Legal

By contributing to this project, you agree that:
- Your contributions can be used under the MIT License
- You have the right to contribute the content
- Your contribution doesn't violate anyone's rights

## Review Timeline

- **Bug fixes:** 1-3 days
- **Documentation improvements:** 3-7 days
- **New content:** 1-2 weeks (depending on scope)
- **Major changes:** May require discussion first

## Maintainer Responsibilities

Maintainers will:
- Review contributions promptly
- Provide constructive feedback
- Help contributors get to completion
- Maintain code quality and consistency
- Manage releases and updates

## Community

This is a community-driven project. We appreciate everyone who contributes!

Join us in making AWS learning more accessible for everyone. 🚀

---

**Thank you for contributing!** 🎉

For questions: See [Supporting Resources](#questions-or-need-help)
