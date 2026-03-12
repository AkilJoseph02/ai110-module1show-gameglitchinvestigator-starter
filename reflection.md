# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
    1. When typing an answer, "Press Enter to apply" appears. Pressing Enter doesn't enter the guess. 
    2. The hints to guess the right answer weren't accurate. For example, I had a game where the answer was 9. However, the hint system lead me between 34 and 35 (go higher for 34, lower at 35). 
    3. After starting new game, the attempts aren't reset. 
    4. Attempts on normal should start at 8, starts at 7 instead. 
    5. The range of the secret numbers in Normal and Hard difficulty (1-100 and 1-50 respectively) should be swapped.
    6. The number of attempts allowed for Easy and Normal difficulty (6 and 8 respectively) should be swapped as well.
    7. Lastly, starting a new game with the "New Game" button is impossible. The button didn't work, a secret number would be updated, but the input for guesses would remain locked after I either game overed or won.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Answer: Used Copilot. The chat client gave me the suggestion to add "st.rerun()" after processing a guess to immediately populate the history array after a guess. This skipped the "You win" screen and just went to the "You already won" screen.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
Answer: I decided a bug was fixed after running a couple with the game's UI and logic. For example, when it came to the issues with hints either being opposite or outright inaccurate, after directing copilot to the part of the code that handled the hint system, I checked if the number I inputted would give the right hint.

If the secret number was 40, and I inputted 39, the hint "Go HIGHER" popped up, which was accurate. If I then inputted 41, the hint "Go LOWER" popped up, which was also accurate. And that point, I determined that the hint system was corrected using Copilot. The AI helped me understand the code after I asked for a specific reason why the hint system wasn't working correctly (issues with boolean logic).

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?
Answer: The secret number kept changing because, once the game was either won or lost, the py file would check the website's state. Specifically if "secret" is currently included in the state. If not, the py file will generate a random number for the secret number based on the range determined by the current difficulty.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
Answer:
