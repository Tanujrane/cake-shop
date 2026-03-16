from flask import Blueprint, flash, redirect, render_template, request, url_for

from .content import CONTACT_DETAILS, FEATURED_CAKES, GALLERY_ITEMS, NAV_ITEMS, PROCESS_STEPS, TESTIMONIALS
from .services.contact import validate_inquiry

main_bp = Blueprint("main", __name__)


@main_bp.app_context_processor
def inject_site_data():
    return {
        "nav_items": NAV_ITEMS,
        "contact_details": CONTACT_DETAILS,
    }


@main_bp.get("/")
def home():
    return render_template(
        "pages/home.html",
        page_name="home",
        featured_cakes=FEATURED_CAKES[:3],
        testimonials=TESTIMONIALS,
        process_steps=PROCESS_STEPS,
    )


@main_bp.get("/cakes")
def cakes():
    return render_template(
        "pages/cakes.html",
        page_name="cakes",
        cakes=FEATURED_CAKES,
        testimonials=TESTIMONIALS,
    )


@main_bp.get("/custom-orders")
def custom_orders():
    return render_template(
        "pages/custom_orders.html",
        page_name="custom_orders",
        process_steps=PROCESS_STEPS,
    )


@main_bp.get("/gallery")
def gallery():
    return render_template(
        "pages/gallery.html",
        page_name="gallery",
        gallery_items=GALLERY_ITEMS,
        testimonials=TESTIMONIALS,
    )


@main_bp.get("/contact")
def contact_page():
    return render_template(
        "pages/contact.html",
        page_name="contact",
        testimonials=TESTIMONIALS,
    )


@main_bp.post("/contact")
def submit_contact():
    inquiry, error = validate_inquiry(request.form)
    if error:
        flash(error, "error")
        return redirect(url_for("main.contact_page"))

    flash(f"Thank you, {inquiry['name']}. Our cake concierge will contact you soon.", "success")
    return redirect(url_for("main.contact_page"))
