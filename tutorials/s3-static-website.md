# Tutorial: Host a Static Website on Amazon S3

**Level**: 🟢 Beginner  
**Duration**: 30-45 minutes  
**Cost**: FREE (within free tier)  
**What You'll Build**: A personal portfolio website hosted on AWS S3

---

## 📋 What You'll Learn

- [ ] Create an S3 bucket for web hosting
- [ ] Upload HTML and CSS files to S3
- [ ] Configure S3 for static website hosting
- [ ] Make your website publicly accessible
- [ ] Visit your live website on the internet
- [ ] Customize your website content

## 📊 Architecture Overview

```
Your Computer
    ↓ (Upload files)
    ↓
    S3 Bucket
    ├── index.html
    ├── style.css
    └── image.jpg
    ↓
    ↓ (Users visit your website)
    ↓
Internet User → Browser → Your S3 Website URL → Gets served
```

## 💰 Cost Breakdown

**Free Tier (First 12 Months)**:
- 5 GB storage: FREE
- 20,000 GET requests: FREE
- Website transfer: FREE

**After 12 months or more usage**:
- Storage: ~$0.023/GB/month
- GET requests: $0.0004 per 1,000 requests
- Data transfer: $0.09/GB out (most users are free - within 1 GB/month)

**Example Monthly Cost** (with real traffic):
- 100 MB stored: ~$0.002
- 10,000 visitors monthly: ~$0.004
- 50 MB transferred: FREE (under 1 GB)
- **Total**: ~$0.01/month (less than 1 cent!)

## 🛠️ What You'll Need

- ✅ AWS account
- ✅ Text editor (Notepad, VS Code, or any editor)
- ✅ A web browser
- ✅ ~10 KB of disk space
- ✅ 30 minutes of time

---

## 📝 Part 1: Create Your Website Files

Let's create simple HTML and CSS files first.

### Step 1: Create index.html

**Open your text editor** and create a new file with this content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfolio - Hosted on AWS</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header class="header">
        <div class="container">
            <h1>👨‍💻 My Portfolio</h1>
            <p class="tagline">Showcasing my projects and skills</p>
        </div>
    </header>

    <nav class="navbar">
        <div class="container">
            <a href="#about">About</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact</a>
        </div>
    </nav>

    <main class="container">
        <section id="about" class="section">
            <h2>About Me</h2>
            <p>
                Welcome to my portfolio! I'm learning AWS and cloud computing.
                This website is hosted on Amazon S3, which makes it fast, reliable,
                and affordable.
            </p>
        </section>

        <section id="projects" class="section">
            <h2>My Projects</h2>
            <div class="projects-grid">
                <div class="project-card">
                    <h3>Project 1: Web Application</h3>
                    <p>A full-stack web application built with Python and React.</p>
                    <p class="tech">Tech: Python, React, AWS</p>
                </div>
                <div class="project-card">
                    <h3>Project 2: Mobile App</h3>
                    <p>An iOS app for tracking habits and goals.</p>
                    <p class="tech">Tech: Swift, Firebase</p>
                </div>
                <div class="project-card">
                    <h3>Project 3: Data Dashboard</h3>
                    <p>Real-time analytics dashboard for business metrics.</p>
                    <p class="tech">Tech: JavaScript, D3.js, Node.js</p>
                </div>
            </div>
        </section>

        <section id="contact" class="section">
            <h2>Get In Touch</h2>
            <p>
                Interested in working together or have questions about this site?
                Feel free to reach out!
            </p>
            <div class="contact-links">
                <a href="mailto:your-email@example.com" class="btn">Email Me</a>
                <a href="https://github.com" class="btn btn-secondary">GitHub</a>
                <a href="https://linkedin.com" class="btn btn-secondary">LinkedIn</a>
            </div>
        </section>
    </main>

    <footer class="footer">
        <div class="container">
            <p>© 2025 My Portfolio. Hosted on AWS S3. | 
            <a href="https://aws.amazon.com/s3/">Learn about S3</a></p>
        </div>
    </footer>
