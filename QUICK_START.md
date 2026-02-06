# ⚡ Quick Start (5 Commands)

## 1. Install
```bash
cd ai-learning-assistant
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## 2. Get Gemini API Key
Go to: [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
Click "Create API Key" → Copy it

## 3. Configure
```bash
cp .env.example .env
notepad .env  # Add your GEMINI_API_KEY
```

## 4. Setup Supabase
- Create project at [supabase.com](https://supabase.com)
- Disable email confirmations
- Run SQL:
```sql
CREATE TABLE conversations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL,
  role TEXT NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```
- Add SUPABASE_URL and SUPABASE_KEY to `.env`

## 5. Run
```bash
streamlit run app.py
```

## 6. Create User
- Supabase Dashboard → Authentication → Users → Add user
- Uncheck "Send email confirmation"
- Login with those credentials

**Done!** 🎉

---

**Using FREE Google Gemini API - No credit card needed!**
