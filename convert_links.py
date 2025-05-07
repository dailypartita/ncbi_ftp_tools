import json

# Load the JSON file
with open('nt-nucl-metadata.json', 'r') as f:
    data = json.load(f)

# Extract URLs and convert to rsync format with .md5
with open('nt.links.list', 'w') as outfile:
    for url in data['files']:
        # Convert ftp:// URLs to rsync:// format
        rsync_url = url.replace('ftp://', 'rsync://')
        # Append .md5 to each URL
        md5_url = rsync_url + '.md5'
        outfile.write(rsync_url + '\n' + md5_url + '\n')

print('Created nt.links.md5.list with', len(data['files']), 'entries') 