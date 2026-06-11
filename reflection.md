# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  Gives the wrong hints. 
  Lets you enter numbers out of range

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|44     |Hint: Lower        |Hint: Higher     | none                   |
|100000 |Out of range       |Gives wrong hint | none                   |
|Click New game button |clear screen|no change |                       |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Copilot

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI agreed that the New Game button doesn't reset the status so it is always stuck in won or lost state. It added playing as a state after which the New Game button effectively cleared the state and generated a new guess. I verified this by manual checking.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
The AI added default values to parameters low=1 and high = 100. This was not needed anywhere because parse_guess() function is always called with explicit values of each difficulty level. I verified this function works by prompting Copilot for pytest cases.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I ran pytest cases and I also ran manual checks on the bugs I observed to see if they were displaying the expected behavior.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
I ran a pytest to investigate why my game's hint logic was inverted. Because the input and secret were being converted into strings, the code was using alphabetical comparison. I evaluated how the code compared 9>10. Since that returned true, it proved that this was the root cause and helped me fix the bug by casting values into integers.

- Did AI help you design or understand any tests? How?
I described the problem. What I expected, what I got and highlighted the logic flaw I suspected. The AI translated that int o structured pytest guesses. When the test failed, it confirmed by theory allowing me to perform the fix. I tested it again after debug to make sure the code was now running as expected.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reflects the code change automatically without having to refresh the page or relaunch the code everytime. The rerun is the streamlit app running everytime from the start when the user interacts with the website. To keep the current session as a buffer though, we need to have session states that remember current data. The session state allows the app to remember the users inputs, scores, etc when the page reruns itself.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
