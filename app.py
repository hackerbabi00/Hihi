# -*- coding: utf-8 -*-
"""
TeleAtlas Portfolio - Single File Flask App
Domain: https://teleatlas.xyz
Render / local ready
"""
import os
from flask import Flask, Response

app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Full-Stack Web Developer | Modern Dijital Çözümler</title>
    <meta name="description" content="4 yıllık deneyimli Full-Stack Web Developer. Modern web siteleri, özel yazılım çözümleri, e-ticaret sistemleri ve SEO optimizasyonu ile işletmelerin dijital başarısına katkı sağlıyorum.">
    <meta name="keywords" content="web developer, full stack developer, web tasarım, özel yazılım, e-ticaret, SEO, frontend, backend">
    <meta name="author" content="Full-Stack Web Developer">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://teleatlas.xyz/">

    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="Full-Stack Web Developer | Modern Dijital Çözümler">
    <meta property="og:description" content="Modern web teknolojileriyle işletmeler ve markalar için güçlü, hızlı ve kullanıcı odaklı dijital çözümler geliştiriyorum.">
    <meta property="og:image" content="https://i.ibb.co/rf4ws4kp/1793729385334.jpg">
    <meta property="og:url" content="https://teleatlas.xyz/">
    <meta property="og:locale" content="tr_TR">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Full-Stack Web Developer | Modern Dijital Çözümler">
    <meta name="twitter:description" content="Modern web teknolojileriyle işletmeler ve markalar için güçlü, hızlı ve kullanıcı odaklı dijital çözümler geliştiriyorum.">
    <meta name="twitter:image" content="https://i.ibb.co/rf4ws4kp/1793729385334.jpg">

    <!-- Schema.org -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Full-Stack Web Developer",
        "jobTitle": "Full-Stack Web Developer & UI/UX Designer",
        "description": "4 yıllık yazılım geliştirme deneyimiyle modern, hızlı ve kullanıcı odaklı web projeleri geliştiriyorum.",
        "url": "https://teleatlas.xyz/",
        "sameAs": [],
        "knowsAbout": ["Web Development", "Frontend Development", "Backend Development", "SEO", "UI/UX Design", "E-commerce"]
    }
    </script>
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": "Full-Stack Web Development Services",
        "description": "Web tasarım, özel yazılım geliştirme, e-ticaret sistemleri ve SEO optimizasyonu hizmetleri.",
        "url": "https://teleatlas.xyz/",
        "areaServed": "Worldwide",
        "serviceType": ["Web Design", "Custom Software Development", "E-commerce Systems", "SEO Optimization"]
    }
    </script>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
/* ============================================
   ROOT & RESET
   ============================================ */
:root {
    --bg-primary: #05050a;
    --bg-secondary: #0a0a14;
    --bg-card: rgba(15, 15, 30, 0.6);
    --bg-card-hover: rgba(20, 20, 40, 0.8);
    
    --neon-purple: #a855f7;
    --neon-blue: #3b82f6;
    --neon-cyan: #22d3ee;
    --electric-blue: #6366f1;
    
    --text-primary: #f1f5f9;
    --text-secondary: #94a3b8;
    --text-muted: #64748b;
    
    --gradient-primary: linear-gradient(135deg, #a855f7 0%, #3b82f6 50%, #22d3ee 100%);
    --gradient-text: linear-gradient(90deg, #c084fc, #60a5fa, #22d3ee);
    --gradient-btn: linear-gradient(135deg, #7c3aed 0%, #2563eb 100%);
    
    --glass-border: rgba(168, 85, 247, 0.2);
    --glass-border-hover: rgba(168, 85, 247, 0.45);
    --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    
    --font-primary: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    --font-display: 'Space Grotesk', 'Inter', sans-serif;
    
    --header-height: 80px;
    --transition-fast: 0.2s ease;
    --transition-normal: 0.35s cubic-bezier(0.4, 0, 0.2, 1);
    --transition-slow: 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    
    --radius-sm: 8px;
    --radius-md: 16px;
    --radius-lg: 24px;
    --radius-xl: 32px;
}

*,
*::before,
*::after {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
    scroll-padding-top: var(--header-height);
}

body {
    font-family: var(--font-primary);
    background-color: var(--bg-primary);
    color: var(--text-primary);
    line-height: 1.6;
    overflow-x: hidden;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

img {
    max-width: 100%;
    height: auto;
    display: block;
}

a {
    text-decoration: none;
    color: inherit;
    transition: color var(--transition-fast);
}

ul {
    list-style: none;
}

button {
    border: none;
    background: none;
    cursor: pointer;
    font-family: inherit;
}

/* ============================================
   UTILITIES
   ============================================ */
.container {
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 24px;
}

.section {
    padding: 120px 0;
    position: relative;
}

.section-header {
    text-align: center;
    margin-bottom: 64px;
}

.section-badge {
    display: inline-block;
    padding: 6px 16px;
    background: rgba(168, 85, 247, 0.12);
    border: 1px solid rgba(168, 85, 247, 0.3);
    border-radius: 50px;
    font-size: 0.8125rem;
    font-weight: 500;
    color: var(--neon-purple);
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin-bottom: 16px;
}

.section-title {
    font-family: var(--font-display);
    font-size: clamp(2rem, 4vw, 2.75rem);
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 16px;
    color: var(--text-primary);
}

.section-subtitle {
    font-size: 1.125rem;
    color: var(--text-secondary);
    max-width: 640px;
    margin: 0 auto;
    line-height: 1.7;
}

.gradient-text {
    background: var(--gradient-text);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.glass-card {
    background: var(--bg-card);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-lg);
    box-shadow: var(--glass-shadow);
    transition: all var(--transition-normal);
}

.glass-card:hover {
    background: var(--bg-card-hover);
    border-color: var(--glass-border-hover);
    box-shadow: 0 12px 40px rgba(168, 85, 247, 0.15);
    transform: translateY(-4px);
}

/* ============================================
   PAGE LOADER
   ============================================ */
.page-loader {
    position: fixed;
    inset: 0;
    background: var(--bg-primary);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 9999;
    transition: opacity 0.5s ease, visibility 0.5s ease;
}

.page-loader.hidden {
    opacity: 0;
    visibility: hidden;
}

.loader-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
}

.loader-ring {
    width: 48px;
    height: 48px;
    border: 3px solid rgba(168, 85, 247, 0.2);
    border-top-color: var(--neon-purple);
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
}

.loader-text {
    font-size: 0.875rem;
    color: var(--text-secondary);
    letter-spacing: 0.1em;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

/* ============================================
   HEADER / NAVIGATION
   ============================================ */
.header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: var(--header-height);
    z-index: 1000;
    transition: all var(--transition-normal);
}

.header.scrolled {
    background: rgba(5, 5, 10, 0.85);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(168, 85, 247, 0.1);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
}

.nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 100%;
}

.nav-logo {
    display: flex;
    align-items: center;
    font-family: var(--font-display);
    font-size: 1.5rem;
    font-weight: 700;
    z-index: 1001;
}

.logo-bracket {
    color: var(--neon-purple);
}

.logo-text {
    color: var(--text-primary);
    margin: 0 2px;
}

.nav-list {
    display: flex;
    align-items: center;
    gap: 8px;
}

.nav-link {
    position: relative;
    padding: 8px 16px;
    font-size: 0.9375rem;
    font-weight: 500;
    color: var(--text-secondary);
    border-radius: var(--radius-sm);
    transition: all var(--transition-fast);
}

.nav-link:hover,
.nav-link.active {
    color: var(--text-primary);
}

.nav-link.active::after {
    content: '';
    position: absolute;
    bottom: 2px;
    left: 50%;
    transform: translateX(-50%);
    width: 20px;
    height: 2px;
    background: var(--gradient-primary);
    border-radius: 2px;
}

.nav-toggle {
    display: none;
    flex-direction: column;
    gap: 6px;
    width: 32px;
    height: 32px;
    justify-content: center;
    z-index: 1001;
}

.hamburger {
    display: block;
    width: 100%;
    height: 2px;
    background: var(--text-primary);
    border-radius: 2px;
    transition: all var(--transition-normal);
}

.nav-toggle.active .hamburger:nth-child(1) {
    transform: translateY(8px) rotate(45deg);
}

.nav-toggle.active .hamburger:nth-child(2) {
    opacity: 0;
}

.nav-toggle.active .hamburger:nth-child(3) {
    transform: translateY(-8px) rotate(-45deg);
}

/* ============================================
   BUTTONS
   ============================================ */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    padding: 14px 28px;
    font-size: 0.9375rem;
    font-weight: 600;
    border-radius: 50px;
    transition: all var(--transition-normal);
    position: relative;
    overflow: hidden;
}

.btn-primary {
    background: var(--gradient-btn);
    color: #fff;
    box-shadow: 0 4px 20px rgba(124, 58, 237, 0.4);
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(124, 58, 237, 0.5);
}

.btn-primary:active {
    transform: translateY(0);
}

.btn-secondary {
    background: transparent;
    color: var(--text-primary);
    border: 1px solid rgba(168, 85, 247, 0.4);
}

.btn-secondary:hover {
    background: rgba(168, 85, 247, 0.1);
    border-color: var(--neon-purple);
    transform: translateY(-2px);
}

.btn-whatsapp {
    background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
    color: #fff;
    box-shadow: 0 4px 20px rgba(37, 211, 102, 0.35);
    width: 100%;
    margin-top: 8px;
}

.btn-whatsapp:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(37, 211, 102, 0.45);
}

