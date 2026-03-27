import sys                                                                                                            
                                                                                                                        
def main():                                                                                                           
    path = sys.argv[1] if len(sys.argv) > 1 else input("Enter file path: ")                                           
                                                                                                                        
    try:        
        with open(path, "r") as f:
            for line in f:                                                                                            
                # print(line, end="")
                result = parse_nmea(line)
                print(result)  
    except FileNotFoundError:                                                                                         
        print(f"Error: file '{path}' not found.", file=sys.stderr)                                                    
        sys.exit(1)


def parse_nmea(line):                                                                                                 
    """                                                                                                               
    Parse a single NMEA 0183 sentence.                                                                                
                                                                                                                        
    Returns a dict with:                                                                                              
        - talker:    2-char talker ID (e.g. 'GP', 'GN')                                                                 
        - sentence:  3-char sentence type (e.g. 'GGA', 'RMC')                                                           
        - fields:    list of data fields (strings)                                                                      
        - checksum:  checksum from sentence (hex string)                                                                
        - valid:     True if checksum matches                                                                           
                                                                                                                        
    Raises ValueError on malformed input.                                                                             
    """                                                                                                               
    line = line.strip()

    if not line.startswith("$"):
        # raise ValueError(f"Sentence must start with '$': {line!r}")
        print(f"Sentence must start with '$': {line!r}")
        return
                                                                                                                        
    # Split off checksum
    if "*" in line:                                                                                                   
        body, checksum_str = line[1:].rsplit("*", 1)                                                                  
        checksum_str = checksum_str[:2].upper()
    else:                                                                                                             
        # raise ValueError(f"No checksum found in sentence: {line!r}")
        print(f"No checksum found in sentence: {line!r}")
        return
                                                                                                                        
    # Validate checksum (XOR of all bytes between $ and *)
    computed = 0                                                                                                      
    for ch in body:                                                                                                   
        computed ^= ord(ch)                                                                                           
    computed_str = f"{computed:02X}"                                                                                  
                                                                                                                        
    # Split fields                                                                                                    
    parts = body.split(",")
    if len(parts[0]) < 5:                                                                                             
        raise ValueError(f"Sentence type too short: {parts[0]!r}")                                                    
   
    talker  = parts[0][:2]                                                                                            
    sentence = parts[0][2:5]
    fields  = parts[1:]                                                                                               
   
    return {                                                                                                          
        "talker":   talker,
        "sentence": sentence,
        "fields":   fields,
        "checksum": checksum_str,
        "valid":    checksum_str == computed_str,                                                                     
    }
                                                                                                                        
                  
# if __name__ == "__main__":
#     examples = [
#         "$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47",                                          
#         "$GPRMC,220516,A,5133.82,N,00042.24,W,173.8,231.8,130694,004.2,W*70",                                         
#         "$GPGLL,4916.45,N,12311.12,W,225444,A,*1D",                                                                   
#     ]                                                                                                                 
                                                                                                                        
#     for sentence in examples:                                                                                         
#         result = parse_nmea(sentence)
#         print(result)                                                                                                     
                                                                                                                        
if __name__ == "__main__":                                                                                            
    main() 