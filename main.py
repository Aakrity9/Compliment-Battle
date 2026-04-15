import google.generativeai as genai
import webbrowser
import urllib.parse
import os

# API Key Setup
# Note: GitHub par daalte waqt yahan apni key mat likhna, 
# balki program run karte waqt input dena safe hota hai.
API_KEY = input("Enter your Gemini API Key: ")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

def play_situational_music(vibe, language):
    """Search and play music based on the game situation and chosen language."""
    query = f"{vibe} song in {language}"
    url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
    print(f"🎵 AI is changing the vibe to: {vibe} ({language})")
    webbrowser.open(url)

def start_compliment_battle():
    print("\n--- 🌸 WELCOME TO THE COMPLIMENT BATTLE 🌸 ---")
    print("Kill them with kindness! Enemy's Ego can only be destroyed by true praise.")
    
    # Language Selection
    print("\nSelect your Music Language Preference:")
    print("1. Hindi")
    print("2. English")
    lang_choice = input("Enter choice (1/2): ")
    user_lang = "Hindi" if lang_choice == "1" else "English"

    enemy_ego = 100
    player_health = 100

    while enemy_ego > 0 and player_health > 100 or True: # Loop runs until game ends
        print(f"\n[Enemy Ego: {enemy_ego}%] | [Your Health: {player_health}%]")
        praise = input("\nWrite a compliment to attack: ")

        # Gemini API Logic: Checking for Positivity (Sentiment)
        prompt = f"""
        User said this praise to the enemy: '{praise}'
        Rules for the game:
        1. If it's a very positive and sincere compliment, set 'EFFECT' to 'CRITICAL_HIT'.
        2. If it's negative, rude, or fake, set 'EFFECT' to 'BACKFIRE'.
        3. Suggest a {user_lang} song vibe (e.g., 'Happy Bollywood', 'Sad Hollywood', 'Thug Life').
        4. Give a funny reaction from the enemy.
        Return in this format: EFFECT: <val> | MUSIC: <vibe> | MSG: <msg>
        """

        try:
            response = model.generate_content(prompt)
            result = response.text
            
            # Parsing response
            if "CRITICAL_HIT" in result:
                damage = 25
                enemy_ego -= damage
                print(f"✨ WOW! Your kindness hurt him. Ego -{damage}%")
                play_situational_music("winning energetic", user_lang)
            else:
                damage = 20
                player_health -= damage
                print(f"💀 Ouch! That wasn't nice enough. Enemy attacked you! Health -{damage}%")
                play_situational_music("funny fail", user_lang)

            print(f"Enemy says: {result.split('|')[-1]}")

            if enemy_ego <= 0:
                print("\n🏆 VICTORY! You won with pure kindness!")
                play_situational_music("victory celebratory", user_lang)
                break
            if player_health <= 0:
                print("\n🥀 DEFEAT! You were too salty for this game.")
                break
        except Exception as e:
            print("Connect your internet and check API key!")
            break

if __name__ == "__main__":
    start_compliment_battle()
