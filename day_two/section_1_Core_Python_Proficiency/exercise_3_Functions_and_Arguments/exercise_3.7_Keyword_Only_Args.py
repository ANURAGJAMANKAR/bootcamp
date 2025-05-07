"""
Keyword Only Args

Instructions:
Complete the exercise according to the requirements.
"""

# Author: Anurag

"""
This function enforces keyword-only arguments using `*`.
Arguments after `*` must be passed as keywords.
"""

def configure(*, debug=False, verbose=True):
    print(f"Debug: {debug}, Verbose: {verbose}")

configure(debug=True, verbose=False)

# This will error:
# configure(True, False)
