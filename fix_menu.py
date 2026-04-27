import re

def fix_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Change mobile menu: remove 'hidden' class, add style="display:none"
    old_menu = 'id="mobile-menu" class="fixed inset-0 z-[60] bg-brand-dark/95 backdrop-blur-md flex flex-col items-center justify-center gap-6 hidden"'
    new_menu = 'id="mobile-menu" class="fixed inset-0 z-[60] bg-brand-dark/95 backdrop-blur-md flex flex-col items-center justify-center gap-6" style="display:none"'
    if old_menu in content:
        content = content.replace(old_menu, new_menu, 1)
        print(f'  [OK] {path}: mobile menu updated')
    else:
        print(f'  [SKIP] {path}: pattern not found')

    # 2. Replace JS: use style.display instead of classList
    old_js = "menuBtn.addEventListener('click', () => mobileMenu.classList.remove('hidden'));\n            mobileClose.addEventListener('click', () => mobileMenu.classList.add('hidden'));\n            mobileMenu.querySelectorAll('a').forEach(link => {\n                link.addEventListener('click', () => mobileMenu.classList.add('hidden'));\n            });"
    new_js = "menuBtn.addEventListener('click', () => { mobileMenu.style.display = 'flex'; });\n            mobileClose.addEventListener('click', () => { mobileMenu.style.display = 'none'; });\n            mobileMenu.querySelectorAll('a').forEach(link => {\n                link.addEventListener('click', () => { mobileMenu.style.display = 'none'; });\n            });"
    if old_js in content:
        content = content.replace(old_js, new_js)
        print(f'  [OK] {path}: JS updated')
    else:
        print(f'  [SKIP] {path}: JS pattern not found')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

files = [
    'index.html',
    'about.html',
    'budget-calculator.html',
    'cost-faq.html',
    'design-styles.html',
    'portfolio.html',
    'renovation-cost.html',
    'renovation-process.html',
]

for f in files:
    fix_file(f)