/* ============================================
   HERO SECTION
   ============================================ */
.hero {
    min-height: 100vh;
    display: flex;
    align-items: center;
    padding-top: var(--header-height);
    overflow: hidden;
}

.hero-bg {
    position: absolute;
    inset: 0;
    z-index: 0;
}

.hero-particles {
    position: absolute;
    inset: 0;
    background: 
        radial-gradient(ellipse 80% 50% at 20% 40%, rgba(168, 85, 247, 0.12) 0%, transparent 50%),
        radial-gradient(ellipse 60% 40% at 80% 60%, rgba(59, 130, 246, 0.1) 0%, transparent 50%),
        radial-gradient(ellipse 40% 30% at 50% 80%, rgba(34, 211, 238, 0.06) 0%, transparent 50%);
}

.hero-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 64px;
    align-items: center;
    position: relative;
    z-index: 1;
}

.hero-badge {
    display: inline-block;
    padding: 6px 14px;
    background: rgba(59, 130, 246, 0.12);
    border: 1px solid rgba(59, 130, 246, 0.3);
    border-radius: 50px;
    font-size: 0.8125rem;
    font-weight: 500;
    color: var(--neon-blue);
    margin-bottom: 20px;
}

.hero-title {
    font-family: var(--font-display);
    font-size: clamp(2.25rem, 5vw, 3.5rem);
    font-weight: 700;
    line-height: 1.15;
    margin-bottom: 24px;
}

.hero-description {
    font-size: 1.125rem;
    color: var(--text-secondary);
    line-height: 1.7;
    margin-bottom: 36px;
    max-width: 520px;
}

.hero-buttons {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    margin-bottom: 48px;
}

.hero-stats {
    display: flex;
    gap: 40px;
}

.stat-item {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.stat-number {
    font-family: var(--font-display);
    font-size: 1.75rem;
    font-weight: 700;
    background: var(--gradient-text);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.stat-label {
    font-size: 0.8125rem;
    color: var(--text-muted);
}

.hero-visual {
    position: relative;
}

.hero-image-wrapper {
    position: relative;
    border-radius: var(--radius-xl);
    overflow: hidden;
    border: 1px solid var(--glass-border);
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5), 0 0 40px rgba(168, 85, 247, 0.15);
}

.hero-image {
    width: 100%;
    height: auto;
    object-fit: cover;
    aspect-ratio: 16 / 10;
}

.hero-glow {
    position: absolute;
    inset: -20%;
    background: radial-gradient(circle at center, rgba(168, 85, 247, 0.2) 0%, transparent 60%);
    pointer-events: none;
    z-index: -1;
    animation: pulse-glow 4s ease-in-out infinite;
}

@keyframes pulse-glow {
    0%, 100% { opacity: 0.6; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.05); }
}

.scroll-indicator {
    position: absolute;
    bottom: 32px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 2;
}

.mouse {
    display: block;
    width: 24px;
    height: 40px;
    border: 2px solid rgba(168, 85, 247, 0.4);
    border-radius: 12px;
    position: relative;
}