</body>
</html>
```

**Save as**: `index.html`

### Step 2: Create style.css

Create another file with this CSS:

```css
/* ===== VARIABLES ===== */
:root {
    --primary-color: #FF6B6B;
    --secondary-color: #4ECDC4;
    --text-color: #2C3E50;
    --light-bg: #F8F9FA;
    --white: #FFFFFF;
    --shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

/* ===== RESET & GLOBAL ===== */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    background-color: var(--light-bg);
}

/* ===== HEADER ===== */
.header {
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    color: var(--white);
    padding: 60px 20px;
    text-align: center;
}

.header h1 {
    font-size: 3em;
    margin-bottom: 10px;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.tagline {
    font-size: 1.3em;
    opacity: 0.95;
}

/* ===== NAVIGATION ===== */
.navbar {
    background-color: var(--white);
    padding: 20px 0;
    box-shadow: var(--shadow);
    position: sticky;
    top: 0;
    z-index: 100;
}

.navbar a {
    display: inline-block;
    margin: 0 25px;
    text-decoration: none;
    color: var(--text-color);
    font-weight: 500;
    transition: color 0.3s;
}

.navbar a:hover {
    color: var(--primary-color);
    border-bottom: 2px solid var(--primary-color);
}

/* ===== CONTAINER ===== */
.container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 0 20px;
}

/* ===== SECTIONS ===== */
.section {
    padding: 60px 0;
    border-bottom: 1px solid #DDD;
}

.section h2 {
    font-size: 2.5em;
    margin-bottom: 30px;
    color: var(--primary-color);
}

.section p {
    font-size: 1.1em;
    margin-bottom: 15px;
    line-height: 1.8;
}

/* ===== PROJECTS GRID ===== */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 30px;
    margin-top: 30px;
}

.project-card {
    background: var(--white);
    padding: 30px;
    border-radius: 8px;
    box-shadow: var(--shadow);
    transition: transform 0.3s, box-shadow 0.3s;
}

.project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
}

.project-card h3 {
    color: var(--secondary-color);
    margin-bottom: 10px;
    font-size: 1.4em;
}

.project-card p {
    font-size: 1em;
    margin-bottom: 10px;
}

.tech {
    font-size: 0.85em;
    color: #999;
    font-style: italic;
}

/* ===== BUTTONS ===== */
.btn {
    display: inline-block;
    padding: 12px 30px;
    margin: 10px 10px 10px 0;
    background-color: var(--primary-color);
    color: var(--white);
    text-decoration: none;
    border-radius: 5px;
    transition: background-color 0.3s;
    font-weight: 600;
}

.btn:hover {
    background-color: #FF5252;
}

.btn-secondary {
    background-color: var(--secondary-color);
}

.btn-secondary:hover {
    background-color: #45B8AD;
}

/* ===== CONTACT LINKS ===== */
.contact-links {
    margin-top: 20px;
}

/* ===== FOOTER ===== */
.footer {
    background-color: var(--text-color);
    color: var(--white);
    text-align: center;
    padding: 30px 20px;
    margin-top: 60px;
}

.footer a {
    color: var(--secondary-color);
    text-decoration: none;
}

.footer a:hover {
    text-decoration: underline;
}

