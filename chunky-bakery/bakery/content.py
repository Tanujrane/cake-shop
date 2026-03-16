NAV_ITEMS = [
    {"label": "Home", "endpoint": "main.home"},
    {"label": "Cakes", "endpoint": "main.cakes"},
    {"label": "Custom Orders", "endpoint": "main.custom_orders"},
    {"label": "Gallery", "endpoint": "main.gallery"},
    {"label": "Contact", "endpoint": "main.contact_page"},
]

FEATURED_CAKES = [
    {
        "name": "Blush Bloom",
        "category": "Birthday Cake",
        "price": "Rs. 2,800",
        "description": "Rose vanilla sponge wrapped in petal piping and edible gold shimmer.",
        "image": "images/blush-bloom.svg",
    },
    {
        "name": "Champagne Pearl",
        "category": "Wedding Cake",
        "price": "Rs. 6,400",
        "description": "A pearl-toned tiered cake with soft florals and airy cream textures.",
        "image": "images/champagne-pearl.svg",
    },
    {
        "name": "Midnight Truffle",
        "category": "Chocolate Cake",
        "price": "Rs. 3,250",
        "description": "Glossy ganache layers with rich cocoa notes and truffle filling.",
        "image": "images/midnight-truffle.svg",
    },
    {
        "name": "Rose Swirl Box",
        "category": "Cupcakes",
        "price": "Rs. 1,450",
        "description": "A couture box of velvet cupcakes finished with satin rosettes.",
        "image": "images/rose-swirl-cupcakes.svg",
    },
    {
        "name": "Hazel Fete",
        "category": "Signature",
        "price": "Rs. 3,600",
        "description": "Chocolate hazelnut sponge with praline crunch and festive piping.",
        "image": "images/hazel-fete.svg",
    },
    {
        "name": "Ivory Petal Tower",
        "category": "Wedding Dessert",
        "price": "Rs. 4,900",
        "description": "Mini cakes and cupcakes arranged into a sculptural dessert tower.",
        "image": "images/ivory-petal.svg",
    },
]

GALLERY_ITEMS = [
    {
        "title": "Atelier Signature",
        "description": "Floral cakes and soft metallic finishes staged in our dessert studio.",
        "image": "data:image/jpeg;base64,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",
    },
    {
        "title": "Dessert Tablescape",
        "description": "Luxury plated sweets curated for intimate celebrations.",
        "image": "https://lh3.googleusercontent.com/gps-cs-s/AHVAweq8NrddutvUnWDZfOak0LsnzoO5NDmY2h03VUU42Dm3HMRSnepkjy18HWb3FfHVPAtQeQZyN19wWEO_EBMBs2Um9n2F1gKehHhTUKEbWL4CWKK0ssdoXIJtMzN0W2g2YP2QiWRJ=w243-h203-n-k-no-nu",
    },
    {
        "title": "Macaron Collection",
        "description": "Blush, cream, and cocoa macarons with hand-finished shells.",
        "image": "https://lh3.googleusercontent.com/p/AF1QipO3dyex_5p1rq1wNTAqVso9_iwZi3oPDYzuL5xY=w243-h174-n-k-no-nu",
    },
    {
        "title": "Cupcake Tower",
        "description": "A sculptural cupcake arrangement for stylish hosting moments.",
        "image": "https://lh3.googleusercontent.com/p/AF1QipMkdUw8btpxTDm5TTkw6Z4BpFMuDPQZZ4_BYkNz=w243-h244-n-k-no-nu",
    },
    {
        "title": "Chocolate Indulgence",
        "description": "Deep ganache layers and berries for rich celebration tables.",
        "image": "https://lh3.googleusercontent.com/gps-cs-s/AHVAweq8NrddutvUnWDZfOak0LsnzoO5NDmY2h03VUU42Dm3HMRSnepkjy18HWb3FfHVPAtQeQZyN19wWEO_EBMBs2Um9n2F1gKehHhTUKEbWL4CWKK0ssdoXIJtMzN0W2g2YP2QiWRJ=w243-h203-n-k-no-nu",
    },
    {
        "title": "Wedding Showcase",
        "description": "Pearl cakes and florals styled for modern wedding receptions.",
        "image": "https://lh3.googleusercontent.com/p/AF1QipO3dyex_5p1rq1wNTAqVso9_iwZi3oPDYzuL5xY=w243-h174-n-k-no-nu",
    },
]

TESTIMONIALS = [
    {
        "name": "Aarohi Mehta",
        "role": "Wedding Client",
        "quote": "Chunky's Cake Shop made our dessert table feel like a luxury editorial shoot.",
    },
    {
        "name": "Rohan Kapoor",
        "role": "Birthday Celebration",
        "quote": "The design, flavor, and finish all felt premium, thoughtful, and unforgettable.",
    },
    {
        "name": "Naina and Vihaan",
        "role": "Private Soiree",
        "quote": "Guests talked about the cake all evening. It looked refined and tasted even better.",
    },
]

PROCESS_STEPS = [
    {
        "title": "Consultation",
        "description": "We shape the concept, palette, portion size, and event mood together.",
    },
    {
        "title": "Design Curation",
        "description": "Textures, florals, trims, and finishing details are selected with care.",
    },
    {
        "title": "Handcrafted Finish",
        "description": "Every layer is baked, frosted, and styled to arrive photo-ready.",
    },
]

CONTACT_DETAILS = {
    "address": "Studio 12, Celebration Avenue, Jaipur",
    "phone": "+91 98765 43210",
    "email": "hello@chunkyscakeshop.com",
    "hours": "Mon - Sat | 10:00 AM - 8:00 PM",
}
