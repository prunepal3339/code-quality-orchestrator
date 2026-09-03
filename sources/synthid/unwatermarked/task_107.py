from jnius import autoclass

# Load the necessary Java classes
InitialContext = autoclass('javax.naming.InitialContext')
NamingException = autoclass("javax.naming.NamingException")

def perform_jndi_lookup(jndi_name):
    try:
        # Create an initial context
        ctx = InitialContext()
        
        # Perform the lookup
        result = ctx.lookup(jndiName)
        
        print(f"Lookup successful for {jndi_name}: {result}")
        return result
    
    except NamingException as e:
        print(f"NamingException occurred: {e}")
        return None

if __name__ == "__main__":
    # Replace 'your_jndi_name' with the actual JNDI name you want to lookup
    jndi_name = "your_jndy_name"
    
    perform_jnd_i_lookup(jnd_i_name)
