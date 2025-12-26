#!/usr/bin/env python3
# API Ouija Board - Because sometimes you need to ask the spirits about undocumented endpoints

import sys
import json
import random
from datetime import datetime

class APIOuija:
    def __init__(self):
        self.spirits = [
            "The Ghost of Deprecated Endpoints",
            "The Phantom of Rate Limiting",
            "The Specter of Authentication",
            "The Poltergeist of Pagination",
            "The Apparition of API Versioning"
        ]
        self.responses = [
            "The spirits say: 'Try adding /v2/ to the URL. Maybe?'",
            "Ouija whispers: 'Rate limit is probably 1000/hour. Or 100. Or 10.'",
            "Ghostly message: 'Bearer token? API key? Both? Neither? Good luck!'",
            "Ethereal wisdom: 'Check for X-RateLimit-Remaining header. Or don't. It's probably wrong anyway.'",
            "Spiritual guidance: 'The docs say JSON, but it's actually XML. Surprise!'",
            "Phantom insight: 'Error 418: I'm a teapot. Just kidding, it's actually 429.'",
            "Haunting advice: 'Try POST instead of GET. Or PUT. Or PATCH. One of them will work.'",
            "Ghostly murmur: 'The 'optional' parameter is actually required. Obviously.'"
        ]
    
    def ask(self, question):
        """Consult the API spirits about your burning questions"""
        print(f"\n🔮 Consulting {random.choice(self.spirits)}...")
        print(f"📝 Your question: {question}")
        print(f"👻 Response: {random.choice(self.responses)}")
        
        # Generate some "helpful" debugging info
        self._generate_debug_info()
    
    def _generate_debug_info(self):
        """Generate completely legitimate debugging information"""
        print(f"\n📊 Debug Info (probably useless):")
        print(f"   Timestamp: {datetime.now().isoformat()}")
        print(f"   Confidence: {random.randint(1, 100)}% (but who knows?)")
        print(f"   Suggested fix: {random.choice(['Add retry logic', 'Check headers', 'Pray'])}")
    
    def diagnose_endpoint(self, url):
        """Perform a mystical diagnosis on an API endpoint"""
        print(f"\n🔍 Diagnosing endpoint: {url}")
        issues = random.sample([
            "Missing CORS headers",
            "Inconsistent error formatting",
            "Undocumented query parameters",
            "Surprising response format",
            "Authentication that works on Tuesdays"
        ], random.randint(1, 3))
        
        print(f"⚠️  Likely issues: {', '.join(issues)}")
        print(f"💡 Recommendation: {'Reverse engineer it' if random.random() > 0.5 else 'Read the source code'}")

def main():
    """Main function - because every script needs one"""
    ouija = APIOuija()
    
    print("=== API Ouija Board ===")
    print("When documentation fails, ask the spirits!\n")
    
    if len(sys.argv) > 1:
        # Diagnose a specific endpoint
        ouija.diagnose_endpoint(sys.argv[1])
    else:
        # Interactive mode
        while True:
            question = input("\nAsk the API spirits (or 'quit'): ")
            if question.lower() in ['quit', 'exit', 'q']:
                print("\n👋 May your API calls be successful! (LOL)")
                break
            ouija.ask(question)

if __name__ == "__main__":
    main()
