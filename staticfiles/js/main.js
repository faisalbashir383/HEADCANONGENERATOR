/**
 * Headcanon Generator - Main JavaScript
 * Vanilla JS, fully optimized
 */

(function () {
    'use strict';

    // DOM Elements
    const form = document.getElementById('generator-form');
    const generateBtn = document.getElementById('generate-btn');
    const outputContainer = document.getElementById('output-container');
    const headcanonList = document.getElementById('headcanon-list');
    const characterOutput = document.getElementById('character-output');
    const copyBtn = document.getElementById('copy-btn');
    const regenerateBtn = document.getElementById('regenerate-btn');

    // State
    let lastRequest = null;
    let isGenerating = false;

    // Initialize FAQ accordions
    function initFAQ() {
        const faqItems = document.querySelectorAll('.faq-item');
        faqItems.forEach(item => {
            const question = item.querySelector('.faq-question');
            question.addEventListener('click', () => {
                const isActive = item.classList.contains('active');
                // Close all other items
                faqItems.forEach(i => {
                    i.classList.remove('active');
                    const btn = i.querySelector('.faq-question');
                    if (btn) btn.setAttribute('aria-expanded', 'false');
                });
                // Toggle current item
                if (!isActive) {
                    item.classList.add('active');
                    question.setAttribute('aria-expanded', 'true');
                }
            });
        });
    }

    // Generate headcanons
    async function generateHeadcanons(characterName, fandom, tone) {
        if (isGenerating) return;
        isGenerating = true;

        // Update button state
        const btnText = generateBtn.querySelector('.btn-text');
        const btnLoading = generateBtn.querySelector('.btn-loading');
        btnText.style.display = 'none';
        btnLoading.style.display = 'inline';
        generateBtn.disabled = true;

        try {
            const response = await fetch('/api/generate/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    character: characterName,
                    fandom: fandom,
                    tone: tone
                })
            });

            const data = await response.json();

            if (data.success) {
                displayHeadcanons(data.headcanons, data.character);
                // Store for regeneration
                lastRequest = { character: characterName, fandom, tone };
            } else {
                showError(data.error || 'Failed to generate headcanons');
            }
        } catch (error) {
            console.error('Error:', error);
            showError('Network error. Please try again.');
        } finally {
            // Reset button state
            btnText.style.display = 'inline';
            btnLoading.style.display = 'none';
            generateBtn.disabled = false;
            isGenerating = false;
        }
    }

    // Display headcanons
    function displayHeadcanons(headcanons, characterName) {
        headcanonList.innerHTML = '';
        characterOutput.textContent = characterName;

        headcanons.forEach((headcanon, index) => {
            const li = document.createElement('li');
            li.textContent = headcanon;
            li.style.animationDelay = `${index * 0.1}s`;
            li.classList.add('fade-in');
            headcanonList.appendChild(li);
        });

        outputContainer.style.display = 'block';
        outputContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    // Show error message
    function showError(message) {
        headcanonList.innerHTML = `<li style="border-left-color: #ef4444;">${message}</li>`;
        characterOutput.textContent = 'Error';
        outputContainer.style.display = 'block';
    }

    // Copy headcanons to clipboard
    async function copyHeadcanons() {
        const headcanons = Array.from(headcanonList.querySelectorAll('li'))
            .map(li => '• ' + li.textContent)
            .join('\n');

        const character = characterOutput.textContent;
        const text = `Headcanons for ${character}:\n\n${headcanons}\n\n— Generated at headcanongenerator.world`;

        try {
            await navigator.clipboard.writeText(text);
            copyBtn.innerHTML = '✓ Copied!';
            copyBtn.classList.add('copied');
            setTimeout(() => {
                copyBtn.innerHTML = '📋 Copy';
                copyBtn.classList.remove('copied');
            }, 2000);
        } catch (err) {
            // Fallback for older browsers
            const textarea = document.createElement('textarea');
            textarea.value = text;
            textarea.style.position = 'fixed';
            textarea.style.opacity = '0';
            document.body.appendChild(textarea);
            textarea.select();
            document.execCommand('copy');
            document.body.removeChild(textarea);
            copyBtn.innerHTML = '✓ Copied!';
            copyBtn.classList.add('copied');
            setTimeout(() => {
                copyBtn.innerHTML = '📋 Copy';
                copyBtn.classList.remove('copied');
            }, 2000);
        }
    }

    // Regenerate headcanons
    function regenerate() {
        if (lastRequest) {
            generateHeadcanons(lastRequest.character, lastRequest.fandom, lastRequest.tone);
        }
    }

    // Form submission handler
    function handleSubmit(e) {
        e.preventDefault();

        const characterName = document.getElementById('character-name').value.trim();
        if (!characterName) {
            document.getElementById('character-name').focus();
            return;
        }

        // Get fandom (prefer dropdown, fallback to custom)
        const fandomSelect = document.getElementById('fandom-select').value;
        const fandomCustom = document.getElementById('fandom-custom').value.trim();
        const fandom = fandomCustom || fandomSelect || '';

        // Get tone
        const toneRadio = document.querySelector('input[name="tone"]:checked');
        const tone = toneRadio ? toneRadio.value : 'random';

        generateHeadcanons(characterName, fandom, tone);
    }

    // Smooth scroll for anchor links
    function initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                const href = this.getAttribute('href');
                if (href === '#') return;

                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({ behavior: 'smooth' });
                }
            });
        });
    }

    // Initialize on DOM ready
    function init() {
        if (form) {
            form.addEventListener('submit', handleSubmit);
        }

        if (copyBtn) {
            copyBtn.addEventListener('click', copyHeadcanons);
        }

        if (regenerateBtn) {
            regenerateBtn.addEventListener('click', regenerate);
        }

        initFAQ();
        initSmoothScroll();
    }

    // Run when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
