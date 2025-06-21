# Telegram Opportunity Discovery System

> An AI-powered automation system that discovers, validates, and extracts academic opportunities from Telegram channels using intelligent content analysis.

## Motivation

This project was created to solve a personal challenge: efficiently tracking valuable academic and professional opportunities (grants, scholarships, internships) that are frequently shared across numerous Telegram channels. Manually monitoring dozens of channels and distinguishing genuine opportunities from irrelevant content was time-consuming and inefficient. The system automates this process, allowing students and researchers to focus on applying for opportunities rather than searching for them.

## Key Features
- **Automated Channel Discovery**: Uses Telegram's recommendation API to find new opportunity-focused channels
- **AI-Powered Content Validation**: Integrates with OpenAI GPT models to classify channel relevance and filter out non-opportunity content
- **Intelligent Opportunity Extraction**: Analyzes and structures individual opportunities from validated channels into actionable data
- **Multi-API Integration**: Supports both OpenAI and Groq APIs for cost-effective AI analysis
- **Persistent Data Management**: SQLite database tracks channel metadata, validation status, and extracted opportunities

## Tech Stack
- **Language:** Python 3.8+
- **Key Libraries:** Telethon (Telegram API), OpenAI, Groq, SQLAlchemy, BeautifulSoup, PyAutoGUI
- **APIs:** OpenAI GPT-3.5/GPT-4, Groq LLaMA, Telegram API
- **Database:** SQLite with structured schema for channels and opportunities
- **Automation:** UI automation and API-based channel interaction

---

## Overview

A comprehensive Python-based system designed to automate the discovery and analysis of academic and professional opportunities (grants, scholarships, internships, research positions) from Telegram channels. This project addresses the challenge of manually tracking numerous Telegram channels that post valuable opportunities for students, researchers, and young professionals.

## Project Motivation

**Problem Statement**: Many valuable opportunities for students and researchers are shared through Telegram channels, but:
- Finding relevant channels is time-consuming
- Manually monitoring multiple channels for opportunities is inefficient  
- Distinguishing between genuine opportunity channels and irrelevant content requires constant attention

**Solution**: An automated system that:
1. **Discovers** new opportunity-focused Telegram channels through recommendation algorithms
2. **Validates** channels using AI to ensure they contain relevant opportunities
3. **Extracts** and categorizes opportunities for easy consumption

## System Architecture

The project consists of several interconnected modules, each serving a specific purpose in the opportunity discovery pipeline:

### Core Modules

#### 1. Channel Discovery (`scrapper/`, `smart_scrapper/`)
- **Purpose**: Automatically find new Telegram channels related to opportunities
- **Approach**: Uses Telegram's channel recommendation API and UI automation
- **Key Files**:
  - `smart_scrapper/main.py`: Modern Telethon-based channel discovery
  - `scrapper/main.py`: Legacy UI automation approach
  - `scrapper/tel_lb.py`: Telegram UI interaction library

#### 2. Channel Validation (`channel_analyzis/`)
- **Purpose**: AI-powered validation of discovered channels
- **Approach**: Analyzes channel content using OpenAI GPT models to determine relevance
- **Key Files**:
  - `channel_analyzis/main.py`: Main validation workflow
  - `channel_analyzis/AI.py`: AI analysis engine
  - `channel_analyzis/telegram.py`: Telegram API interactions

#### 3. Database Management (`channel_analyzis/database.py`)
- **Purpose**: Persistent storage of channel data and analysis results
- **Technology**: SQLite with structured schema for channels, posts, and validation status
- **Features**: Tracks parsing status, validation results, and channel metadata

#### 4. Opportunity Extraction (`alpha/`)
- **Purpose**: Extract and structure individual opportunities from validated channels
- **Approach**: AI-powered content analysis with structured data extraction
- **Key Files**:
  - `alpha/extraction.py`: Main extraction engine
  - `alpha/extraction_schemas.py`: Data structure definitions

### Supporting Components