.wheel {
    position: absolute;
    top: 8px;
    left: 50%;
    transform: translateX(-50%);
    width: 3px;
    height: 8px;
    background: var(--neon-purple);
    border-radius: 2px;
    animation: scroll-wheel 1.5s ease-in-out infinite;
}

@keyframes scroll-wheel {
    0% { opacity: 1; transform: translateX(-50%) translateY(0); }
    100% { opacity: 0; transform: translateX(-50%) translateY(12px); }
}

/* ============================================
   ABOUT SECTION
   ============================================ */
.about {
    background: var(--bg-secondary);
}

.about-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 64px;
    align-items: center;
}

.about-text {
    font-size: 1.0625rem;
    color: var(--text-secondary);
    line-height: 1.8;
    margin-bottom: 32px;
}

.about-skills {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 36px;
}

.skill-tag {
    padding: 8px 16px;
    background: rgba(99, 102, 241, 0.1);
    border: 1px solid rgba(99, 102, 241, 0.25);
    border-radius: 50px;
    font-size: 0.8125rem;
    font-weight: 500;
    color: var(--electric-blue);
    transition: all var(--transition-fast);
}

.skill-tag:hover {
    background: rgba(99, 102, 241, 0.2);
    border-color: var(--electric-blue);
    transform: translateY(-2px);
}

.about-image-wrapper {
    overflow: hidden;
    padding: 8px;
}

.about-image {
    width: 100%;
    border-radius: calc(var(--radius-lg) - 4px);
    object-fit: cover;
    aspect-ratio: 4 / 3;
}

/* ============================================
   SERVICES SECTION
   ============================================ */
.services {
    position: relative;
    overflow: hidden;
}

.services-bg {
    position: absolute;
    inset: 0;
    z-index: 0;
}

.services-bg-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 0.08;
}

.services-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, var(--bg-primary) 0%, transparent 20%, transparent 80%, var(--bg-primary) 100%);
}

.services .container {
    position: relative;
    z-index: 1;
}

.services-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 28px;
}

.service-card {
    padding: 36px;
}

.service-icon {
    width: 64px;
    height: 64px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(168, 85, 247, 0.1);
    border: 1px solid rgba(168, 85, 247, 0.25);
    border-radius: var(--radius-md);
    color: var(--neon-purple);
    margin-bottom: 24px;
    transition: all var(--transition-normal);
}

.service-card:hover .service-icon {
    background: rgba(168, 85, 247, 0.2);
    box-shadow: 0 0 20px rgba(168, 85, 247, 0.3);
    transform: scale(1.05);
}

.service-title {
    font-family: var(--font-display);
    font-size: 1.25rem;
    font-weight: 600;
    margin-bottom: 12px;
    color: var(--text-primary);
}

.service-description {
    font-size: 0.9375rem;
    color: var(--text-secondary);
    line-height: 1.7;
    margin-bottom: 20px;
}

.service-features {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.service-features li {
    padding: 4px 12px;
    background: rgba(34, 211, 238, 0.08);
    border: 1px solid rgba(34, 211, 238, 0.2);
    border-radius: 50px;
    font-size: 0.75rem;
    color: var(--neon-cyan);
}

/* ============================================
   PORTFOLIO SECTION
   ============================================ */
.portfolio {
    background: var(--bg-secondary);
}

.portfolio-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 28px;
}

.portfolio-card {
    overflow: hidden;
    padding: 0;
}

.portfolio-image-wrapper {
    position: relative;
    overflow: hidden;
    aspect-ratio: 16 / 10;
}

.portfolio-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform var(--transition-slow);
}

.portfolio-card:hover .portfolio-image {
    transform: scale(1.08);
}

.portfolio-overlay {
    position: absolute;
    inset: 0;
    background: rgba(5, 5, 10, 0.7);
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: opacity var(--transition-normal);
}

.portfolio-card:hover .portfolio-overlay {
    opacity: 1;
}

.portfolio-link {
    width: 56px;
    height: 56px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--gradient-btn);
    border-radius: 50%;
    color: #fff;
    transform: scale(0.8);
    transition: transform var(--transition-normal);
}

.portfolio-card:hover .portfolio-link {
    transform: scale(1);
}

.portfolio-content {
    padding: 24px;
}

.portfolio-category {
    display: inline-block;
    font-size: 0.75rem;
    font-weight: 500;
    color: var(--neon-purple);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 8px;
}

.portfolio-title {
    font-family: var(--font-display);
    font-size: 1.125rem;
    font-weight: 600;
    margin-bottom: 8px;
    color: var(--text-primary);
}

.portfolio-description {
    font-size: 0.875rem;
    color: var(--text-secondary);
    line-height: 1.6;
}

/* ============================================
   SEO SECTION
   ============================================ */
.seo-grid {
    display: grid;
    grid-template-columns: 1fr 1.2fr;
    gap: 48px;
    align-items: center;
}

.seo-image-wrapper {
    overflow: hidden;
    padding: 8px;
}

.seo-image {
    width: 100%;
    border-radius: calc(var(--radius-lg) - 4px);
    object-fit: cover;
    aspect-ratio: 4 / 3;
}

.seo-cards {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
}

.seo-card {
    padding: 28px;
}

.seo-card-icon {
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(59, 130, 246, 0.1);
    border: 1px solid rgba(59, 130, 246, 0.25);
    border-radius: var(--radius-sm);
    color: var(--neon-blue);
    margin-bottom: 16px;
}

.seo-card-title {
    font-family: var(--font-display);
    font-size: 1.0625rem;
    font-weight: 600;
    margin-bottom: 8px;
    color: var(--text-primary);
}

.seo-card-text {
    font-size: 0.875rem;
    color: var(--text-secondary);
    line-height: 1.65;
}

/* ============================================
   CONTACT SECTION
   ============================================ */
.contact {
    background: var(--bg-secondary);
}

.contact-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 48px;
    align-items: center;
}

.contact-info {
    padding: 40px;
}

.contact-info-title {
    font-family: var(--font-display);
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 12px;
}

.contact-info-text {
    font-size: 1rem;
    color: var(--text-secondary);
    line-height: 1.7;
    margin-bottom: 28px;
}

.contact-details {
    margin-top: 28px;
    padding-top: 24px;
    border-top: 1px solid rgba(168, 85, 247, 0.15);
}

.contact-detail-item {
    display: flex;
    align-items: center;
    gap: 12px;
    color: var(--text-secondary);
    font-size: 0.9375rem;
}

