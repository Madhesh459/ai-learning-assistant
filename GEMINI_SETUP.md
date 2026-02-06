# 🚀 Quick Setup with Google Gemini (FREE)

## Why Gemini?
- ✅ **Completely FREE** - 60 requests per minute
- ✅ **No credit card required**
- ✅ **Better than OpenAI free tier**
- ✅ **Fast and capable** (Gemini 1.5 Flash)

---

## Step-by-Step Setup (10 minutes)

### Step 1: Get Google Gemini API Key (2 min)

1. Go to [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy the API key (starts with `AIza...`)
5. Save it somewhere safe

### Step 2: Install Dependencies (2 min)

```bash
cd ai-learning-assistant
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables (2 min)

1. Copy the example file:
```bash
cp .env.example .env
```

2. Edit `.env` file:
```bash
# On Windows:
notepad .env
# On macOS/Linux:
nano .env
```

3. Replace with your actual keys:
```bash
GEMINI_API_KEY=AIzaSy...YOUR_ACTUAL_KEY_HERE
SUPABASE_URL=https://YOUR_PROJECT_ID.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...YOUR_ACTUAL_KEY_HERE
```

4. Save and close

### Step 4: Set Up Supabase (3 min)

1. Go to [supabase.com](https://supabase.com) → Create project
2. **Authentication → Settings** → **Disable "Enable email confirmations"**
3. **SQL Editor** → Run this:

```sql
CREATE TABLE conversations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL,
  role TEXT NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

4. **Settings → API** → Copy Project URL and anon key to `.env`

### Step 5: Run the App (1 min)

```bash
streamlit run app.py
```

App opens at `http://localhost:8501`

### Step 6: Create User in Supabase Dashboard

**To avoid rate limit issues:**

1. Go to Supabase Dashboard → **Authentication → Users**
2. Click **"Add user"** or **"Invite user"**
3. Enter your email and password
4. **Uncheck "Send email confirmation"**
5. Click **"Create user"**
6. Go back to the app and login with these credentials

---

## ✅ Test It Out

1. Login with your credentials
2. Paste this code:
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
```
3. Ask: "What does this code do?"
4. Ask follow-up: "How can I optimize this?"

---

## 🎉 Done!

Your AI Learning Assistant is now running with **FREE Google Gemini API**!

**No credit card, no quota limits, completely free!**

---

## 🐛 Troubleshooting

### "Missing required secret: GEMINI_API_KEY"
- Check that `.env` file exists in project root
- Verify the key is correct (starts with `AIza`)
- Make sure you're running from `ai-learning-assistant` directory

### "Signup failed: email rate limit exceeded"
- Use Solution 6 above (create user in Supabase Dashboard)
- Or wait 10 minutes and try again

### Gemini API errors
- Verify your API key is valid
- Check you're signed in to Google AI Studio
- Try generating a new API key

---

## 📊 Gemini vs OpenAI

| Feature | Google Gemini | OpenAI |
|---------|--------------|--------|
| **Free Tier** | 60 req/min | $5 minimum |
| **Credit Card** | Not required | Required |
| **Model** | Gemini 1.5 Flash | GPT-3.5/4 |
| **Speed** | Fast | Fast |
| **Quality** | Excellent | Excellent |

**Winner: Gemini for hackathons and demos!** 🏆

---

**Ready to demo!** 🚀
