# Define the initial counter value
paused_offer_count = 0

# Define the DELAY function
def DELAY():
    # Access the global paused_offer_count variable
    global paused_offer_count
    
    # Increment the paused offer counter
    paused_offer_count += 1
    
    # Check if the counter has reached 200
    if paused_offer_count >= 200:
        # Reset the counter
        paused_offer_count = 0
        
        # Your code for the DELAY function here
        # ...
        
    else:
        # If the counter hasn't reached 200, do nothing
        pass
