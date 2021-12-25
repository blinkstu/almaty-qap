window.addEventListener("load", function () {
    hide_page = false;
    django.jQuery(document).ready(function () {
        console.log(123)
        if (django.jQuery('#id_to_page').is(':checked')) {
            django.jQuery(".field-url, .field-open_on_new_tab").hide();
            django.jQuery(".field-page").show()
            hide_page = true;
        } else {
            django.jQuery(".field-url, .field-open_on_new_tab").show();
            django.jQuery(".field-page").hide()
            hide_page = false;
        }
        django.jQuery("#id_to_page").click(function () {
            hide_page = !hide_page;
            if (hide_page) {
                django.jQuery(".field-url, .field-open_on_new_tab").hide();
                django.jQuery(".field-page").show()
            } else {
                django.jQuery(".field-url, .field-open_on_new_tab").show();
                django.jQuery(".field-page").hide()
            }
        })
    })
})