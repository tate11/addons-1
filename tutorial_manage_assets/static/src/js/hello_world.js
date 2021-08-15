odoo.define('hello_world.main', function (require) {
    const AbstractAction = require('web.AbstractAction');
    const core = require('web.core');
    //console.log(AbstractAction);
    const OurAction = AbstractAction.extend({
        template: "hello_world.ClientAction",
        info: "This message comes from the JS"
    });
    core.action_registry.add('hello_world.action', OurAction);
});