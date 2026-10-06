import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I want to insert `<div id="possible-conditions-container" class="possible-conditions-section" style="display: none;"></div>`
# at the end of `<section class="screen-view" id="screen-result">`

match = re.search(r'(<section class="screen-view" id="screen-result">.*?</section>)', content, re.DOTALL)
if match:
    section_html = match.group(1)
    if 'id="possible-conditions-container"' not in section_html:
        new_section = section_html.replace('</section>', '\n      <!-- POSSIBLE CONDITIONS LAYER -->\n      <div id="possible-conditions-container" class="possible-conditions-section" style="display: none;"></div>\n    </section>')
        content = content.replace(section_html, new_section)
        with open('dashboard.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated dashboard.html successfully.")
    else:
        print("Container already exists in dashboard.html")
else:
    print("Could not find screen-result in dashboard.html")