.contact-detail-item svg {
    color: var(--neon-purple);
    flex-shrink: 0;
}

.contact-image-wrapper {
    overflow: hidden;
    padding: 8px;
}

.contact-image {
    width: 100%;
    border-radius: calc(var(--radius-lg) - 4px);
    object-fit: cover;
    aspect-ratio: 4 / 3;
}

/* ============================================
   FOOTER
   ============================================ */
.footer {
    padding: 48px 0 32px;
    border-top: 1px solid rgba(168, 85, 247, 0.1);
    background: var(--bg-primary);
}

.footer-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 32px;
}

.footer-logo {
    display: flex;
    align-items: center;
    font-family: var(--font-display);
    font-size: 1.25rem;
    font-weight: 700;
    margin-bottom: 8px;
}

.footer-tagline {
    font-size: 0.875rem;
    color: var(--text-muted);
}

.footer-links {
    display: flex;
    flex-wrap: wrap;
    gap: 24px;
}

.footer-links a {
    font-size: 0.875rem;
    color: var(--text-secondary);
}

.footer-links a:hover {
    color: var(--neon-purple);
}

.footer-bottom {
    text-align: center;
    padding-top: 24px;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
}

.footer-bottom p {
    font-size: 0.8125rem;
    color: var(--text-muted);
}

/* ============================================
   WHATSAPP FLOAT
   ============================================ */
.whatsapp-float {
    position: fixed;
    bottom: 28px;
    right: 28px;
    width: 60px;
    height: 60px;
    background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    box-shadow: 0 4px 24px rgba(37, 211, 102, 0.4);
    z-index: 999;
    transition: all var(--transition-normal);
}

.whatsapp-float:hover {
    transform: scale(1.1);
    box-shadow: 0 6px 32px rgba(37, 211, 102, 0.55);
}

.whatsapp-float:focus-visible {
    outline: 2px solid #25D366;
    outline-offset: 4px;
}

/* ============================================
   REVEAL ANIMATIONS
   ============================================ */
.reveal-up,
.reveal-left,
.reveal-right {
    opacity: 0;
    transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
}

.reveal-up {
    transform: translateY(40px);
}

.reveal-left {
    transform: translateX(-40px);
}

.reveal-right {
    transform: translateX(40px);
}

.reveal-up.revealed,
.reveal-left.revealed,
.reveal-right.revealed {
    opacity: 1;
    transform: translate(0);
}

/* Stagger delays */
.reveal-up:nth-child(2) { transition-delay: 0.1s; }
.reveal-up:nth-child(3) { transition-delay: 0.2s; }
.reveal-up:nth-child(4) { transition-delay: 0.3s; }

/* ============================================
   FOCUS & ACCESSIBILITY
   ============================================ */
a:focus-visible,
button:focus-visible {
    outline: 2px solid var(--neon-purple);
    outline-offset: 3px;
}

.btn:focus-visible {
    outline: 2px solid var(--neon-blue);
    outline-offset: 3px;
}

/* Reduce motion */
@media (prefers-reduced-motion: reduce) {
    html {
        scroll-behavior: auto;
    }
    
    *,
    *::before,
    *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
    
    .reveal-up,
    .reveal-left,
    .reveal-right {
        opacity: 1;
        transform: none;
    }
}

/* ============================================
   TABLET (max-width: 1024px)
   ============================================ */
@media (max-width: 1024px) {
    .section {
        padding: 96px 0;
    }

    .hero-container {
        gap: 48px;
    }

    .hero-title {
        font-size: clamp(2rem, 4.5vw, 2.75rem);
    }

    .about-grid,
    .seo-grid,
    .contact-grid {
        gap: 40px;
    }

    .services-grid {
        gap: 24px;
    }

    .portfolio-grid {
        grid-template-columns: repeat(2, 1fr);
    }

    .seo-cards {
        gap: 16px;
    }
}

/* ============================================
   TABLET SMALL / LARGE MOBILE (max-width: 768px)
   ============================================ */
@media (max-width: 768px) {
    :root {
        --header-height: 70px;
    }

    .container {
        padding: 0 20px;
    }

    .section {
        padding: 80px 0;
    }

    .section-header {
        margin-bottom: 48px;
    }

    /* Navigation */
    .nav-toggle {
        display: flex;
    }

    .nav-menu {
        position: fixed;
        top: 0;
        right: -100%;
        width: 100%;
        max-width: 320px;
        height: 100vh;
        background: rgba(5, 5, 10, 0.97);
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        border-left: 1px solid rgba(168, 85, 247, 0.15);
        padding: 100px 32px 40px;
        transition: right var(--transition-normal);
        z-index: 1000;
    }

    .nav-menu.active {
        right: 0;
    }

    .nav-list {
        flex-direction: column;
        align-items: flex-start;
        gap: 4px;
    }

    .nav-link {
        display: block;
        width: 100%;
        padding: 14px 16px;
        font-size: 1.0625rem;
    }

    .nav-link.active::after {
        left: 16px;
        transform: none;
        width: 3px;
        height: 20px;
        top: 50%;
        transform: translateY(-50%);
        bottom: auto;
    }

    /* Hero */
    .hero {
        min-height: auto;
        padding: calc(var(--header-height) + 40px) 0 80px;
    }

    .hero-container {
        grid-template-columns: 1fr;
        gap: 48px;
        text-align: center;
    }

    .hero-content {
        order: 1;
    }

    .hero-visual {
        order: 0;
        max-width: 480px;
        margin: 0 auto;
    }

    .hero-description {
        margin-left: auto;
        margin-right: auto;
    }

    .hero-buttons {
        justify-content: center;
    }

    .hero-stats {
        justify-content: center;
        gap: 32px;
    }

    .scroll-indicator {
        display: none;
    }

    /* About */
    .about-grid {
        grid-template-columns: 1fr;
        gap: 40px;
    }

    .about-content {
        order: 1;
    }

    .about-visual {
        order: 0;
        max-width: 520px;
        margin: 0 auto;
    }

    .about-skills {
        justify-content: center;
    }

    .about-cta {
        display: flex;
        margin: 0 auto;
        width: fit-content;
    }

    /* Services */
    .services-grid {
        grid-template-columns: 1fr;
        max-width: 480px;
        margin: 0 auto;
    }

    .service-card {
        padding: 28px;
    }

    /* Portfolio */
    .portfolio-grid {
        grid-template-columns: 1fr;
        max-width: 480px;
        margin: 0 auto;
    }

    /* SEO */
    .seo-grid {
        grid-template-columns: 1fr;
        gap: 40px;
    }

    .seo-visual {
        max-width: 520px;
        margin: 0 auto;
    }

    .seo-cards {
        grid-template-columns: 1fr;
        max-width: 480px;
        margin: 0 auto;
    }

    /* Contact */
    .contact-grid {
        grid-template-columns: 1fr;
        gap: 40px;
    }

    .contact-content {
        order: 1;
    }

    .contact-visual {
        order: 0;
        max-width: 480px;
        margin: 0 auto;
    }

    .contact-info {
        padding: 32px;
    }

    /* Footer */
    .footer-content {
        flex-direction: column;
        gap: 28px;
        text-align: center;
    }

    .footer-links {
        justify-content: center;
        gap: 16px 24px;
    }

    /* WhatsApp */
    .whatsapp-float {
        bottom: 20px;
        right: 20px;
        width: 54px;
        height: 54px;
    }
}

