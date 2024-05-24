import hashlib

def hash_image(file_path):
    with open(file_path, 'rb') as f:
        bytes = f.read()
        hash = hashlib.sha256(bytes).hexdigest()
    return hash

image_hash = hash_image('path/to/image.jpg')
print(f'Image Hash: {image_hash}')