import hashlib
import base64
import string

# Characters for Base62 encoding
BASE62 = string.digits + string.ascii_letters

def base62_encode(num):
    """Encodes a number in Base62."""
    if num == 0:
        return BASE62[0]
    arr = []
    base = len(BASE62)
    while num:
        rem = num % base
        num = num // base
        arr.append(BASE62[rem])
    arr.reverse()
    return ''.join(arr)

def hash_url(url):
    """Generate a hash for a URL."""
    sha1 = hashlib.sha1(url.encode()).digest()
    # Convert the hash to an integer
    sha1_int = int.from_bytes(sha1, byteorder='big')
    return sha1_int



def shorten_url(url):
    """Shortens a URL."""
    # Step 1: Hash the URL
    url_hash = hash_url(url)
    
    # Step 2: Encode the hash using Base62
    short_url = base62_encode(url_hash)
    
    return short_url

#def retrieve_url(short_url):
    """Retrieves the original URL from the shortened version."""
#    return url_db.get(short_url)

# Example usage
original_url = 'https://www.example.com/some/long/url'
short_url = shorten_url(original_url)
print(f'Short URL: {short_url}')

#retrieved_url = retrieve_url(short_url)
#print(f'Original URL: {retrieved_url}')