/* ============================================
   MOBILE (max-width: 480px)
   ============================================ */
@media (max-width: 480px) {
    .container {
        padding: 0 16px;
    }

    .section {
        padding: 64px 0;
    }

    .section-title {
        font-size: 1.75rem;
    }

    .section-subtitle {
        font-size: 1rem;
    }

    .hero-title {
        font-size: 1.875rem;
    }

    .hero-description {
        font-size: 1rem;
    }

    .hero-buttons {
        flex-direction: column;
        width: 100%;
    }

    .hero-buttons .btn {
        width: 100%;
    }

    .hero-stats {
        flex-direction: column;
        gap: 20px;
        align-items: center;
    }

    .stat-item {
        align-items: center;
    }

    .service-card {
        padding: 24px;
    }

    .service-icon {
        width: 56px;
        height: 56px;
    }

    .portfolio-content {
        padding: 20px;
    }

    .seo-card {
        padding: 24px;
    }

    .contact-info {
        padding: 28px 24px;
    }

    .btn {
        padding: 13px 24px;
        font-size: 0.875rem;
    }

    .footer-links {
        gap: 12px 16px;
    }

    .footer-links a {
        font-size: 0.8125rem;
    }
}

/* ============================================
   LARGE DESKTOP (min-width: 1400px)
   ============================================ */
@media (min-width: 1400px) {
    .container {
        max-width: 1280px;
    }

    .hero-title {
        font-size: 3.75rem;
    }
}

    </style>
