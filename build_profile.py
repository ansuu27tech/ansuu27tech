import base64
import os

def build_svg():
    width = 832
    height = 3700

    # Read the portrait image as base64
    with open('images/id.png', 'rb') as f:
        b64_img = base64.b64encode(f.read()).decode('utf-8')
    b64_uri = f"data:image/png;base64,{b64_img}"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" fill="none">
    <defs>
        <style>
            .bg {{ fill: #070B16; }}
            .text-white {{ fill: #F5F7FA; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"; }}
            .text-muted {{ fill: #8B95A7; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }}
            .text-mono {{ font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace; fill: #247BFF; }}
            .text-mono-red {{ font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace; fill: #FF354F; }}
            
            .role-text {{ opacity: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-weight: 600; fill: #247BFF; font-size: 16px; letter-spacing: 2px; text-transform: uppercase; }}
            .card {{ fill: #0B1020; stroke: rgba(255,255,255,0.06); stroke-width: 1; filter: url(#shadow3d); }}
            .card-hover:hover {{ stroke: rgba(36,123,255,0.4); filter: url(#shadow3d-hover); }}
            
            .timeline-line {{ stroke: rgba(255,255,255,0.08); stroke-width: 2; }}
            .dot {{ fill: #247BFF; }}
            .dot-red {{ fill: #FF354F; }}
            
            .orbit {{ fill: none; stroke: rgba(255,255,255,0.08); stroke-width: 1; }}
            
            @keyframes dashFlow {{ to {{ stroke-dashoffset: -1260; }} }}
            @keyframes dashFlowRed {{ to {{ stroke-dashoffset: -1040; }} }}
            .orbit-glow {{ fill: none; stroke: rgba(36, 123, 255, 0.3); stroke-width: 2; stroke-dasharray: 60 1200; animation: dashFlow 15s linear infinite; }}
            .orbit-glow-red {{ fill: none; stroke: rgba(255, 53, 79, 0.4); stroke-width: 2; stroke-dasharray: 40 1000; animation: dashFlowRed 12s linear infinite; }}
            
            .btn {{ fill: #FF354F; }}
            .btn-text {{ fill: #F5F7FA; font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace; font-size: 12px; font-weight: 700; letter-spacing: 1px; }}
            .hover-zone:hover .btn {{ fill: #D9253C; }}
            .social-icon {{ fill: #F5F7FA; }}
            
            .id-card {{ fill: #03050A; stroke: rgba(255,255,255,0.2); stroke-width: 1; filter: url(#shadow3d); }}
            .barcode {{ fill: rgba(255,255,255,0.9); }}
            
            /* Animations */
            @keyframes fadeSlide {{
                0%, 20%, 100% {{ opacity: 0; transform: translateY(10px); }}
                5%, 15% {{ opacity: 1; transform: translateY(0); }}
            }}
            .role-anim {{ animation: fadeSlide 16s infinite; }}
            .r1 {{ animation-delay: 0s; }}
            .r2 {{ animation-delay: 4s; }}
            .r3 {{ animation-delay: 8s; }}
            .r4 {{ animation-delay: 12s; }}
            
            @keyframes bob {{
                0%, 100% {{ transform: translateY(0px); }}
                50% {{ transform: translateY(-6px); }}
            }}
            .bob-1 {{ animation: bob 4s ease-in-out infinite; }}
            .bob-2 {{ animation: bob 5s ease-in-out infinite; }}
            .bob-3 {{ animation: bob 6s ease-in-out infinite; }}
            
            @keyframes pulseOuter {{
                0% {{ r: 12px; opacity: 0.8; stroke-width: 2; }}
                100% {{ r: 35px; opacity: 0; stroke-width: 0; }}
            }}
            .pulse-ring {{ fill: none; stroke: #247BFF; animation: pulseOuter 2.5s ease-out infinite; transform-origin: center; }}
            .pulse-ring-2 {{ fill: none; stroke: #247BFF; animation: pulseOuter 2.5s ease-out infinite; animation-delay: 1.25s; transform-origin: center; }}
            
            @keyframes floatOrb {{
                0%, 100% {{ transform: translate(0px, 0px); }}
                50% {{ transform: translate(30px, -50px); }}
            }}
            .orb-anim {{ animation: floatOrb 20s ease-in-out infinite; }}
            .orb-anim2 {{ animation: floatOrb 25s ease-in-out infinite reverse; }}
            
            .swing {{ transform-origin: 416px 0px; }}
            
            @media (prefers-reduced-motion: reduce) {{
                .anim-el, .role-anim, .swing, .sweep, .bob-1, .bob-2, .bob-3, .pulse-ring, .pulse-ring-2 {{ animation: none !important; opacity: 1 !important; transform: none !important; }}
                .r1 {{ display: block; opacity: 1; }}
                .r2, .r3, .r4 {{ display: none; }}
            }}
        </style>
        <clipPath id="avatar-clip">
            <rect width="180" height="240" rx="16" />
        </clipPath>
        <clipPath id="id-avatar-clip">
            <rect x="0" y="0" width="140" height="140" rx="16" />
        </clipPath>
        
        <filter id="shadow3d" x="-20%" y="-20%" width="140%" height="140%">
            <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#000000" flood-opacity="0.8" />
            <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4" />
        </filter>
        <filter id="shadow3d-hover" x="-20%" y="-20%" width="140%" height="140%">
            <feDropShadow dx="0" dy="16" stdDeviation="24" flood-color="#000000" flood-opacity="1.0" />
            <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#247BFF" flood-opacity="0.2" />
        </filter>
        
        <filter id="glowBlurHeavy" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="150" />
        </filter>
        
        <radialGradient id="bgFade" cx="50%" cy="50%" r="70%" fx="50%" fy="50%">
            <stop offset="0%" stop-color="#070B16" stop-opacity="0" />
            <stop offset="100%" stop-color="#070B16" stop-opacity="1" />
        </radialGradient>
        <linearGradient id="foil" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="rgba(255,255,255,0)" />
            <stop offset="45%" stop-color="rgba(255,255,255,0.02)" />
            <stop offset="50%" stop-color="rgba(255,255,255,0.15)" />
            <stop offset="55%" stop-color="rgba(255,255,255,0.02)" />
            <stop offset="100%" stop-color="rgba(255,255,255,0)" />
        </linearGradient>
        <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(255,255,255,0.015)" stroke-width="1"/>
            <animate attributeName="y" values="0; 40" dur="4s" repeatCount="indefinite" />
        </pattern>
        <linearGradient id="sheen" x1="-100%" y1="0%" x2="0%" y2="0%">
            <stop offset="0%" stop-color="rgba(36, 123, 255, 0)" />
            <stop offset="50%" stop-color="rgba(36, 123, 255, 0.5)" />
            <stop offset="100%" stop-color="rgba(36, 123, 255, 0)" />
            <animate attributeName="x1" values="-100%; 200%" dur="3s" repeatCount="indefinite" />
            <animate attributeName="x2" values="0%; 300%" dur="3s" repeatCount="indefinite" />
        </linearGradient>
        <linearGradient id="text-sheen" x1="-100%" y1="0%" x2="0%" y2="0%">
            <stop offset="0%" stop-color="#247BFF" />
            <stop offset="50%" stop-color="#FFFFFF" />
            <stop offset="100%" stop-color="#247BFF" />
            <animate attributeName="x1" values="-100%; 200%" dur="4s" repeatCount="indefinite" />
            <animate attributeName="x2" values="0%; 300%" dur="4s" repeatCount="indefinite" />
        </linearGradient>
    </defs>

    <!-- Base Background -->
    <rect width="{width}" height="{height}" class="bg" rx="24" />
    
    <!-- 3D Atmospheric Background Orbs -->
    <circle cx="100" cy="300" r="250" fill="rgba(36, 123, 255, 0.15)" filter="url(#glowBlurHeavy)" class="orb-anim" />
    <circle cx="700" cy="800" r="300" fill="rgba(94, 23, 235, 0.12)" filter="url(#glowBlurHeavy)" class="orb-anim2" />
    <circle cx="200" cy="2000" r="350" fill="rgba(36, 123, 255, 0.1)" filter="url(#glowBlurHeavy)" class="orb-anim" />
    <circle cx="600" cy="3000" r="400" fill="rgba(0, 240, 255, 0.08)" filter="url(#glowBlurHeavy)" class="orb-anim2" />

    <!-- Animated Grid -->
    <rect width="{width}" height="{height}" fill="url(#grid)" rx="24" />
    <!-- Fade grid edges -->
    <rect width="{width}" height="{height}" fill="url(#bgFade)" rx="24" />
    
    <rect x="1" y="1" width="830" height="{height-2}" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1" rx="24" />

    <!-- ========================================== -->
    <!-- HERO SECTION -->
    <!-- ========================================== -->
    <g transform="translate(60, 80)">
        <text x="0" y="0" class="text-mono" font-size="12" font-weight="700" letter-spacing="3px">HELLO, I'M</text>
        
        <text x="-4" y="60" class="text-white" font-size="64" font-weight="800" letter-spacing="-2px">N. MOHAMMED</text>
        <text x="-4" y="125" class="text-white" font-size="64" font-weight="800" letter-spacing="-2px">ANAS</text>

        <g transform="translate(0, 160)">
            <text x="0" y="0" class="role-text role-anim r1">AI &amp; DATA SCIENCE</text>
            <text x="0" y="0" class="role-text role-anim r2">CREATIVE DEVELOPER</text>
            <text x="0" y="0" class="role-text role-anim r3">UI/UX DESIGNER</text>
            <text x="0" y="0" class="role-text role-anim r4">FOUNDER &amp; CREATIVE DIRECTOR</text>
        </g>
        
        <text x="0" y="210" class="text-muted" font-size="16">Blending AI thinking with clean design to build ideas that stand out.</text>

        <!-- Stats/Metadata -->
        <g transform="translate(0, 250)">
            <rect x="0" y="0" width="180" height="26" class="card" rx="4" />
            <text x="10" y="17" class="text-mono-red" font-size="9">B.TECH AI &amp; DATA SCIENCE</text>

            <rect x="190" y="0" width="130" height="26" class="card" rx="4" />
            <text x="200" y="17" class="text-mono-red" font-size="9">2+ YEARS ACTIVE</text>

            <rect x="330" y="0" width="160" height="26" class="card" rx="4" />
            <text x="340" y="17" class="text-mono-red" font-size="9">15+ PROJECTS DELIVERED</text>
        </g>

        <!-- Portrait -->
        <g transform="translate(540, -20)">
            <g class="bob-2">
                <rect width="180" height="240" fill="#0B1020" rx="16" />
                <image href="{b64_uri}" width="180" height="240" clip-path="url(#avatar-clip)" preserveAspectRatio="xMidYMid slice" />
                <!-- Border overlay -->
                <rect width="180" height="240" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="2" rx="16" />
                <rect width="180" height="240" fill="none" stroke="url(#sheen)" stroke-width="2" rx="16" />
            </g>
        </g>
    </g>

    <!-- ========================================== -->
    <!-- ABOUT SECTION -->
    <!-- ========================================== -->
    <g transform="translate(60, 460)">
        <text x="0" y="0" class="text-mono" font-size="10" font-weight="700" letter-spacing="2px">ABOUT / LIFE</text>
        
        <g transform="translate(0, 30)">
            <!-- Column 1 -->
            <g transform="translate(0, 0)">
                <text x="0" y="20" class="text-white" font-size="16" font-weight="700">01 — AI &amp; TECHNOLOGY</text>
                <text x="0" y="45" class="text-muted" font-size="14">Deep technical foundation in</text>
                <text x="0" y="65" class="text-muted" font-size="14">machine learning, NLP, and</text>
                <text x="0" y="85" class="text-muted" font-size="14">data-driven automation.</text>
            </g>
            
            <!-- Column 2 -->
            <g transform="translate(240, 0)">
                <text x="0" y="20" class="text-white" font-size="16" font-weight="700">02 — DESIGN &amp; CREATIVITY</text>
                <text x="0" y="45" class="text-muted" font-size="14">Elevating user experiences</text>
                <text x="0" y="65" class="text-muted" font-size="14">with modern editorial aesthetics,</text>
                <text x="0" y="85" class="text-muted" font-size="14">motion, and spatial design.</text>
            </g>
            
            <!-- Column 3 -->
            <g transform="translate(480, 0)">
                <text x="0" y="20" class="text-white" font-size="16" font-weight="700">03 — BUILDING &amp; STRATEGY</text>
                <text x="0" y="45" class="text-muted" font-size="14">Founder mindset focused on</text>
                <text x="0" y="65" class="text-muted" font-size="14">scalable digital products and</text>
                <text x="0" y="85" class="text-muted" font-size="14">impactful branding strategies.</text>
            </g>
        </g>
    </g>

    <!-- ========================================== -->
    <!-- CAPABILITIES SECTION -->
    <!-- ========================================== -->
    <g transform="translate(60, 680)">
        <text x="0" y="0" class="text-mono" font-size="10" font-weight="700" letter-spacing="2px">CAPABILITIES</text>

        <!-- Cards -->
        <g transform="translate(0, 25)">
            <g transform="translate(0, 0)"><g class="bob-1">
                <rect x="0" y="0" width="165" height="150" class="card card-hover" rx="8" />
                <rect x="0" y="0" width="165" height="150" fill="none" stroke="url(#sheen)" stroke-width="1.5" rx="8" />
                <text x="20" y="30" class="text-white" font-size="14" font-weight="700">AI &amp; DATA</text>
                <text x="20" y="55" class="text-muted" font-size="13">Python</text>
                <text x="20" y="75" class="text-muted" font-size="13">Machine Learning</text>
                <text x="20" y="95" class="text-muted" font-size="13">Data Analysis</text>
                <text x="20" y="115" class="text-muted" font-size="13">AI Automation</text>
                <text x="20" y="135" class="text-muted" font-size="13">NLP</text>
            </g></g>

            <g transform="translate(182, 0)"><g class="bob-2">
                <rect x="0" y="0" width="165" height="150" class="card card-hover" rx="8" />
                <rect x="0" y="0" width="165" height="150" fill="none" stroke="url(#sheen)" stroke-width="1.5" rx="8" />
                <text x="20" y="30" class="text-white" font-size="14" font-weight="700">ENGINEERING</text>
                <text x="20" y="55" class="text-muted" font-size="13">React &amp; Next.js</text>
                <text x="20" y="75" class="text-muted" font-size="13">TypeScript</text>
                <text x="20" y="95" class="text-muted" font-size="13">HTML / CSS</text>
                <text x="20" y="115" class="text-muted" font-size="13">Framer Motion</text>
                <text x="20" y="135" class="text-muted" font-size="13">Three.js</text>
            </g></g>

            <g transform="translate(364, 0)"><g class="bob-3">
                <rect x="0" y="0" width="165" height="150" class="card card-hover" rx="8" />
                <rect x="0" y="0" width="165" height="150" fill="none" stroke="url(#sheen)" stroke-width="1.5" rx="8" />
                <text x="20" y="30" class="text-white" font-size="14" font-weight="700">CREATIVE</text>
                <text x="20" y="55" class="text-muted" font-size="13">UI/UX Design</text>
                <text x="20" y="75" class="text-muted" font-size="13">Branding</text>
                <text x="20" y="95" class="text-muted" font-size="13">Graphic Design</text>
                <text x="20" y="115" class="text-muted" font-size="13">Motion Design</text>
                <text x="20" y="135" class="text-muted" font-size="13">Figma</text>
            </g></g>

            <g transform="translate(546, 0)"><g class="bob-1">
                <rect x="0" y="0" width="165" height="150" class="card card-hover" rx="8" />
                <rect x="0" y="0" width="165" height="150" fill="none" stroke="url(#sheen)" stroke-width="1.5" rx="8" />
                <text x="20" y="30" class="text-white" font-size="14" font-weight="700">STRATEGY</text>
                <text x="20" y="55" class="text-muted" font-size="13">Digital Marketing</text>
                <text x="20" y="75" class="text-muted" font-size="13">Social Media</text>
                <text x="20" y="95" class="text-muted" font-size="13">Content Strategy</text>
                <text x="20" y="115" class="text-muted" font-size="13">Analytics</text>
                <text x="20" y="135" class="text-muted" font-size="13">Growth</text>
            </g></g>
        </g>
    </g>

    <!-- ========================================== -->
    <!-- TECH STACK SECTION -->
    <!-- ========================================== -->
    <g transform="translate(60, 920)">
        <text x="0" y="0" class="text-mono" font-size="10" font-weight="700" letter-spacing="2px">TECH STACK</text>

        <g transform="translate(356, 170)">
            <circle cx="0" cy="0" r="24" fill="#090D18" stroke="rgba(255,255,255,0.1)" stroke-width="1" />
            <circle cx="0" cy="0" r="12" class="pulse-ring" />
            <circle cx="0" cy="0" r="12" class="pulse-ring-2" />
            <circle cx="0" cy="0" r="12" fill="#247BFF" opacity="0.8">
                <animate class="anim-el" attributeName="r" values="10;14;10" dur="4s" repeatCount="indefinite" />
            </circle>
            <text x="0" y="4" class="text-white" font-size="10" text-anchor="middle">CORE</text>

            <!-- Orbit 1 -->
            <g transform="rotate(20)">
                <ellipse cx="0" cy="0" rx="300" ry="100" class="orbit" />
                <ellipse cx="0" cy="0" rx="300" ry="100" class="orbit-glow-red">
                    <animate class="anim-el" attributeName="stroke-dashoffset" from="1200" to="0" dur="15s" repeatCount="indefinite" />
                </ellipse>
                <g transform="translate(-260, -50)"><circle r="5" class="dot-red" /><text x="-15" y="-10" class="text-muted" font-size="11" font-family="monospace">Python</text></g>
                <g transform="translate(260, 50)"><circle r="5" class="dot" /><text x="15" y="5" class="text-muted" font-size="11" font-family="monospace">TensorFlow</text></g>
            </g>

            <!-- Orbit 2 -->
            <g transform="rotate(-15)">
                <ellipse cx="0" cy="0" rx="220" ry="70" class="orbit" />
                <ellipse cx="0" cy="0" rx="220" ry="70" class="orbit-glow">
                    <animate class="anim-el" attributeName="stroke-dashoffset" from="1000" to="0" dur="12s" repeatCount="indefinite" />
                </ellipse>
                <g transform="translate(-180, -40)"><circle r="5" class="dot" /><text x="-20" y="-10" class="text-muted" font-size="11" font-family="monospace">React / Next.js</text></g>
                <g transform="translate(180, 40)"><circle r="5" class="dot-red" /><text x="15" y="5" class="text-muted" font-size="11" font-family="monospace">TypeScript</text></g>
            </g>

            <!-- Orbit 3 -->
            <g transform="rotate(35)">
                <ellipse cx="0" cy="0" rx="140" ry="45" class="orbit" />
                <ellipse cx="0" cy="0" rx="140" ry="45" class="orbit-glow">
                    <animate class="anim-el" attributeName="stroke-dashoffset" from="800" to="0" dur="10s" repeatCount="indefinite" />
                </ellipse>
                <g transform="translate(-110, -28)"><circle r="5" class="dot-red" /><text x="-20" y="-10" class="text-muted" font-size="11" font-family="monospace" transform="rotate(-35)">UI/UX</text></g>
                <g transform="translate(110, 28)"><circle r="5" class="dot" /><text x="15" y="5" class="text-muted" font-size="11" font-family="monospace" transform="rotate(-35)">Figma</text></g>
            </g>
        </g>
    </g>

    <!-- ========================================== -->
    <!-- EXPERIENCE SECTION -->
    <!-- ========================================== -->
    <g transform="translate(60, 1260)">
        <text x="0" y="0" class="text-mono" font-size="10" font-weight="700" letter-spacing="2px">EXPERIENCE</text>

        <g transform="translate(0, 30)">
            <path d="M 140 10 L 140 260" class="timeline-line" />
            <!-- Animated Flow Line -->
            <rect x="139" y="10" width="2" height="60" fill="url(#sheen)" rx="1">
                <animate attributeName="y" values="10; 220; 10" dur="6s" repeatCount="indefinite" />
            </rect>

            <!-- 1 -->
            <g transform="translate(0, 0)">
                <text x="0" y="24" class="text-mono-red" font-size="11">2026 — PRESENT</text>
                <circle cx="140" cy="20" r="5" class="dot-red" />
                <rect x="170" y="0" width="540" height="60" class="card" rx="8" />
                <text x="190" y="24" class="text-white" font-size="16" font-weight="700">DIGITAL MARKETING STRATEGIST</text>
                <text x="190" y="44" class="text-muted" font-size="13">DRAUGHTSMAN STUDIO</text>
            </g>

            <!-- 2 -->
            <g transform="translate(0, 80)">
                <text x="0" y="24" class="text-mono" font-size="11">2024 — PRESENT</text>
                <circle cx="140" cy="20" r="5" class="dot" />
                <rect x="170" y="0" width="540" height="60" class="card" rx="8" />
                <text x="190" y="24" class="text-white" font-size="16" font-weight="700">FOUNDER &amp; CREATIVE DIRECTOR</text>
                <text x="190" y="44" class="text-muted" font-size="13">PIXELMINT STUDIO MVS</text>
            </g>

            <!-- 3 -->
            <g transform="translate(0, 160)">
                <text x="100" y="24" class="text-mono" fill="#8B95A7" font-size="11">2024</text>
                <circle cx="140" cy="20" r="4" class="dot" fill="#8B95A7" />
                <rect x="170" y="0" width="540" height="60" class="card" rx="8" />
                <text x="190" y="24" class="text-white" font-size="16" font-weight="700">E-BOOK AUTHOR</text>
                <text x="190" y="44" class="text-muted" font-size="13">DIGITAL PUBLICATION</text>
            </g>

            <!-- 4 -->
            <g transform="translate(0, 240)">
                <text x="44" y="24" class="text-mono" fill="#8B95A7" font-size="11">2023 — 2024</text>
                <circle cx="140" cy="20" r="4" class="dot" fill="#8B95A7" />
                <rect x="170" y="0" width="540" height="60" class="card" rx="8" />
                <text x="190" y="24" class="text-white" font-size="16" font-weight="700">FREELANCE DEVELOPER</text>
                <text x="190" y="44" class="text-muted" font-size="13">SELF-EMPLOYED</text>
            </g>
        </g>
    </g>

    <!-- ========================================== -->
    <!-- PROJECTS SECTION -->
    <!-- ========================================== -->
    <g transform="translate(60, 1660)">
        <text x="0" y="0" class="text-mono" font-size="10" font-weight="700" letter-spacing="2px">SELECTED WORK</text>

        <g transform="translate(0, 25)">
            <!-- Row 1 -->
            <g transform="translate(0, 0)"><g class="bob-2">
                <rect width="225" height="150" class="card" rx="8" />
                <text x="20" y="30" class="text-white" font-size="15" font-weight="700">MINDMAP AI</text>
                <text x="20" y="55" class="text-muted" font-size="13">Intelligent Knowledge</text>
                <text x="20" y="75" class="text-muted" font-size="13">Graph Builder</text>
                <rect x="20" y="95" width="20" height="2" fill="#247BFF" />
                <text x="20" y="125" class="text-mono-red" font-size="9">MACHINE LEARNING · NLP</text>
            </g></g>

            <g transform="translate(243, 0)"><g class="bob-1">
                <rect width="225" height="150" class="card" rx="8" />
                <text x="20" y="30" class="text-white" font-size="15" font-weight="700">PULSE ANALYTICS</text>
                <text x="20" y="55" class="text-muted" font-size="13">Real-Time Social</text>
                <text x="20" y="75" class="text-muted" font-size="13">Sentiment Dashboard</text>
                <rect x="20" y="95" width="20" height="2" fill="#247BFF" />
                <text x="20" y="125" class="text-mono" font-size="9">REAL-TIME CHARTS · API</text>
            </g></g>

            <g transform="translate(486, 0)"><g class="bob-3">
                <rect width="225" height="150" class="card" rx="8" />
                <text x="20" y="30" class="text-white" font-size="15" font-weight="700">AURA HEALTH</text>
                <text x="20" y="55" class="text-muted" font-size="13">Personalized AI</text>
                <text x="20" y="75" class="text-muted" font-size="13">Wellness Companion</text>
                <rect x="20" y="95" width="20" height="2" fill="#FF354F" />
                <text x="20" y="125" class="text-mono" font-size="9">LLM · MOBILE UX</text>
            </g></g>

            <!-- Row 2 -->
            <g transform="translate(0, 168)"><g class="bob-3">
                <rect width="225" height="150" class="card" rx="8" />
                <text x="20" y="30" class="text-white" font-size="15" font-weight="700">GRIDFORGE</text>
                <text x="20" y="55" class="text-muted" font-size="13">No-Code Data</text>
                <text x="20" y="75" class="text-muted" font-size="13">Pipeline Builder</text>
                <rect x="20" y="95" width="20" height="2" fill="#FF354F" />
                <text x="20" y="125" class="text-mono" font-size="9">DRAG &amp; DROP · ETL</text>
            </g></g>

            <g transform="translate(243, 168)"><g class="bob-2">
                <rect width="225" height="150" class="card" rx="8" />
                <text x="20" y="30" class="text-white" font-size="15" font-weight="700">SYNTHWAVE FM</text>
                <text x="20" y="55" class="text-muted" font-size="13">Generative AI</text>
                <text x="20" y="75" class="text-muted" font-size="13">Music Experience</text>
                <rect x="20" y="95" width="20" height="2" fill="#247BFF" />
                <text x="20" y="125" class="text-mono" font-size="9">GENERATIVE AI · AUDIO</text>
            </g></g>

            <g transform="translate(486, 168)"><g class="bob-1">
                <rect width="225" height="150" class="card" rx="8" />
                <text x="20" y="30" class="text-white" font-size="15" font-weight="700">DRAUGHTSMAN</text>
                <text x="20" y="55" class="text-muted" font-size="13">Architectural Firm</text>
                <text x="20" y="75" class="text-muted" font-size="13">Official Website</text>
                <rect x="20" y="95" width="20" height="2" fill="#247BFF" />
                <text x="20" y="125" class="text-mono" font-size="9">NEXT.JS · WEB DESIGN</text>
            </g></g>
            
            <!-- Row 3 -->
            <g transform="translate(0, 336)"><g class="bob-1">
                <rect width="225" height="150" class="card" rx="8" />
                <text x="20" y="30" class="text-white" font-size="15" font-weight="700">SS BUILDERS</text>
                <text x="20" y="55" class="text-muted" font-size="13">Construction &amp;</text>
                <text x="20" y="75" class="text-muted" font-size="13">Builders Website</text>
                <rect x="20" y="95" width="20" height="2" fill="#247BFF" />
                <text x="20" y="125" class="text-mono" font-size="9">JAVA · HTML · CSS</text>
            </g></g>

            <g transform="translate(243, 336)"><g class="bob-3">
                <rect width="225" height="150" class="card" rx="8" />
                <text x="20" y="30" class="text-white" font-size="15" font-weight="700">ARCHIDRAFT</text>
                <text x="20" y="55" class="text-muted" font-size="13">Project Workflow</text>
                <text x="20" y="75" class="text-muted" font-size="13">Platform</text>
                <rect x="20" y="95" width="20" height="2" fill="#247BFF" />
                <text x="20" y="125" class="text-mono" font-size="9">FLUTTER · FIREBASE</text>
            </g></g>
        </g>
    </g>

    <!-- ========================================== -->
    <!-- PIXELMINT STUDIO SECTION -->
    <!-- ========================================== -->
    <g transform="translate(60, 2240)">
        <text x="0" y="0" class="text-mono" font-size="10" font-weight="700" letter-spacing="2px">FOUNDER / STUDIO</text>

        <g transform="translate(0, 25)">
            <rect width="712" height="190" class="card" fill="#090D18" rx="12" />
            <rect width="712" height="190" fill="none" stroke="url(#sheen)" stroke-width="2" rx="12" />
            
            <text x="40" y="50" class="text-white" font-size="32" font-weight="800" letter-spacing="-1px">PIXEL<tspan fill="url(#text-sheen)">MINT</tspan></text>
            <text x="40" y="70" class="text-mono-red" font-size="10">STUDIO MVS</text>

            <text x="40" y="110" class="text-white" font-size="16" font-weight="700">CRAFTING THE FUTURE OF DIGITAL.</text>
            
            <text x="40" y="140" class="text-muted" font-size="14">A specialized design and engineering collective combining</text>
            <text x="40" y="160" class="text-muted" font-size="14">experimental aesthetics with rigorous logic.</text>
            
            <!-- Service Tags -->
            <g transform="translate(420, 30)">
                <rect x="0" y="0" width="130" height="24" fill="#0B1020" stroke="rgba(255,255,255,0.06)" rx="4" />
                <text x="10" y="16" fill="#8B95A7" font-family="monospace" font-size="10">Website Design</text>
                
                <rect x="140" y="0" width="130" height="24" fill="#0B1020" stroke="rgba(255,255,255,0.06)" rx="4" />
                <text x="150" y="16" fill="#8B95A7" font-family="monospace" font-size="10">Web Development</text>
                
                <rect x="0" y="32" width="130" height="24" fill="#0B1020" stroke="rgba(255,255,255,0.06)" rx="4" />
                <text x="10" y="48" fill="#8B95A7" font-family="monospace" font-size="10">E-Commerce</text>
                
                <rect x="140" y="32" width="130" height="24" fill="#0B1020" stroke="rgba(255,255,255,0.06)" rx="4" />
                <text x="150" y="48" fill="#8B95A7" font-family="monospace" font-size="10">UI/UX Design</text>
                
                <rect x="0" y="64" width="130" height="24" fill="#0B1020" stroke="rgba(255,255,255,0.06)" rx="4" />
                <text x="10" y="80" fill="#8B95A7" font-family="monospace" font-size="10">Branding</text>
                
                <rect x="140" y="64" width="130" height="24" fill="#0B1020" stroke="rgba(255,255,255,0.06)" rx="4" />
                <text x="150" y="80" fill="#8B95A7" font-family="monospace" font-size="10">Landing Pages</text>

                <rect x="0" y="96" width="130" height="24" fill="#0B1020" stroke="rgba(255,255,255,0.06)" rx="4" />
                <text x="10" y="112" fill="#8B95A7" font-family="monospace" font-size="10">Digital Marketing</text>
                
                <rect x="140" y="96" width="130" height="24" fill="#0B1020" stroke="rgba(255,255,255,0.06)" rx="4" />
                <text x="150" y="112" fill="#8B95A7" font-family="monospace" font-size="10">Social Media</text>
            </g>
        </g>
    </g>

    <!-- ========================================== -->
    <!-- DIGITAL ID SECTION -->
    <!-- ========================================== -->
    <g transform="translate(60, 2560)">
        <text x="0" y="0" class="text-mono" font-size="10" font-weight="700" letter-spacing="2px">DIGITAL ID</text>
        
        <g transform="translate(0, 30)">
            <path d="M 356 -50 L 356 70" stroke="#0B1020" stroke-width="8" />
            <rect x="336" y="55" width="40" height="15" rx="4" fill="#247BFF" />
            <rect x="346" y="70" width="20" height="15" rx="2" fill="#8B95A7" />

            <g class="swing" transform-origin="356px 0px">
                <animateTransform attributeName="transform" type="rotate" values="0; 1; -1; 0.5; -0.5; 0" keyTimes="0; 0.2; 0.4; 0.6; 0.8; 1" dur="3s" repeatCount="1" />
                <animateTransform attributeName="transform" type="rotate" values="0; 1.5; -1.5; 0" dur="8s" repeatCount="indefinite" additive="sum" />
                
                <g transform="translate(196, 85)">
                    <rect width="320" height="380" class="id-card" rx="16" />
                    <rect width="320" height="380" fill="url(#foil)" rx="16" class="sweep">
                        <animate attributeName="x" values="-320; 320" dur="4s" repeatCount="indefinite" />
                    </rect>

                    <!-- Hole punch -->
                    <rect x="125" y="15" width="70" height="12" rx="6" fill="#070B16" />

                    <!-- Avatar placeholder -->
                    <g transform="translate(90, 45)">
                        <rect width="140" height="140" rx="16" fill="#0B1020" stroke="#247BFF" stroke-width="1" />
                        <image href="{b64_uri}" width="140" height="140" clip-path="url(#id-avatar-clip)" preserveAspectRatio="xMidYMid slice" />
                    </g>

                    <text x="160" y="215" class="text-white" font-size="20" font-weight="800" text-anchor="middle">N. MOHAMMED ANAS</text>
                    <text x="160" y="235" class="text-mono" font-size="12" text-anchor="middle">@ansuu27tech</text>

                    <rect x="30" y="255" width="260" height="1" fill="rgba(255,255,255,0.1)" />

                    <text x="160" y="285" class="text-muted" font-size="11" font-weight="500" letter-spacing="1px" text-anchor="middle">AI &amp; DATA SCIENCE</text>
                    <text x="160" y="305" class="text-muted" font-size="11" font-weight="500" letter-spacing="1px" text-anchor="middle">CREATIVE DEVELOPER</text>
                    <text x="160" y="325" fill="#F5F7FA" font-family="monospace" font-size="10" text-anchor="middle">FOUNDER — PIXELMINT STUDIO MVS</text>

                    <!-- Barcode mockup -->
                    <g transform="translate(60, 345)">
                        <rect x="0" y="0" width="2" height="20" class="barcode" />
                        <rect x="4" y="0" width="1" height="20" class="barcode" />
                        <rect x="8" y="0" width="3" height="20" class="barcode" />
                        <rect x="14" y="0" width="1" height="20" class="barcode" />
                        <rect x="18" y="0" width="4" height="20" class="barcode" />
                        <rect x="26" y="0" width="1" height="20" class="barcode" />
                        <rect x="30" y="0" width="2" height="20" class="barcode" />
                        <rect x="36" y="0" width="3" height="20" class="barcode" />
                        <rect x="42" y="0" width="1" height="20" class="barcode" />
                        <rect x="46" y="0" width="4" height="20" class="barcode" />
                        <rect x="54" y="0" width="2" height="20" class="barcode" />
                        <rect x="60" y="0" width="3" height="20" class="barcode" />
                        <rect x="66" y="0" width="1" height="20" class="barcode" />
                        <rect x="70" y="0" width="2" height="20" class="barcode" />
                        <rect x="76" y="0" width="4" height="20" class="barcode" />
                        <rect x="84" y="0" width="1" height="20" class="barcode" />
                        <rect x="88" y="0" width="2" height="20" class="barcode" />
                        <rect x="94" y="0" width="3" height="20" class="barcode" />
                        <rect x="100" y="0" width="1" height="20" class="barcode" />
                        <rect x="104" y="0" width="4" height="20" class="barcode" />
                        <rect x="112" y="0" width="2" height="20" class="barcode" />
                        <rect x="118" y="0" width="1" height="20" class="barcode" />
                        <rect x="122" y="0" width="3" height="20" class="barcode" />
                        <rect x="128" y="0" width="1" height="20" class="barcode" />
                        <rect x="132" y="0" width="4" height="20" class="barcode" />
                        <rect x="140" y="0" width="2" height="20" class="barcode" />
                        <rect x="146" y="0" width="1" height="20" class="barcode" />
                        <rect x="150" y="0" width="3" height="20" class="barcode" />
                        <rect x="156" y="0" width="1" height="20" class="barcode" />
                        <rect x="160" y="0" width="4" height="20" class="barcode" />
                        <rect x="168" y="0" width="2" height="20" class="barcode" />
                        <rect x="174" y="0" width="3" height="20" class="barcode" />
                        <rect x="180" y="0" width="1" height="20" class="barcode" />
                        <rect x="184" y="0" width="2" height="20" class="barcode" />
                        <rect x="190" y="0" width="4" height="20" class="barcode" />
                        <rect x="198" y="0" width="2" height="20" class="barcode" />
                    </g>
                </g>
            </g>
        </g>
    </g>

    <!-- ========================================== -->
    <!-- CONNECT SECTION -->
    <!-- ========================================== -->
    <g transform="translate(60, 3140)">
        <text x="0" y="0" class="text-mono" font-size="10" font-weight="700" letter-spacing="2px">CONNECT</text>

        <g transform="translate(0, 30)">
            <text x="0" y="20" class="text-white" font-size="24" font-weight="800" letter-spacing="-0.5px">LET'S BUILD SOMETHING EXTRAORDINARY.</text>
            <text x="0" y="50" class="text-muted" font-size="14">Always open to discussing AI, Data Science, and Creative Tech.</text>
            
            <g class="hover-zone">
                <rect x="0" y="80" width="160" height="36" class="btn" rx="4" />
                <rect x="0" y="80" width="160" height="36" fill="none" stroke="url(#sheen)" stroke-width="2" rx="4" />
                <text x="80" y="102" class="btn-text" text-anchor="middle">GET IN TOUCH</text>
            </g>

            <g transform="translate(0, 150)">
                <rect x="0" y="0" width="712" height="1" fill="rgba(255,255,255,0.06)" />
                <text x="0" y="30" class="text-muted" font-size="12">GitHub: ansuu27tech   ·   LinkedIn: mohammed-anas-30110b35   ·   Email: mohdanas53n@gmail.com</text>
                <text x="0" y="50" class="text-muted" font-size="12">Studio: PixelMint Studio MVS   ·   Instagram: @ansuu__._   ·   X: @anas_moham80856</text>
            </g>
        </g>
    </g>

</svg>
"""

    with open('assets/profile.svg', 'w', encoding='utf-8') as out_f:
        out_f.write(svg)
    print("Generated assets/profile.svg!")

if __name__ == '__main__':
    build_svg()