#### Configuration Management
- **Files**: `config.json`, `credentials.json`
- **Purpose**: Centralized configuration for API keys, request limits, and system parameters

#### Web Interface (`web.py`)
- **Purpose**: User interface for interacting with discovered opportunities
- **Technology**: Web-based dashboard for opportunity browsing and management

## Technical Implementation

### Technologies Used

#### Core Libraries
- **Telethon**: Modern Telegram client API for channel discovery and content extraction
- **OpenAI API**: GPT models for intelligent content analysis and channel validation
- **Groq API**: Alternative AI provider for cost-effective analysis
- **SQLAlchemy**: Database ORM for robust data management
- **SQLite**: Lightweight database for local data persistence

#### Automation Tools
- **PyAutoGUI**: UI automation for legacy Telegram desktop client interaction
- **BeautifulSoup**: HTML parsing for web-based Telegram content extraction

### Data Flow

```
1. Channel Discovery
   ├── Input: Seed channels from parent_channels.txt
   ├── Process: Telegram recommendation API calls
   └── Output: New channel candidates

2. Channel Validation  
   ├── Input: Channel candidates from discovery
   ├── Process: AI analysis of channel content
   └── Output: Validated opportunity channels

3. Opportunity Extraction
   ├── Input: Validated channels
   ├── Process: AI-powered content structuring
   └── Output: Structured opportunity data

4. User Interface
   ├── Input: Structured opportunities
   ├── Process: Web-based filtering and presentation
   └── Output: User-friendly opportunity dashboard
```

### Key Algorithms

#### Channel Relevance Scoring
The AI validation system uses carefully crafted prompts to assess whether a channel contains:
- Academic opportunities (scholarships, research positions)
- Professional development (internships, training programs)  
- Funding opportunities (grants, competitions)
- Educational resources (courses, workshops)

#### Recommendation Network Traversal
The system leverages Telegram's built-in recommendation algorithm to discover new channels by:
1. Starting with known relevant channels (seed set)
2. Fetching recommendations for each seed channel
3. Recursively exploring recommendations to build a comprehensive network

## Development Evolution

This project represents an iterative development process with several experimental phases:

### Phase 1: Manual UI Automation (`scrapper/`)
- **Approach**: Direct interaction with Telegram desktop client
- **Limitations**: Fragile, slow, desktop-dependent
- **Learning**: Proof of concept for channel discovery feasibility

### Phase 2: API-Based Discovery (`smart_scrapper/`)
- **Approach**: Direct Telegram API usage via Telethon
- **Improvements**: More reliable, faster, programmatically controllable
- **Benefits**: Foundation for scalable solution

### Phase 3: Integrated Analysis System (`channel_analyzis/`)
- **Approach**: Combined discovery, validation, and storage
- **Features**: AI-powered content analysis, persistent data management
- **Result**: Production-ready system for automated opportunity discovery

### Phase 4: Opportunity Extraction (`alpha/`)
- **Approach**: Structured data extraction from validated channels
- **Goal**: Transform raw channel content into actionable opportunity data

## File Structure Details

### Configuration Files
- `config.json`: System configuration (API limits, timeouts, model parameters)
- `credentials.json`: API keys and authentication tokens
- `creation.sql`: Database schema definitions

### Data Files
- `chats.db`: Main SQLite database
- `posts.json`: Cached channel posts for analysis
- `channels/parents.txt`: Seed channels for discovery
- `lists/farcing/childrens.json`: Discovered channel relationships

### Session Files
- `*.session`: Telethon session files for authenticated API access
- Persistent authentication to avoid repeated login requirements

## Usage Examples

### Basic Channel Discovery
```python
# Initialize Telegram client
client = TelegramClient('session_name', 'YOUR_API_ID', 'YOUR_API_HASH')

# Discover channels related to a seed channel
children = telegram.get_children(client, '@education_opportunities')

# Validate each discovered channel
for child in children:
    posts = telegram.fetch_first_5_posts(client, child.username)
    is_relevant = AI.validate_channel(posts)
```