</head>
<body>
    <!-- Page Loader -->
    <div class="page-loader" id="pageLoader">
        <div class="loader-content">
            <div class="loader-ring"></div>
            <span class="loader-text">Yükleniyor...</span>
        </div>
    </div>

    <!-- Navigation -->
    <header class="header" id="header">
        <nav class="nav container">
            <a href="#home" class="nav-logo" aria-label="Ana Sayfa">
                <span class="logo-bracket">&lt;</span>
                <span class="logo-text">Dev</span>
                <span class="logo-bracket">/&gt;</span>
            </a>

            <div class="nav-menu" id="navMenu">
                <ul class="nav-list">
                    <li class="nav-item">
                        <a href="#home" class="nav-link active" data-section="home">Ana Sayfa</a>
                    </li>
                    <li class="nav-item">
                        <a href="#about" class="nav-link" data-section="about">Hakkımda</a>
                    </li>
                    <li class="nav-item">
                        <a href="#services" class="nav-link" data-section="services">Hizmetler</a>
                    </li>
                    <li class="nav-item">
                        <a href="#portfolio" class="nav-link" data-section="portfolio">Projeler</a>
                    </li>
                    <li class="nav-item">
                        <a href="#seo" class="nav-link" data-section="seo">SEO</a>
                    </li>
                    <li class="nav-item">
                        <a href="#contact" class="nav-link" data-section="contact">İletişim</a>
                    </li>
                </ul>
            </div>

            <button class="nav-toggle" id="navToggle" aria-label="Menüyü Aç/Kapat" aria-expanded="false">
                <span class="hamburger"></span>
                <span class="hamburger"></span>
                <span class="hamburger"></span>
            </button>
        </nav>
    </header>

    <main>
        <!-- Hero Section -->
        <section class="hero section" id="home">
            <div class="hero-bg">
                <div class="hero-particles" id="particles"></div>
            </div>
            <div class="container hero-container">
                <div class="hero-content">
                    <p class="hero-badge reveal-up">Full-Stack Web Developer</p>
                    <h1 class="hero-title reveal-up">
                        Fikirlerinizi Dijital Dünyada<br>
                        <span class="gradient-text">Hayata Geçiriyorum</span>
                    </h1>
                    <p class="hero-description reveal-up">
                        Modern web teknolojileriyle işletmeler ve markalar için güçlü, hızlı ve kullanıcı odaklı dijital çözümler geliştiriyorum.
                    </p>
                    <div class="hero-buttons reveal-up">
                        <a href="#portfolio" class="btn btn-primary">
                            <span>Projelerimi İncele</span>
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M5 12h14M12 5l7 7-7 7"/>
                            </svg>
                        </a>
                        <a href="#contact" class="btn btn-secondary">
                            <span>Benimle İletişime Geç</span>
                        </a>
                    </div>
                    <div class="hero-stats reveal-up">
                        <div class="stat-item">
                            <span class="stat-number">4+</span>
                            <span class="stat-label">Yıl Deneyim</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-number">50+</span>
                            <span class="stat-label">Tamamlanan Proje</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-number">100%</span>
                            <span class="stat-label">Müşteri Memnuniyeti</span>
                        </div>
                    </div>
                </div>
                <div class="hero-visual reveal-right">
                    <div class="hero-image-wrapper">
                        <img src="https://i.ibb.co/rf4ws4kp/1793729385334.jpg" alt="Profesyonel yazılım geliştirme çalışma alanı - modern ofis ve kod editörü" class="hero-image" loading="eager">
                        <div class="hero-glow"></div>
                    </div>
                </div>
            </div>
            <div class="scroll-indicator">
                <a href="#about" aria-label="Aşağı kaydır">
                    <span class="mouse">
                        <span class="wheel"></span>
                    </span>
                </a>
            </div>
        </section>

        <!-- About Section -->
        <section class="about section" id="about">
            <div class="container">
                <div class="section-header">
                    <span class="section-badge reveal-up">Hakkımda</span>
                    <h2 class="section-title reveal-up">4 Yıllık Deneyim, Güçlü Dijital Çözümler</h2>
                </div>
                <div class="about-grid">
                    <div class="about-content reveal-left">
                        <p class="about-text">
                            4 yıllık yazılım geliştirme deneyimimle modern, hızlı ve kullanıcı odaklı web projeleri geliştiriyorum. Bugüne kadar birçok büyük projeyi hayata geçirdim. Web geliştirme, özel yazılım çözümleri ve SEO odaklı projelerde aktif rol alarak işletmelerin dijital dünyada daha güçlü yer edinmesine katkı sağladım.
                        </p>
                        <div class="about-skills">
                            <div class="skill-tag">HTML5 & CSS3</div>
                            <div class="skill-tag">JavaScript</div>
                            <div class="skill-tag">Responsive Design</div>
                            <div class="skill-tag">UI/UX Design</div>
                            <div class="skill-tag">SEO</div>
                            <div class="skill-tag">Performance</div>
                            <div class="skill-tag">Accessibility</div>
                            <div class="skill-tag">Modern Frameworks</div>
                        </div>
                        <a href="#contact" class="btn btn-primary about-cta">
                            <span>Birlikte Çalışalım</span>
                        </a>
                    </div>
                    <div class="about-visual reveal-right">
                        <div class="about-image-wrapper glass-card">
                            <img src="https://i.ibb.co/LdxTPWFv/1793729956220.jpg" alt="Geliştirici çalışma ortamı - çoklu ekran ve modern web arayüzleri" class="about-image" loading="lazy">
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Services Section -->
        <section class="services section" id="services">
            <div class="services-bg">
                <img src="https://i.ibb.co/pjV2TwBQ/1793729924917.jpg" alt="" class="services-bg-image" loading="lazy" aria-hidden="true">
                <div class="services-overlay"></div>
            </div>
            <div class="container">
                <div class="section-header">
                    <span class="section-badge reveal-up">Hizmetler</span>
                    <h2 class="section-title reveal-up">Profesyonel Hizmetlerim</h2>
                    <p class="section-subtitle reveal-up">İşletmenizin dijital ihtiyaçlarına özel, kaliteli ve sürdürülebilir çözümler sunuyorum.</p>
                </div>
                <div class="services-grid">
                    <article class="service-card glass-card reveal-up">
                        <div class="service-icon">
                            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                                <rect x="2" y="3" width="20" height="14" rx="2"/>
                                <path d="M8 21h8M12 17v4"/>
                            </svg>
                        </div>
                        <h3 class="service-title">Web Tasarım ve Geliştirme</h3>
                        <p class="service-description">Modern, hızlı, mobil uyumlu ve kullanıcı dostu web siteleri. Markanızın kimliğini yansıtan, dönüşüm odaklı arayüzler tasarlıyorum.</p>
                        <ul class="service-features">
                            <li>Responsive Tasarım</li>
                            <li>Yüksek Performans</li>
                            <li>Modern UI/UX</li>
                        </ul>
                    </article>
                    <article class="service-card glass-card reveal-up">
                        <div class="service-icon">
                            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                                <path d="M16 18l6-6-6-6M8 6l-6 6 6 6"/>
                            </svg>
                        </div>
                        <h3 class="service-title">Özel Yazılım Geliştirme</h3>
                        <p class="service-description">İşletmelere özel, ihtiyaca yönelik yazılım sistemleri. Süreçlerinizi dijitalleştiren, verimliliği artıran çözümler üretiyorum.</p>
                        <ul class="service-features">
                            <li>Özel İhtiyaç Analizi</li>
                            <li>Ölçeklenebilir Mimari</li>
                            <li>Güvenli Altyapı</li>
                        </ul>
                    </article>
                    <article class="service-card glass-card reveal-up">
                        <div class="service-icon">
                            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                                <circle cx="9" cy="21" r="1"/>
                                <circle cx="20" cy="21" r="1"/>
                                <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/>
                            </svg>
                        </div>
                        <h3 class="service-title">E-Ticaret Sistemleri</h3>
                        <p class="service-description">Güvenli, modern ve dönüşüm odaklı e-ticaret platformları. Satışlarınızı artıracak, kullanıcı deneyimini ön planda tutan mağazalar kuruyorum.</p>
                        <ul class="service-features">
                            <li>Güvenli Ödeme</li>
                            <li>Stok Yönetimi</li>
                            <li>Analitik Entegrasyon</li>
                        </ul>
                    </article>
                    <article class="service-card glass-card reveal-up">
                        <div class="service-icon">
                            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                                <circle cx="11" cy="11" r="8"/>
                                <path d="M21 21l-4.35-4.35"/>
                                <path d="M11 8v6M8 11h6"/>
                            </svg>
                        </div>
                        <h3 class="service-title">SEO Optimizasyonu</h3>
                        <p class="service-description">Arama motorlarında görünürlüğü artırmaya yönelik teknik ve içerik odaklı SEO çalışmaları. Organik trafiğinizi sürdürülebilir şekilde büyütüyorum.</p>
                        <ul class="service-features">
                            <li>Teknik SEO</li>
                            <li>İçerik Stratejisi</li>
                            <li>Performans İyileştirme</li>
                        </ul>
                    </article>
                </div>
            </div>
        </section>

        <!-- Portfolio Section -->
        <section class="portfolio section" id="portfolio">
            <div class="container">
                <div class="section-header">
                    <span class="section-badge reveal-up">Portföy</span>
                    <h2 class="section-title reveal-up">Hayata Geçirdiğim Projeler</h2>
                    <p class="section-subtitle reveal-up">Farklı sektörlerden seçilmiş çalışmalar. Her proje, özgün ihtiyaçlara özel çözümler içerir.</p>
                </div>
                <div class="portfolio-grid">
                    <article class="portfolio-card glass-card reveal-up">
                        <div class="portfolio-image-wrapper">
                            <img src="https://i.ibb.co/LdxTPWFv/1793729956220.jpg" alt="Kurumsal web sitesi ve dashboard arayüzleri" class="portfolio-image" loading="lazy">
                            <div class="portfolio-overlay">
                                <a href="#contact" class="portfolio-link" aria-label="Proje detayı için iletişime geç">
                                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                        <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6M15 3h6v6M10 14L21 3"/>
                                    </svg>
                                </a>
                            </div>
                        </div>
                        <div class="portfolio-content">
                            <span class="portfolio-category">Kurumsal Web Sitesi</span>
                            <h3 class="portfolio-title">Kurumsal Dijital Platform</h3>
                            <p class="portfolio-description">Modern tasarım, yüksek performans ve SEO odaklı kurumsal web sitesi. Responsive yapı ve kullanıcı deneyimi ön planda tutuldu.</p>
                        </div>
                    </article>
                    <article class="portfolio-card glass-card reveal-up">
                        <div class="portfolio-image-wrapper">
                            <img src="https://i.ibb.co/LdxTPWFv/1793729956220.jpg" alt="E-ticaret ürün galerisi ve yönetim paneli" class="portfolio-image" loading="lazy">
                            <div class="portfolio-overlay">
                                <a href="#contact" class="portfolio-link" aria-label="Proje detayı için iletişime geç">
                                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                        <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6M15 3h6v6M10 14L21 3"/>
                                    </svg>
                                </a>
                            </div>
                        </div>
                        <div class="portfolio-content">
                            <span class="portfolio-category">E-Ticaret</span>
                            <h3 class="portfolio-title">Modern E-Ticaret Platformu</h3>
                            <p class="portfolio-description">Güvenli ödeme entegrasyonu, stok yönetimi ve dönüşüm odaklı ürün sayfaları ile tam kapsamlı e-ticaret çözümü.</p>
                        </div>
                    </article>
                    <article class="portfolio-card glass-card reveal-up">
                        <div class="portfolio-image-wrapper">
                            <img src="https://i.ibb.co/LdxTPWFv/1793729956220.jpg" alt="Analitik dashboard ve veri görselleştirme arayüzü" class="portfolio-image" loading="lazy">
                            <div class="portfolio-overlay">
                                <a href="#contact" class="portfolio-link" aria-label="Proje detayı için iletişime geç">
                                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                        <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6M15 3h6v6M10 14L21 3"/>
                                    </svg>
                                </a>
                            </div>
                        </div>
                        <div class="portfolio-content">
                            <span class="portfolio-category">Özel Yazılım</span>
                            <h3 class="portfolio-title">İş Süreçleri Yönetim Sistemi</h3>
                            <p class="portfolio-description">İşletmeye özel geliştirilmiş panel, raporlama ve süreç otomasyonu. Verimliliği artıran ölçeklenebilir yazılım çözümü.</p>
                        </div>
                    </article>
                </div>
            </div>
        </section>

        <!-- SEO Section -->
        <section class="seo section" id="seo">
            <div class="container">
                <div class="section-header">
                    <span class="section-badge reveal-up">SEO</span>
                    <h2 class="section-title reveal-up">SEO Odaklı Dijital Başarı</h2>
                    <p class="section-subtitle reveal-up">Web projelerinde yalnızca tasarıma değil, arama motorlarının teknik gereksinimlerine, performansa, kullanıcı deneyimine ve organik görünürlüğe de önem veriyorum.</p>
                </div>
                <div class="seo-grid">
                    <div class="seo-visual reveal-left">
                        <div class="seo-image-wrapper glass-card">
                            <img src="https://i.ibb.co/zhL265Td/1793729981872.jpg" alt="SEO ve veri analitiği görselleştirmesi - grafikler ve network diyagramları" class="seo-image" loading="lazy">
                        </div>
                    </div>
                    <div class="seo-cards">
                        <article class="seo-card glass-card reveal-up">
                            <div class="seo-card-icon">
                                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                                    <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
                                </svg>
                            </div>
                            <h3 class="seo-card-title">Teknik SEO</h3>
                            <p class="seo-card-text">Site mimarisi, yapılandırılmış veri, canonical etiketler, sitemap ve robots.txt optimizasyonu ile arama motorlarına net sinyaller gönderiyorum.</p>
                        </article>
                        <article class="seo-card glass-card reveal-up">
                            <div class="seo-card-icon">
                                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                                    <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
                                </svg>
                            </div>
                            <h3 class="seo-card-title">Site Hızı</h3>
                            <p class="seo-card-text">Görsel optimizasyonu, lazy loading, kritik CSS ve performans metrikleri ile Core Web Vitals hedeflerine odaklanıyorum.</p>
                        </article>
                        <article class="seo-card glass-card reveal-up">
                            <div class="seo-card-icon">
                                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                                    <rect x="5" y="2" width="14" height="20" rx="2"/>
                                    <path d="M12 18h.01"/>
                                </svg>
                            </div>
                            <h3 class="seo-card-title">Mobil Uyumluluk</h3>
                            <p class="seo-card-text">Mobile-first yaklaşım, responsive tasarım ve dokunmatik dostu arayüzler ile tüm cihazlarda kusursuz deneyim sağlıyorum.</p>
                        </article>
                        <article class="seo-card glass-card reveal-up">
                            <div class="seo-card-icon">
                                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                                    <path d="M14 2v6h6M16 13H8M16 17H8M10 9H8"/>
                                </svg>
                            </div>
                            <h3 class="seo-card-title">İçerik Optimizasyonu</h3>
                            <p class="seo-card-text">Anlamlı başlık hiyerarşisi, meta etiketleri, alt metinler ve kullanıcı niyetine uygun içerik yapısı ile organik görünürlüğü artırıyorum.</p>
                        </article>
                    </div>
                </div>
            </div>
        </section>

        <!-- Contact Section -->
        <section class="contact section" id="contact">
            <div class="container">
                <div class="section-header">
                    <span class="section-badge reveal-up">İletişim</span>
                    <h2 class="section-title reveal-up">Projenizi Birlikte Hayata Geçirelim</h2>
                    <p class="section-subtitle reveal-up">Yeni bir web sitesi, özel yazılım veya dijital projeniz mi var? Fikirlerinizi konuşalım ve birlikte hayata geçirelim.</p>
                </div>
                <div class="contact-grid">
                    <div class="contact-content reveal-left">
                        <div class="contact-info glass-card">
                            <h3 class="contact-info-title">Hemen İletişime Geçin</h3>
                            <p class="contact-info-text">WhatsApp üzerinden hızlıca ulaşabilirsiniz. Projenizi dinleyip size en uygun çözümü birlikte planlayalım.</p>
                            <a href="https://wa.me/79605539465" class="btn btn-whatsapp" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp ile iletişime geç">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                                    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.435 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
                                </svg>
                                <span>WhatsApp ile Yazın</span>
                            </a>
                            <div class="contact-details">
                                <div class="contact-detail-item">
                                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                        <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
                                    </svg>
                                    <span>+7 960 553 94 65</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="contact-visual reveal-right">
                        <div class="contact-image-wrapper glass-card">
                            <img src="https://i.ibb.co/C5b5zHnY/1793730006052.jpg" alt="Mobil uygulama arayüzü ve modern iletişim teknolojileri" class="contact-image" loading="lazy">
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-brand">
                    <a href="#home" class="footer-logo">
                        <span class="logo-bracket">&lt;</span>
                        <span class="logo-text">Dev</span>
                        <span class="logo-bracket">/&gt;</span>
                    </a>
                    <p class="footer-tagline">Fikirlerinizi dijital dünyada hayata geçiriyorum.</p>
                </div>
                <div class="footer-links">
                    <a href="#home">Ana Sayfa</a>
                    <a href="#about">Hakkımda</a>
                    <a href="#services">Hizmetler</a>
                    <a href="#portfolio">Projeler</a>
                    <a href="#seo">SEO</a>
                    <a href="#contact">İletişim</a>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; <span id="currentYear"></span> Tüm hakları saklıdır.</p>
            </div>
        </div>
    </footer>

    <!-- Fixed WhatsApp Button -->
    <a href="https://wa.me/79605539465" class="whatsapp-float" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp ile iletişime geç">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
            <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.435 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
        </svg>
    </a>

    <script>
