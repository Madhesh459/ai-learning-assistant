# 🤖 AI Learning Assistant 

An AI-powered coding tutor that helps developers understand complex codebases in minutes. Built with Streamlit, OpenAI, and Supabase.

## ✨ Features

- ✅ **User Authentication**: Email + password signup/login (Supabase Auth)
- ✅ **Code Explanation**: Paste code or upload files for AI explanations
- ✅ **Multi-Input Support**: Text area and file upload (.py, .js, .java, .cpp, .txt, .md)
- ✅ **Conversation Context**: Ask follow-up questions with context
- ✅ **Response Modes**: Simple (concise) vs Detailed (comprehensive)
- ✅ **Persistence**: Conversation history saved across sessions

## 🚀 Quick Start

### 1. Get Google Gemini API Key (FREE)

1. Go to [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the API key
5. **Free Tier**: 60 requests per minute, completely free!

### 2. Set Up Supabase

```bash
cd ai-learning-assistant
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Set Up Supabase

1. Go to [supabase.com](https://supabase.com) and create a free account
2. Create a new project
3. Go to **Authentication → Settings**:
   - **Disable "Enable email confirmations"** (for demo)
   - Enable "Email" provider
4. Go to **SQL Editor** and run:

```sql
CREATE TABLE conversations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL,
  role TEXT NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

5. Go to **Settings → API** and copy:
   - Project URL
   - `anon` `public` key

### 3. Configure API Keys

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your keys:

```bash
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxx
SUPABASE_URL=https://xxxxxxxxxxxxx.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### 4. Run the App

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 📖 Usage

1. **Sign Up**: Create an account with email and password
2. **Paste Code**: Use the text area or upload a file
3. **Ask Questions**: Type your question and click "Ask"
4. **Follow-Up**: Ask more questions - the AI remembers context
5. **Switch Modes**: Toggle between Simple and Detailed explanations
6. **Logout**: Your conversation is saved and will be restored on next login

## 🏗️ Architecture

```
Streamlit App (Frontend + Backend)
├── Session State (Live conversation context)
├── Supabase Auth (User authentication)
├── Supabase DB (Conversation persistence)
└── OpenAI API (GPT-4 explanations)
```

**Key Design Decisions:**
- **Session State**: Holds live conversation for prompt building
- **Supabase**: Used ONLY for persistence (save/load on login/logout)
- **No Retry Logic**: Minimal error handling per hackathon constraints
- **Modern OpenAI**: Uses latest client syntax

## 📁 Project Structure

```
ai-learning-assistant/
├── app.py                 # Main Streamlit app
├── auth_service.py        # Supabase Auth
├── ai_service.py          # OpenAI API wrapper
├── db_service.py          # Supabase persistence
├── context_manager.py     # Code chunking
├── prompt_builder.py      # Prompt templates
├── requirements.txt       # Dependencies
├── .env.example           # API key template
├── .gitignore
└── README.md
```

## 🎯 Demo Script (2 minutes)

**[0:00-0:20] Problem**
"Developers waste hours understanding complex code. Our AI tutor solves this."

**[0:20-0:40] Authentication**
1. Sign up with email/password (instant, no confirmation)
2. Show personalized dashboard

**[0:40-1:10] Core Features**
1. Paste Python code → Get simple explanation
2. Switch to detailed mode → See in-depth breakdown
3. Ask follow-up: "How would I optimize this?" → AI answers with context

**[1:10-1:40] Persistence**
1. Upload JavaScript file
2. AI explains the code
3. Logout → Login → Conversation history restored!

**[1:40-2:00] Wrap Up**
"Built in 48 hours with Streamlit + OpenAI + Supabase. Try it yourself!"

## 🚫 Out of Scope (By Design)

This is a hackathon MVP focused on demo reliability:

- ❌ OAuth providers (Google, GitHub)
- ❌ Password reset
- ❌ Email confirmation
- ❌ User profiles
- ❌ Progress tracking
- ❌ Retry logic / rate limiting
- ❌ Production-grade error handling

## 🐛 Troubleshooting

**"Missing required secret" error:**
- Check that `.env` file exists and contains all three keys
- Verify keys are correct (no extra spaces)

**"Signup failed" error:**
- Ensure email confirmations are disabled in Supabase
- Check that Email provider is enabled

**"Failed to save message" error:**
- Verify `conversations` table exists in Supabase
- Check that table has correct schema (UUID primary key)

**OpenAI API errors:**
- Verify API key is valid and has credits
- Check internet connection

## 📝 License

MIT License - Built for hackathon demonstration purposes.

## 🙏 Acknowledgments

- Streamlit for the amazing framework
- OpenAI for GPT-4 API
- Supabase for auth and database
