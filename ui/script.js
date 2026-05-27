document.addEventListener('DOMContentLoaded', () => {
    // Number Counter Animation
    const counter = document.getElementById('counter');
    const target = parseInt(counter.getAttribute('data-target'), 10);
    
    // Format number as currency
    const formatCurrency = (num) => {
        return new Intl.NumberFormat('en-US').format(num);
    };

    let startTime = null;
    const duration = 2500; // 2.5 seconds

    const easeOutExpo = (t) => {
        return t === 1 ? 1 : 1 - Math.pow(2, -10 * t);
    };

    const animateNumber = (timestamp) => {
        if (!startTime) startTime = timestamp;
        const progress = Math.min((timestamp - startTime) / duration, 1);
        
        const currentNum = Math.floor(easeOutExpo(progress) * target);
        counter.innerText = formatCurrency(currentNum);
        
        if (progress < 1) {
            window.requestAnimationFrame(animateNumber);
        } else {
            counter.innerText = formatCurrency(target);
        }
    };

    // Start animation slightly after page load for effect
    setTimeout(() => {
        window.requestAnimationFrame(animateNumber);
    }, 500);

    // Scroll Reveal Animation (Intersection Observer)
    const fadeElements = document.querySelectorAll('.card, .case-card, .method-step');
    
    // Set initial state
    fadeElements.forEach(el => {
        el.classList.add('fade-up');
    });

    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                // Add staggered delay based on index for grid elements
                setTimeout(() => {
                    entry.target.classList.add('visible');
                }, index * 100);
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    fadeElements.forEach(el => {
        observer.observe(el);
    });

    // Smooth scroll for nav links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Evidence Tabs Logic
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all
            tabBtns.forEach(b => b.classList.remove('active'));
            tabContents.forEach(c => c.classList.remove('active'));

            // Add active class to clicked
            btn.classList.add('active');
            const targetId = `tab-${btn.getAttribute('data-target')}`;
            document.getElementById(targetId).classList.add('active');
        });
    });
});
