# EC2 Key Pairs 🔐

An **EC2 Key Pair** is a security credential that allows you to connect remotely to your EC2 instances. It's like a digital key - you keep the private key private, and AWS keeps the public key.

## How Key Pairs Work

```
Your Computer                  AWS EC2 Instance
      │                              │
      │  Private Key (SECRET)       │
      │  (stores on your computer)  │
      │                              │
      │  Public Key (VISIBLE)       │
      │  (stored in EC2)            │
      │◄────────────────────────────│
      │                              │
      │  SSH Connection              │
      ├─────── Using private key ──► │ (Uses public key to verify)
      │                              │
      │  Access Granted!             │
      │                              │

How it works:
1. You create a key pair in AWS
2. Download the private key (.pem file) - KEEP SECRET
3. AWS stores the public key on the EC2 instance
4. When you SSH, private key proves it's you
5. Connection granted!
```

## Types of Key Pairs

### EC2 Key Pair (AWS Created)
```
Creating in AWS Console:
1. EC2 Dashboard → Key Pairs → Create Key Pair
2. Give it a name (e.g., "my-app-key")
3. AWS generates both keys
4. Download the .pem file (only once!)
5. Keep it safe - you can't download again

Format: RSA 2048-bit
```

### Imported Key Pair
```
If you already have a key:
1. Generate your own key pair (ssh-keygen)
2. Import public key to AWS
3. Use your existing private key

Useful for: Terraform, Ansible, existing infrastructure
```

## Using Your Key Pair

### Linux/Mac - SSH Connection

```
$ chmod 600 my-app-key.pem
(Make sure only you can read it)

$ ssh -i my-app-key.pem ec2-user@54.12.34.56
(Connect to instance)

$ logout
(Close connection)
```

### Windows - Using PuTTY

```
1. Download PuTTY
2. Use PuTTYgen to convert .pem to .ppk
3. Open PuTTY
4. Hostname: ec2-user@54.12.34.56
5. Auth → Private Key → Select .ppk file
6. Click Open
```

### Windows 10+ - Using SSH

```
Windows 10+ has built-in SSH:

PS C:\Users\YourName> ssh -i path\to\key.pem ec2-user@54.12.34.56
(Same as Linux/Mac)
```

## Default Users by AMI

```
Amazon Linux 2: ec2-user
Ubuntu: ubuntu
RHEL: ec2-user
Windows: Administrator (use RDP, not SSH)
CentOS: centos
Debian: admin
```

## Best Practices

✅ **Store securely** - Use AWS Systems Manager Parameter Store or Secrets Manager
✅ **Don't commit to Git** - Add .pem to .gitignore
✅ **Rotate regularly** - Create new keys periodically
✅ **Use one per environment** - Separate keys for prod/dev
✅ **Backup** - Keep secure backups offline
✅ **Permissions** - chmod 600 on Linux/Mac
✅ **Delete unused** - Remove when no longer needed

## Common Mistakes

### ✗ Mistake 1: Lost Private Key
```
Lost my-app-key.pem

Problem: Can't connect to instance anymore

✅ Solution: Terminate instance, launch new one with different key
           (Can't recover access)

Prevention: Store multiple copies securely
```

### ✗ Mistake 2: Wrong Permissions
```
$ ssh -i my-key.pem ec2-user@54.12.34.56
WARNING: UNPROTECTED PRIVATE KEY FILE!
Permissions 0644 are too open.

Problem: File readable by others (security risk)

✅ Fix: chmod 600 my-key.pem
```

### ✗ Mistake 3: Wrong User
```
$ ssh -i my-key.pem root@54.12.34.56
(Permission denied)

Problem: Amazon Linux default user is ec2-user, not root

✅ Fix: ssh -i my-key.pem ec2-user@54.12.34.56
```

### ✗ Mistake 4: Sharing Keys
```
Me: "Here's my production key, set it up"
Coworker: Copies it to their computer
Manager: Copies it to their laptop
...

Risk: Who has access? Can't audit. Security nightmare.

✅ Solution: Use AWS Systems Manager Session Manager
           (No key files needed!)
```

## Alternative: EC2 Instance Connect

```
No key pair needed (newer instances):

AWS Console:
1. Select EC2 instance
2. Connect → EC2 Instance Connect
3. Browser-based terminal opens
4. Use right away!

Requirements:
- EC2 Instance Connect enabled
- Security group allows port 22
- Instance has internet access
```

## Cost

✓ Key Pairs: FREE to create and use
✓ EC2 Instance Connect: FREE
✓ No extra charges for connection

## Troubleshooting

### Can't Connect: "Connection refused"
```
Check:
1. Is instance running? (green circle)
2. Does security group allow port 22?
3. Is instance in public subnet with IGW?
4. Is your IP in security group rules?
5. Are you using correct user (ec2-user, ubuntu, etc.)?
```

### Can't Connect: "Permission denied (publickey)"
```
Check:
1. Do you have the right .pem file?
2. Is private key permissions set to 600?
3. Did you use correct username?
4. Is key pair still associated with instance?
```

## Next Steps

→ [Connecting to Instances](./connecting-to-instances.md) - SSH tutorials
→ [Security Groups](./security-groups.md) - Network access control
→ [Launching Instances](./launching-first-instance.md) - Getting started