### AI-Powered Channel Validation
```python
# Analyze channel content for relevance
def validate_channel(posts):
    combined_content = "\n".join(posts)
    prompt = f"Analyze if this content relates to opportunities like grants, scholarships, internships: {combined_content}"
    return openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
```

## Current Status and Limitations

### Completed Features
✅ **Channel Discovery**: Automated discovery of new channels via Telegram API  
✅ **AI Validation**: Intelligent filtering of relevant vs. irrelevant channels  
✅ **Data Persistence**: Structured storage of channel data and analysis results  
✅ **Multi-API Support**: Integration with both OpenAI and Groq for AI analysis  

### In Development
🔄 **Opportunity Extraction**: Structured extraction of individual opportunities  
🔄 **Web Interface**: User-friendly dashboard for opportunity browsing  
🔄 **Content Categorization**: Advanced classification of opportunity types  

### Known Limitations
⚠️ **Language Focus**: Primarily designed for Ukrainian/English content  
⚠️ **Manual Oversight**: Requires periodic manual review of AI decisions  
⚠️ **Rate Limiting**: Subject to Telegram API rate limits  
⚠️ **Code Maturity**: Developed as experimental tool rather than production software  

## Technical Requirements

### Dependencies
```
telethon>=1.24.0
openai>=1.0.0
groq>=0.4.0
sqlite3 (built-in)
sqlalchemy>=2.0.0
pyautogui>=0.9.54
beautifulsoup4>=4.11.1
requests>=2.28.0
```

### API Requirements
- **Telegram API**: Requires api_id and api_hash from my.telegram.org
- **OpenAI API**: Requires valid API key for GPT model access  
- **Groq API**: Optional alternative AI provider

### System Requirements
- **Python**: 3.8 or higher
- **Operating System**: Windows, macOS, or Linux
- **Storage**: Minimum 100MB for database and session files
- **Network**: Stable internet connection for API calls

## Academic and Research Applications

### Use Cases
- **Graduate Students**: Finding funding opportunities and research positions
- **Academic Researchers**: Discovering grants and collaboration opportunities  
- **Young Professionals**: Identifying internships and career development programs
- **Institution Administrators**: Monitoring available opportunities for students

### Research Value
This project demonstrates practical applications of:
- **Natural Language Processing**: AI-powered content classification
- **Social Network Analysis**: Mapping relationships between information channels
- **Information Retrieval**: Automated discovery and filtering of relevant content
- **Human-Computer Interaction**: Balancing automation with human oversight

## Future Development Directions

### Technical Enhancements
1. **Machine Learning Pipeline**: Implement supervised learning for improved channel classification
2. **Real-time Processing**: Stream processing for immediate opportunity detection
3. **Multi-language Support**: Expansion beyond Ukrainian/English content
4. **API Optimization**: Improved rate limiting and request batching

### Feature Expansions  
1. **Personalization**: User-specific opportunity filtering based on interests/qualifications
2. **Notification System**: Real-time alerts for new relevant opportunities
3. **Integration APIs**: Connections with university systems and career platforms
4. **Analytics Dashboard**: Insights into opportunity trends and channel performance

## Acknowledgments

This project was developed as a personal tool to address the challenge of efficiently tracking academic and professional opportunities shared through Telegram channels. It represents an iterative learning process in automation, AI integration, and data management.

The codebase reflects experimental development practices, with multiple approaches tested and refined over time. While not production-ready, it demonstrates practical problem-solving using modern Python libraries and AI services.

## License and Usage

This project is shared for educational and research purposes. Users should:
- Respect Telegram's Terms of Service when using their APIs
- Ensure compliance with data privacy regulations
- Use AI services in accordance with provider terms
- Consider rate limiting and ethical use of automated tools

---

*This documentation reflects the current state of an evolving research project. The system continues to be refined based on practical usage and technical discoveries.*
