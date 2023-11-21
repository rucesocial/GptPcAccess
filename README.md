# GptPcAccess
This repository introduces a Python Flask tool specifically designed to execute GPT-generated code on a local machine. Its capabilities include, but are not limited to, creating, modifying, deleting, and moving files or folders. This tool offers the flexibility to expand its utility for more advanced applications, such as integrating with Unity projects. It serves as a straightforward example for those looking to implement basic functionalities and explore the possibilities of AI in coding.It works by ChatGPT making a GET request.
<p align="center">
  <a href="https://bit.ly/3R5pMUg">Discord</a> | <a href="https://bit.ly/46AZJsR">Linkedin Group</a>
</p>
<p align="center">
  <img src="https://blogger.googleusercontent.com/img/a/AVvXsEghIEJFxIbDBwGtwwAHFimwmzyWfpGc_Kdi4aWXubLVQpHaa2tgMdWRko9-_BxSPBUj0mn9AKtu67FTuk3XV1357IzVBb9Qexkn0ABFtB7tSE-UVrGNucGl7jPCbyFshDY6yZmkig9_HrYCc9qA0zLxTDLkqa-5wZ9fewmmZJmBW6_doHkI__rmKVYiSDQ" alt="GptPcAccess Demo">
</p>


## Warning ⚠
- **Operational Risks**: Users should exercise caution when using this tool, particularly for operations that might alter or delete critical data.
- **Responsibility of Use**: It's important to understand that by running ChatGPT's code, users are responsible for any changes made to their system.

## How It Works
<p align="center">
  <a href="https://bit.ly/3R5UfBQ">
    <img src="https://blogger.googleusercontent.com/img/a/AVvXsEhJvBqvpNnsO9oEXV8JhRgzFzAPxlWSEJxConFJIusS-a0rpiw8EFbchHCh2GBA3JLAIpPGSQBLELB7vMrHqKkM9EC5WU6fj9r6goktabCgEVfDipDp_kWxy8xtwTVvPn9mEaFiElXpgtsW0dwa6Fa3AM74H37lhZMXeKm5elmBCI-Yintw8EUULO5HSfg" alt="GptPcAccess Demo" width="500">
  </a>
</p>


- **Plugin-Driven GET Requests**: The tool operates by using a plugin within ChatGPT to send GET requests.
- **Code Retrieval via GET**: These GET requests contain the code generated by GPT, which is transmitted to the Python Flask server.
- **Ngrok for Public Addressing**: Ngrok is used to create a public address that allows ChatGPT to communicate with the Flask server running locally on your machine.
- **Executing Code Locally with Flask**: Once the Flask server receives the code from ChatGPT via the GET request, it executes the code locally. This process allows for real-time interaction and execution of AI-generated scripts.


# Setup Instructions for GptPcAccess

Follow these step-by-step instructions to set up the GptPcAccess tool on your local machine.

## Step 1: Download and Run the Python Code

- Download the Python code provided in the [Python](https://github.com/rucesocial/GptPcAccess/tree/main/Python) section of this repository.
- Ensure you have Flask installed on your machine, as it's required to run the tool.
- Run the Python code. This will start listening on port 5000.

## Step 2: Set Up Ngrok

- Download and install Ngrok on your machine.
- Open a command prompt or terminal and run the command `ngrok http 5000`.
- Ngrok will provide you with a public address. Keep this address handy for the next steps.

## Step 3: Configure ChatGPT Plugins

- In ChatGPT, go to the plugins section and load the "Web Reader" plugin.
- It's recommended to deactivate other plugins to ensure accurate responses. Make sure only the "Web Reader" plugin is active.

## Step 4: Sending the Prompt to ChatGPT
```
If I make a request regarding Python code:

Create the requested Python code.
Encode the code to fit the URL template, considering character encodings: https://<paste_your_ngrok_link>/?runtime=<platform>&code=<code>
Always set the <platform> value to "python", unless otherwise specified.
Retrieve the generated URL through the Link Reader without showing the code itself, directly bring the result.
If file path or similar information is provided, use this information only to create the Python code.
Character Encodings:

Space: %20
!: %21
": %22
+: %2B
... (For example, use "i%2B" for "i++") .. (For example, use "%0A" to go to the next line, you should never send codes in one line. If you understood this, you need to say "I understood"))
EXAMPLE USAGE:

If I say "print the contents of the file named pat.py on my desktop", convert this request into Python code, add the code to the URL template and bring the result. Do this without waiting for a confirmation. 

#1  Don't waste time explaining, just take action.
#2 If you have plugins installed, your priority should be to use them.
#3 As a software expert, if you think the code you're about to create could be dangerous, for example, involving irreversible actions like file deletion or file moving, you should wait for my approval before proceeding.

Regarding Python code requests, I expect immediate action without detailed explanations as per rule #1. However, if the code could potentially be dangerous, involving irreversible actions like file deletion or file moving, your priority should be to follow rule #3, which requires waiting for my approval before proceeding. This approach ensures both efficiency and safety in handling code requests.
```

- Use the provided prompt template. Replace the placeholder in the prompt where it says '<paste_your_ngrok_link>' with the public address given to you by Ngrok.
- Send the prompt to ChatGPT.

And that's it! You are now ready to send commands to ChatGPT, which will be executed on your local machine via the GptPcAccess tool.

## Step 5: How to Integrate with Unity

1. Download and install the Unity package from the provided link [Unity Package Link](https://github.com/rucesocial/GptPcAccess/releases/tag/UnityRelase).
2. Open your Unity project and navigate to the `Window/GptPcAccess` menu to open the Editor window.
3. Click on the `Start Listening` button to activate the server. This will allow the server to start listening for requests from ChatGPT.
4. Now, continue your conversation with ChatGPT. Initially, you need to send the first prompt to ChatGPT. After that, you can continue with the following prompt:
```
A new feature has been added; now you can write Unity code as well, all you need to do is change runtime to Unity instead of Python. runtime=unity

But there are things to be careful about when writing Unity code:

-Always write a Unity Editor script, not a MonoBehaviour.
-It provides its functionality as a menu item placed under 'Edit' > 'Do Task'.
-It doesn’t provide any editor window. It immediately does the task when the menu item is invoked.
-Don’t use GameObject.FindGameObjectsWithTag.
-There is no selected object. Find game objects manually.
-Do not inherit from any class (For example, do not use MonoBehaviour).
-I only need the script body. Don’t add any explanation.
-Make sure you add all namespaces, there should be no missing namespaces.
-If you use a class that doesn't exist in the code, it will cause problems. Build without relying on external or undefined classes.
-If a prefab is not specified you should use primitive objects.

Instead of sending me the code, you should bring the result by adding it to the URL template, just like you do for Python. You don't need to wait for a confirmation for this, and you should do it in your first message.
... (Use 'i%2B' for 'i++') ... (Use '%0A' for 'new line', never send the codes in a single line. If you understand this, you need to say you understood).

If you have understood, I might ask you for a Unity code.

```
5. That's it! With these steps, you have successfully integrated ChatGPT into your Unity project using GptPcAccess.

(I drew upon some of the strategies used in Keijiro's 'AI command')

# Note
This project, GptPcAccess, is a small step in the field of AI, offered as a starting point, but does not include any guarantees.
# Thank you!