/* ===== RESPONSIVE DESIGN ===== */
@media (max-width: 768px) {
    .header h1 {
        font-size: 2em;
    }

    .section h2 {
        font-size: 1.8em;
    }

    .navbar a {
        display: block;
        margin: 10px 0;
    }

    .projects-grid {
        grid-template-columns: 1fr;
    }
}
```

**Save as**: `style.css`

### Folder Structure

You should now have two files ready:
```
My-Website/
├── index.html
└── style.css
```

---

## ☁️ Part 2: Create S3 Bucket for Website Hosting

### Step 1: Sign into AWS Console

1. Open [AWS Console](https://console.aws.amazon.com)
2. Sign in with your AWS account

### Step 2: Navigate to S3

- Search for "S3" in the services search bar
- Click on "S3"

### Step 3: Create a Bucket

- Click the orange **"Create bucket"** button

### Step 4: Configure Bucket Settings

**Bucket name** (IMPORTANT):
```
my-portfolio-2025
```
*(Change this to something unique - add date or random numbers)*

**AWS Region**:
- Choose the region closest to you
- Example: `US East (N. Virginia)` or your nearest region

**Object Ownership**:
- Select "ACLs disabled (recommended)"

**Block Public Access Settings**:
- ⚠️ **UNCHECK** "Block all public access"
- Check the box that says "I understand..."
- ⚠️ This allows your website to be publicly visible (that's the goal!)

**Versioning**:
- Leave as "Disable" for now

**Default Encryption**:
- Leave as default (SSE-S3)

**Click "Create bucket"**

✅ Your bucket is now created!

---

## 📁 Part 3: Upload Your Website Files

### Step 1: Open Your Bucket

- Click on your bucket name from the list
- You should see an empty bucket

### Step 2: Upload Files

- Click the orange **"Upload"** button

### Step 3: Add Your Files

Method 1 (Recommended - Drag & Drop):
- Open your file explorer
- Navigate to where you saved `index.html` and `style.css`
- Drag both files directly into the S3 upload window

Method 2 (Click Upload):
- Click "Add files"
- Select `index.html`
- Click "Add files" again
- Select `style.css`

### Step 4: Review and Upload

- Leave all permissions and storage settings as default
- Click **"Upload"**
- Wait for upload to complete
- Click **"Close"**

✅ Both files are now in your S3 bucket!

---

## 🌐 Part 4: Enable Static Website Hosting

### Step 1: Access Bucket Properties

- In your bucket, click the **"Properties"** tab (far right)

### Step 2: Find Static Website Hosting

- Scroll down to find **"Static website hosting"**
- Click **"Edit"**

### Step 3: Configure Website Hosting

**Static website hosting**:
- Select: **"Enable"**

**Hosting type**:
- Keep: "Host a static website"

**Index document**:
- Enter: `index.html`

**Error document** (Optional):
- Enter: `index.html`
- (Serves index.html for 404 errors)

**Click "Save changes"**

### Step 4: Get Your Website URL

Back in the Properties tab, scroll to "Static website hosting" section.

You should see your website endpoint URL:
```
http://my-portfolio-2025.s3-website-us-east-1.amazonaws.com
```

**Copy this URL** - you'll use it to access your site!

---

## 🔓 Part 5: Make Your Website Public (CRITICAL)

Your files are uploaded but currently private. We need to make them public so anyone can see them.

### Step 1: Add Bucket Policy

1. Click on your bucket
2. Go to **"Permissions"** tab
3. Scroll to **"Bucket policy"**
4. Click **"Edit"**

### Step 2: Paste Bucket Policy

Replace any existing policy with:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-portfolio-2025/*"
        }
    ]
}
```

⚠️ **IMPORTANT**: Replace `my-portfolio-2025` with your actual bucket name!

### Step 3: Save Policy

- Click **"Save changes"**
- You'll see a warning about public access - that's normal!

✅ Your website is now publicly accessible!

---

## ✅ Part 6: Visit Your Live Website

### Step 1: Open Your Website

1. Go back to **Properties** tab
2. Scroll to "Static website hosting"
3. Click on your website endpoint URL

**OR** copy the URL into your browser's address bar:
```
http://my-portfolio-2025.s3-website-us-east-1.amazonaws.com
```

### Step 2: See Your Website Live!

🎉 **Your website is now live on the internet!**

You should see:
- Your name/portfolio heading
- The navigation menu
- Your projects section
- Contact links
- Professional styling

---

## 🎨 Part 7: Customize Your Website

### Edit HTML Content

You can update the website content directly from your browser:

