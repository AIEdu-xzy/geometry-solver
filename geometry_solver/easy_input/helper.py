
# Helper functions.

def _get_target(parser, entity_id, entity_type, attr_name):
    parser.set_target(entity_id, entity_type, attr_name)
    return parser.execute()

