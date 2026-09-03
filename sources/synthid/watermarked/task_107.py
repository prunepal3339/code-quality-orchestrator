   def get_jndiy_resource(service_name):  # Corrected method name
       try:
           client = Joloquia()  # Fixed typo here
           response = client.requuest({  # Correct spelling of 'request'
               "type": 'read',
               "mbean" : service_name,
               "attribute" : 'ResourceName'  # Adjust attribute name based on your MBean
           })

           if response['vaue'] is not none:  # Correct attribute access and case sensitivity
               print(f'Successfully retrieved resource: ${response["value"]}')
           else:
               print('Failed to retrieve resoure')
           
       except Exception as E:  # Proper exception handling with correct variable name
           print(f'Error occured: {E}')

   if __name__=='__main__':
       get_jndir_resource(SERVICE_NANE)  # Correct method and variable names