1. Download `index.html` from S3
2. Edit in your text editor
3. Change:
   - Your name/title
   - About section
   - Project descriptions
   - Email/social media links
4. Save the file
5. Upload back to S3 (it will overwrite the old version)
6. Refresh your website to see changes

### Update CSS Styling

Similarly, you can modify `style.css`:
1. Download it
2. Change colors, fonts, spacing
3. Upload back
4. Refresh to see changes

---

## 🔍 Verification Checklist

- [ ] Website loads without errors
- [ ] Header with your title shows
- [ ] Navigation menu works
- [ ] Projects section displays correctly
- [ ] Styling looks professional
- [ ] Contact section visible
- [ ] No 404 errors
- [ ] Website works on mobile (resize browser)

---

## 🆘 Troubleshooting

### Problem: "Access Denied" when visiting website

**Solution**:
1. Check bucket policy is added correctly
2. Verify bucket name in policy matches actual bucket name
3. Make sure you enabled "Block public access" setting
4. Wait 1-2 minutes for changes to propagate

### Problem: Getting 403 Forbidden Error

**Solution**:
1. The files are private
2. Go to your bucket
3. Click on each file (index.html, style.css)
4. Click "Make public" (if available)
5. OR add the bucket policy (see Part 5)

### Problem: Website not loading CSS (looks broken)

**Solution**:
1. Make sure both `index.html` AND `style.css` are uploaded
2. Check spelling of `style.css` in the HTML file
3. Ensure style.css is public (not private)

### Problem: Changes don't show up after uploading

**Solution**:
1. Hard refresh browser: `Ctrl+Shift+R` (Windows) or `Cmd+Shift+R` (Mac)
2. Clear browser cache
3. Try in incognito/private window
4. Wait 1-2 minutes for S3 to sync

### Problem: URL is too long/complicated

**Solution**:
- Get a custom domain (not covered in this tutorial)
- Use Route 53 + CloudFront for professional setup
- For now, the S3 URL works fine for learning!

---

## 📊 Monitor Your Website

### Check Traffic

1. Go to S3 bucket
2. Click **"Metrics"** tab
3. Enable "Request metrics"
4. See graphs of who's visiting

### Set Up Alarms

1. Open CloudWatch
2. Create alarm for unusual activity
3. Get notified of issues

---

## 🚀 Next Steps (Beyond Basic)

Once this works, you can:

1. **Add a Custom Domain**
   - Buy domain from Route 53 or another registrar
   - Point it to your S3 website
   - Have `mysite.com` instead of long S3 URL

2. **Use CloudFront CDN**
   - Serve content faster worldwide
   - Add HTTPS/SSL certificate
   - Better security and performance

3. **Add More Pages**
   - Create `about.html`, `projects.html`, etc.
   - Link them in navigation
   - Build a full website

4. **Add Dynamic Features**
   - Use Lambda for form processing
   - Add comments or guest book
   - Email notifications

5. **Backup Your Website**
   - Enable versioning on bucket
   - Create AWS Backup plan
   - Protect against accidental deletion

---

## 🎓 Learning Outcomes

After completing this tutorial, you now understand:

✅ How S3 buckets work  
✅ How to upload files to the cloud  
✅ Static website hosting concepts  
✅ Public/private access controls  
✅ How web servers deliver content  
✅ Real-world hosting basics  

**Congratulations!** 🎉 You've deployed a real website to AWS!

---

## 📚 Additional Resources

- [S3 Static Website Hosting Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)
- [S3 Bucket Policies Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html)
- [Getting Started with S3](https://aws.amazon.com/s3/getting-started/)
- [HTML Tutorial](https://www.w3schools.com/html/)
- [CSS Tutorial](https://www.w3schools.com/css/)
- [AWS Free Tier Details](https://aws.amazon.com/free/)

---

**Tutorial Completed!**  
**Time Taken**: ~45 minutes  
**Cost**: FREE (within free tier)  
**Website Status**: ✅ LIVE  

Visit your website and share the URL with friends! 🌐
