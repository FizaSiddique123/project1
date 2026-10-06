import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<a href="#" class="nav-link-disabled">.*?</a>\s*', '', content, flags=re.DOTALL)

def remove_empty_groups(match):
    group = match.group(0)
    if 'nav-link' not in group and 'btn' not in group:
        return ''
    return group

# A bit fragile, but we can do a simpler replacement for the entire nav-groups that we know are empty.
empty_groups = [
    r'<div class="nav-group">\s*<div class="nav-group-title">CARE</div>\s*</div>',
    r'<div class="nav-group">\s*<div class="nav-group-title">RECORDS</div>\s*</div>',
    r'<div class="nav-group">\s*<div class="nav-group-title">ASSISTANCE</div>\s*</div>',
    r'<div class="nav-group" style="margin-bottom:16px;">\s*</div>'
]

for g in empty_groups:
    content = re.sub(g, '', content, flags=re.DOTALL)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)
