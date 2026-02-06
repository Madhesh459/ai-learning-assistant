# 🚀 Setup Guide - AI Learning Assistant

## Step-by-Step Setup (15 minutes)

### Step 1: Install Dependencies (2 min)

```bash
cd ai-learning-assistant
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### Step 2: Get OpenAI API Key (3 min)

1. Go to [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Sign up or log in
3. Click "Create new secret key"
4. Copy the key (starts with `sk-proj-...`)
5. **Save it somewhere safe** - you won't see it again!

### Step 3: Set Up Supabase (5 min)

#### 3.1 Create Project
1. Go to [supabase.com](https://supabase.com)
2. Sign up (free tier)
3. Click "New Project"
4. Choose a name and password
5. Wait ~2 minutes for provisioning

#### 3.2 Configure Authentication
1. Go to **Authentication → Settings**
2. Find "Enable email confirmations"
3. **Toggle it OFF** (critical for demo!)
4. Ensure "Email" provider is enabled
5. Click "Save"

#### 3.3 Create Database Table
1. Go to **SQL Editor**
2. Click "New Query"
3. Paste this SQL:

```sql
CREATE TABLE conversations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL,
  role TEXT NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

4. Click "Run" (bottom right)
5. You should see "Success. No rows returned"

#### 3.4 Get API Keys
1. Go to **Settings → API**
2. Copy **Project URL** (looks like `https://xxxxx.supabase.co`)
3. Copy **anon public** key (long string starting with `eyJ...`)

### Step 4: Configure Environment Variables (2 min)

1. Copy the example file:
```bash
cp .env.example .env
```

2. Edit `.env` with your favorite editor:
```bash
# On macOS/Linux:
nano .env
# On Windows:
notepad .env
```

3. Replace the placeholder values:
```bash
OPENAI_API_KEY=sk-proj-YOUR_ACTUAL_KEY_HERE
SUPABASE_URL=https://YOUR_PROJECT_ID.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.YOUR_ACTUAL_KEY_HERE
```

4. Save and close

### Step 5: Run the App (1 min)

```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

### Step 6: Test It Out (2 min)

1. **Sign Up**: Create an account with any email (e.g., `test@example.com`)
2. **Paste Code**: Try this Python snippet:
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```
3. **Ask**: "What does this code do?"
4. **Follow-Up**: "How can I optimize this?"
5. **Test Persistence**: Logout and login again - your conversation should be restored!

---

## ✅ Verification Checklist

Before the demo, verify:

- [ ] Virtual environment activated
- [ ] All dependencies installed (`pip list` shows streamlit, openai, supabase)
- [ ] `.env` file exists with all three keys
- [ ] Supabase project is running
- [ ] Email confirmations are DISABLED in Supabase
- [ ] `conversations` table exists in Supabase
- [ ] App runs without errors (`streamlit run app.py`)
- [ ] Can sign up with test account
- [ ] Can paste code and get explanation
- [ ] Can ask follow-up questions
- [ ] Conversation persists after logout/login

---

## 🐛 Common Issues

### Issue: "Missing required secret: OPENAI_API_KEY"
**Solution**: 
- Check that `.env` file exists in the project root
- Verify the key is correct (no extra spaces or quotes)
- Make sure you're running the app from the `ai-learning-assistant` directory

### Issue: "Signup failed: User already registered"
**Solution**: 
- Use a different email address
- Or go to Supabase Dashboard → Authentication → Users and delete the test user

### Issue: "Failed to save message"
**Solution**: 
- Verify the `conversations` table exists in Supabase
- Check that the table schema matches (UUID primary key, not bigserial)
- Ensure RLS is disabled for demo purposes

### Issue: OpenAI API returns 401 Unauthorized
**Solution**: 
- Verify your API key is valid
- Check that you have credits in your OpenAI account
- Try generating a new API key

### Issue: App is slow or times out
**Solution**: 
- Check your internet connection
- Verify OpenAI API is not experiencing outages
- Try switching to a simpler model (edit `ai_service.py` and change to `gpt-3.5-turbo`)

---

## 🎯 Demo Tips

1. **Prepare Code Samples**: Have 3-4 code snippets ready to paste
2. **Test Internet**: Verify connection before demo
3. **Clear Browser Cache**: Use incognito mode for clean demo
4. **Have Backup**: Record a demo video in case of technical issues
5. **Practice**: Run through the demo 2-3 times before presenting

---

## 📞 Need Help?

If you encounter issues:
1. Check the troubleshooting section in README.md
2. Verify all setup steps were completed
3. Check Supabase dashboard for error logs
4. Review OpenAI API usage dashboard

---

**Good luck with your hackathon! 🚀**
