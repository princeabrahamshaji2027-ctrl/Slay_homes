import re

with open('templates/base.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Tailwind config colors for dark theme
dark_colors = """
                    "colors": {
                        "background": "#0b0b0f",
                        "on-background": "#f8f9ff",
                        "surface": "#12121a",
                        "on-surface": "#f8f9ff",
                        "surface-variant": "#1a1a26",
                        "on-surface-variant": "#a1a7b3",
                        "surface-container-lowest": "#050508",
                        "surface-container-low": "#0b0b0f",
                        "surface-container": "#12121a",
                        "surface-container-high": "#1a1a26",
                        "surface-container-highest": "#232333",
                        "outline": "#717783",
                        "outline-variant": "#333344",
                        "primary": "#3b82f6",
                        "on-primary": "#ffffff",
                        "primary-container": "#1e3a8a",
                        "on-primary-container": "#dbeafe",
                        "secondary": "#10b981",
                        "on-secondary": "#ffffff",
                        "secondary-container": "#064e3b",
                        "on-secondary-container": "#d1fae5",
                        "error": "#ef4444",
                        "on-error": "#ffffff",
                        "error-container": "#7f1d1d",
                        "on-error-container": "#fee2e2"
                    },"""

content = re.sub(r'"colors":\s*{[^}]*}(?:,[^}]*}|)', dark_colors, content, count=1, flags=re.DOTALL)

# 2. Fix CSS for mobile sidebar
mobile_css_old = r'''        /\* Mobile Drawer State - Removed to unify behavior \*/
        @media \(max-width: 767px\) {
            .sidebar-container {
                width: var\(--sidebar-width\);
                z-index: 100;
                height: 100vh;
                left: 0;
            }
            .main-content {
                margin-left: var\(--sidebar-width\);
            }
            body.sidebar-collapsed .main-content {
                margin-left: var\(--sidebar-collapsed-width\);
            }
            body.sidebar-collapsed .sidebar-container {
                width: var\(--sidebar-collapsed-width\);
            }
            body.sidebar-collapsed .sidebar-text,
            body.sidebar-collapsed .sidebar-header-desc {
                display: none !important;
            }
        }

        .sidebar-overlay {
            display: none; /\* Overlay not needed if pushing content \*/
        }'''

mobile_css_new = r'''        /* Mobile Drawer State */
        @media (max-width: 767px) {
            .sidebar-container {
                width: var(--sidebar-width);
                position: fixed;
                z-index: 100;
                height: 100vh;
                left: 0;
                transform: translateX(0);
                background-color: #12121a !important; /* Ensure dark background */
                border-right: 1px solid #333344 !important;
                transition: transform var(--transition-speed) cubic-bezier(0.4, 0, 0.2, 1);
            }
            .main-content {
                margin-left: 0 !important; /* Don't push content on mobile */
                width: 100%;
            }
            
            body.sidebar-collapsed .sidebar-container {
                transform: translateX(-100%);
            }
            
            /* Hamburger button when sidebar is collapsed */
            .mobile-menu-btn {
                display: none;
            }
            body.sidebar-collapsed .mobile-menu-btn {
                display: flex;
                position: fixed;
                top: 1rem;
                left: 1rem;
                z-index: 90;
                background: #1a1a26;
                padding: 0.5rem;
                border-radius: 0.5rem;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.5);
                border: 1px solid #333344;
            }
            
            .sidebar-overlay {
                display: block;
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                background: rgba(0,0,0,0.5);
                backdrop-filter: blur(4px);
                z-index: 90;
                opacity: 1;
                transition: opacity 0.3s;
            }
            
            body.sidebar-collapsed .sidebar-overlay {
                opacity: 0;
                pointer-events: none;
            }
        }
        @media (min-width: 768px) {
            .mobile-menu-btn {
                display: none !important;
            }
            .sidebar-overlay {
                display: none !important;
            }
        }'''

content = re.sub(mobile_css_old, mobile_css_new, content, flags=re.DOTALL)

body_start = r'<body class="bg-[#0b0b0f] font-body-md text-white min-h-screen relative">'
body_new = r'''<body class="bg-[#0b0b0f] font-body-md text-white min-h-screen relative">
    <button onclick="toggleSidebar()" aria-label="Open Menu" class="mobile-menu-btn text-white">
        <span class="material-symbols-outlined">menu</span>
    </button>
    <div class="sidebar-overlay" onclick="toggleSidebar()"></div>'''
content = content.replace(body_start, body_new)

# if duplicate overlay exists, remove one
content = content.replace('<div class="sidebar-overlay" onclick="toggleSidebar()"></div>\n    <div class="sidebar-overlay" onclick="toggleSidebar()"></div>', '<div class="sidebar-overlay" onclick="toggleSidebar()"></div>')
content = content.replace('<div class="sidebar-overlay" onclick="toggleSidebar()"></div>\n    {% if messages %}', '{% if messages %}')

# Let's fix JS
js_old = r'''                link.addEventListener\('click', \(e\) => {
                    // For small screens, we might want to auto-collapse after selection
                    if \(window.innerWidth < 768\) {
                        document.body.classList.add\('sidebar-collapsed'\);
                        localStorage.setItem\('sidebarCollapsed', 'true'\);
                    } else {
                        localStorage.setItem\('sidebarCollapsed', 'true'\);
                    }
                }\);'''
js_new = r'''                link.addEventListener('click', (e) => {
                    if (window.innerWidth < 768) {
                        document.body.classList.add('sidebar-collapsed');
                        localStorage.setItem('sidebarCollapsed', 'true');
                    }
                });'''
content = re.sub(js_old, js_new, content, flags=re.DOTALL)

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(content)
