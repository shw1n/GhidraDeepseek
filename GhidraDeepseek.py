# Forked from GptHidra

import urllib2
import json
from ghidra.util.task import TaskMonitor
from ghidra.app.decompiler import DecompInterface

# Get your API key from https://api.deepseek.com and add it in here when you create your script
API_KEY = ''

def explainFunction(c_code):
    """
        Calls the Deepseek API to explain the given code.

        Args:
            c_code (str): The code to be explained.

        Returns:
            str: The explanation provided by the API.
    """
    url = 'https://api.deepseek.com/v1/chat/completions'
    data = {"messages":[ {"role": "user","content":"Explain code:\n" + c_code} ], "model": "deepseek-reasoner"}

    # Use this is you want to use deepseek chat
    #data = {"messages":[ {"role": "user","content":"Explain code:\n" + c_code} ], "model": "deepseek-chat"}
    data = json.dumps(data)

    req = urllib2.Request(url, data,
                          {'Authorization': 'Bearer ' + API_KEY,
                           'Content-Type': 'application/json'})
    response = json.loads(urllib2.urlopen(req).read())

    if "error" in response:
        raise ValueError(response["error"])
    else:
        return response["choices"][0]["message"]["content"]


def getCurrentDecompiledFunction():
    """
        Returns the C code for the function currently selected in the Ghidra decompiler.

        Returns:
            str: The C code for the selected function.
    """
    # Reference: https://ghidra.re/ghidra_docs/api/ghidra/app/decompiler/DecompInterface.html

    # Create a TaskMonitor object
    monitor = TaskMonitor.DUMMY

    # Create a DecompInterface object
    decompiler = DecompInterface()

    # Set the current program for the decompiler
    decompiler.openProgram(currentProgram)

    # Get the current address and the function containing it
    currentAddress = currentLocation.getAddress()
    function = getFunctionContaining(currentAddress)

    if function is None:
        raise ValueError("No function is currently selected.")

    # Decompile the function and get the resulting C code
    try:
        return decompiler.decompileFunction(function, 30, monitor).getDecompiledFunction().getC()
    except Exception as e:
        raise ValueError("Unable to decompile function: " + str(e))

try:
    c_code = getCurrentDecompiledFunction()
    explanation = explainFunction(c_code)
    print(explanation)
except ValueError as e:
    print(e)
