odoo.define('hello_world.main', function (require) {
  const AbstractAction = require('web.AbstractAction');
  const core = require('web.core');
  //console.log(AbstractAction);
  const OurAction = AbstractAction.extend({
      start: function () {
          this.$el.html('hello');
      }
  });

  core.action_registry.add('hello_world.action', OurAction);
});