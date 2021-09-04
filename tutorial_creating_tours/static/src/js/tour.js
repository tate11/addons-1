odoo.define('tutorial_creating_tours.example_tour', function(require) {
    "use strict";

    // Minimal requirements needed to create a tour
    var core = require('web.core');
    var tour = require('web_tour.tour');

    // Allows you to translate tour steps
    var _t = core._t;

    // You can find more complex example tours in the official source code too. See
    // https://github.com/odoo/odoo/blob/12.0/addons/sale_management/static/tests/product_configurator_advanced_test_ui.js
    // or https://github.com/odoo/odoo/search?l=JavaScript&q=tour&type=

    tour.register('example_tour', {
        url: "/web",
        // You can find all step options at:
        //     https://github.com/odoo/odoo/blob/master/addons/web_tour/static/src/js/tour_step_utils.js
        //
        // - showAppsMenuItem(): shows a tour blinker on the app that you mention.
        // - toggleHomeMenu(): shows a tour blinker to go back to the zhome screen of Odoo.
    }, [tour.stepUtils.showAppsMenuItem(), {
        trigger: '.o_app[data-menu-xmlid="contacts.menu_contacts"]',
        content: _t('Want to manage <b>your contacts</b>? <i>It starts here.</i>'),
        position: 'bottom',
    }, {
        trigger: '.o-kanban-button-new',
        extra_trigger: '.o_res_partner_kanban',
        content: _t('Let\'s create your first contact by clicking on create.'),
        position: 'bottom',
        width: 200,
    }, {
        // The trigger will tell that you would like to input a value in the field 'Name'
        trigger: 'input[placeholder="Name"]',
        extra_trigger: '.o_form_editable',
        // This is the 'hint' / tooltip that is shown to the end user
        content: _t('Fill in the name of the contact.'),
        // When you run the test (from the developer tools) it will automatically fill in 'James Cook'.
        run: 'text James Cook',
        position: 'right',
    }, {
        trigger: '.o_form_button_save',
        extra_trigger: '.oe_avatar',
        content: _t('Click on save to <b>save your new contact</b>. You can use this contact throughout Odoo later on.'),
        position: 'bottom',
    }]);
});
