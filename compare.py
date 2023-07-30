import hashlib

def compare(string1, string2):

    # convert strings to binary val
    string1 = string1.encode('utf-8')
    string2 = string2.encode('utf-8')

    hash1 = calculate_sha256_hash( string1 )
    hash2 = calculate_sha256_hash( string2 )

    if ( hash1 == hash2 ):
        return True
    else:
        return False

def calculate_sha256_hash(data):
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Update the hash object with the data from the byte array
    sha256_hash.update(data)

    # Get the hexadecimal representation of the hash
    hash_result = sha256_hash.hexdigest()

    return hash_result

# Example usage: ####################################
string1 = b"Hello, this is a test message!"
hash_value = calculate_sha256_hash(string1)
print("SHA-256 Hash for string1:", hash_value)


string2 = b"New message"
hash_value = calculate_sha256_hash( string2 )

print("SHA-256 Hash for string2:", hash_value)
print('\n\n')

print('Testing comparison function')


####################################################
if (compare('Hi', 'Hi')):
    print('Hi is equal to hi')
else:
    print('Hi is not equal to hi')


######################################################
if (compare('Hi', 'hi')):
    print('Hi is equal to hi')
else:
    print('hi is not equal to hi')



# Output:
# PS C:\Users\Abdul\Desktop\programs> python -u "c:\Users\Abdul\Desktop\programs\stringComparisonUsingHash.py"
# SHA-256 Hash for string1: c8d3d67f662a787e96e74ccb0a77803138c0f13495a186ccbde495c57c385608
# SHA-256 Hash for string2: 78f5975a5d705e9528dd0e8d41206534b7e8c269b139bb151d5c0ca0928247c3



# Testing comparison function
# Hi is equal to hi
# hi is not equal to hi
