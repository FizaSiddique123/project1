import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the footer
footer_match = re.search(r'(<!-- =*[^<]*FOOTER[^<]*=* -->\s*<footer class="site-footer">.*?</footer>)', content, flags=re.DOTALL)
if footer_match:
    footer_html = footer_match.group(1)
    
    # Remove it from the current location
    content = content.replace(footer_html, '')
    
    # Let's see if we have </main>
    if '</main>' in content:
        content = content.replace('</main>', footer_html + '\n</main>')
        print("Inserted before </main>")
    else:
        # It seems the dashboard.html might have lost its </main> tag due to the previous automated edits.
        # Let's insert it at the very bottom of the #site-main-content area, which might just be before the first closing </div> that wraps the content.
        # Actually, wait, the screens are <section class="screen-view">
        # Let's put it right after the last </section> that has screen-view.
        sections = list(re.finditer(r'</section>', content))
        if sections:
            last_section = sections[-1]
            idx = last_section.end()
            content = content[:idx] + '\n' + footer_html + content[idx:]
            print("Inserted after last </section>")
        
    with open('dashboard.html', 'w', encoding='utf-8') as f:
        f.write(content)
else:
    print("Footer not found")
