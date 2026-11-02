request basic auth:
                  In request basic auth i firstlt imported requests and created variables username and password to use input the values ,
                  and passed the variables as arguments in the function called (basic_auth_request) used the requests.get to and httpbin 
                  site to test out the basic authentication and stored it in r, then finally to check if it worked i used another requests 
                  functionality (.ok) which checks the status of the request and if 200 then gives result true .
