def ipinfo(self, ip:str, token:str) -> None:
    ''' Uses the ipinfo.io API to get details about the IP address

        Args: 
            ip (str): an IP address.
            token (str): an IPInfo API token 
            
        Returns: 
            dict: the results as a dictionary
    '''
    
    # Base case: no token given 
    if not token: 
        print("NOTICE: Not given IPInfo API token. Returning.")
        return {}
    
    try:
        print(f"IPInfo: Looking up {ip}")
        
        # Perform DNS lookup to get the server IP address
        url = f"https://ipinfo.io/{ip}?token={token}"
        headers = { 
            "Accept": "application/json"
        }
        
        ip_info = requests.get(url, headers=headers).json()   
        
        # Extract complex attributes
        loc:list[float] = ip_info.get('loc', '')
        latitude:float = None
        longitude:float = None
        if loc: 
            loc = loc.split(',')
            latitude:float = float(loc[0])
            longitude:float = float(loc[1])

        split_as:list = ip_info['org'].split(" ")
        asn:int = split_as[0][2:]
        as_org:str = " ".join(split_as[1:])
        
        return {
            'hostname': ip_info.get('hostname', ''),
            'city': ip_info.get('city', ''),
            'region': ip_info.get('region', ''),
            'country': ip_info.get('country', ''),
            'timezone': ip_info.get('timezone', ''),
            'asn': asn,
            'asn_org': asn_org
            
        }
    
    except Exception as e:
        return {}