/* ============================================
   PORTFOLIO SITE - VANILLA JS
   ============================================ */

(function () {
    'use strict';

    // ---------- DOM Elements ----------
    const pageLoader = document.getElementById('pageLoader');
    const header = document.getElementById('header');
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('.section');
    const currentYearEl = document.getElementById('currentYear');

    // ---------- Page Loader ----------
    function hideLoader() {
        if (pageLoader) {
            pageLoader.classList.add('hidden');
            setTimeout(() => {
                pageLoader.style.display = 'none';
            }, 500);
        }
    }

    window.addEventListener('load', () => {
        setTimeout(hideLoader, 400);
    });

    // Fallback if load event already fired
    if (document.readyState === 'complete') {
        setTimeout(hideLoader, 400);
    }

    // ---------- Current Year ----------
    if (currentYearEl) {
        currentYearEl.textContent = new Date().getFullYear();
    }

    // ---------- Mobile Navigation ----------
    function toggleMenu() {
        const isOpen = navMenu.classList.toggle('active');
        navToggle.classList.toggle('active', isOpen);
        navToggle.setAttribute('aria-expanded', isOpen);
        document.body.style.overflow = isOpen ? 'hidden' : '';
    }

    function closeMenu() {
        navMenu.classList.remove('active');
        navToggle.classList.remove('active');
        navToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
    }

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', toggleMenu);

        navLinks.forEach(link => {
            link.addEventListener('click', closeMenu);
        });

        // Close on Escape
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && navMenu.classList.contains('active')) {
                closeMenu();
            }
        });

        // Close when clicking outside
        document.addEventListener('click', (e) => {
            if (
                navMenu.classList.contains('active') &&
                !navMenu.contains(e.target) &&
                !navToggle.contains(e.target)
            ) {
                closeMenu();
            }
        });
    }

    // ---------- Header Scroll Effect ----------
    function handleHeaderScroll() {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    }

    window.addEventListener('scroll', handleHeaderScroll, { passive: true });
    handleHeaderScroll();

    // ---------- Active Nav Link (Scroll Spy) ----------
    function updateActiveLink() {
        const scrollPos = window.scrollY + 120;

        sections.forEach(section => {
            const top = section.offsetTop;
            const height = section.offsetHeight;
            const id = section.getAttribute('id');

            if (scrollPos >= top && scrollPos < top + height) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('data-section') === id) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }

    window.addEventListener('scroll', updateActiveLink, { passive: true });
    updateActiveLink();

    // ---------- Smooth Scroll (enhanced) ----------
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                const offset = header ? header.offsetHeight : 80;
                const top = target.getBoundingClientRect().top + window.pageYOffset - offset;

                window.scrollTo({
                    top: top,
                    behavior: 'smooth'
                });
            }
        });
    });

    // ---------- Scroll Reveal Animations ----------
    const revealElements = document.querySelectorAll('.reveal-up, .reveal-left, .reveal-right');

    const revealObserver = new IntersectionObserver(
        (entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('revealed');
                    // Optional: unobserve after reveal for performance
                    // revealObserver.unobserve(entry.target);
                }
            });
        },
        {
            threshold: 0.12,
            rootMargin: '0px 0px -40px 0px'
        }
    );

    revealElements.forEach(el => {
        revealObserver.observe(el);
    });

    // ---------- Keyboard Accessibility for Cards ----------
    document.querySelectorAll('.service-card, .portfolio-card, .seo-card').forEach(card => {
        card.setAttribute('tabindex', '0');
    });

})();

    </script>
