// setup lightbox
frappe.setup_lightbox = function() {
	lightbox.option({ positionFromTop: 20 })
    $(".screenshot").each(function() {
		if($(this).parent().attr("data-lightbox")) return;
        var name = this.src.split("/").splice(-1)[0].split(".")[0];
        var a = $('<a data-lightbox="'+ name
            +'" href="' + this.src + '" data-title="' + this.alt + '"></a>').insertBefore(this);
        $(this).appendTo(a);
    })
}

frappe.ready(function() { frappe.setup_lightbox(); })
$(document).on("page-change", frappe.setup_lightbox);
