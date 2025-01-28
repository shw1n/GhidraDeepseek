# GhidraDeepseek

GhidraDeepseek is a Ghidra plugin forked from GptHidra that uses the [Deepseek](https://api.deepseek.com/) to explain functions. With GhidraDeepseek, you can easily understand the purpose and behavior of functions in your codebase.

![example.gif](images/example.gif)

## Defaults to R1
Self-explanatory

## Requirements

- Ghidra `>= 10.1.5` (https://ghidra-sre.org).
- An API key for the Deepseek API

## Installation

1. Download the GhidraDeepseek script
2. Open the Ghidra Script Manager (found in the `Tools` menu).
3. Click the `New` button to create a new script.
4. Select `Python` as the language and give the script the name `GptHidra.py`.
5. Paste the contents of the GptHidra.py script into the editor window.
6. Replace `API_KEY = ''` with your Deepseek API key.
7. Click the `Save` button to save the script.

## Usage

To use GhidraDeepseek, select a function in the Ghidra decompiler and do one of the following:

1. Press `Ctrl + Alt + G` (you can edit the script to change this shortcut).

2. Go to `Tools -> GptHidra` (you can edit the script to change this menu item).

An explanation of the selected function will be printed to the Ghidra console.



## References

[https://ghidra.re/ghidra_docs/api/ghidra/app/decompiler/DecompInterface.html](https://ghidra.re/ghidra_docs/api/ghidra/app/decompiler/DecompInterface.html)



## Support
You can support my work buying me a coffee:

Check out the original GptHidra


## Stargazers over time

[![Stargazers over time](https://starchart.cc/evyatar9/GptHidra.svg)](https://starchart.cc/evyatar9/GptHidra)
