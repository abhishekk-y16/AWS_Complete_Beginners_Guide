#!/usr/bin/env python3
"""Simple script to populate placeholder markdown files"""
import os
import glob

root_dir = r"c:\Users\abhy4\Desktop\AWS Beginner Gude"
successful = 0
failed = 0

for md_file in glob.glob(os.path.join(root_dir, "**/*.md"), recursive=True):
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.strip().split('\n')
            
            # Check if placeholder
            if len(lines) <= 5 and any(x in content for x in ['Detailed documentation', 'Content for', 'Documentation for']):
                filename = os.path.basename(md_file)
                dirname = os.path.basename(os.path.dirname(md_file))
                
                # Generate new content
                if "what-is" in filename:
                    new_content = f"""# AWS {dirname.upper()}

## 🎯 What is {dirname.upper()}?

[Service overview placeholder - to be filled with detailed information]

## 🔑 Key Concepts

- Concept 1
- Concept 2  
- Concept 3
- Concept 4
- Concept 5

## 💡 Real-World Analogy

[Real-world comparison]

## 🚀 Common Use Cases

1. Use Case 1
2. Use Case 2
3. Use Case 3
4. Use Case 4

## 💰 Pricing Overview

[Basic pricing]

## ⚠️ Important Things to Know

- Important point 1
- Important point 2
- Important point 3

## 🔗 Related Services

- Service A
- Service B
- Service C

## 🆘 Common Issues & Solutions

### Issue 1
**Problem**: [Description]
**Solution**: [Fix]

## 💡 Best Practices

- Practice 1
- Practice 2
- Practice 3

## 📖 Additional Resources

- [AWS Documentation](https://docs.aws.amazon.com/)
- [AWS Blog](https://aws.amazon.com/blogs/)"""

                elif "pricing" in filename:
                    new_content = f"""# {dirname.upper()} Pricing

## 💾 Cost Factors

[Pricing details]

## 📊 Pricing Models

### On-Demand
[On-demand pricing]

### Reserved/Commitment
[Reserved pricing]

### Free Tier
[Free tier details]

## 📈 Cost Examples

| Scenario | Cost |
|----------|------|
| Small | $-$$ |
| Medium | $$-$$$ |
| Large | $$$-$$$$ |

## 💡 Cost Optimization

- Optimization tip 1
- Optimization tip 2
- Optimization tip 3
- Optimization tip 4

## 📊 Calculator

[AWS Pricing Calculator](https://calculator.aws/)"""

                elif "use-cases" in filename:
                    new_content = f"""# {dirname.upper()} Use Cases

## Use Case 1

**Scenario**: [Description]
**Why**: [Benefits]
**Setup**: [Configuration]

## Use Case 2

**Scenario**: [Description]
**Why**: [Benefits]
**Setup**: [Configuration]

## Use Case 3

**Scenario**: [Description]
**Why**: [Benefits]
**Setup**: [Configuration]

## Use Case 4

**Scenario**: [Description]
**Why**: [Benefits]
**Setup**: [Configuration]

## Service Comparison

| Need | {dirname.upper()} | Alt 1 | Alt 2 |
|------|---------|-----------|-----------|
| Feature 1 | ✅ | ❌ | ✅ |
| Feature 2 | ✅ | ✅ | ❌ |
| Feature 3 | ❌ | ✅ | ✅ |"""

                elif "best-practices" in filename or "best_practices" in filename:
                    new_content = f"""# {dirname.upper()} Best Practices

## Performance

- Performance practice 1
- Performance practice 2
- Performance practice 3

## Reliability  

- Reliability practice 1
- Reliability practice 2
- Reliability practice 3

## Security

- Security practice 1
- Security practice 2
- Security practice 3

## Cost Optimization

- Cost optimization 1
- Cost optimization 2
- Cost optimization 3

## Operations

- Operations practice 1
- Operations practice 2
- Operations practice 3"""

                elif "troubleshooting" in filename:
                    new_content = f"""# {dirname.upper()} Troubleshooting

## Common Issues

### Issue 1

**Symptoms**: [What you see]
**Cause**: [Why it happens]
**Solution**: [How to fix it]

### Issue 2

**Symptoms**: [What you see]
**Cause**: [Why it happens]
**Solution**: [How to fix it]

### Issue 3

**Symptoms**: [What you see]
**Cause**: [Why it happens]
**Solution**: [How to fix it]

## Debugging Steps

1. Check logs
2. Monitor metrics
3. Verify configuration
4. Test connectivity
5. Review security settings

## Getting Help

- Review AWS documentation
- Check CloudWatch logs
- Contact AWS Support
- Search AWS forums"""

                else:
                    new_content = f"""# {filename.replace('.md', '').replace('-', ' ').title()}

## Overview

[Content overview]

## Key Information

- Point 1
- Point 2
- Point 3
- Point 4

## Related Topics

- [Related Article 1](link)
- [Related Article 2](link)
- [Related Article 3](link)

## Resources

- [AWS Documentation](https://docs.aws.amazon.com/)
- [AWS Tutorials](https://aws.amazon.com/getting-started/)"""

                # Write new content
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                successful += 1
                if successful % 30 == 0:
                    print(f"✓ Updated {successful} files...")
    except Exception as e:
        failed += 1
        if failed <= 5:  # Show first 5 errors
            print(f"✗ Error on {md_file}: {str(e)}")

print(f"\n✅ Successfully populated {successful} markdown files")
if failed > 0:
    print(f"⚠️  {failed} files encountered errors")
print(f"\n📊 Total: {successful}/{successful + failed} completed")
