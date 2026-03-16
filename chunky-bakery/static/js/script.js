document.addEventListener("DOMContentLoaded", () => {
    const cursor = document.querySelector(".custom-cursor");
    if (cursor && window.matchMedia("(pointer: fine)").matches) {
        document.addEventListener("mousemove", (event) => {
            cursor.style.opacity = "1";
            cursor.style.left = `${event.clientX}px`;
            cursor.style.top = `${event.clientY}px`;
        });

        const interactive = document.querySelectorAll("a, button, .tilt-card");
        interactive.forEach((item) => {
            item.addEventListener("mouseenter", () => cursor.classList.add("is-active"));
            item.addEventListener("mouseleave", () => cursor.classList.remove("is-active"));
        });
    }

    const buttons = document.querySelectorAll(".filter-btn");
    const cards = document.querySelectorAll(".product-card");

    if (buttons.length && cards.length) {
        buttons.forEach((button) => {
            button.addEventListener("click", () => {
                const target = button.dataset.filter || "all";
                buttons.forEach((btn) => btn.classList.remove("active"));
                button.classList.add("active");

                cards.forEach((card) => {
                    const category = card.dataset.category;
                    const isMatch = target === "all" || category === target;
                    card.style.display = isMatch ? "grid" : "none";
                });
            });
        });
    }

    const revealTargets = document.querySelectorAll(".reveal");
    if (revealTargets.length) {
        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add("is-visible");
                        observer.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.2 }
        );

        revealTargets.forEach((target) => {
            if (target.classList.contains("product-card") || target.classList.contains("gallery-tile")) {
                const siblings = Array.from(target.parentElement?.children || []);
                const index = siblings.indexOf(target);
                target.style.transitionDelay = `${Math.min(index * 80, 400)}ms`;
            } else {
                target.style.transitionDelay = "0ms";
            }
            observer.observe(target);
        });
    }

    const lightbox = document.getElementById("gallery-lightbox");
    const lightboxImage = document.getElementById("lightbox-image");
    const lightboxTitle = document.getElementById("lightbox-title");
    const lightboxDescription = document.getElementById("lightbox-description");
    const lightboxClose = document.getElementById("lightbox-close");

    if (lightbox) {
        document.querySelectorAll(".gallery-tile").forEach((tile) => {
            tile.addEventListener("click", () => {
                const image = tile.dataset.image;
                const title = tile.dataset.title || "";
                const description = tile.dataset.description || "";

                if (lightboxImage) {
                    lightboxImage.src = image || "";
                    lightboxImage.alt = title;
                }
                if (lightboxTitle) {
                    lightboxTitle.textContent = title;
                }
                if (lightboxDescription) {
                    lightboxDescription.textContent = description;
                }

                lightbox.classList.add("is-visible");
                lightbox.setAttribute("aria-hidden", "false");
            });
        });
    }

    if (lightboxClose && lightbox) {
        lightboxClose.addEventListener("click", () => {
            lightbox.classList.remove("is-visible");
            lightbox.setAttribute("aria-hidden", "true");
        });
    }

    const tiltCards = document.querySelectorAll("[data-tilt]");
    tiltCards.forEach((card) => {
        card.addEventListener("mousemove", (event) => {
            const rect = card.getBoundingClientRect();
            const x = event.clientX - rect.left;
            const y = event.clientY - rect.top;
            const rotateX = ((y / rect.height) - 0.5) * -10;
            const rotateY = ((x / rect.width) - 0.5) * 10;
            card.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
        });
        card.addEventListener("mouseleave", () => {
            card.style.transform = "";
        });
    });

    const parallaxItems = document.querySelectorAll(".floating-sculpt, .floating-desserts, .hero-sculpture");
    const onScroll = () => {
        const offset = window.scrollY;
        parallaxItems.forEach((item, index) => {
            const speed = 0.1 + index * 0.04;
            item.style.transform = `translateY(${offset * speed}px)`;
        });
    };
    if (parallaxItems.length) {
        window.addEventListener("scroll", onScroll, { passive: true });
        onScroll();
    }

    const counters = document.querySelectorAll("[data-count]");
    const counterObserver = new IntersectionObserver(
        (entries, observer) => {
            entries.forEach((entry) => {
                if (!entry.isIntersecting) return;
                const el = entry.target;
                const target = Number(el.dataset.count || 0);
                const suffix = el.dataset.suffix || "";
                let current = 0;
                const step = Math.max(1, Math.floor(target / 40));
                const tick = () => {
                    current = Math.min(target, current + step);
                    el.textContent = `${current}${suffix}`;
                    if (current < target) {
                        requestAnimationFrame(tick);
                    }
                };
                tick();
                observer.unobserve(el);
            });
        },
        { threshold: 0.6 }
    );
    counters.forEach((counter) => counterObserver.observe(counter));
});