</body>
</html>
"""

ROBOTS = """User-agent: *
Allow: /

Sitemap: https://teleatlas.xyz/sitemap.xml
"""

SITEMAP = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://teleatlas.xyz/</loc>
        <lastmod>2026-11-03</lastmod>
        <changefreq>monthly</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>https://teleatlas.xyz/#about</loc>
        <lastmod>2026-11-03</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://teleatlas.xyz/#services</loc>
        <lastmod>2026-11-03</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://teleatlas.xyz/#portfolio</loc>
        <lastmod>2026-11-03</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://teleatlas.xyz/#seo</loc>
        <lastmod>2026-11-03</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>
    <url>
        <loc>https://teleatlas.xyz/#contact</loc>
        <lastmod>2026-11-03</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.9</priority>
    </url>
</urlset>
"""


@app.route("/")
def index():
    return Response(HTML, mimetype="text/html; charset=utf-8")


@app.route("/robots.txt")
def robots():
    return Response(ROBOTS, mimetype="text/plain; charset=utf-8")


@app.route("/sitemap.xml")
def sitemap():
    return Response(SITEMAP, mimetype="application/xml; charset=utf-8")


@app.errorhandler(404)
def not_found(e):
    return Response(HTML, mimetype="text/html; charset=utf-8")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
