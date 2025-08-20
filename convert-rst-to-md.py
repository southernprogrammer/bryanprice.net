import os
import pypandoc

# Define source and destination directories
SOURCE_DIR = os.path.join(os.path.dirname(__file__), 'content')
DEST_DIR = os.path.join(os.path.dirname(__file__), 'content-md')

for root, dirs, files in os.walk(SOURCE_DIR):
    # Compute relative path from source root
    rel_path = os.path.relpath(root, SOURCE_DIR)
    dest_path = os.path.join(DEST_DIR, rel_path)

    # Create corresponding directory in destination
    os.makedirs(dest_path, exist_ok=True)

    for file in files:
        if file.endswith('.rst'):
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_path, os.path.splitext(file)[0] + '.md')

            try:
                # Convert .rst to .md using pypandoc
                output = pypandoc.convert_file(src_file, 'markdown', format='rst')
                with open(dest_file, 'w', encoding='utf-8') as f:
                    f.write(output)
                print(f"Converted: {src_file} → {dest_file}")
            except Exception as e:
                print(f"Failed to convert {src_file}: {e}")