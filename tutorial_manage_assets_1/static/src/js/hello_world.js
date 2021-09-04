odoo.define('hello_world.main', function (require) {
  // The require will import the AbstractAction from the web module.
  // The AbstractAction is the base class for all actions in Odoo
  const AbstractAction = require('web.AbstractAction');
  const core = require('web.core');

  const OurAction = AbstractAction.extend({
    // Loads the template from static/src/xml/hello_world.xml
    template: "hello_world.ClientAction",
    info: "this message comes from the JS"
  });

  // Adds it to the registry so that the action is loaded by Odoo
  core.action_registry.add('hello_world.action', OurAction);
});
