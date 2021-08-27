from odoo.tests.common import TransactionCase


class ContactNoteTests(TransactionCase):
    def setUp(self):
        super().setUp()
        self.contact_note = self.env.ref("tutorial_chatter_functionalities.contact_note_three")
        self.note_type = self.env.ref("mail.mt_note")
        self.comment_type = self.env.ref("mail.mt_comment")

        # give us a clean slate for messages and activities
        self.contact_note.message_ids.unlink()
        self.contact_note.activity_ids.unlink()

    def test_generating_internal_message(self):
        self.assertEqual(len(self.contact_note.message_ids), 0)
        message = self.contact_note.generate_internal_message()
        self.assertEqual(len(self.contact_note.message_ids), 1)
        self.assertEqual(message.message_type, "comment")
        self.assertEqual(message.subtype_id.id, self.note_type.id)

    def test_generating_message(self):
        self.assertEqual(len(self.contact_note.message_ids), 0)
        message = self.contact_note.generate_message()
        self.assertEqual(len(self.contact_note.message_ids), 1)
        self.assertEqual(message.message_type, "comment")
        self.assertEqual(message.subtype_id.id, self.comment_type.id)

    def test_generating_activity(self):
        self.assertEqual(len(self.contact_note.activity_ids), 0)
        activity = self.contact_note.generate_activity()
        self.assertEqual(len(self.contact_note.message_ids), 0)
        self.assertEqual(len(self.contact_note.activity_ids), 1)
